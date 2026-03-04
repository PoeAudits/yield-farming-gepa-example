from __future__ import annotations

import csv
import os
from pathlib import Path

__all__ = ["load_train_set", "load_val_set"]

_MESSAGE_REVIEW_DATA_PATH = Path(
    os.environ.get(
        "YIELD_FARMING_DATA_PATH", "/home/thomas/Overlord/files/Input/MessageReview030226"
    )
)

# (csv_filename, source_tag, label_column_name)
_CSV_SOURCES: tuple[tuple[str, str, str], ...] = (
    ("Valuable_Agreed.csv", "agreed", "keep"),
    ("Valuable_Disagreed.csv", "disagreed", "keep"),
    ("Filtered_Low_Confidence.csv", "low_confidence", "keep"),
)

_TRAIN_LABELS = {"1": "yes", "0": "no"}
# Annotator-assigned codes: A/B/C = "yes" (keep), X/Y/Z = "no" (filter).
_VAL_LABELS = {
    "A": "yes",
    "X": "no",
    "B": "yes",
    "Y": "no",
    "C": "yes",
    "Z": "no",
}


def _to_text(value: object) -> str:
    """Return a CSV field value as a string."""
    if value is None:
        return ""
    return str(value)


def _build_example(row: dict[str, str], *, label: str, source_file: str) -> dict[str, str]:
    """Map a MessageReview row into the classifier example schema."""
    return {
        "text": _to_text(row.get("text")),
        "label": label,
        "explanation": _to_text(row.get("Explanation")),
        "id": _to_text(row.get("id")),
        "predicted_category": _to_text(row.get("predicted_category")),
        "confidence": _to_text(row.get("confidence")),
        "author": _to_text(row.get("author")),
        "summary": _to_text(row.get("summary")),
        "source_file": source_file,
    }


def _iter_source_rows() -> list[tuple[dict[str, str], str, str]]:
    """Load all MessageReview rows with source metadata."""
    rows: list[tuple[dict[str, str], str, str]] = []
    for file_name, source_file, label_column in _CSV_SOURCES:
        path = _MESSAGE_REVIEW_DATA_PATH / file_name
        with path.open(newline="", encoding="utf-8-sig") as file_obj:
            reader = csv.DictReader(file_obj)
            for row in reader:
                label_code = _to_text(row.get(label_column)).strip()
                rows.append((row, source_file, label_code))
    return rows


def load_train_set() -> list[dict[str, str]]:
    """Load training examples from rows labeled with 0 or 1."""
    examples: list[dict[str, str]] = []
    for row, source_file, label_code in _iter_source_rows():
        label = _TRAIN_LABELS.get(label_code)
        if label is None:
            continue
        examples.append(_build_example(row, label=label, source_file=source_file))
    return examples


def load_val_set() -> list[dict[str, str]]:
    """Load validation examples from rows labeled with A/B/C/X/Y/Z."""
    examples: list[dict[str, str]] = []
    for row, source_file, label_code in _iter_source_rows():
        label = _VAL_LABELS.get(label_code)
        if label is None:
            continue
        examples.append(_build_example(row, label=label, source_file=source_file))
    return examples


def load_unlabeled_set() -> list[dict[str, str]]:
    """Load unlabeled examples from rows with empty keep values."""
    examples: list[dict[str, str]] = []
    for row, source_file, label_code in _iter_source_rows():
        if label_code:
            continue
        examples.append(_build_example(row, label="", source_file=source_file))
    return examples
