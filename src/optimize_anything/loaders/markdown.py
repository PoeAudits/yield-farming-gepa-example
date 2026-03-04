from __future__ import annotations

import re
from pathlib import Path

_HEADER_PATTERN = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


def load_markdown_artifact(path: str | Path) -> dict[str, str]:
    """Load a markdown artifact and split it into frontmatter and header sections."""
    markdown_path = Path(path)
    raw_text = markdown_path.read_text(encoding="utf-8")

    sections: dict[str, str] = {}
    body_text = raw_text

    if raw_text.startswith("---"):
        lines = raw_text.splitlines()
        if lines and lines[0].strip() == "---":
            closing_index = _find_frontmatter_end(lines)
            if closing_index is not None:
                frontmatter_lines = lines[1:closing_index]
                body_lines = lines[closing_index + 1 :]
                sections["frontmatter"] = "\n".join(frontmatter_lines).strip()
                body_text = "\n".join(body_lines)

    section_lines: list[str] = []
    section_key: str | None = None

    for line in body_text.splitlines():
        if _is_markdown_header(line):
            if section_key is None:
                preamble = "\n".join(section_lines).strip()
                if preamble:
                    sections["body"] = preamble
            else:
                sections[section_key] = "\n".join(section_lines).strip()

            section_key = line.strip()
            section_lines = []
            continue

        section_lines.append(line)

    if section_key is None:
        body_content = "\n".join(section_lines).strip()
        if body_content:
            sections["body"] = body_content
    else:
        sections[section_key] = "\n".join(section_lines).strip()

    return sections


def _find_frontmatter_end(lines: list[str]) -> int | None:
    """Return the index of the closing frontmatter delimiter if present."""
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return index
    return None


def _is_markdown_header(line: str) -> bool:
    """Return True when the line is an ATX markdown header."""
    return _HEADER_PATTERN.match(line) is not None
