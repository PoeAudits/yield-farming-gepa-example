from __future__ import annotations

import csv
from pathlib import Path


def load_csv_artifact(path: str | Path, mode: str = "columns") -> dict[str, str]:
    """Load a CSV artifact and return seed-candidate sections by columns or rows."""
    csv_path = Path(path)

    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        rows = list(reader)

    if not rows:
        return {}

    headers = rows[0]
    data_rows = rows[1:]

    if mode == "columns":
        return _load_columns(headers, data_rows)
    if mode == "rows":
        return _load_rows(headers, data_rows)

    msg = "mode must be either 'columns' or 'rows'"
    raise ValueError(msg)


def _load_columns(headers: list[str], data_rows: list[list[str]]) -> dict[str, str]:
    """Convert CSV data rows into per-column section values."""
    sections: dict[str, str] = {}

    for index, header in enumerate(headers):
        key = header.strip() or f"column_{index}"
        values: list[str] = []
        for row in data_rows:
            values.append(row[index] if index < len(row) else "")
        sections[key] = "\n".join(values)

    return sections


def _load_rows(headers: list[str], data_rows: list[list[str]]) -> dict[str, str]:
    """Convert CSV data rows into per-row formatted section values."""
    sections: dict[str, str] = {}

    for row_index, row in enumerate(data_rows):
        values = row + [""] * max(0, len(headers) - len(row))
        pairs = [f"{header}={value}" for header, value in zip(headers, values, strict=True)]
        sections[f"row_{row_index}"] = "\n".join(pairs)

    return sections
