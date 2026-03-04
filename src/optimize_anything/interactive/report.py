from __future__ import annotations

import re
from collections import Counter, defaultdict
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from optimize_anything.interactive.session import IterationScoreRecord, SessionState

_LOW_CONFIDENCE_THRESHOLD = 0.6  # Values below 60% are considered low confidence
_PERCENTAGE_SCALE_THRESHOLD = 1.0  # Values above this are assumed to be on 0-100 scale

# Matches: "expected: yes, got: no" or "expected=positive; got=negative"
_EXPECTED_GOT_PATTERN = re.compile(
    r"expected\s*[:=]\s*([a-zA-Z0-9_\- ]+)\s*[,;]\s*got\s*[:=]\s*([a-zA-Z0-9_\- ]+)",
    re.IGNORECASE,
)
# Matches: "expected yes got no" (no delimiter)
_EXPECTED_GOT_FALLBACK_PATTERN = re.compile(
    r"expected\s+([a-zA-Z0-9_\- ]+)\s+got\s+([a-zA-Z0-9_\- ]+)",
    re.IGNORECASE,
)
# Matches numeric values like "0.85" or "-0.5" for confidence extraction
_CONFIDENCE_FLOAT_PATTERN = re.compile(r"-?\d+(?:\.\d+)?")
# Matches lowercase words of 4+ characters for failure theme analysis
_SUGGESTION_TOKEN_PATTERN = re.compile(r"\b[a-z]{4,}\b")

_POSITIVE_LABELS = {
    "allow",
    "allowed",
    "approve",
    "approved",
    "positive",
    "true",
    "yes",
    "y",
    "1",
}
_NEGATIVE_LABELS = {
    "block",
    "blocked",
    "deny",
    "denied",
    "negative",
    "false",
    "no",
    "n",
    "0",
}
_AMBIGUITY_MARKERS = (
    "ambiguous",
    "ambiguity",
    "unclear",
    "uncertain",
    "borderline",
    "mixed",
)
_TOKEN_STOPWORDS = {
    "about",
    "after",
    "before",
    "expected",
    "feedback",
    "found",
    "from",
    "generated",
    "input",
    "inputs",
    "message",
    "model",
    "output",
    "response",
    "shows",
    "that",
    "this",
    "with",
}


@dataclass
class _FailureExample:
    component_name: str
    message_text: str
    expected_label: str
    model_response: str
    explanation: str
    confidence: str
    source_file: str
    feedback: str
    failure_kind: str


class ReportGenerator:
    def __init__(
        self,
        raw_evaluation_asi: Mapping[str, Sequence[Mapping[str, Any]]] | None = None,
    ) -> None:
        self._raw_evaluation_asi = raw_evaluation_asi

    def generate(
        self,
        candidate: dict[str, str],
        reflective_dataset: Mapping[str, Sequence[Mapping[str, Any]]],
        session_state: SessionState,
    ) -> str:
        timestamp = datetime.now(tz=UTC)
        failures = self._extract_failures(reflective_dataset, session_state)
        false_positives = [failure for failure in failures if failure.failure_kind == "fp"]
        false_negatives = [failure for failure in failures if failure.failure_kind == "fn"]
        edge_cases = self._extract_edge_cases(failures)

        report_lines: list[str] = []
        report_lines.extend(self._build_header(timestamp, session_state, candidate))
        report_lines.extend(self._build_aggregate_scores(session_state))
        report_lines.extend(self._build_score_history(session_state.score_history))
        report_lines.extend(self._build_failure_section("False positives", false_positives))
        report_lines.extend(self._build_failure_section("False negatives", false_negatives))
        report_lines.extend(self._build_edge_case_section(edge_cases))
        report_lines.extend(
            self._build_suggestion_section(false_positives, false_negatives, failures)
        )
        report_lines.extend(self._build_gepa_note())
        return "\n".join(report_lines).rstrip() + "\n"

    def write_report(self, content: str, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def _extract_failures(
        self,
        reflective_dataset: Mapping[str, Sequence[Mapping[str, Any]]],
        session_state: SessionState,
    ) -> list[_FailureExample]:
        merged_asi = self._resolve_raw_asi(reflective_dataset, session_state)
        failures: list[_FailureExample] = []

        for component_name, records in reflective_dataset.items():
            component_asi = merged_asi.get(component_name, [])
            for index, record in enumerate(records):
                feedback = str(record.get("Feedback", "")).strip()
                expected_label, model_response = self._parse_expected_and_response(feedback, record)
                failure_kind = self._classify_failure(feedback, expected_label, model_response)
                if failure_kind not in {"fp", "fn"}:
                    continue

                asi_record = component_asi[index] if index < len(component_asi) else {}
                failure = _FailureExample(
                    component_name=component_name,
                    message_text=self._string_or_default(
                        record.get("Inputs") or record.get("input") or asi_record.get("input"),
                        "(not provided)",
                    ),
                    expected_label=self._string_or_default(
                        expected_label or asi_record.get("expected"), "(unknown)"
                    ),
                    model_response=self._string_or_default(
                        model_response
                        or record.get("Generated Outputs")
                        or record.get("generated_output")
                        or asi_record.get("response"),
                        "(unknown)",
                    ),
                    explanation=self._string_or_default(
                        asi_record.get("explanation") or record.get("Explanation"), ""
                    ),
                    confidence=self._string_or_default(
                        asi_record.get("confidence") or record.get("confidence"), ""
                    ),
                    source_file=self._string_or_default(
                        asi_record.get("source_file") or record.get("source_file"), "unknown"
                    ),
                    feedback=feedback,
                    failure_kind=failure_kind,
                )
                failures.append(failure)

        return failures

    def _resolve_raw_asi(
        self,
        reflective_dataset: Mapping[str, Sequence[Mapping[str, Any]]],
        session_state: SessionState,
    ) -> dict[str, list[Mapping[str, Any]]]:
        payload = self._raw_evaluation_asi
        if payload is None:
            metadata_payload = session_state.session_metadata.get("raw_evaluation_asi")
            if isinstance(metadata_payload, Mapping):
                payload = metadata_payload

        merged: dict[str, list[Mapping[str, Any]]] = {}
        for component_name in reflective_dataset:
            if payload and isinstance(payload.get(component_name), Sequence):
                component_payload = payload.get(component_name, [])
                merged[component_name] = [
                    entry for entry in component_payload if isinstance(entry, Mapping)
                ]
            else:
                merged[component_name] = []
        return merged

    def _parse_expected_and_response(
        self,
        feedback: str,
        record: Mapping[str, Any],
    ) -> tuple[str, str]:
        for pattern in (_EXPECTED_GOT_PATTERN, _EXPECTED_GOT_FALLBACK_PATTERN):
            match = pattern.search(feedback)
            if match:
                expected_label = self._clean_label(match.group(1))
                model_response = self._clean_label(match.group(2))
                return expected_label, model_response

        return "", self._string_or_default(record.get("Generated Outputs"), "")

    def _classify_failure(self, feedback: str, expected_label: str, model_response: str) -> str:
        # Classification priority: explicit string signals ("false positive"/"false negative")
        # take precedence over label-based inference. Do not reorder these checks.
        feedback_lower = feedback.lower()
        if "false positive" in feedback_lower:
            return "fp"
        if "false negative" in feedback_lower:
            return "fn"

        expected_lower = self._clean_label(expected_label)
        response_lower = self._clean_label(model_response)
        if not expected_lower or not response_lower:
            return "unknown"

        if self._is_positive_label(response_lower) and self._is_negative_label(expected_lower):
            return "fp"
        if self._is_negative_label(response_lower) and self._is_positive_label(expected_lower):
            return "fn"
        return "unknown"

    def _build_header(
        self,
        timestamp: datetime,
        session_state: SessionState,
        candidate: dict[str, str],
    ) -> list[str]:
        lines = ["# Interactive Failure Analysis Report", "", "## Header"]
        lines.append(f"- Iteration: {session_state.current_iteration}")
        lines.append(f"- Generated at (UTC): {timestamp.isoformat()}")
        component_names = ", ".join(candidate.keys()) if candidate else "(none)"
        lines.append(f"- Candidate components: {component_names}")
        lines.append("")
        return lines

    def _build_aggregate_scores(self, session_state: SessionState) -> list[str]:
        lines = ["## Aggregate scores"]
        latest_score = session_state.score_history[-1] if session_state.score_history else None
        if latest_score is None:
            lines.append("- Accuracy: n/a")
            lines.append("- False positives: n/a")
            lines.append("- False negatives: n/a")
        else:
            lines.append(f"- Accuracy: {latest_score.aggregate_accuracy:.4f}")
            lines.append(f"- False positives: {latest_score.false_positive_count}")
            lines.append(f"- False negatives: {latest_score.false_negative_count}")
        lines.append("")
        return lines

    def _build_score_history(self, score_history: Sequence[IterationScoreRecord]) -> list[str]:
        lines = ["## Score history"]
        lines.append("| Iteration | Accuracy | Delta | False positives | False negatives |")
        lines.append("| --- | ---: | ---: | ---: | ---: |")

        if not score_history:
            lines.append("| - | - | - | - | - |")
            lines.append("")
            return lines

        for record in score_history:
            delta = (
                "-" if record.delta_from_previous is None else f"{record.delta_from_previous:+.4f}"
            )
            lines.append(
                "| "
                f"{record.iteration} | {record.aggregate_accuracy:.4f} | {delta} | "
                f"{record.false_positive_count} | {record.false_negative_count} |"
            )
        lines.append("")
        return lines

    def _build_failure_section(self, title: str, failures: Sequence[_FailureExample]) -> list[str]:
        lines = [f"## {title}"]
        if not failures:
            lines.append("No examples identified from reflective feedback.")
            lines.append("")
            return lines

        grouped: dict[str, list[_FailureExample]] = defaultdict(list)
        for failure in failures:
            grouped[failure.source_file or "unknown"].append(failure)

        for source_file in sorted(grouped):
            lines.append(f"### Source: {source_file}")
            for failure in grouped[source_file]:
                lines.append("- Message text: " + failure.message_text)
                lines.append("  - Expected label: " + failure.expected_label)
                lines.append("  - Model response: " + failure.model_response)
                if failure.explanation:
                    lines.append("  - Explanation: " + failure.explanation)
                if failure.confidence:
                    lines.append("  - Confidence: " + failure.confidence)
                if failure.source_file:
                    lines.append("  - Source file: " + failure.source_file)
                if failure.feedback:
                    lines.append("  - Feedback: " + failure.feedback)
        lines.append("")
        return lines

    def _build_edge_case_section(self, edge_cases: Sequence[_FailureExample]) -> list[str]:
        lines = ["## Edge cases / ambiguous examples"]
        if not edge_cases:
            lines.append("No low-confidence or ambiguous examples identified.")
            lines.append("")
            return lines

        for failure in edge_cases:
            reason = (
                "ambiguous feedback"
                if self._has_ambiguity_marker(failure.feedback)
                else "low confidence"
            )
            lines.append(f"- [{failure.failure_kind.upper()}] {failure.message_text}")
            lines.append(f"  - Reason: {reason}")
            lines.append(f"  - Expected label: {failure.expected_label}")
            lines.append(f"  - Model response: {failure.model_response}")
            if failure.confidence:
                lines.append(f"  - Confidence: {failure.confidence}")
            if failure.source_file:
                lines.append(f"  - Source file: {failure.source_file}")
        lines.append("")
        return lines

    def _build_suggestion_section(
        self,
        false_positives: Sequence[_FailureExample],
        false_negatives: Sequence[_FailureExample],
        failures: Sequence[_FailureExample],
    ) -> list[str]:
        lines = ["## Prompt refinement suggestions"]
        if not failures:
            lines.append("- Not enough failure data to generate targeted suggestions.")
            lines.append("")
            return lines

        fp_by_source = self._count_by_source(false_positives)
        fn_by_source = self._count_by_source(false_negatives)
        for source_name in sorted(set(fp_by_source) | set(fn_by_source)):
            fp_count = fp_by_source.get(source_name, 0)
            fn_count = fn_by_source.get(source_name, 0)
            if fp_count > fn_count and fp_count > 0:
                lines.append(
                    f"- `{source_name}` shows more false positives ({fp_count}) than "
                    f"false negatives ({fn_count}); tighten acceptance criteria for "
                    "this source category."
                )
            elif fn_count > fp_count and fn_count > 0:
                lines.append(
                    f"- `{source_name}` shows more false negatives ({fn_count}) than "
                    f"false positives ({fp_count}); loosen criteria to recover "
                    "borderline positives for this category."
                )

        frequent_tokens = self._frequent_failure_tokens(failures)
        if frequent_tokens:
            token_list = ", ".join(frequent_tokens)
            lines.append(
                "- Frequent failure themes in feedback: "
                f"{token_list}. Consider adding explicit guidance for these patterns."
            )

        if len(lines) == 1:
            lines.append(
                "- FP and FN rates are balanced across sources; refine language incrementally."
            )

        lines.append("")
        return lines

    def _build_gepa_note(self) -> list[str]:
        return [
            "## GEPA acceptance note",
            "GEPA accepts a proposed prompt only when `new_sum > old_sum` on the "
            "evaluated subsample.",
            "A candidate can improve overall behavior yet still be rejected if it "
            "does not outperform the "
            "current prompt on that mini-batch.",
            "",
        ]

    def _extract_edge_cases(self, failures: Sequence[_FailureExample]) -> list[_FailureExample]:
        edge_cases: list[_FailureExample] = []
        for failure in failures:
            if self._has_ambiguity_marker(failure.feedback) or self._is_low_confidence(
                failure.confidence
            ):
                edge_cases.append(failure)
        return edge_cases

    def _has_ambiguity_marker(self, text: str) -> bool:
        lowered = text.lower()
        return any(marker in lowered for marker in _AMBIGUITY_MARKERS)

    def _is_low_confidence(self, confidence_value: str) -> bool:
        if not confidence_value:
            return False

        lowered = confidence_value.lower()
        if "low" in lowered:
            return True

        match = _CONFIDENCE_FLOAT_PATTERN.search(lowered)
        if not match:
            return False

        numeric_value = float(match.group(0))
        if numeric_value > _PERCENTAGE_SCALE_THRESHOLD:
            numeric_value /= 100.0
        return numeric_value < _LOW_CONFIDENCE_THRESHOLD

    def _count_by_source(self, failures: Sequence[_FailureExample]) -> dict[str, int]:
        counts: dict[str, int] = defaultdict(int)
        for failure in failures:
            source_name = failure.source_file or "unknown"
            counts[source_name] += 1
        return counts

    def _frequent_failure_tokens(self, failures: Sequence[_FailureExample]) -> list[str]:
        token_counts: Counter[str] = Counter()
        for failure in failures:
            for token in _SUGGESTION_TOKEN_PATTERN.findall(failure.feedback.lower()):
                if token in _TOKEN_STOPWORDS:
                    continue
                token_counts[token] += 1
        return [token for token, _count in token_counts.most_common(5)]

    def _string_or_default(self, value: Any, default_value: str) -> str:
        if value is None:
            return default_value
        normalized = str(value).strip()
        if not normalized:
            return default_value
        return normalized

    def _clean_label(self, raw_label: str) -> str:
        return raw_label.strip().lower().strip(".?!\"'")

    def _is_positive_label(self, label: str) -> bool:
        return self._clean_label(label) in _POSITIVE_LABELS

    def _is_negative_label(self, label: str) -> bool:
        return self._clean_label(label) in _NEGATIVE_LABELS


__all__ = ["ReportGenerator"]
