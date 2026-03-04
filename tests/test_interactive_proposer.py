"""Tests for SessionState, HandoffManager, and InteractiveProposer."""

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
from tests.conftest import build_score_record, build_session_state

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

_SAMPLE_CANDIDATE: dict[str, str] = {"system_prompt": "You are a helpful assistant."}

_SAMPLE_DATASET: dict[str, list[dict[str, Any]]] = {
    "system_prompt": [{"text": "example text", "label": "yes"}],
}


# ---------------------------------------------------------------------------
# SessionState — serialization round-trip
# ---------------------------------------------------------------------------


def test_session_state_round_trip(tmp_path: Path) -> None:
    """SessionState saved and loaded produces identical field values."""
    handoff_dir = tmp_path / "handoff"
    run_dir = tmp_path / "run"
    state = build_session_state(
        tmp_path,
        iteration=1,
        score_history=[build_score_record(1, 0.85, fp_count=2, fn_count=3, delta=0.05)],
        session_metadata={"run_id": "test-run-001", "model": "gpt-4"},
        handoff_dir=handoff_dir,
        run_dir=run_dir,
    )

    save_path = save_session_state(state, tmp_path)
    loaded = load_session_state(save_path)

    assert loaded.current_iteration == state.current_iteration
    assert loaded.handoff_dir == state.handoff_dir
    assert loaded.run_dir == state.run_dir
    assert loaded.session_metadata == state.session_metadata
    assert len(loaded.score_history) == len(state.score_history)

    original_record = state.score_history[0]
    loaded_record = loaded.score_history[0]
    assert loaded_record.iteration == original_record.iteration
    assert loaded_record.aggregate_accuracy == original_record.aggregate_accuracy
    assert loaded_record.false_positive_count == original_record.false_positive_count
    assert loaded_record.false_negative_count == original_record.false_negative_count
    assert loaded_record.delta_from_previous == original_record.delta_from_previous


def test_session_state_round_trip_empty_history(tmp_path: Path) -> None:
    """SessionState with no score history survives serialization."""
    state = SessionState(
        current_iteration=0,
        score_history=[],
        handoff_dir=tmp_path / "handoff",
        run_dir=tmp_path / "run",
        session_metadata={},
    )
    save_path = save_session_state(state, tmp_path)
    loaded = load_session_state(save_path)

    assert loaded.current_iteration == 0
    assert loaded.score_history == []
    assert loaded.session_metadata == {}


def test_save_session_state_creates_file(tmp_path: Path) -> None:
    """save_session_state writes a JSON file at the expected path."""
    state = SessionState(current_iteration=3)
    save_path = save_session_state(state, tmp_path)

    assert save_path.exists()
    assert save_path.suffix == ".json"


def test_save_session_state_accepts_json_path_directly(tmp_path: Path) -> None:
    """save_session_state accepts a direct .json file path."""
    json_path = tmp_path / "custom_name.json"
    state = SessionState(current_iteration=5)
    save_path = save_session_state(state, json_path)

    assert save_path == json_path
    assert save_path.exists()


# ---------------------------------------------------------------------------
# HandoffManager — directory creation and path resolution
# ---------------------------------------------------------------------------


def test_handoff_manager_creates_base_dir(tmp_path: Path) -> None:
    """HandoffManager creates the base handoff directory on init."""
    base_dir = tmp_path / "handoff"
    state = SessionState(current_iteration=1)

    assert not base_dir.exists()
    HandoffManager(base_dir, state)
    assert base_dir.is_dir()


def test_handoff_manager_zero_padded_iteration_dir(tmp_path: Path) -> None:
    """resolve_iteration_dir uses three-digit zero-padded numbering."""
    state = SessionState(current_iteration=1)
    manager = HandoffManager(tmp_path / "handoff", state)

    iteration_dir = manager.resolve_iteration_dir()
    assert iteration_dir.name == "iteration_001"


def test_handoff_manager_iteration_dir_for_different_values(tmp_path: Path) -> None:
    """Zero-padding applies correctly to single and double digit iterations."""
    state = SessionState(current_iteration=5)
    manager = HandoffManager(tmp_path / "handoff", state)

    assert manager.resolve_iteration_dir().name == "iteration_005"
    assert manager.resolve_iteration_dir(iteration=12).name == "iteration_012"
    assert manager.resolve_iteration_dir(iteration=100).name == "iteration_100"


def test_handoff_manager_resolve_report_path(tmp_path: Path) -> None:
    """resolve_report_path returns Path ending in report.md inside iteration dir."""
    state = SessionState(current_iteration=1)
    manager = HandoffManager(tmp_path / "handoff", state)

    report_path = manager.resolve_report_path()
    assert report_path.name == "report.md"
    assert report_path.parent.name == "iteration_001"


def test_handoff_manager_resolve_prompt_used_path(tmp_path: Path) -> None:
    """resolve_prompt_used_path returns Path ending in prompt_used.md inside iteration dir."""
    state = SessionState(current_iteration=2)
    manager = HandoffManager(tmp_path / "handoff", state)

    prompt_used_path = manager.resolve_prompt_used_path()
    assert prompt_used_path.name == "prompt_used.md"
    assert prompt_used_path.parent.name == "iteration_002"


def test_handoff_manager_resolve_new_prompt_path(tmp_path: Path) -> None:
    """resolve_new_prompt_path returns Path ending in new_prompt.md inside iteration dir."""
    state = SessionState(current_iteration=3)
    manager = HandoffManager(tmp_path / "handoff", state)

    new_prompt_path = manager.resolve_new_prompt_path()
    assert new_prompt_path.name == "new_prompt.md"
    assert new_prompt_path.parent.name == "iteration_003"


def test_handoff_manager_advance_iteration(tmp_path: Path) -> None:
    """advance_iteration increments current_iteration and creates the new directory."""
    state = SessionState(current_iteration=1)
    manager = HandoffManager(tmp_path / "handoff", state)

    advanced_dir = manager.advance_iteration()
    assert state.current_iteration == 2
    assert advanced_dir.name == "iteration_002"
    assert advanced_dir.is_dir()


# ---------------------------------------------------------------------------
# InteractiveProposer — start mode
# ---------------------------------------------------------------------------


def test_interactive_proposer_start_mode_returns_candidate_unchanged(tmp_path: Path) -> None:
    """In start mode, the proposer returns the input candidate dict unchanged."""
    state = SessionState(current_iteration=1)
    manager = HandoffManager(tmp_path / "handoff", state)
    proposer = InteractiveProposer(manager, state, ReportGenerator())

    result = proposer(_SAMPLE_CANDIDATE, _SAMPLE_DATASET, ["system_prompt"])
    assert result == _SAMPLE_CANDIDATE


def test_interactive_proposer_start_mode_writes_report(tmp_path: Path) -> None:
    """In start mode, report.md is created at the iteration directory."""
    state = SessionState(current_iteration=1)
    manager = HandoffManager(tmp_path / "handoff", state)
    proposer = InteractiveProposer(manager, state, ReportGenerator())

    proposer(_SAMPLE_CANDIDATE, _SAMPLE_DATASET, ["system_prompt"])

    report_path = tmp_path / "handoff" / "iteration_001" / "report.md"
    assert report_path.exists()
    assert "# Interactive Failure Analysis Report" in report_path.read_text(encoding="utf-8")


def test_interactive_proposer_start_mode_writes_prompt_used(tmp_path: Path) -> None:
    """In start mode, prompt_used.md is written with candidate content."""
    state = SessionState(current_iteration=1)
    manager = HandoffManager(tmp_path / "handoff", state)
    proposer = InteractiveProposer(manager, state, ReportGenerator())

    proposer(_SAMPLE_CANDIDATE, _SAMPLE_DATASET, ["system_prompt"])

    prompt_used_path = tmp_path / "handoff" / "iteration_001" / "prompt_used.md"
    assert prompt_used_path.exists()
    content = prompt_used_path.read_text(encoding="utf-8")
    assert "## system_prompt" in content
    assert "You are a helpful assistant." in content


def test_interactive_proposer_start_mode_saves_session_state(tmp_path: Path) -> None:
    """In start mode, session state JSON is written to the handoff directory."""
    state = SessionState(current_iteration=1)
    manager = HandoffManager(tmp_path / "handoff", state)
    proposer = InteractiveProposer(manager, state, ReportGenerator())

    proposer(_SAMPLE_CANDIDATE, _SAMPLE_DATASET, ["system_prompt"])

    state_path = tmp_path / "handoff" / "session_state.json"
    assert state_path.exists()


def test_interactive_proposer_start_mode_stores_reflective_dataset(tmp_path: Path) -> None:
    """In start mode, the reflective dataset is stored in session metadata."""
    state = SessionState(current_iteration=1)
    manager = HandoffManager(tmp_path / "handoff", state)
    proposer = InteractiveProposer(manager, state, ReportGenerator())

    proposer(_SAMPLE_CANDIDATE, _SAMPLE_DATASET, ["system_prompt"])

    assert "reflective_dataset" in state.session_metadata
    stored = state.session_metadata["reflective_dataset"]
    assert "system_prompt" in stored


# ---------------------------------------------------------------------------
# InteractiveProposer — resume mode
# ---------------------------------------------------------------------------


def test_interactive_proposer_resume_mode_reads_new_prompt(tmp_path: Path) -> None:
    """Resume mode reads new_prompt.md and returns a dict keyed to the first component."""
    state = SessionState(current_iteration=1)
    manager = HandoffManager(tmp_path / "handoff", state)

    # Pre-write the new_prompt.md file to simulate a human edit
    iteration_dir = tmp_path / "handoff" / "iteration_001"
    iteration_dir.mkdir(parents=True, exist_ok=True)
    new_prompt_content = "You are a revised, helpful assistant."
    (iteration_dir / "new_prompt.md").write_text(new_prompt_content, encoding="utf-8")

    proposer = InteractiveProposer(manager, state, ReportGenerator())
    result = proposer(_SAMPLE_CANDIDATE, _SAMPLE_DATASET, ["system_prompt"])

    assert result == {"system_prompt": new_prompt_content}


def test_interactive_proposer_resume_mode_uses_first_component(tmp_path: Path) -> None:
    """Resume mode keys the returned candidate to components_to_update[0]."""
    state = SessionState(current_iteration=1)
    manager = HandoffManager(tmp_path / "handoff", state)

    iteration_dir = tmp_path / "handoff" / "iteration_001"
    iteration_dir.mkdir(parents=True, exist_ok=True)
    (iteration_dir / "new_prompt.md").write_text("New content here.", encoding="utf-8")

    proposer = InteractiveProposer(manager, state, ReportGenerator())
    result = proposer(_SAMPLE_CANDIDATE, _SAMPLE_DATASET, ["user_prompt", "system_prompt"])

    assert "user_prompt" in result
    assert result["user_prompt"] == "New content here."


# ---------------------------------------------------------------------------
# InteractiveProposer — error handling
# ---------------------------------------------------------------------------


def test_interactive_proposer_resume_mode_missing_file_raises(tmp_path: Path) -> None:
    """FileNotFoundError is raised when resume_mode is set but new_prompt.md is absent."""
    state = SessionState(
        current_iteration=1,
        session_metadata={"interactive_mode": "resume"},
    )
    manager = HandoffManager(tmp_path / "handoff", state)
    proposer = InteractiveProposer(manager, state, ReportGenerator())

    with pytest.raises(FileNotFoundError, match="new_prompt"):
        proposer(_SAMPLE_CANDIDATE, _SAMPLE_DATASET, ["system_prompt"])


def test_interactive_proposer_resume_flag_alternative(tmp_path: Path) -> None:
    """resume_mode=True in session_metadata also triggers the FileNotFoundError."""
    state = SessionState(
        current_iteration=1,
        session_metadata={"resume_mode": True},
    )
    manager = HandoffManager(tmp_path / "handoff", state)
    proposer = InteractiveProposer(manager, state, ReportGenerator())

    with pytest.raises(FileNotFoundError, match="new_prompt"):
        proposer(_SAMPLE_CANDIDATE, _SAMPLE_DATASET, ["system_prompt"])


def test_interactive_proposer_raises_on_empty_components(tmp_path: Path) -> None:
    """ValueError is raised when components_to_update is an empty list."""
    state = SessionState(current_iteration=1)
    manager = HandoffManager(tmp_path / "handoff", state)
    proposer = InteractiveProposer(manager, state, ReportGenerator())

    with pytest.raises(ValueError, match="components_to_update"):
        proposer(_SAMPLE_CANDIDATE, _SAMPLE_DATASET, [])
