"""Smoke tests: verify the package is importable and basic fixtures work."""

from __future__ import annotations

from typing import Any


def test_import_optimize_anything() -> None:
    """The top-level package must be importable."""
    import optimize_anything  # noqa: F401


def test_package_version() -> None:
    """The package exposes a __version__ string."""
    import optimize_anything

    assert isinstance(optimize_anything.__version__, str)
    assert optimize_anything.__version__  # non-empty


def test_mock_evaluator_signature(mock_evaluator) -> None:
    """mock_evaluator returns (float, dict) for a minimal candidate."""
    candidate = {"prompt": "hello world"}
    context: dict[str, Any] = {}

    score, metadata = mock_evaluator(candidate, context)

    assert isinstance(score, float)
    assert 0.0 <= score <= 1.0
    assert isinstance(metadata, dict)
    assert "char_count" in metadata


def test_mock_evaluator_deterministic(mock_evaluator) -> None:
    """Calling mock_evaluator twice with the same input yields identical results."""
    candidate = {"system": "You are a helpful assistant.", "user": "Tell me a joke."}
    context: dict[str, Any] = {"run_id": 42}

    result_a = mock_evaluator(candidate, context)
    result_b = mock_evaluator(candidate, context)

    assert result_a == result_b


def test_mock_evaluator_score_capped(mock_evaluator) -> None:
    """Score never exceeds 1.0 regardless of candidate length."""
    candidate = {"text": "x" * 1000}
    score, metadata = mock_evaluator(candidate, {})

    assert score == 1.0
    assert metadata["char_count"] == 1000
