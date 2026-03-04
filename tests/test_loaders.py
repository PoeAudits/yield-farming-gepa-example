"""Tests for artifact loaders (Markdown, CSV) and their round-trip write/load fidelity."""

from __future__ import annotations

from pathlib import Path

from optimize_anything.loaders.csv import load_csv_artifact
from optimize_anything.loaders.markdown import load_markdown_artifact
from optimize_anything.loaders.writers import write_csv_artifact, write_markdown_artifact


def test_load_markdown_with_frontmatter_and_sections(tmp_path: Path) -> None:
    markdown_path = tmp_path / "artifact.md"
    markdown_path.write_text(
        "---\n"
        "title: Sample\n"
        "author: Test\n"
        "---\n\n"
        "Intro body text.\n\n"
        "## Details\n"
        "Line one.\n"
        "Line two.\n",
        encoding="utf-8",
    )

    loaded = load_markdown_artifact(markdown_path)

    assert loaded == {
        "frontmatter": "title: Sample\nauthor: Test",
        "body": "Intro body text.",
        "## Details": "Line one.\nLine two.",
    }


def test_load_markdown_without_frontmatter_with_sections(tmp_path: Path) -> None:
    markdown_path = tmp_path / "artifact.md"
    markdown_path.write_text(
        "Preface paragraph.\n\n# Section One\nAlpha\n\n### Section Two\nBeta",
        encoding="utf-8",
    )

    loaded = load_markdown_artifact(markdown_path)

    assert loaded == {
        "body": "Preface paragraph.",
        "# Section One": "Alpha",
        "### Section Two": "Beta",
    }


def test_load_markdown_with_only_body_text(tmp_path: Path) -> None:
    markdown_path = tmp_path / "artifact.md"
    markdown_path.write_text("Only body text with no headers.", encoding="utf-8")

    loaded = load_markdown_artifact(markdown_path)

    assert loaded == {"body": "Only body text with no headers."}


def test_load_csv_in_columns_mode(tmp_path: Path) -> None:
    csv_path = tmp_path / "artifact.csv"
    csv_path.write_text("name,age\nAlice,30\nBob,31\n", encoding="utf-8")

    loaded = load_csv_artifact(csv_path, mode="columns")

    assert loaded == {"name": "Alice\nBob", "age": "30\n31"}


def test_load_csv_in_rows_mode(tmp_path: Path) -> None:
    csv_path = tmp_path / "artifact.csv"
    csv_path.write_text("name,age\nAlice,30\nBob,31\n", encoding="utf-8")

    loaded = load_csv_artifact(csv_path, mode="rows")

    assert loaded == {
        "row_0": "name=Alice\nage=30",
        "row_1": "name=Bob\nage=31",
    }


def test_markdown_round_trip_load_write_load_equivalent(tmp_path: Path) -> None:
    source_path = tmp_path / "source.md"
    source_path.write_text(
        "---\nauthor: Jane\nversion: 1\n---\n\nIntro text.\n\n# Usage\nUse it.\n\n## Notes\nA\nB",
        encoding="utf-8",
    )
    roundtrip_path = tmp_path / "roundtrip.md"

    first_load = load_markdown_artifact(source_path)
    write_markdown_artifact(first_load, roundtrip_path)
    second_load = load_markdown_artifact(roundtrip_path)

    assert second_load == first_load


def test_csv_round_trip_load_write_load_equivalent(tmp_path: Path) -> None:
    source_path = tmp_path / "source.csv"
    source_path.write_text("city,country\nParis,France\nTokyo,Japan\n", encoding="utf-8")
    roundtrip_path = tmp_path / "roundtrip.csv"

    first_load = load_csv_artifact(source_path, mode="columns")
    write_csv_artifact(first_load, roundtrip_path)
    second_load = load_csv_artifact(roundtrip_path, mode="columns")

    assert second_load == first_load
