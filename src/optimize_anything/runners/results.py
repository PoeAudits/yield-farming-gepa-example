from __future__ import annotations

from typing import Any

__all__ = [
    "extract_best_score",
    "extract_summary",
    "is_probable_missing_api_key",
]


def extract_best_score(result: Any) -> float | None:
    """Extract the best numeric score from an optimizer result object."""
    for key in ("best_score", "score", "val_score"):
        value = getattr(result, key, None)
        if isinstance(value, int | float):
            return float(value)
    return None


def extract_summary(result: Any) -> str:
    """Extract a human-readable summary string from an optimizer result object."""
    summary_value = getattr(result, "summary", None)
    if isinstance(summary_value, str) and summary_value.strip():
        return summary_value

    stats_value = getattr(result, "stats", None)
    if stats_value is not None:
        return str(stats_value)

    return "No summary provided by optimizer."


def is_probable_missing_api_key(error: Exception) -> bool:
    """Check whether an exception message suggests a missing or invalid API key."""
    message = str(error).lower()
    signals = (
        "api key",
        "missing api key",
        "authentication",
        "unauthorized",
        "openai_api_key",
    )
    return any(signal in message for signal in signals)
