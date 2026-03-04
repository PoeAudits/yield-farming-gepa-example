from __future__ import annotations

import csv
from pathlib import Path


def write_markdown_artifact(
    candidate: dict[str, str],
    path: str | Path,
    frontmatter: str | None = None,
) -> None:
    """Reassemble a markdown document from candidate sections and write to path.

    Frontmatter is sourced from the ``frontmatter`` argument first, then from
    ``candidate["frontmatter"]`` if present. Body sections are ordered so the
    "body" key (pre-header preamble) comes first, followed by header-keyed
    sections in sorted order.
    """
    output_path = Path(path)
    parts: list[str] = []

    resolved_frontmatter = frontmatter or candidate.get("frontmatter")
    if resolved_frontmatter:
        parts.append(f"---\n{resolved_frontmatter}\n---")

    body_content = candidate.get("body")
    if body_content:
        parts.append(body_content)

    header_keys = sorted(key for key in candidate if key not in ("frontmatter", "body"))
    for key in header_keys:
        section_content = candidate[key]
        parts.append(f"{key}\n{section_content}" if section_content else key)

    output_path.write_text("\n\n".join(parts), encoding="utf-8")


def write_csv_artifact(candidate: dict[str, str], path: str | Path) -> None:
    """Reconstitute a CSV file from candidate column sections and write to path.

    Assumes "columns" mode: keys are column headers and values are
    newline-separated column data (one value per row).
    """
    output_path = Path(path)
    headers = list(candidate.keys())

    column_values: list[list[str]] = []
    for header in headers:
        raw = candidate[header]
        column_values.append(raw.split("\n") if raw else [])

    row_count = max((len(col) for col in column_values), default=0)

    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(headers)
        for row_index in range(row_count):
            row = [col[row_index] if row_index < len(col) else "" for col in column_values]
            writer.writerow(row)
