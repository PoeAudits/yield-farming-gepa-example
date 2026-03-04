# Evaluator Implementations Reference

Provide authoritative evaluator protocol guidance, reusable evaluator templates, advanced implementation patterns, and common evaluator mistakes for `optimize_anything` workflows.

## 1. Evaluator Protocol

Implement every evaluator with the local library protocol from `src/optimize_anything/evaluators/base.py`.

```python
from collections.abc import Callable
from typing import Any

EvaluatorFn = Callable[[dict[str, str], dict[str, Any]], tuple[float, dict[str, Any]]]
```

Use the following callable shape:

```python
def evaluator(
    candidate: dict[str, str],
    example: dict[str, Any],
) -> tuple[float, dict[str, Any]]:
    ...
```

- `candidate`: current artifact state, keyed by stable section names.
- `example`: one training or validation item with task-defined schema.
- Return `(score, asi)` where `score` is normalized to `[0.0, 1.0]` and `asi` is a structured dictionary.

Handle per-example failures inside the evaluator. Return `0.0` with diagnostic ASI for recoverable errors. Reserve raised exceptions for unrecoverable failures only.

Deliver ASI through tuple return values and optionally through `oa.log()` calls captured in GEPA side information.

## 2. Classification Evaluator (Complete)

Use this implementation for exact-match text classification tasks.

```python
from __future__ import annotations

import os
from typing import Any

from litellm import completion

from optimize_anything.evaluators.base import EvaluatorFn


def sentiment_evaluator(
    candidate: dict[str, str], example: dict[str, Any]
) -> tuple[float, dict[str, Any]]:
    """Score a sentiment classification example using an LLM prediction.

    candidate keys used: "system_prompt"
    example keys used: "text" (input), "label" (expected output)
    """
    system_prompt = candidate["system_prompt"]
    input_text = str(example["text"])
    expected_label = str(example["label"])

    try:
        response = completion(
            model=_resolve_model(),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": input_text},
            ],
        )
        llm_output = _extract_response_text(response).strip()
    except Exception as e:
        return 0.0, {
            "response": None,
            "expected": expected_label,
            "match": False,
            "input": input_text,
            "error": str(e),
            "type": "runtime_error",
        }

    is_match = _normalize_label(llm_output) == _normalize_label(expected_label)
    score = 1.0 if is_match else 0.0

    asi: dict[str, Any] = {
        "response": llm_output,
        "expected": expected_label,
        "match": is_match,
        "input": input_text,
        "error": None,
        "type": None,
    }
    return score, asi


def _resolve_model() -> str:
    """Resolve the task LLM model name from environment or default value."""
    return os.getenv("OPTIMIZE_TASK_LM", "openai/gpt-4.1-mini")


def _normalize_label(value: str) -> str:
    """Normalize classification labels for case-insensitive exact matching."""
    return value.strip().lower()


def _extract_response_text(response: Any) -> str:
    """Extract text content from a LiteLLM completion response."""
    message = response.choices[0].message
    content = message.content
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        chunks = [part.get("text", "") for part in content if isinstance(part, dict)]
        return "".join(chunks)
    return str(content)
```

## 3. Agent-Definition Evaluator (Skeleton)

Use this skeleton for rule-plus-rubric evaluation of agent definition artifacts.

```python
# SKELETON: Customize rule checks and model before use.
from __future__ import annotations

import re
from typing import Any

from litellm import completion

from optimize_anything.evaluators.base import EvaluatorFn

_STRUCTURAL_RULES: list[tuple[str, str]] = [
    ("has_name_field", r"^name:\s*\S"),
    ("has_description_field", r"^description:\s*\S"),
    ("has_model_field", r"^model:\s*\S"),
    ("has_instructions_field", r"(?m)^instructions:"),
    ("no_empty_instructions", r"(?ms)^instructions:\s*\S"),
]


def agent_definition_evaluator(
    candidate: dict[str, str], example: dict[str, Any]
) -> tuple[float, dict[str, Any]]:
    candidate_text = "\n".join(candidate.values())

    rule_results: dict[str, bool] = {}
    for label, pattern in _STRUCTURAL_RULES:
        rule_results[label] = bool(re.search(pattern, candidate_text))

    structural_pass_count = sum(rule_results.values())
    structural_score = structural_pass_count / max(len(_STRUCTURAL_RULES), 1)

    rubric = (
        "Evaluate clarity, consistency, and role alignment. "
        "Return score 0-10 with concise explanation."
    )

    try:
        judge_response = _call_judge(candidate_text, rubric, example)
        rubric_score = max(0.0, min(1.0, judge_response["score_raw"] / 10.0))
        judge_explanation = judge_response["explanation"]
        runtime_error = None
    except Exception as e:
        rubric_score = 0.0
        judge_explanation = ""
        runtime_error = str(e)

    combined_score = 0.5 * structural_score + 0.5 * rubric_score

    asi: dict[str, Any] = {
        "structural_score": structural_score,
        "rubric_score": rubric_score,
        "combined_score": combined_score,
        "rule_results": rule_results,
        "structural_pass_count": structural_pass_count,
        "structural_total": len(_STRUCTURAL_RULES),
        "judge_explanation": judge_explanation,
        "task": str(example.get("task", "default")),
        "error": runtime_error,
    }
    return combined_score, asi


def _call_judge(candidate_text: str, rubric: str, example: dict[str, Any]) -> dict[str, Any]:
    import json

    judge_prompt = (
        "Act as an expert evaluator. Score the candidate on a 0-10 integer scale "
        "against the rubric. Return strict JSON with keys score and explanation."
    )
    judge_input = (
        f"Rubric:\n{rubric}\n\n"
        f"Candidate:\n{candidate_text}\n\n"
        f"Example context:\n{json.dumps(example, ensure_ascii=True)}"
    )
    response = completion(
        model="openai/gpt-4.1-mini",
        messages=[
            {"role": "system", "content": judge_prompt},
            {"role": "user", "content": judge_input},
        ],
    )
    message = response.choices[0].message
    content = message.content if isinstance(message.content, str) else str(message.content)
    try:
        payload = json.loads(content)
        score_raw = float(payload.get("score", 0))
        explanation = str(payload.get("explanation", "")).strip()
    except (json.JSONDecodeError, TypeError, ValueError):
        score_raw = 0.0
        explanation = content.strip()
    return {"score_raw": max(0.0, min(10.0, score_raw)), "explanation": explanation}
```

## 4. Skill Evaluator (Skeleton)

Use this deterministic evaluator to score SKILL.md format compliance.

```python
# SKELETON: Extend _CONTENT_CHECKS with project-specific rules.
from __future__ import annotations

import re
from typing import Any

from optimize_anything.evaluators.base import EvaluatorFn

_REQUIRED_SECTIONS: list[str] = [
    "1. Purpose and Scope",
    "2. Core Principles",
    "3. Anatomy/Structure",
    "4. Creation Process",
    "5. Structural Rules",
    "6. Validation Checklist",
    "7. Common Mistakes",
    "8. References Usage",
]

_CONTENT_CHECKS: list[tuple[str, str, bool]] = [
    ("has_frontmatter_name", r"(?m)^name:\s*\S", True),
    ("has_frontmatter_description", r"(?m)^description:\s*\S", True),
    ("has_trigger_phrases", r"(?i)trigger", True),
    ("has_validation_checkboxes", r"- \[[ x]\]", True),
    ("has_common_mistakes_fixes", r"(?i)\bfix\b", True),
    ("references_usage_nonempty", r"## 8\. References Usage\s*\n\s*\S", True),
]


def skill_format_evaluator(
    candidate: dict[str, str], example: dict[str, Any]
) -> tuple[float, dict[str, Any]]:
    del example
    full_text = "\n".join(candidate.values())

    section_results: dict[str, bool] = {}
    for section in _REQUIRED_SECTIONS:
        pattern = rf"(?m)^#+\s*{re.escape(section)}"
        section_results[section] = bool(re.search(pattern, full_text))

    section_pass_count = sum(section_results.values())
    section_score = section_pass_count / len(_REQUIRED_SECTIONS)

    content_results: dict[str, bool] = {}
    required_content_checks = 0
    required_content_passes = 0

    for label, pattern, required in _CONTENT_CHECKS:
        matched = bool(re.search(pattern, full_text))
        if required:
            content_results[label] = matched
            required_content_checks += 1
            if matched:
                required_content_passes += 1

    content_score = (
        required_content_passes / required_content_checks
        if required_content_checks > 0
        else 1.0
    )
    final_score = 0.7 * section_score + 0.3 * content_score

    asi: dict[str, Any] = {
        "section_score": section_score,
        "content_score": content_score,
        "final_score": final_score,
        "section_results": section_results,
        "section_pass_count": section_pass_count,
        "section_total": len(_REQUIRED_SECTIONS),
        "content_results": content_results,
        "missing_sections": [s for s, v in section_results.items() if not v],
        "failing_content_checks": [k for k, v in content_results.items() if not v],
    }
    return final_score, asi
```

## 5. Advanced Evaluator Patterns

### Graceful Error Handling

Never terminate a run for expected per-example failures.

```python
# Wrong: exception terminates the run
def evaluate(candidate, example):
    result = risky_operation(candidate, example)  # Raises on bad input
    return result.score, {"output": result}

# Correct: graceful failure with diagnostic ASI
def evaluate(candidate, example):
    try:
        result = risky_operation(candidate, example)
    except Exception as e:
        return 0.0, {"error": str(e), "type": "runtime_error"}
    return result.score, {"output": result}
```

### Thread Safety Under `parallel=True`

Avoid mutable global state when evaluator calls run concurrently. Shared counters and unsynchronized caches create race conditions and unstable scores.

```python
from threading import Lock

_counter_lock = Lock()
_counter = 0


def evaluate(candidate, example):
    global _counter
    with _counter_lock:
        _counter += 1
        call_index = _counter
    score = compute_score(candidate, example)
    return score, {"call_index": call_index}
```

Prefer pure evaluators over lock-heavy shared state whenever possible.

### Multi-Objective Pattern with `scores`

Expose metric breakdowns in ASI using a `scores` dictionary for Pareto-aware selection.

```python
def evaluate(candidate, example):
    accuracy = compute_accuracy(candidate, example)
    latency = measure_latency(candidate, example)
    return accuracy, {
        "scores": {
            "accuracy": accuracy,
            "latency_inv": 1.0 / max(latency, 0.001),  # higher is better
        },
        "accuracy": accuracy,
        "latency_ms": latency,
    }
```

### Parameter-Specific Feedback

Return section-specific diagnostics using `"{param}_specific_info"` keys.

```python
def evaluate(candidate, example):
    # ... evaluation logic ...
    score = compute_score(candidate, example)
    return score, {
        "overall_score": score,
        "system_prompt_specific_info": {
            "scores": {"relevance": 0.7},
            "feedback": "System prompt too generic for the domain",
        },
        "task_instructions_specific_info": {
            "scores": {"clarity": 0.9},
            "feedback": "Task instructions are clear and specific",
        },
    }
```

## 6. Common Evaluator Mistakes

### Bare scores without ASI

```python
# Wrong
return 1.0 if is_match else 0.0, {}

# Correct
return score, {"response": llm_output, "expected": expected, "match": is_match, "input": text}
```

### Raising exceptions for per-example failures

```python
# Wrong
def evaluate(candidate, example):
    prediction = run_model(candidate, example)  # may raise
    return score_prediction(prediction), {"prediction": prediction}

# Correct
def evaluate(candidate, example):
    try:
        prediction = run_model(candidate, example)
    except Exception as e:
        return 0.0, {"error": str(e), "type": "runtime_error"}
    return score_prediction(prediction), {"prediction": prediction}
```

### Non-deterministic scoring on deterministic tasks

```python
# Wrong
response = completion(model=model, messages=messages, temperature=1.0)

# Correct
response = completion(model=model, messages=messages)
```

### Wrong score ranges

```python
# Wrong
return score_raw, asi

# Correct
normalized_score = max(0.0, min(1.0, score_raw / 10.0))
return normalized_score, asi
```

### Mutable global state with parallel evaluation

```python
# Wrong
_call_count = 0

def evaluate(candidate, example):
    global _call_count
    _call_count += 1
    return 1.0 / _call_count, {"call_count": _call_count}

# Correct
def evaluate(candidate, example):
    score = _compute_pure_score(candidate, example)
    return score, {"call_count": None}
```

### Inconsistent ASI schema across branches

```python
# Wrong
if is_match:
    return 1.0, {"match": True}
return 0.0, {"match": False, "response": llm_output, "expected": expected}

# Correct
asi = {
    "response": llm_output,
    "expected": expected,
    "match": is_match,
    "input": input_text,
}
return score, asi
```

### Missing candidate key guardrails

```python
# Wrong
system_prompt = candidate["system_prompt"]

# Correct
system_prompt = candidate.get("system_prompt", "")
if not system_prompt:
    return 0.0, {"error": "missing_system_prompt", "match": False}
```
