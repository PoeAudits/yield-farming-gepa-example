"""Tests for the yield_farming_classifier example evaluators."""

from __future__ import annotations

from inspect import signature
from typing import Any

import pytest

yf_mod = pytest.importorskip("examples.yield_farming_classifier")

from examples.yield_farming_classifier.evaluator import (  # noqa: E402
    mock_evaluator,
    real_evaluator,
)

_SEED_CANDIDATE: dict[str, str] = {
    "system_prompt": (
        "Classify whether the message is a yield farming opportunity. Respond yes or no."
    )
}

_EXAMPLE: dict[str, Any] = {
    "text": "Stake ETH and earn 5% APY on Lido",
    "label": "yes",
    "explanation": "",
    "predicted_category": "",
    "confidence": "",
    "source_file": "agreed",
}


# ---------------------------------------------------------------------------
# Signature conformance — GEPA calls evaluators with example= keyword arg
# ---------------------------------------------------------------------------


def test_real_evaluator_accepts_example_keyword() -> None:
    """real_evaluator must accept 'example' as a keyword argument (GEPA passes it this way)."""
    params = signature(real_evaluator).parameters
    assert "example" in params, (
        f"real_evaluator must have an 'example' parameter for GEPA compatibility; "
        f"found params: {list(params)}"
    )


def test_mock_evaluator_accepts_example_keyword() -> None:
    """mock_evaluator must accept 'example' as a keyword argument (GEPA passes it this way)."""
    params = signature(mock_evaluator).parameters
    assert "example" in params, (
        f"mock_evaluator must have an 'example' parameter for GEPA compatibility; "
        f"found params: {list(params)}"
    )


# ---------------------------------------------------------------------------
# Mock evaluator behavior
# ---------------------------------------------------------------------------


def test_mock_evaluator_returns_valid_type() -> None:
    """mock_evaluator returns tuple[float, dict] with score in [0.0, 1.0]."""
    result = mock_evaluator(_SEED_CANDIDATE, _EXAMPLE)

    assert isinstance(result, tuple)
    assert len(result) == 2
    score, asi = result
    assert isinstance(score, float)
    assert 0.0 <= score <= 1.0
    assert isinstance(asi, dict)


def test_mock_evaluator_is_deterministic() -> None:
    """Calling mock_evaluator twice with identical inputs produces identical output."""
    result_a = mock_evaluator(_SEED_CANDIDATE, _EXAMPLE)
    result_b = mock_evaluator(_SEED_CANDIDATE, _EXAMPLE)
    assert result_a == result_b


def test_mock_evaluator_callable_with_keyword() -> None:
    """mock_evaluator works when called with example as a keyword argument (GEPA style)."""
    score, asi = mock_evaluator(_SEED_CANDIDATE, example=_EXAMPLE)
    assert isinstance(score, float)
    assert isinstance(asi, dict)


def test_real_evaluator_callable_with_keyword() -> None:
    """real_evaluator works when called with example as a keyword argument (GEPA style).

    This test does NOT make LLM calls — it verifies the function accepts the
    keyword without TypeError before hitting the API call.
    """
    # We only verify the signature is callable with the keyword; the function
    # will fail at the litellm.completion call, which we catch.
    try:
        real_evaluator(_SEED_CANDIDATE, example=_EXAMPLE)
    except TypeError:
        pytest.fail("real_evaluator must accept 'example' as a keyword argument")
    except Exception:
        # Any other exception (API error, network, etc.) is fine — the
        # signature accepted the keyword arg successfully.
        pass
