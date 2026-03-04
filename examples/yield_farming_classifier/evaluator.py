from __future__ import annotations

import os
from typing import Any

from litellm import completion

from optimize_anything.config import ENV_TASK_LM
from optimize_anything.evaluators import extract_response_text, normalize_label

try:
    from .config import TASK_LM
except ImportError:
    from config import TASK_LM

__all__ = ["real_evaluator", "mock_evaluator"]

_MOCK_MAX_CHARS = 800
_MOCK_KEYWORD_COUNT = 6
_MOCK_LENGTH_WEIGHT = 0.4
_MOCK_KEYWORD_WEIGHT = 0.6


def real_evaluator(
    candidate: dict[str, str], example: dict[str, Any]
) -> tuple[float, dict[str, Any]]:
    """Score exact-match classification for a yield farming message."""
    system_prompt = candidate["system_prompt"]
    data = example
    input_text = str(data.get("text", ""))
    expected_label = normalize_label(str(data.get("label", "")))
    explanation = str(data.get("explanation", ""))
    predicted_category = str(data.get("predicted_category", ""))
    confidence = str(data.get("confidence", ""))
    source_file = str(data.get("source_file", ""))

    try:
        response = completion(
            model=os.environ.get(ENV_TASK_LM, TASK_LM),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": input_text},
            ],
        )
        llm_output = extract_response_text(response)
        normalized_output = normalize_label(llm_output)
        is_match = normalized_output == expected_label
        score = 1.0 if is_match else 0.0
        asi: dict[str, Any] = {
            "response": llm_output,
            "expected": expected_label,
            "match": is_match,
            "input": input_text,
            "explanation": explanation,
            "predicted_category": predicted_category,
            "confidence": confidence,
            "source_file": source_file,
            "error": None,
            "type": "success",
        }
        return score, asi
    except Exception as exc:
        asi = {
            "response": "",
            "expected": expected_label,
            "match": False,
            "input": input_text,
            "explanation": explanation,
            "predicted_category": predicted_category,
            "confidence": confidence,
            "source_file": source_file,
            "error": str(exc),
            "type": "runtime_error",
        }
        return 0.0, asi


def mock_evaluator(
    candidate: dict[str, str], example: dict[str, Any]
) -> tuple[float, dict[str, Any]]:
    """Return a deterministic score using prompt length and keyword coverage."""
    del example
    system_prompt = candidate.get("system_prompt", "")
    lowered_prompt = system_prompt.lower()
    char_count = len(system_prompt)

    has_yield = "yield" in lowered_prompt
    has_farming = "farming" in lowered_prompt
    has_staking = "staking" in lowered_prompt
    has_apy = "apy" in lowered_prompt
    has_apr = "apr" in lowered_prompt
    has_liquidity = "liquidity" in lowered_prompt

    keyword_hits = sum((has_yield, has_farming, has_staking, has_apy, has_apr, has_liquidity))
    length_score = min(char_count / _MOCK_MAX_CHARS, 1.0)
    keyword_score = keyword_hits / _MOCK_KEYWORD_COUNT
    score = min(length_score * _MOCK_LENGTH_WEIGHT + keyword_score * _MOCK_KEYWORD_WEIGHT, 1.0)

    asi: dict[str, Any] = {
        "char_count": char_count,
        "mock": True,
        "has_yield": has_yield,
        "has_farming": has_farming,
        "has_staking": has_staking,
        "has_apy": has_apy,
        "has_apr": has_apr,
        "has_liquidity": has_liquidity,
        "keyword_hits": keyword_hits,
        "length_score": length_score,
        "keyword_score": keyword_score,
        "type": "mock",
    }
    return score, asi
