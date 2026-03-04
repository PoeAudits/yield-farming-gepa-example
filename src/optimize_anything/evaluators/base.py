"""Core evaluator protocol definitions.

An evaluator is a callable with signature:

    (candidate: dict[str, str], example: dict[str, Any]) -> tuple[float, dict[str, Any]]

- ``candidate`` contains the current candidate artifact fields produced by optimization.
- ``example`` contains task-specific evaluation data (for example, input text and labels).
- The return tuple contains:
  1. A score in the range ``0.0`` to ``1.0``.
  2. An ASI payload (Actionable Side Information): structured metadata explaining why the
     candidate received that score. ASI is consumed by reflection loops to improve future
     candidate revisions.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

EvaluatorFn = Callable[[dict[str, str], dict[str, Any]], tuple[float, dict[str, Any]]]


def normalize_label(value: str) -> str:
    """Normalize a classification label to lowercase stripped form."""
    return value.strip().lower()


__all__ = ["EvaluatorFn", "normalize_label"]
