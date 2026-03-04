"""Integration tests for the end-to-end interactive proposer flow.

These tests exercise the full pipeline — ReportGenerator + HandoffManager +
InteractiveProposer + SessionState — without making any real LLM calls.
All file system operations use the tmp_path fixture.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from optimize_anything.interactive import (
    HandoffManager,
    InteractiveProposer,
    ReportGenerator,
    SessionState,
    load_session_state,
    save_session_state,
)
from tests.conftest import build_score_record

# ---------------------------------------------------------------------------
# Shared test fixtures and constants
# ---------------------------------------------------------------------------

_SEED_CANDIDATE: dict[str, str] = {
    "system_prompt": (
        "Classify whether the message is a yield farming opportunity. Respond yes or no."
    )
}

_REFLECTIVE_DATASET: dict[str, list[dict[str, Any]]] = {
    "system_prompt": [
        {
            "Inputs": "Earn 12% APY by staking ETH on our platform — join now!",
            "Generated Outputs": "yes",
            "Feedback": (
                "expected: no, got: yes. False positive — marketing hype without protocol details."
            ),
        },
        {
            "Inputs": "Provide liquidity to USDC/ETH pool and earn 8% APR.",
            "Generated Outputs": "no",
            "Feedback": (
                "expected: yes, got: no. False negative — concrete yield opportunity missed."
            ),
        },
        {
            "Inputs": "Bitcoin is up today, great time to buy.",
            "Generated Outputs": "no",
            "Feedback": "expected: no, got: no. Correct.",
        },
    ]
}

_REFLECTIVE_DATASET_WITH_SOURCE: dict[str, list[dict[str, Any]]] = {
    "system_prompt": [
        {
            "Inputs": "Stake your SOL and earn 7% APY.",
            "Generated Outputs": "yes",
            "Feedback": "expected: no, got: yes. False positive due to vague phrasing.",
            "source_file": "telegram_channel_alpha.jsonl",
        },
        {
            "Inputs": "Deposit USDT to earn vault rewards.",
            "Generated Outputs": "no",
            "Feedback": "expected: yes, got: no. False negative — actionable yield opportunity.",
            "source_file": "discord_server_beta.jsonl",
        },
    ]
}

# ---------------------------------------------------------------------------
# Test 1: Report generator with realistic reflective dataset
# ---------------------------------------------------------------------------


def test_report_generator_with_realistic_gepa_dataset(tmp_path: Path) -> None:
    """ReportGenerator produces valid markdown from a realistic GEPA reflective dataset."""
    session_state = SessionState(
        current_iteration=2,
        score_history=[
            build_score_record(1, 0.72, fp_count=3, fn_count=4, delta=None),
            build_score_record(2, 0.79, fp_count=2, fn_count=2, delta=0.07),
        ],
        handoff_dir=tmp_path / "handoff",
        run_dir=tmp_path / "run",
    )
    raw_asi: dict[str, list[dict[str, Any]]] = {
        "system_prompt": [
            {
                "response": "yes",
                "expected": "no",
                "explanation": "Platform mentions APY but does not describe staking mechanics.",
                "confidence": "0.45",
                "source_file": "telegram_dump_01.jsonl",
            },
            {
                "response": "no",
                "expected": "yes",
                "explanation": "Liquidity provision is a concrete actionable yield step.",
                "confidence": "0.52",
                "source_file": "discord_dump_02.jsonl",
            },
            {},
        ]
    }

    report = ReportGenerator(raw_evaluation_asi=raw_asi).generate(
        candidate=_SEED_CANDIDATE,
        reflective_dataset=_REFLECTIVE_DATASET,
        session_state=session_state,
    )

    # Header section
    assert "# Interactive Failure Analysis Report" in report
    assert "## Header" in report
    assert "Iteration: 2" in report
    assert "system_prompt" in report

    # Aggregate scores section
    assert "## Aggregate scores" in report
    assert "0.7900" in report

    # Score history table
    assert "## Score history" in report
    assert "| 1 |" in report
    assert "| 2 |" in report
    assert "+0.0700" in report

    # False positives section
    assert "## False positives" in report
    assert "Earn 12% APY by staking ETH on our platform" in report

    # False negatives section
    assert "## False negatives" in report
    assert "Provide liquidity to USDC/ETH pool" in report

    # Suggestions section
    assert "## Prompt refinement suggestions" in report

    # GEPA acceptance note
    assert "## GEPA acceptance note" in report
    assert "new_sum > old_sum" in report


# ---------------------------------------------------------------------------
# Test 2: Full start-mode cycle
# ---------------------------------------------------------------------------


def test_full_start_mode_cycle(tmp_path: Path) -> None:
    """Start-mode: proposer writes report.md, prompt_used.md, session state, returns candidate."""
    handoff_dir = tmp_path / "handoff"
    session_state = SessionState(
        current_iteration=1,
        score_history=[
            build_score_record(1, 0.65, fp_count=5, fn_count=6, delta=None),
        ],
        handoff_dir=handoff_dir,
        run_dir=tmp_path / "run",
    )
    manager = HandoffManager(handoff_dir, session_state)
    report_generator = ReportGenerator()
    proposer = InteractiveProposer(manager, session_state, report_generator)

    result = proposer(_SEED_CANDIDATE, _REFLECTIVE_DATASET, ["system_prompt"])

    # Returned candidate is unchanged in start mode
    assert result == _SEED_CANDIDATE

    # report.md is written at the expected path
    report_path = handoff_dir / "iteration_001" / "report.md"
    assert report_path.exists(), "report.md must exist after start-mode call"
    report_content = report_path.read_text(encoding="utf-8")
    assert "# Interactive Failure Analysis Report" in report_content

    # prompt_used.md is written with candidate content
    prompt_used_path = handoff_dir / "iteration_001" / "prompt_used.md"
    assert prompt_used_path.exists(), "prompt_used.md must exist after start-mode call"
    prompt_used_content = prompt_used_path.read_text(encoding="utf-8")
    assert "## system_prompt" in prompt_used_content
    assert "Classify whether the message is a yield farming opportunity" in prompt_used_content

    # session_state.json is written to the handoff directory
    state_path = handoff_dir / "session_state.json"
    assert state_path.exists(), "session_state.json must exist after start-mode call"


def test_full_start_mode_cycle_persists_reflective_dataset(tmp_path: Path) -> None:
    """Start-mode stores the reflective dataset in session metadata for resume access."""
    handoff_dir = tmp_path / "handoff"
    session_state = SessionState(
        current_iteration=1,
        handoff_dir=handoff_dir,
        run_dir=tmp_path / "run",
    )
    manager = HandoffManager(handoff_dir, session_state)
    proposer = InteractiveProposer(manager, session_state, ReportGenerator())

    proposer(_SEED_CANDIDATE, _REFLECTIVE_DATASET, ["system_prompt"])

    assert "reflective_dataset" in session_state.session_metadata
    stored = session_state.session_metadata["reflective_dataset"]
    assert "system_prompt" in stored
    assert len(stored["system_prompt"]) == len(_REFLECTIVE_DATASET["system_prompt"])


def test_full_start_mode_cycle_session_state_round_trips(tmp_path: Path) -> None:
    """Session state written in start mode is re-loadable with correct iteration value."""
    handoff_dir = tmp_path / "handoff"
    session_state = SessionState(
        current_iteration=1,
        score_history=[build_score_record(1, 0.80, fp_count=1, fn_count=2, delta=None)],
        handoff_dir=handoff_dir,
        run_dir=tmp_path / "run",
    )
    manager = HandoffManager(handoff_dir, session_state)
    proposer = InteractiveProposer(manager, session_state, ReportGenerator())

    proposer(_SEED_CANDIDATE, _REFLECTIVE_DATASET, ["system_prompt"])

    state_path = handoff_dir / "session_state.json"
    loaded_state = load_session_state(state_path)
    assert loaded_state.current_iteration == 1
    assert len(loaded_state.score_history) == 1
    assert loaded_state.score_history[0].aggregate_accuracy == pytest.approx(0.80)


# ---------------------------------------------------------------------------
# Test 3: Simulated resume cycle
# ---------------------------------------------------------------------------


def test_simulated_resume_cycle_reads_new_prompt(tmp_path: Path) -> None:
    """Resume mode: proposer reads new_prompt.md and returns the correct candidate dict."""
    handoff_dir = tmp_path / "handoff"
    session_state = SessionState(
        current_iteration=1,
        handoff_dir=handoff_dir,
        run_dir=tmp_path / "run",
    )
    manager = HandoffManager(handoff_dir, session_state)

    # Simulate human writing the new prompt file
    iteration_dir = handoff_dir / "iteration_001"
    iteration_dir.mkdir(parents=True, exist_ok=True)
    new_prompt_text = (
        "You are a strict yield farming classifier. "
        "Respond only yes for messages with explicit APY/APR and a concrete protocol step. "
        "Respond no for general news, competition announcements, or vague claims."
    )
    (iteration_dir / "new_prompt.md").write_text(new_prompt_text, encoding="utf-8")

    proposer = InteractiveProposer(manager, session_state, ReportGenerator())
    result = proposer(_SEED_CANDIDATE, _REFLECTIVE_DATASET, ["system_prompt"])

    assert result == {"system_prompt": new_prompt_text}


def test_simulated_resume_cycle_maps_to_first_component(tmp_path: Path) -> None:
    """Resume mode maps new_prompt.md content to the first element of components_to_update."""
    handoff_dir = tmp_path / "handoff"
    session_state = SessionState(
        current_iteration=2,
        handoff_dir=handoff_dir,
        run_dir=tmp_path / "run",
    )
    manager = HandoffManager(handoff_dir, session_state)

    iteration_dir = handoff_dir / "iteration_002"
    iteration_dir.mkdir(parents=True, exist_ok=True)
    new_prompt_content = "Refined user prompt text for iteration 2."
    (iteration_dir / "new_prompt.md").write_text(new_prompt_content, encoding="utf-8")

    proposer = InteractiveProposer(manager, session_state, ReportGenerator())
    result = proposer(_SEED_CANDIDATE, _REFLECTIVE_DATASET, ["user_prompt", "system_prompt"])

    assert "user_prompt" in result
    assert result["user_prompt"] == new_prompt_content
    assert "system_prompt" not in result


def test_simulated_resume_cycle_report_written_for_next_iteration(tmp_path: Path) -> None:
    """After a start-mode pass, a resume cycle on iteration 2 writes the next report."""
    handoff_dir = tmp_path / "handoff"
    session_state = SessionState(
        current_iteration=1,
        score_history=[build_score_record(1, 0.70, fp_count=3, fn_count=4, delta=None)],
        handoff_dir=handoff_dir,
        run_dir=tmp_path / "run",
    )
    manager = HandoffManager(handoff_dir, session_state)
    report_generator = ReportGenerator()
    proposer = InteractiveProposer(manager, session_state, report_generator)

    # Start-mode pass: evaluate seed candidate
    start_result = proposer(_SEED_CANDIDATE, _REFLECTIVE_DATASET, ["system_prompt"])
    assert start_result == _SEED_CANDIDATE

    # Advance iteration to simulate GEPA moving forward
    manager.advance_iteration()
    assert session_state.current_iteration == 2

    # Human writes new_prompt.md for iteration 2
    iteration_dir = handoff_dir / "iteration_002"
    new_prompt_text = "Improved classifier prompt for iteration 2."
    (iteration_dir / "new_prompt.md").write_text(new_prompt_text, encoding="utf-8")

    # Resume-mode pass: proposer reads new_prompt.md
    resume_result = proposer(_SEED_CANDIDATE, _REFLECTIVE_DATASET, ["system_prompt"])
    assert resume_result == {"system_prompt": new_prompt_text}


# ---------------------------------------------------------------------------
# Test 4: SessionState iteration tracking
# ---------------------------------------------------------------------------


def test_session_state_iteration_tracking_across_cycles(tmp_path: Path) -> None:
    """Iteration counter increments correctly across simulated start/resume cycles."""
    handoff_dir = tmp_path / "handoff"
    session_state = SessionState(
        current_iteration=1,
        handoff_dir=handoff_dir,
        run_dir=tmp_path / "run",
    )
    manager = HandoffManager(handoff_dir, session_state)

    assert session_state.current_iteration == 1
    assert manager.resolve_iteration_dir().name == "iteration_001"

    # Simulate GEPA advancing after the first proposal cycle
    advanced_dir = manager.advance_iteration()
    assert session_state.current_iteration == 2
    assert advanced_dir.name == "iteration_002"

    advanced_dir_2 = manager.advance_iteration()
    assert session_state.current_iteration == 3
    assert advanced_dir_2.name == "iteration_003"


def test_session_state_iteration_tracking_persists_across_save_load(tmp_path: Path) -> None:
    """Iteration counter is preserved faithfully through save/load cycles."""
    handoff_dir = tmp_path / "handoff"
    session_state = SessionState(
        current_iteration=1,
        score_history=[build_score_record(1, 0.72, fp_count=3, fn_count=4, delta=None)],
        handoff_dir=handoff_dir,
        run_dir=tmp_path / "run",
    )
    manager = HandoffManager(handoff_dir, session_state)

    # Start mode — writes session_state.json at iteration 1
    proposer = InteractiveProposer(manager, session_state, ReportGenerator())
    proposer(_SEED_CANDIDATE, _REFLECTIVE_DATASET, ["system_prompt"])

    # Advance iteration and save again
    manager.advance_iteration()
    assert session_state.current_iteration == 2
    save_path = save_session_state(session_state, handoff_dir)

    loaded_state = load_session_state(save_path)
    assert loaded_state.current_iteration == 2
    assert len(loaded_state.score_history) == 1

    # Advance again from loaded state
    manager_reloaded = HandoffManager(handoff_dir, loaded_state)
    manager_reloaded.advance_iteration()
    assert loaded_state.current_iteration == 3


def test_session_state_score_history_accumulates(tmp_path: Path) -> None:
    """Score history grows correctly as IterationScoreRecords are appended."""
    session_state = SessionState(
        current_iteration=1,
        handoff_dir=tmp_path / "handoff",
        run_dir=tmp_path / "run",
    )

    record_1 = build_score_record(1, 0.70, fp_count=5, fn_count=4, delta=None)
    session_state.score_history.append(record_1)
    assert len(session_state.score_history) == 1

    record_2 = build_score_record(2, 0.77, fp_count=3, fn_count=3, delta=0.07)
    session_state.score_history.append(record_2)
    assert len(session_state.score_history) == 2
    assert session_state.score_history[-1].delta_from_previous == pytest.approx(0.07)

    record_3 = build_score_record(3, 0.83, fp_count=2, fn_count=2, delta=0.06)
    session_state.score_history.append(record_3)
    assert len(session_state.score_history) == 3
    assert session_state.score_history[-1].aggregate_accuracy == pytest.approx(0.83)


# ---------------------------------------------------------------------------
# Test 5: Report content assertions for required sections
# ---------------------------------------------------------------------------


def test_report_content_contains_all_required_sections(tmp_path: Path) -> None:
    """Generated report markdown contains every required section heading."""
    session_state = SessionState(
        current_iteration=1,
        score_history=[build_score_record(1, 0.75, fp_count=2, fn_count=3, delta=None)],
        handoff_dir=tmp_path / "handoff",
        run_dir=tmp_path / "run",
    )

    report = ReportGenerator().generate(
        candidate=_SEED_CANDIDATE,
        reflective_dataset=_REFLECTIVE_DATASET,
        session_state=session_state,
    )

    required_sections = [
        "# Interactive Failure Analysis Report",
        "## Header",
        "## Aggregate scores",
        "## Score history",
        "## False positives",
        "## False negatives",
        "## Edge cases / ambiguous examples",
        "## Prompt refinement suggestions",
        "## GEPA acceptance note",
    ]
    for section_heading in required_sections:
        assert section_heading in report, (
            f"Required section missing from report: {section_heading!r}"
        )


def test_report_content_fp_list_present(tmp_path: Path) -> None:
    """Report correctly identifies and includes false positive examples from the dataset."""
    session_state = SessionState(
        current_iteration=1,
        handoff_dir=tmp_path / "handoff",
        run_dir=tmp_path / "run",
    )

    report = ReportGenerator().generate(
        candidate=_SEED_CANDIDATE,
        reflective_dataset=_REFLECTIVE_DATASET,
        session_state=session_state,
    )

    assert "## False positives" in report
    # The first record is a false positive — its message text must appear under FP section
    assert "Earn 12% APY by staking ETH on our platform" in report


def test_report_content_fn_list_present(tmp_path: Path) -> None:
    """Report correctly identifies and includes false negative examples from the dataset."""
    session_state = SessionState(
        current_iteration=1,
        handoff_dir=tmp_path / "handoff",
        run_dir=tmp_path / "run",
    )

    report = ReportGenerator().generate(
        candidate=_SEED_CANDIDATE,
        reflective_dataset=_REFLECTIVE_DATASET,
        session_state=session_state,
    )

    assert "## False negatives" in report
    # The second record is a false negative — its message text must appear under FN section
    assert "Provide liquidity to USDC/ETH pool" in report


def test_report_content_score_history_renders_table_rows(tmp_path: Path) -> None:
    """Score history section renders a markdown table with correct values."""
    session_state = SessionState(
        current_iteration=2,
        score_history=[
            build_score_record(1, 0.68, fp_count=4, fn_count=5, delta=None),
            build_score_record(2, 0.74, fp_count=3, fn_count=3, delta=0.06),
        ],
        handoff_dir=tmp_path / "handoff",
        run_dir=tmp_path / "run",
    )

    report = ReportGenerator().generate(
        candidate=_SEED_CANDIDATE,
        reflective_dataset=_REFLECTIVE_DATASET,
        session_state=session_state,
    )

    assert "## Score history" in report
    assert "| 1 | 0.6800 |" in report
    assert "| 2 | 0.7400 | +0.0600 |" in report


def test_report_content_gepa_acceptance_note_present(tmp_path: Path) -> None:
    """GEPA acceptance note is always present and explains the mini-batch acceptance criterion."""
    session_state = SessionState(
        current_iteration=1,
        handoff_dir=tmp_path / "handoff",
        run_dir=tmp_path / "run",
    )

    report = ReportGenerator().generate(
        candidate=_SEED_CANDIDATE,
        reflective_dataset={},
        session_state=session_state,
    )

    assert "## GEPA acceptance note" in report
    assert "new_sum > old_sum" in report
    assert "mini-batch" in report


def test_report_content_with_source_file_grouping(tmp_path: Path) -> None:
    """Report groups FP/FN failures by source_file when the field is present."""
    session_state = SessionState(
        current_iteration=1,
        score_history=[build_score_record(1, 0.75, fp_count=1, fn_count=1, delta=None)],
        handoff_dir=tmp_path / "handoff",
        run_dir=tmp_path / "run",
    )

    report = ReportGenerator().generate(
        candidate=_SEED_CANDIDATE,
        reflective_dataset=_REFLECTIVE_DATASET_WITH_SOURCE,
        session_state=session_state,
    )

    assert "### Source: telegram_channel_alpha.jsonl" in report
    assert "### Source: discord_server_beta.jsonl" in report


def test_report_content_aggregate_scores_from_session_state(tmp_path: Path) -> None:
    """Aggregate scores section reflects the latest entry in score_history."""
    session_state = SessionState(
        current_iteration=3,
        score_history=[
            build_score_record(1, 0.60, fp_count=6, fn_count=7, delta=None),
            build_score_record(2, 0.70, fp_count=4, fn_count=4, delta=0.10),
            build_score_record(3, 0.82, fp_count=2, fn_count=1, delta=0.12),
        ],
        handoff_dir=tmp_path / "handoff",
        run_dir=tmp_path / "run",
    )

    report = ReportGenerator().generate(
        candidate=_SEED_CANDIDATE,
        reflective_dataset=_REFLECTIVE_DATASET,
        session_state=session_state,
    )

    assert "- Accuracy: 0.8200" in report
    assert "- False positives: 2" in report
    assert "- False negatives: 1" in report
