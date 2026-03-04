"""Tests for evaluator protocol conformance and mock evaluator behavior."""

from __future__ import annotations

from inspect import signature
from typing import Any

from optimize_anything.evaluators.base import EvaluatorFn
from optimize_anything.evaluators.templates import mock_evaluator


def test_mock_evaluator_returns_float_and_dict_tuple() -> None:
    evaluator = mock_evaluator()

    result = evaluator(
        {"system_prompt": "Classify sentiment."}, {"text": "Great", "label": "positive"}
    )

    assert isinstance(result, tuple)
    assert len(result) == 2
    score, asi = result
    assert isinstance(score, float)
    assert isinstance(asi, dict)


def test_mock_evaluator_is_deterministic_for_same_input() -> None:
    evaluator = mock_evaluator(base_score=0.7)
    candidate = {"field": "same text"}
    example: dict[str, Any] = {"any": "value"}

    first = evaluator(candidate, example)
    second = evaluator(candidate, example)

    assert first == second


def test_mock_evaluator_score_is_between_zero_and_one() -> None:
    evaluator = mock_evaluator(base_score=0.9)

    score, _ = evaluator({"content": "x" * 5000}, {"unused": True})

    assert 0.0 <= score <= 1.0


def test_mock_evaluator_asi_contains_expected_keys() -> None:
    evaluator = mock_evaluator(base_score=0.3)

    _, asi = evaluator({"field": "abc"}, {"ignored": "value"})

    assert set(asi.keys()) == {"char_count", "base_score", "mock"}
    assert asi["mock"] is True


def test_mock_evaluator_factory_returns_callable_with_evaluator_signature() -> None:
    evaluator: EvaluatorFn = mock_evaluator()

    assert callable(evaluator)
    params = list(signature(evaluator).parameters)
    assert params == ["candidate", "example"]
