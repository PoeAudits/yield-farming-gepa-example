from __future__ import annotations

import argparse
import random
from pathlib import Path
from typing import Any

from gepa.optimize_anything import EngineConfig, GEPAConfig, ReflectionConfig

from optimize_anything import (
    HandoffManager,
    InteractiveProposer,
    ReportGenerator,
    SessionState,
    load_session_state,
)
from optimize_anything.runners.optimize import run_optimization
from optimize_anything.runners.results import (
    extract_best_score,
    is_probable_missing_api_key,
)

try:
    from .config import (
        BEST_PROMPT_PATH,
        MAX_METRIC_CALLS,
        REFLECTION_MINIBATCH_SIZE,
    )
    from .data import load_train_set, load_val_set
    from .evaluator import mock_evaluator, real_evaluator
except ImportError:
    from config import (  # type: ignore[no-redef]
        BEST_PROMPT_PATH,
        MAX_METRIC_CALLS,
        REFLECTION_MINIBATCH_SIZE,
    )
    from data import load_train_set, load_val_set  # type: ignore[no-redef]
    from evaluator import mock_evaluator, real_evaluator  # type: ignore[no-redef]

__all__ = ["main"]

_OBJECTIVE = (
    "Maximize exact-match classification accuracy for identifying genuine, actionable "
    "yield farming opportunities in crypto messages. Labels are yes and no."
)

_BACKGROUND = (
    "Messages come from crypto Telegram and Discord channels. A yield farming opportunity "
    "is a message that presents a concrete, actionable way to earn passive yield on crypto "
    "assets - including staking, liquidity provision, vault deposits, savings products, and "
    "earn programs with stated APY/APR. Messages that are general news, require active "
    "trading, are competitions or lotteries, or lack specifics are not yield farming "
    "opportunities. The dataset includes messages where ML models agreed, disagreed, or had "
    "low confidence, so edge cases are heavily represented."
)

_DEFAULT_HANDOFF_DIR = Path(__file__).parent / "handoff"
_DEFAULT_TEST_HANDOFF_DIR = Path(__file__).parent / "handoff-test"
_TEST_VAL_SET_SIZE = 20
_TEST_MINIBATCH_SIZE = 10
_TEST_RANDOM_SEED = 20260303
_SOURCE_FILES = ("agreed", "disagreed", "low_confidence")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run interactive yield farming prompt optimization.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    start_parser = subparsers.add_parser("start", help="Start a new interactive session.")
    start_parser.add_argument(
        "--mock",
        action="store_true",
        help="Use deterministic mock evaluator (no external API calls).",
    )
    start_parser.add_argument(
        "--handoff-dir",
        type=Path,
        default=_DEFAULT_HANDOFF_DIR,
        help="Path for interactive handoff artifacts.",
    )
    start_parser.add_argument(
        "--prompt",
        type=Path,
        default=BEST_PROMPT_PATH,
        help="Seed prompt file path.",
    )
    start_parser.add_argument(
        "--test",
        action="store_true",
        help="Use reduced validation subset and minibatch for development.",
    )

    resume_parser = subparsers.add_parser("resume", help="Resume an interactive session.")
    resume_parser.add_argument(
        "--mock",
        action="store_true",
        help="Use deterministic mock evaluator (no external API calls).",
    )
    resume_parser.add_argument(
        "--handoff-dir",
        type=Path,
        default=_DEFAULT_HANDOFF_DIR,
        help="Path for interactive handoff artifacts.",
    )
    resume_parser.add_argument(
        "--test",
        action="store_true",
        help="Use reduced validation subset and minibatch for development.",
    )

    return parser.parse_args()


def _build_config(
    interactive_proposer: InteractiveProposer,
    handoff_dir: Path,
    minibatch_size: int = REFLECTION_MINIBATCH_SIZE,
) -> GEPAConfig:
    """Build GEPA config for interactive mode.

    max_candidate_proposals=1 ensures GEPA pauses after each proposal for human review.
    use_cloudpickle=False avoids requiring an optional dependency for state persistence.
    """
    return GEPAConfig(
        engine=EngineConfig(
            run_dir=str(handoff_dir),
            max_metric_calls=MAX_METRIC_CALLS,
            max_candidate_proposals=1,
            use_cloudpickle=False,
        ),
        reflection=ReflectionConfig(
            custom_candidate_proposer=interactive_proposer,
            reflection_lm=None,
            reflection_minibatch_size=minibatch_size,
        ),
    )


def _load_seed_candidate(prompt_path: Path) -> dict[str, str]:
    return {"system_prompt": prompt_path.read_text(encoding="utf-8").strip()}


def _pop_random_example(rng: random.Random, examples: list[dict[str, str]]) -> dict[str, str]:
    index = rng.randrange(len(examples))
    return examples.pop(index)


def _build_test_subset(val_set: list[dict[str, str]]) -> list[dict[str, str]]:
    rng = random.Random(_TEST_RANDOM_SEED)
    per_label_target = _TEST_VAL_SET_SIZE // 2
    subset: list[dict[str, str]] = []

    for label in ("yes", "no"):
        by_source: dict[str, list[dict[str, str]]] = {
            source: [
                example
                for example in val_set
                if example.get("label") == label and example.get("source_file") == source
            ]
            for source in _SOURCE_FILES
        }

        selected_for_label: list[dict[str, str]] = []
        for source in _SOURCE_FILES:
            candidates = by_source[source]
            if not candidates:
                continue
            if len(selected_for_label) >= per_label_target:
                break
            selected_for_label.append(_pop_random_example(rng, candidates))

        remaining_pool: list[dict[str, str]] = []
        for source in _SOURCE_FILES:
            remaining_pool.extend(by_source[source])
        rng.shuffle(remaining_pool)

        remaining_needed = per_label_target - len(selected_for_label)
        if remaining_needed < 0:
            remaining_needed = 0
        if len(remaining_pool) < remaining_needed:
            raise ValueError(
                f"Insufficient validation examples for label '{label}' in test subset construction."
            )

        selected_for_label.extend(remaining_pool[:remaining_needed])
        subset.extend(selected_for_label)

    if len(subset) != _TEST_VAL_SET_SIZE:
        raise ValueError(
            f"Test subset must contain exactly {_TEST_VAL_SET_SIZE} examples; got {len(subset)}."
        )

    rng.shuffle(subset)
    return subset


def _load_session_resources(
    args: argparse.Namespace,
) -> tuple[list[dict[str, str]], list[dict[str, str]], Any, str]:
    train_set = load_train_set()
    val_set = load_val_set()
    if args.test:
        val_set = _build_test_subset(val_set)
    evaluator = mock_evaluator if args.mock else real_evaluator
    mode = "mock" if args.mock else "real"
    return train_set, val_set, evaluator, mode


def _resolve_handoff_dir(args: argparse.Namespace) -> Path:
    if args.test:
        return _DEFAULT_TEST_HANDOFF_DIR
    return args.handoff_dir


def _print_session_header(
    command: str,
    mode: str,
    train_count: int,
    val_count: int,
    handoff_dir: Path,
    extra_lines: list[str] | None = None,
) -> None:
    print("=== Yield Farming Interactive Optimization ===")
    print(f"Command: {command}")
    print(f"Mode: {mode}")
    print(f"Training examples: {train_count}")
    print(f"Validation examples: {val_count}")
    print(f"Handoff directory: {handoff_dir}")
    if extra_lines:
        for line in extra_lines:
            print(line)


def _print_agent_instructions_start() -> None:
    print(
        """
================================================================================
INTERACTIVE PROMPT OPTIMIZATION - AGENT INSTRUCTIONS
================================================================================

ROLE: You are the "reflection engine" for a yield farming classifier. You
analyze classification failures, identify patterns, and propose targeted prompt
changes to improve accuracy.

WHAT THE SYSTEM DOES:
The yield farming classifier reads crypto Telegram/Discord messages and outputs
"yes" or "no" - whether the message describes an actionable yield farming
opportunity. A system prompt controls the LLM's classification behavior. Your
goal is to iteratively refine this prompt to maximize classification accuracy.

ITERATION LIFECYCLE:
  1. System evaluates current prompt against labeled examples
  2. System writes a failure analysis report (report.md)
  3. YOU read the report, analyze failure patterns, write a revised prompt
  4. System evaluates the new prompt and accepts it if it scores better

THE CYCLE PAUSES after step 2, waiting for you.

DIRECTORY STRUCTURE:
  handoff/
    session_state.json       # Iteration counter, score history
    gepa_state.bin           # Optimizer state (do not modify)
    iteration_001/
      report.md              # Failure analysis - READ THIS
      prompt_used.md         # The prompt that was evaluated
      new_prompt.md          # YOUR revised prompt - WRITE THIS

YOUR WORKFLOW:
  Step 1: Read the latest iteration_NNN/report.md
          Look at: aggregate scores, false positives, false negatives,
          edge cases, and prompt refinement suggestions.

  Step 2: Analyze failure patterns
          - False positives (model says yes, should be no): prompt too permissive
          - False negatives (model says no, should be yes): prompt too restrictive
          - Source groupings matter:
            * "agreed" = clear-cut examples, failures here = clear prompt gaps
            * "disagreed" = ambiguous cases, harder
            * "low_confidence" = borderline, failures expected

  Step 3: Write the revised prompt to iteration_NNN/new_prompt.md
          CRITICAL RULES:
          - Write the ENTIRE prompt (full replacement, not a diff)
          - Plain text only (no markdown headers, no frontmatter)
          - File goes in the CURRENT iteration directory
          - Prompt must produce single-token output (yes or no)
          - End with "Respond with only: yes or no"

  Step 4: Run: make optimize-resume (or make optimize-resume-test)

STRATEGY TIPS:
  - Be surgical: change one thing at a time
  - Address the highest-impact failure pattern first
  - Use exact language from failure examples in your rules
  - Balance FP and FN fixes (tightening one often loosens the other)
  - Preserve what works - don't rewrite the whole prompt

GEPA ACCEPTANCE CRITERION:
  GEPA evaluates on a mini-batch, not the full dataset. Your prompt is accepted
  only if it scores strictly higher on that mini-batch. Rejection doesn't mean
  your prompt is worse overall - try a different approach.

SCORE INTERPRETATION:
  - Accuracy: fraction of examples classified correctly (1.0 = perfect)
  - False positives: messages wrongly classified as "yes"
  - False negatives: genuine opportunities the model missed
  - Delta: change from previous iteration (positive = improvement)

================================================================================
""".strip()
    )


def _print_next_steps_start(report_path: Path, new_prompt_path: Path) -> None:
    print(
        f"""
================================================================================
EVALUATION COMPLETE - YOUR TURN
================================================================================

  1. Read the failure report: {report_path}
  2. Analyze false positives and false negatives
  3. Write your revised prompt to: {new_prompt_path}
  4. Run: make optimize-resume (or make optimize-resume-test)

================================================================================
""".strip()
    )


def _print_agent_instructions_resume(
    session_state: SessionState,
    report_path: Path,
    new_prompt_path: Path,
) -> None:
    print("=" * 80)
    print(f"ITERATION {session_state.current_iteration} COMPLETE - NEXT STEPS")
    print("=" * 80)
    print()
    print("SCORE HISTORY:")
    if not session_state.score_history:
        print("  No scores recorded yet")
    else:
        print("  Iteration | Accuracy | Delta")
        for record in session_state.score_history:
            delta = "N/A"
            if record.delta_from_previous is not None:
                delta = f"{record.delta_from_previous:+.4f}"
            print(f"  {record.iteration:9d} | {record.aggregate_accuracy:8.4f} | {delta}")
    print()
    print("WHAT TO DO NOW:")
    print(f"  1. Read the failure report: {report_path}")
    print("  2. Analyze false positives and false negatives")
    print("  3. Write your revised prompt (full replacement, plain text) to:")
    print(f"     {new_prompt_path}")
    print("  4. Run: make optimize-resume (or make optimize-resume-test)")
    print()
    print("REMINDERS:")
    print("  - Write the ENTIRE prompt to new_prompt.md (not a diff)")
    print("  - Plain text only, no markdown headers")
    print('  - End with "Respond with only: yes or no"')
    print("  - Be surgical: change one thing at a time")
    print()
    print("=" * 80)


def _run_with_error_handling(args: argparse.Namespace, **run_kwargs: Any) -> Any:
    try:
        return run_optimization(**run_kwargs)
    except Exception as exc:
        if not args.mock and is_probable_missing_api_key(exc):
            print("\nOptimization failed: missing or invalid API credentials.")
            print("Set the provider API key (for example OPENAI_API_KEY) and retry.")
            raise SystemExit(1) from exc
        print(f"\nOptimization failed: {exc}")
        raise SystemExit(1) from exc


def _start_session(args: argparse.Namespace) -> int:
    handoff_dir = _resolve_handoff_dir(args)
    handoff_dir.mkdir(parents=True, exist_ok=True)

    state_path = handoff_dir / "session_state.json"
    gepa_state_path = handoff_dir / "gepa_state.bin"
    if state_path.exists() or gepa_state_path.exists():
        print("Interactive session state already exists in the handoff directory.")
        print(f"Use `resume` or choose a different --handoff-dir: {handoff_dir}")
        return 1

    if not args.prompt.exists():
        print(f"Seed prompt file not found: {args.prompt}")
        return 1

    seed_candidate = _load_seed_candidate(args.prompt)
    train_set, val_set, evaluator, mode = _load_session_resources(args)

    session_state = SessionState(
        current_iteration=1,
        handoff_dir=handoff_dir,
        run_dir=handoff_dir,
        session_metadata={"interactive_mode": "start"},
    )
    handoff_manager = HandoffManager(handoff_dir, session_state)
    report_generator = ReportGenerator()
    interactive_proposer = InteractiveProposer(handoff_manager, session_state, report_generator)
    minibatch_size = _TEST_MINIBATCH_SIZE if args.test else REFLECTION_MINIBATCH_SIZE
    config = _build_config(
        interactive_proposer,
        handoff_dir,
        minibatch_size=minibatch_size,
    )

    extra_lines: list[str] = []
    if args.test:
        extra_lines.append(
            "[TEST MODE] Using reduced dataset "
            f"({_TEST_VAL_SET_SIZE} val examples, minibatch={_TEST_MINIBATCH_SIZE})"
        )

    _print_session_header(
        command="start",
        mode=mode,
        train_count=len(train_set),
        val_count=len(val_set),
        handoff_dir=handoff_dir,
        extra_lines=extra_lines,
    )
    _print_agent_instructions_start()
    _run_with_error_handling(
        args,
        seed_candidate=seed_candidate,
        evaluator=evaluator,
        dataset=train_set,
        valset=val_set,
        objective=_OBJECTIVE,
        background=_BACKGROUND,
        config=config,
    )

    report_path = handoff_manager.resolve_report_path()
    new_prompt_path = handoff_manager.resolve_new_prompt_path()
    _print_next_steps_start(report_path, new_prompt_path)
    return 0


def _resume_session(args: argparse.Namespace) -> int:
    handoff_dir = _resolve_handoff_dir(args)
    state_path = handoff_dir / "session_state.json"
    gepa_state_path = handoff_dir / "gepa_state.bin"
    if not state_path.exists():
        print(f"Session state not found: {state_path}")
        print("Run `start` first or provide the correct --handoff-dir.")
        return 1
    if not gepa_state_path.exists():
        print(f"GEPA state not found: {gepa_state_path}")
        print("Run `start` first so resume can load optimizer state.")
        return 1

    try:
        session_state = load_session_state(state_path)
    except Exception as exc:
        print(f"Failed to load session state: {exc}")
        return 1

    session_state.handoff_dir = handoff_dir
    session_state.run_dir = handoff_dir
    session_state.session_metadata["interactive_mode"] = "resume"

    handoff_manager = HandoffManager(handoff_dir, session_state)
    new_prompt_path = handoff_manager.resolve_new_prompt_path()
    if not new_prompt_path.exists():
        print(f"Resume failed: missing new prompt file at {new_prompt_path}")
        print("Write the revised prompt to new_prompt.md for this iteration, then retry.")
        return 1

    if not BEST_PROMPT_PATH.exists():
        print(f"Seed prompt file not found: {BEST_PROMPT_PATH}")
        return 1

    seed_candidate = _load_seed_candidate(BEST_PROMPT_PATH)
    proposed_prompt = new_prompt_path.read_text(encoding="utf-8").strip()

    train_set, val_set, evaluator, mode = _load_session_resources(args)

    report_generator = ReportGenerator()
    interactive_proposer = InteractiveProposer(handoff_manager, session_state, report_generator)
    minibatch_size = _TEST_MINIBATCH_SIZE if args.test else REFLECTION_MINIBATCH_SIZE
    config = _build_config(
        interactive_proposer,
        handoff_dir,
        minibatch_size=minibatch_size,
    )

    extra_lines = [f"Resuming iteration: {session_state.current_iteration}"]
    if args.test:
        extra_lines.append(
            "[TEST MODE] Using reduced dataset "
            f"({_TEST_VAL_SET_SIZE} val examples, minibatch={_TEST_MINIBATCH_SIZE})"
        )

    _print_session_header(
        command="resume",
        mode=mode,
        train_count=len(train_set),
        val_count=len(val_set),
        handoff_dir=handoff_dir,
        extra_lines=extra_lines,
    )
    result = _run_with_error_handling(
        args,
        seed_candidate=seed_candidate,
        evaluator=evaluator,
        dataset=train_set,
        valset=val_set,
        objective=_OBJECTIVE,
        background=_BACKGROUND,
        config=config,
    )

    best_candidate = getattr(result, "best_candidate", {})
    best_prompt = ""
    if isinstance(best_candidate, dict):
        best_prompt = str(best_candidate.get("system_prompt", "")).strip()

    accepted = bool(best_prompt) and best_prompt == proposed_prompt
    status_text = "accepted" if accepted else "rejected"
    best_score = extract_best_score(result)

    print(f"\nResume outcome: {status_text}")
    if best_score is None:
        print("New score: <unavailable>")
    else:
        print(f"New score: {best_score:.4f}")

    report_path = handoff_manager.resolve_report_path()
    next_new_prompt_path = handoff_manager.resolve_new_prompt_path()
    _print_agent_instructions_resume(session_state, report_path, next_new_prompt_path)
    return 0


def main() -> int:
    args = parse_args()
    if args.command == "start":
        return _start_session(args)
    return _resume_session(args)


if __name__ == "__main__":
    raise SystemExit(main())
