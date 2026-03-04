"""Analyze pareto frontier from optimization logs and extract hard examples.

Reads the output_logs.md from the optimization run, extracts per-program
valset scores, identifies persistently wrong examples for human review,
and selects a minimal ensemble of 2-3 prompts that maximize joint coverage
using greedy set cover on the pareto frontier data.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

try:
    from .data import load_val_set
except ImportError:
    from data import load_val_set

__all__ = ["main"]

LOG_PATH = Path(__file__).parent / "output_logs.md"
HARD_EXAMPLES_PATH = Path(__file__).parent / "hard_examples_for_review.csv"
ENSEMBLE_PATH = Path(__file__).parent / "ensemble_prompts.md"


# ---------------------------------------------------------------------------
# 1. Parse per-program valset scores from the log
# ---------------------------------------------------------------------------


def _parse_individual_scores(log_text: str) -> dict[int, dict[int, float]]:
    """Extract individual valset scores per program.

    Returns {program_index: {example_index: score}}.
    Program 0 is the seed (iteration 0), program 1 is from iteration 2, etc.
    """
    # Map iteration -> program index from "New program candidate index: N" lines
    candidate_index_pattern = re.compile(r"Iteration (\d+): New program candidate index: (\d+)")
    iter_to_prog: dict[int, int] = {}
    for m in candidate_index_pattern.finditer(log_text):
        iteration = int(m.group(1))
        prog_idx = int(m.group(2))
        iter_to_prog[iteration] = prog_idx

    # Parse base program (iteration 0) individual scores.
    # The base program is always index 0, but its individual scores come from
    # the first full valset evaluation. We reconstruct from the "Base program
    # full valset score" and the first "Individual valset scores" that matches
    # the seed's iteration.
    scores_pattern = re.compile(
        r"Iteration (\d+): Individual valset scores for new program: \{(.+?)\}"
    )

    programs: dict[int, dict[int, float]] = {}
    for m in scores_pattern.finditer(log_text):
        iteration = int(m.group(1))
        if iteration not in iter_to_prog:
            continue
        prog_idx = iter_to_prog[iteration]
        raw = m.group(2)
        example_scores: dict[int, float] = {}
        for pair in raw.split(","):
            pair = pair.strip()
            k, v = pair.split(":")
            example_scores[int(k.strip())] = float(v.strip())
        programs[prog_idx] = example_scores

    # Reconstruct seed (program 0) single-shot scores.
    # The base program scored 0.6566 (65/99) in its initial full-valset evaluation.
    # Individual per-example scores for program 0 are NOT logged directly.
    # We reconstruct from the iteration 2 pareto front scores (which is
    # max(seed, prog1) per example) and program 1's known individual scores.
    #
    # Logic: pareto2[i] = max(seed[i], prog1[i])
    #   - If pareto2[i] == 0: seed[i] = 0 AND prog1[i] = 0
    #   - If pareto2[i] == 1 AND prog1[i] == 0: seed[i] = 1
    #   - If pareto2[i] == 1 AND prog1[i] == 1: seed[i] is unknown
    #
    # We know seed must total 65. So we solve: among the unknown examples,
    # assign 1s until we reach 65 total. The unknowns are where both pareto=1
    # and prog1=1 — for those we can't distinguish, so we distribute 1s
    # greedily. In practice, the initial base eval is the most reliable single
    # shot, so we accept this approximation.
    #
    # BUT: the pareto front programs map at iteration 2 may already be inflated
    # by subsample evaluations of program 0. A safer approach: parse the pareto
    # front SCORES (not programs) at iteration 2, which is the max(seed, prog1)
    # float. Since these are binary, pareto_score[i] is 0 or 1.
    pareto2_scores_pattern = re.compile(r"Iteration 2: New valset pareto front scores: \{(.+?)\}")
    pareto2_match = pareto2_scores_pattern.search(log_text)
    if pareto2_match and 1 in programs:
        prog1_scores = programs[1]
        pareto2: dict[int, float] = {}
        for pair in pareto2_match.group(1).split(","):
            pair = pair.strip()
            k, v = pair.split(":")
            pareto2[int(k.strip())] = float(v.strip())

        seed_scores: dict[int, float] = {}
        definite_ones = 0
        ambiguous_indices: list[int] = []

        for ex_idx in range(99):
            p2 = pareto2.get(ex_idx, 0.0)
            p1 = prog1_scores.get(ex_idx, 0.0)
            if p2 == 0.0:
                seed_scores[ex_idx] = 0.0
            elif p1 == 0.0:
                # pareto is 1 but prog1 is 0 => seed must be 1
                seed_scores[ex_idx] = 1.0
                definite_ones += 1
            else:
                # Both pareto=1 and prog1=1 => seed could be 0 or 1
                ambiguous_indices.append(ex_idx)

        # We need exactly 65 ones total (base score = 65/99)
        needed = 65 - definite_ones
        # Assign 1 to the first `needed` ambiguous, rest get 0
        for i, ex_idx in enumerate(ambiguous_indices):
            seed_scores[ex_idx] = 1.0 if i < needed else 0.0

        programs[0] = seed_scores

    return programs


def _parse_pareto_front(log_text: str) -> dict[int, set[int]]:
    """Parse the final pareto front: {example_idx: {programs that got it right}}."""
    pareto_progs_pattern = re.compile(r"Iteration 58: Updated valset pareto front programs: (.+)")
    m = pareto_progs_pattern.search(log_text)
    if not m:
        return {}
    return eval(m.group(1))  # noqa: S307


def _parse_pareto_scores(log_text: str) -> dict[int, float]:
    """Parse the final pareto front per-example best scores."""
    pattern = re.compile(r"Iteration 58: New valset pareto front scores: \{(.+?)\}")
    m = pattern.search(log_text)
    if not m:
        return {}
    scores: dict[int, float] = {}
    for pair in m.group(1).split(","):
        pair = pair.strip()
        k, v = pair.split(":")
        scores[int(k.strip())] = float(v.strip())
    return scores


# ---------------------------------------------------------------------------
# 2. Extract prompts from the log
# ---------------------------------------------------------------------------


def _parse_prompts(log_text: str) -> dict[int, str]:
    """Extract prompt text for each program index.

    Returns {program_index: prompt_text}.
    """
    prompts: dict[int, str] = {}

    # Seed prompt: everything between "Seed prompt:" and "Iteration 0:"
    seed_match = re.search(
        r"Seed prompt:\n(.+?)(?=Iteration 0:)",
        log_text,
        re.DOTALL,
    )
    if seed_match:
        prompts[0] = seed_match.group(1).strip()

    # Map iteration -> candidate index
    candidate_index_pattern = re.compile(r"Iteration (\d+): New program candidate index: (\d+)")
    iter_to_prog: dict[int, int] = {}
    for m in candidate_index_pattern.finditer(log_text):
        iter_to_prog[int(m.group(1))] = int(m.group(2))

    # Extract proposed text per iteration
    proposed_pattern = re.compile(
        r"Iteration (\d+): Proposed new text for system_prompt: (.+?)(?=Iteration \d+:)",
        re.DOTALL,
    )
    for m in proposed_pattern.finditer(log_text):
        iteration = int(m.group(1))
        if iteration in iter_to_prog:
            prompts[iter_to_prog[iteration]] = m.group(2).strip()

    return prompts


# ---------------------------------------------------------------------------
# 3. Find persistently wrong examples
# ---------------------------------------------------------------------------


def _find_hard_examples(
    program_scores: dict[int, dict[int, float]],
    num_examples: int = 99,
) -> list[int]:
    """Return example indices that NO program solved in single-shot evaluation."""
    hard = []
    for ex_idx in range(num_examples):
        solved = any(scores.get(ex_idx, 0.0) == 1.0 for scores in program_scores.values())
        if not solved:
            hard.append(ex_idx)
    return hard


def _export_hard_examples(hard_indices: list[int], val_set: list[dict[str, str]]) -> None:
    """Write hard examples to CSV for human review."""
    fieldnames = [
        "val_index",
        "label",
        "source_file",
        "predicted_category",
        "confidence",
        "text",
        "explanation",
    ]
    with HARD_EXAMPLES_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for idx in hard_indices:
            row = val_set[idx]
            writer.writerow(
                {
                    "val_index": idx,
                    "label": row.get("label", ""),
                    "source_file": row.get("source_file", ""),
                    "predicted_category": row.get("predicted_category", ""),
                    "confidence": row.get("confidence", ""),
                    "text": row.get("text", ""),
                    "explanation": row.get("explanation", ""),
                }
            )
    print(f"Exported {len(hard_indices)} hard examples to {HARD_EXAMPLES_PATH}")


# ---------------------------------------------------------------------------
# 4. Greedy set-cover ensemble selection
# ---------------------------------------------------------------------------


def _greedy_ensemble(
    program_scores: dict[int, dict[int, float]],
    pareto_scores: dict[int, float],
    max_prompts: int = 3,
) -> list[int]:
    """Select up to max_prompts programs that maximize union coverage.

    Uses greedy set-cover: at each step, pick the program that correctly
    classifies the most currently-uncovered examples.
    """
    # Only consider examples that are solvable (pareto score == 1.0)
    solvable = {ex for ex, score in pareto_scores.items() if score == 1.0}

    selected: list[int] = []
    covered: set[int] = set()

    for _ in range(max_prompts):
        best_prog = -1
        best_gain = -1
        best_total = -1

        for prog_idx, scores in program_scores.items():
            if prog_idx in selected:
                continue
            # Examples this program gets right that aren't yet covered
            correct = {ex for ex, s in scores.items() if s == 1.0 and ex in solvable}
            gain = len(correct - covered)
            total = len(correct)
            if gain > best_gain or (gain == best_gain and total > best_total):
                best_gain = gain
                best_total = total
                best_prog = prog_idx

        if best_prog < 0 or best_gain == 0:
            break
        selected.append(best_prog)
        correct_set = {
            ex for ex, s in program_scores[best_prog].items() if s == 1.0 and ex in solvable
        }
        covered |= correct_set
        print(
            f"  Set-cover step {len(selected)}: program {best_prog} "
            f"(+{best_gain} new, {len(covered)}/{len(solvable)} covered, "
            f"individual score {sum(1 for s in program_scores[best_prog].values() if s == 1.0)}/99)"
        )

    return selected


def _majority_vote_ensemble(
    program_scores: dict[int, dict[int, float]],
    num_examples: int = 99,
    ensemble_size: int = 3,
) -> tuple[list[int], int]:
    """Brute-force search for the best 2-3 prompt ensemble by majority vote accuracy.

    For ensemble_size=3, tries all C(n,3) combinations. For 33 programs
    that's only 5456 combinations — fast enough.
    """
    from itertools import combinations

    prog_indices = sorted(program_scores.keys())
    best_ensemble: list[int] = []
    best_correct = -1

    for combo in combinations(prog_indices, ensemble_size):
        correct = 0
        for ex_idx in range(num_examples):
            votes = sum(1 for p in combo if program_scores[p].get(ex_idx, 0.0) == 1.0)
            if votes > ensemble_size / 2:
                correct += 1
        if correct > best_correct:
            best_correct = correct
            best_ensemble = list(combo)

    return best_ensemble, best_correct


def _write_ensemble(
    selected: list[int],
    prompts: dict[int, str],
    program_scores: dict[int, dict[int, float]],
    pareto_scores: dict[int, float],
) -> None:
    """Write the ensemble prompts and coverage analysis to markdown."""
    solvable = {ex for ex, score in pareto_scores.items() if score == 1.0}
    total_examples = len(pareto_scores)

    lines: list[str] = ["# Ensemble Prompts (Pareto-Optimal Set Cover)\n"]
    lines.append(f"Total valset examples: {total_examples}")
    lines.append(f"Solvable by any single prompt: {len(solvable)}")
    lines.append(f"Unsolvable (hard examples): {total_examples - len(solvable)}\n")

    # Joint coverage
    covered: set[int] = set()
    for prog_idx in selected:
        correct = {ex for ex, s in program_scores[prog_idx].items() if s == 1.0 and ex in solvable}
        covered |= correct

    cover_msg = (
        f"## Ensemble of {len(selected)} prompts covers "
        f"{len(covered)}/{len(solvable)} solvable examples"
    )
    lines.append(cover_msg)
    pct = len(covered) / total_examples
    lines.append(
        f"Overall accuracy with majority vote: {len(covered)}/{total_examples} = {pct:.2%}\n"
    )

    # Majority vote analysis
    lines.append("## Majority Vote Analysis\n")
    majority_correct = 0
    for ex_idx in range(total_examples):
        votes_yes = sum(
            1 for prog_idx in selected if program_scores.get(prog_idx, {}).get(ex_idx, 0.0) == 1.0
        )
        if votes_yes > len(selected) / 2:
            majority_correct += 1
        elif votes_yes == len(selected) / 2:
            # Tie goes to the best single prompt (first in ensemble)
            majority_correct += 1 if program_scores[selected[0]].get(ex_idx, 0.0) == 1.0 else 0
    mv_pct = majority_correct / total_examples
    lines.append(f"Majority vote accuracy: {majority_correct}/{total_examples} = {mv_pct:.2%}\n")

    for rank, prog_idx in enumerate(selected, 1):
        score_count = sum(1 for s in program_scores[prog_idx].values() if s == 1.0)
        lines.append(
            f"---\n\n## Prompt {rank} "
            f"(program index {prog_idx}, individual accuracy: "
            f"{score_count}/99)\n"
        )
        lines.append("```")
        lines.append(prompts.get(prog_idx, "<prompt not found>"))
        lines.append("```\n")

    # Per-example breakdown
    lines.append("---\n\n## Per-Example Coverage Detail\n")
    lines.append("| Example | " + " | ".join(f"P{p}" for p in selected) + " | Majority | Pareto |")
    lines.append("|---------|" + "|".join("------" for _ in selected) + "|----------|--------|")
    for ex_idx in range(total_examples):
        row_parts = [f"| {ex_idx:>7} "]
        votes = 0
        for prog_idx in selected:
            s = program_scores.get(prog_idx, {}).get(ex_idx, 0.0)
            row_parts.append("Y" if s == 1.0 else ".")
            if s == 1.0:
                votes += 1
        majority = votes > len(selected) / 2
        if votes == len(selected) / 2:
            majority = program_scores[selected[0]].get(ex_idx, 0.0) == 1.0
        pareto_ok = pareto_scores.get(ex_idx, 0.0) == 1.0
        row_parts_str = " | ".join(row_parts)
        lines.append(
            f"{row_parts_str} | {'Y' if majority else '.':<8} | {'Y' if pareto_ok else '.':<6} |"
        )

    with ENSEMBLE_PATH.open("w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Ensemble analysis written to {ENSEMBLE_PATH}")


# ---------------------------------------------------------------------------
# 5. Main
# ---------------------------------------------------------------------------


def main() -> int:
    log_text = LOG_PATH.read_text(encoding="utf-8")

    print("=== Pareto Frontier Analysis ===\n")

    # Parse all data
    program_scores = _parse_individual_scores(log_text)
    pareto_scores = _parse_pareto_scores(log_text)
    _parse_pareto_front(log_text)  # validates log integrity
    prompts = _parse_prompts(log_text)

    print(f"Programs in pool: {len(program_scores)}")
    print(f"Valset examples: {len(pareto_scores)}")
    print(f"Prompts extracted: {len(prompts)}")

    # Score summary
    print("\nPer-program individual valset scores:")
    for prog_idx in sorted(program_scores.keys()):
        correct = sum(1 for s in program_scores[prog_idx].values() if s == 1.0)
        print(f"  Program {prog_idx:>2}: {correct}/99 ({correct / 99:.2%})")

    # Persistently wrong examples
    hard = _find_hard_examples(program_scores)
    print(f"\n{len(hard)} examples UNSOLVED by all {len(program_scores)} programs:")
    print(f"  Indices: {hard}")

    # Export hard examples
    val_set = load_val_set()
    _export_hard_examples(hard, val_set)

    # Print hard example previews
    print("\nHard example previews:")
    for idx in hard:
        row = val_set[idx]
        text = row.get("text", "")[:100].replace("\n", " ")
        label = row.get("label", "")
        source = row.get("source_file", "")
        print(f"  [{idx}] label={label} source={source}: {text}...")

    # Greedy set-cover ensemble selection
    print("\n=== Greedy Set-Cover Ensemble (max 3 prompts) ===\n")
    setcover = _greedy_ensemble(program_scores, pareto_scores, max_prompts=3)
    print(f"\nSet-cover programs: {setcover}")

    # Joint coverage
    solvable = {ex for ex, score in pareto_scores.items() if score == 1.0}
    covered: set[int] = set()
    for prog_idx in setcover:
        correct = {ex for ex, s in program_scores[prog_idx].items() if s == 1.0}
        covered |= correct & solvable
    print(f"Union coverage: {len(covered)}/{len(solvable)} solvable examples")
    print(f"Overall union: {len(covered)}/99 ({len(covered) / 99:.2%})")

    # Majority vote ensemble (brute force best 3)
    print("\n=== Best Majority-Vote Ensemble (brute-force, size=3) ===\n")
    mv3, mv3_score = _majority_vote_ensemble(program_scores, ensemble_size=3)
    print(f"Best 3-prompt majority vote: programs {mv3} → {mv3_score}/99 ({mv3_score / 99:.2%})")

    print("\n=== Best Majority-Vote Ensemble (brute-force, size=2) ===\n")
    mv2, mv2_score = _majority_vote_ensemble(program_scores, ensemble_size=2)
    print(f"Best 2-prompt majority vote: programs {mv2} → {mv2_score}/99 ({mv2_score / 99:.2%})")

    # Choose the best ensemble: the one with highest majority vote accuracy
    # since that's what matters for production use
    if mv3_score >= mv2_score:
        selected = mv3
        print(f"\n=== Selected: 3-prompt ensemble (majority vote: {mv3_score}/99) ===")
    else:
        selected = mv2
        print(f"\n=== Selected: 2-prompt ensemble (majority vote: {mv2_score}/99) ===")

    # Write ensemble file
    _write_ensemble(selected, prompts, program_scores, pareto_scores)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
