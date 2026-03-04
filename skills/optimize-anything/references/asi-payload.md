# ASI Payload Reference

Define Actionable Side Information (ASI) payloads that maximize reflection quality, preserve machine readability, and support stable optimization behavior across runs.

## 1. ASI as Optimization Gradient

Treat ASI as the text-optimization analogue of a gradient. A scalar score alone expresses quality but not direction. Structured ASI expresses both quality and revision targets.

- Score-only signal: `0.3`
- Score plus revision signal: `0.3` with `missing_sections: ["Validation Checklist"]`

Use ASI fields to expose which constraints failed, what evidence triggered failure, and which section or parameter requires revision.

## 2. Delivery Mechanisms

Deliver ASI through two complementary channels.

### 2.1 Return Tuple

Return a `(score, asi)` tuple directly from the evaluator.

```python
def evaluate(candidate, example):
    score = compute_score(candidate, example)
    return score, {"field": "value"}
```

### 2.2 `oa.log()` Capture

Write diagnostic messages with `oa.log()` inside evaluator execution. GEPA captures these messages under the reserved `"log"` key in ASI.

```python
import gepa.optimize_anything as oa


def evaluate(candidate, example):
    oa.log("diagnostic message")
    score = compute_score(candidate, example)
    return score, {"match": True}
```

Use tuple-return ASI for structured fields and `oa.log()` for lightweight trace lines.

## 3. ASI Structure Taxonomy

Use consistent field groups so reflection loops can aggregate diagnostics across examples.

### 3.1 Evidence Fields

- `response`
- `expected`
- `match`
- `input`

Capture what was produced and what was required.

### 3.2 Diagnosis Fields

- `failure_category`
- `violated_rule`
- `parse_status`

Capture why the score was assigned.

### 3.3 Quantitative Fields

- `structural_score`
- `rubric_score`
- `pass_count`
- `total`

Expose normalized component scores and checklist progress.

### 3.4 Multi-Objective Scores

Include Pareto-compatible metrics under `scores` with higher-is-better semantics.

```python
{
    "scores": {
        "metric1": val,
        "metric2": val,
    }
}
```

### 3.5 Parameter-Specific Info

Attach targeted diagnostics per candidate section using `"{param}_specific_info"` objects.

```python
{
    "system_prompt_specific_info": {
        "scores": {"relevance": 0.7},
        "feedback": "Prompt lacks domain anchors"
    }
}
```

### 3.6 Image Payloads

Attach visual artifacts when reflection uses a VLM-compatible `reflection_lm`.

```python
from gepa.optimize_anything import Image


asi = {"rendered": Image("path/to/file")}
```

## 4. Reserved Keys and Collision Rules

Reserve the following keys for GEPA-managed capture channels:

- `log` from `oa.log()`
- `stdout` from `capture_stdio=True`
- `stderr` from `capture_stdio=True`

Avoid returning these keys directly from evaluator ASI. GEPA renames collisions with `_gepa_` prefixes and emits warnings.

- `log` -> `_gepa_log`
- `stdout` -> `_gepa_stdout`
- `stderr` -> `_gepa_stderr`

Prefer evaluator-owned names such as `run_log`, `program_output`, or `diagnostic_stderr`.

## 5. Thread Safety for ASI Logging

Propagate log context before invoking `oa.log()` in child threads. Without propagation, child-thread logs are not captured.

```python
import gepa.optimize_anything as oa


ctx = oa.get_log_context()


def worker():
    oa.set_log_context(ctx)
    oa.log("from child thread")  # Now captured
```

Keep evaluator logic single-threaded when possible. Use explicit context transfer for required concurrency.

## 6. Serialization Requirements

Keep all ASI values JSON-serializable.

- Use plain lists instead of numpy arrays.
- Use plain strings instead of custom class instances.
- Use booleans, numbers, lists, dictionaries, and `None` for absent values.

Avoid non-serializable objects that break reflection storage, caching, or downstream logging pipelines.

## 7. Consistent Field Naming and Schema Stability

Keep one stable ASI schema across all examples in a run. Schema drift prevents systematic aggregation in reflection loops.

- Keep field names in `snake_case`.
- Keep score keys suffixed with `_score`.
- Keep raw-value keys suffixed with `_raw`.
- Keep list diagnostics prefixed with `missing_` or `failing_`.
- Keep absent fields present with sentinel values (`None`, `False`) rather than omission.

## 8. Minimal and Rich ASI Examples

### 8.1 Minimal Binary-Task ASI

```python
asi: dict[str, object] = {
    "response": llm_output,
    "expected": expected_label,
    "match": is_match,
    "input": input_text,
}
```

### 8.2 Rich Multi-Criterion ASI

```python
asi: dict[str, object] = {
    "response": candidate_output,
    "expected": reference_output,
    "match": is_match,
    "input": input_text,
    "failure_category": "format_violation" if not is_match else "none",
    "violated_rule": "output must be single word" if not is_match else None,
    "parse_status": "valid" if parseable else "malformed",
    "format_score": format_score,
    "content_score": content_score,
    "combined_score": final_score,
    "scores": {
        "accuracy": accuracy,
        "latency_inv": latency_inv,
    },
    "system_prompt_specific_info": {
        "scores": {"relevance": relevance_score},
        "feedback": "Prompt omits domain vocabulary",
    },
}
```
