"""Pytest configuration and shared fixtures for optimize_anything tests."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from optimize_anything.evaluators.base import EvaluatorFn
from optimize_anything.interactive import IterationScoreRecord, SessionState


def build_score_record(
    iteration: int,
    accuracy: float,
    fp_count: int,
    fn_count: int,
    delta: float | None = None,
) -> IterationScoreRecord:
    return IterationScoreRecord(
        iteration=iteration,
        aggregate_accuracy=accuracy,
        false_positive_count=fp_count,
        false_negative_count=fn_count,
        delta_from_previous=delta,
    )


def build_session_state(
    tmp_path: Path,
    *,
    iteration: int = 1,
    score_history: list[IterationScoreRecord] | None = None,
    session_metadata: dict[str, Any] | None = None,
    handoff_dir: Path | None = None,
    run_dir: Path | None = None,
) -> SessionState:
    return SessionState(
        current_iteration=iteration,
        score_history=list(score_history or []),
        handoff_dir=handoff_dir or (tmp_path / "handoff"),
        run_dir=run_dir or (tmp_path / "run"),
        session_metadata=dict(session_metadata or {}),
    )


@pytest.fixture
def mock_evaluator() -> EvaluatorFn:
    """Return the canonical mock evaluator from the templates module."""
    from optimize_anything.evaluators.templates import mock_evaluator as _factory

    return _factory(base_score=1.0)
