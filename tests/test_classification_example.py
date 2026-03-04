"""Tests for the classification example pipeline."""

from __future__ import annotations

from types import SimpleNamespace
from typing import Any
from unittest.mock import patch

import pytest

classification_mod = pytest.importorskip("classification")

from classification.data import load_train_set, load_val_set  # noqa: E402
from classification.evaluator import mock_evaluator  # noqa: E402

from optimize_anything.config.presets import quick_preset  # noqa: E402
from optimize_anything.runners.optimize import run_optimization  # noqa: E402

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_SEED_CANDIDATE: dict[str, str] = {
    "system_prompt": (
        "Classify the following text as positive, negative, or neutral. "
        "Respond with only the label."
    )
}

# ---------------------------------------------------------------------------
# Dataset tests
# ---------------------------------------------------------------------------


def test_dataset_loads_correctly() -> None:
    """Train and val sets load and each item has 'text' and 'label' keys with valid labels."""
    train_set = load_train_set()
    val_set = load_val_set()
    valid_labels = {"positive", "negative", "neutral"}

    assert isinstance(train_set, list), "train_set must be a list"
    assert isinstance(val_set, list), "val_set must be a list"
    assert len(train_set) > 0, "train_set must not be empty"
    assert len(val_set) > 0, "val_set must not be empty"

    for item in train_set:
        assert "text" in item, f"train item missing 'text' key: {item}"
        assert "label" in item, f"train item missing 'label' key: {item}"
        assert item["label"] in valid_labels, (
            f"train item has invalid label {item['label']!r}; expected one of {valid_labels}"
        )

    for item in val_set:
        assert "text" in item, f"val item missing 'text' key: {item}"
        assert "label" in item, f"val item missing 'label' key: {item}"
        assert item["label"] in valid_labels, (
            f"val item has invalid label {item['label']!r}; expected one of {valid_labels}"
        )


def test_dataset_sizes() -> None:
    """Train set has exactly 12 examples and val set has at least 6 examples."""
    train_set = load_train_set()
    val_set = load_val_set()

    assert len(train_set) == 12, f"expected 12 training examples, got {len(train_set)}"
    assert len(val_set) >= 6, f"expected at least 6 validation examples, got {len(val_set)}"


# ---------------------------------------------------------------------------
# Mock evaluator tests
# ---------------------------------------------------------------------------


def test_mock_evaluator_returns_valid_type() -> None:
    """mock_evaluator returns tuple[float, dict] and score is in [0.0, 1.0]."""
    result = mock_evaluator(_SEED_CANDIDATE, {"text": "Great product!", "label": "positive"})

    assert isinstance(result, tuple), "mock_evaluator must return a tuple"
    assert len(result) == 2, "mock_evaluator must return a 2-tuple"

    score, info = result

    assert isinstance(score, float), f"score must be a float, got {type(score).__name__}"
    assert 0.0 <= score <= 1.0, f"score must be in [0.0, 1.0], got {score}"
    assert isinstance(info, dict), f"second element must be a dict, got {type(info).__name__}"


def test_mock_evaluator_is_deterministic() -> None:
    """Calling mock_evaluator twice with identical inputs produces identical output."""
    candidate = _SEED_CANDIDATE.copy()
    example: dict[str, Any] = {"text": "Absolutely fantastic experience.", "label": "positive"}

    result_a = mock_evaluator(candidate, example)
    result_b = mock_evaluator(candidate, example)

    assert result_a == result_b, (
        f"mock_evaluator must be deterministic: got {result_a!r} then {result_b!r}"
    )


# ---------------------------------------------------------------------------
# Seed candidate test
# ---------------------------------------------------------------------------


def test_seed_candidate_is_valid() -> None:
    """The local seed candidate constant is a dict[str, str] with a 'system_prompt' key."""
    candidate = _SEED_CANDIDATE

    assert isinstance(candidate, dict), "seed_candidate must be a dict"
    assert all(isinstance(k, str) and isinstance(v, str) for k, v in candidate.items()), (
        "seed_candidate must have str keys and str values"
    )
    assert "system_prompt" in candidate, "seed_candidate must contain a 'system_prompt' key"
    assert candidate["system_prompt"], "seed_candidate 'system_prompt' must not be empty"


# ---------------------------------------------------------------------------
# Pipeline integration test (mock)
# ---------------------------------------------------------------------------


def test_pipeline_with_mock() -> None:
    """Full pipeline integration: run_optimization completes with a mocked GEPA call."""
    train_set = load_train_set()
    val_set = load_val_set()
    config = quick_preset()

    mock_result = SimpleNamespace(best_candidate=_SEED_CANDIDATE, best_score=0.75)

    with patch(
        "optimize_anything.runners.optimize.gepa_optimize_anything", return_value=mock_result
    ):
        result = run_optimization(
            seed_candidate=_SEED_CANDIDATE,
            evaluator=mock_evaluator,
            dataset=train_set,
            valset=val_set,
            objective=(
                "Maximize exact-match sentiment classification accuracy for labels "
                "positive, negative, and neutral."
            ),
            background=(
                "This is a prototype sentiment classifier optimized on small train/val "
                "datasets for quick iteration."
            ),
            config=config,
        )

    assert result is mock_result, "run_optimization must return the result from GEPA"
    assert result.best_candidate == _SEED_CANDIDATE
    assert result.best_score == 0.75
