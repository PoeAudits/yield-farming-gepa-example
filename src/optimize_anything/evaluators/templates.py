from __future__ import annotations

import json
from typing import Any

from litellm import completion

from optimize_anything.config.presets import DEFAULT_TASK_LM
from optimize_anything.evaluators.base import EvaluatorFn, normalize_label


def llm_classification_evaluator(
    model: str = DEFAULT_TASK_LM,
    label_key: str = "label",
    input_key: str = "text",
    prompt_key: str = "system_prompt",
) -> EvaluatorFn:
    """Create an evaluator that scores exact-match label classification via LLM output."""

    def evaluate(
        candidate: dict[str, str], example: dict[str, Any]
    ) -> tuple[float, dict[str, Any]]:
        """Evaluate a single example against the expected label and return score with ASI."""
        system_prompt = candidate[prompt_key]
        input_text = str(example[input_key])
        expected_label = str(example[label_key])

        response = completion(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": input_text},
            ],
        )
        llm_output = extract_response_text(response).strip()
        is_match = normalize_label(llm_output) == normalize_label(expected_label)
        score = 1.0 if is_match else 0.0

        asi: dict[str, Any] = {
            "response": llm_output,
            "expected": expected_label,
            "match": is_match,
            "input": input_text,
        }
        return score, asi

    return evaluate


def rubric_evaluator(
    model: str = DEFAULT_TASK_LM,
    rubric: str = "",
    prompt_key: str = "system_prompt",
) -> EvaluatorFn:
    """Create an evaluator that uses an LLM judge and rubric to score candidate content."""

    def evaluate(
        candidate: dict[str, str], example: dict[str, Any]
    ) -> tuple[float, dict[str, Any]]:
        """Evaluate candidate content using a rubric judge and return normalized score with ASI."""
        candidate_content = candidate[prompt_key]

        judge_prompt = (
            "You are an expert evaluator. Score the candidate on a 0-10 integer scale against "
            "the rubric. Return strict JSON with keys score and explanation."
        )
        judge_input = (
            f"Rubric:\n{rubric}\n\n"
            f"Candidate content:\n{candidate_content}\n\n"
            f"Example context:\n{json.dumps(example, ensure_ascii=True)}"
        )

        response = completion(
            model=model,
            messages=[
                {"role": "system", "content": judge_prompt},
                {"role": "user", "content": judge_input},
            ],
        )
        response_text = extract_response_text(response)
        score_raw, explanation = _parse_rubric_response(response_text)

        normalized_score = max(0.0, min(1.0, score_raw / 10.0))
        asi: dict[str, Any] = {
            "score_raw": score_raw,
            "explanation": explanation,
            "rubric": rubric,
        }
        return normalized_score, asi

    return evaluate


def mock_evaluator(base_score: float = 0.5) -> EvaluatorFn:
    """Create a deterministic evaluator for tests without external calls."""

    def evaluate(
        candidate: dict[str, str], example: dict[str, Any]
    ) -> tuple[float, dict[str, Any]]:
        """Compute deterministic score from candidate character count and return ASI."""
        del example
        total_chars = sum(len(value) for value in candidate.values())
        score = min(total_chars / 500.0, 1.0) * base_score + (1.0 - base_score) * 0.5

        asi: dict[str, Any] = {
            "char_count": total_chars,
            "base_score": base_score,
            "mock": True,
        }
        return score, asi

    return evaluate


def extract_response_text(response: Any) -> str:
    """Extract text content from a LiteLLM completion response."""
    message = response.choices[0].message
    content = message.content
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        text_parts = [part.get("text", "") for part in content if isinstance(part, dict)]
        return "".join(text_parts)
    return str(content)


def _parse_rubric_response(response_text: str) -> tuple[float, str]:
    """Parse judge response JSON and clamp score to the 0-10 range."""
    try:
        payload = json.loads(response_text)
    except json.JSONDecodeError:
        return 0.0, response_text.strip()

    score_raw = 0.0
    explanation = response_text.strip()

    if isinstance(payload, dict):
        score_value = payload.get("score", 0)
        explanation = str(payload.get("explanation", "")).strip()
        try:
            score_raw = float(score_value)
        except (TypeError, ValueError):
            score_raw = 0.0

    score_raw = max(0.0, min(10.0, score_raw))
    return score_raw, explanation


__all__ = [
    "llm_classification_evaluator",
    "rubric_evaluator",
    "mock_evaluator",
    "extract_response_text",
]
