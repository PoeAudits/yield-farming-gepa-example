# GEPA API Patterns

Detailed reference for the `optimize_anything` library and underlying GEPA `optimize_anything` API. Covers function signatures, configuration structures, seed candidate formats, optimization modes, and result consumption. Consult this file when the core SKILL.md leaves a specific API question unanswered.

---

## 1. `optimize_anything()` Function Signature

The top-level entry point for optimization is `gepa.optimize_anything.optimize_anything`. The local library exposes two wrappers that delegate to this function: `run_optimization` for in-memory candidates and `run_from_file` for file-based artifacts.

### Direct GEPA call

```python
from gepa.optimize_anything import optimize_anything, GEPAConfig, EngineConfig, ReflectionConfig

result = optimize_anything(
    seed_candidate={"system_prompt": "Classify the sentiment of the text."},
    evaluator=eval_fn,
    dataset=train_examples,
    valset=val_examples,          # optional; enables generalization tracking
    objective="Maximize exact-match accuracy on sentiment labels.",
    background="Labels are 'positive', 'negative', and 'neutral'. Output only the label.",
    config=GEPAConfig(
        engine=EngineConfig(max_metric_calls=100),
        reflection=ReflectionConfig(reflection_lm="openai/gpt-4.1-mini"),
    ),
)
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `seed_candidate` | `dict[str, str]` | Yes | Initial artifact state; named sections that GEPA mutates during search. |
| `evaluator` | `EvaluatorFn` | Yes | Callable scoring each candidate-example pair; consult `skills/optimize-anything/references/evaluator-implementations.md` for protocol details. |
| `dataset` | `list[dict]` | Yes | Training examples used for evaluation feedback during search. |
| `valset` | `list[dict] \| None` | No | Held-out validation examples for generalization tracking. Defaults to `None`. |
| `objective` | `str` | Yes | One sentence describing the measurable optimization target. |
| `background` | `str` | No | Constraints, domain rules, and context for the reflection loop. Defaults to `""`. |
| `config` | `GEPAConfig` | Yes | Engine and reflection configuration controlling budget and model selection. |

### Local wrapper: `run_optimization`

`src/optimize_anything/runners/optimize.py`

```python
from optimize_anything import run_optimization

result = run_optimization(
    seed_candidate={"system_prompt": "Classify the sentiment of the text."},
    evaluator=eval_fn,
    dataset=train_examples,
    objective="Maximize exact-match accuracy on sentiment labels.",
    background="Output only the label: positive, negative, or neutral.",
    valset=val_examples,          # optional
    config=None,                  # explicit GEPAConfig; overrides preset when provided
    preset="standard",            # "quick" | "standard" | "thorough"; ignored when config is set
)
```

`run_optimization` resolves the preset to a `GEPAConfig` when `config` is `None`. Providing an explicit `config` bypasses preset resolution entirely.

### Local wrapper: `run_from_file`

```python
from optimize_anything import run_from_file

result = run_from_file(
    path="agents/classifier.md",  # .md, .markdown, or .csv
    evaluator=eval_fn,
    dataset=train_examples,
    objective="Maximize exact-match accuracy on sentiment labels.",
    background="Output only the label: positive, negative, or neutral.",
    valset=val_examples,
    config=None,
    preset="standard",
    write_back=False,             # set True to persist best_candidate to disk on completion
)
```

`run_from_file` dispatches to `load_markdown_artifact` or `load_csv_artifact` based on the file extension, then calls `run_optimization`. When `write_back=True`, it writes `result.best_candidate` back to `path` using the matching writer.

Supported extensions: `.md`, `.markdown`, `.csv`. All other extensions raise `ValueError`.

---

## 2. Configuration Structures

### `GEPAConfig`

`GEPAConfig` is the top-level configuration object. It composes `EngineConfig`, `ReflectionConfig`, `MergeConfig`, `RefinerConfig`, `TrackingConfig`, and `stop_callbacks`.

```python
from gepa.optimize_anything import (
    GEPAConfig,
    EngineConfig,
    ReflectionConfig,
    MergeConfig,
    RefinerConfig,
    TrackingConfig,
)

config = GEPAConfig(
    engine=EngineConfig(max_metric_calls=100),
    reflection=ReflectionConfig(reflection_lm="openai/gpt-4.1-mini"),
    merge=MergeConfig(),
    refiner=RefinerConfig(),
    tracking=TrackingConfig(),
)
```

### `EngineConfig`

Controls optimization budget, execution behavior, and evaluation strategy.

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `max_metric_calls` | `int` | varies by preset | Maximum number of evaluator calls during the search. |
| `max_candidate_proposals` | `int \| None` | `None` | Alternative stopping condition based on proposal count. |
| `parallel` | `bool` | unset upstream | Whether to run evaluator calls in parallel where supported. |
| `cache_evaluation` | `bool` | `False` | Enable evaluator-result caching to avoid repeated metric calls. |
| `cache_evaluation_storage` | `str` | `"memory"` | Cache backend: `"memory"`, `"disk"`, or `"auto"`. |
| `run_dir` | `str \| None` | `None` | Required cache directory when using disk-backed evaluation cache. |
| `capture_stdio` | `bool` | `False` | Capture `print()` output into ASI `stdout`/`stderr` keys. |
| `candidate_selection_strategy` | `str` | implementation-defined | Candidate chooser strategy: `"pareto"`, `"current_best"`, or `"epsilon_greedy"`. |
| `frontier_type` | `str` | implementation-defined | Frontier construction type: `"instance"`, `"objective"`, `"hybrid"`, or `"cartesian"`. |

### `ReflectionConfig`

Controls reflection behavior and candidate proposal settings.

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `reflection_lm` | `str` | `"openai/gpt-4.1-mini"` | LiteLLM model string for the reflection proposer. |
| `reflection_minibatch_size` | `int` | mode-dependent | Examples shown per reflection step; use `1` for single-task and `3` for multi-task defaults. |
| `skip_perfect_score` | `bool` | `False` | Skip reflection updates for examples at or above `perfect_score`. |
| `perfect_score` | `float \| None` | `None` | Threshold used by `skip_perfect_score`; required when skipping perfect scores. |
| `module_selector` | `str` | `"round_robin"` | Candidate section selector: `"round_robin"` or `"all"`. |

### `RefinerConfig`

Enable post-evaluation refinement where the LLM proposes improved candidate content from feedback prior to the next cycle.

### Stopping Conditions and Validation Notes

At least one stopping condition (`max_metric_calls` or `max_candidate_proposals`) MUST be set. Omitting both raises `ValueError`.

Common configuration pitfalls:

- Missing stopping condition -> `ValueError`
- `cache_evaluation_storage="disk"` without `run_dir` -> `ValueError`
- `skip_perfect_score=True` without `perfect_score` -> `ValueError`

The reflection LM proposes revised candidate sections based on ASI from each evaluation step. Higher-quality models produce better revisions at higher cost.

### Preset Factories

`src/optimize_anything/config/presets.py`

Three factory functions produce `GEPAConfig` instances at common budget levels.

```python
from optimize_anything import quick_preset, standard_preset, thorough_preset

# Fast iteration and evaluator debugging
config = quick_preset()                                    # max_metric_calls=30

# Regular development runs
config = standard_preset()                                 # max_metric_calls=100

# High-quality sweeps and final search
config = thorough_preset()                                 # max_metric_calls=300

# Override reflection model for any preset
config = standard_preset(reflection_lm="openai/gpt-4.1")
```

The reflection LM defaults to `"openai/gpt-4.1-mini"` when neither the `reflection_lm` argument nor the `OPTIMIZE_REFLECTION_LM` environment variable is set.

All preset factories accept `**overrides` to forward additional keyword arguments to `GEPAConfig`.

### Configuration Selection Strategy

| Phase | Preset | Rationale |
|-------|--------|-----------|
| Evaluator debugging | `quick` | Fail fast; 30 calls is sufficient to detect broken evaluators. |
| Stable development | `standard` | 100 calls provides consistent improvement signal without high cost. |
| Final quality sweep | `thorough` | 300 calls explores more of the candidate space at known evaluator quality. |

Increase budget only after the evaluator produces stable, diagnostic ASI and the candidate decomposition is locked.

---

## 3. `seed_candidate` Format

The `seed_candidate` is a `dict[str, str]` where each key names a section of the artifact and each value holds the section's text content. GEPA mutates individual section values across iterations; stable key names preserve evaluator assumptions across the run.

### General rules

- All values must be `str`. No nested structures, no `None` values.
- Keys must remain stable across all runs in a comparison series.
- Use semantically meaningful names that match evaluator key access patterns.
- Keys are UTF-8-safe text; avoid special characters that break writer functions.

### Artifact type: plain text prompt

Single-section candidate for simple prompt optimization.

```python
seed_candidate = {
    "system_prompt": (
        "Act as a helpful assistant. "
        "Classify the sentiment of the user's text."
    )
}
```

The evaluator accesses `candidate["system_prompt"]` directly.

### Artifact type: agent definition

Agent definitions use a 5-field YAML frontmatter and six markdown body sections. Load with `load_markdown_artifact` to produce stable keys.

```python
from optimize_anything import load_markdown_artifact

seed_candidate = load_markdown_artifact("agents/classifier-agent.md")
# Resulting keys (example):
# {
#   "frontmatter": "name: classifier-agent\ndescription: ...\n...",
#   "## 1. Role": "Execute classification tasks ...",
#   "## 2. Responsibilities": "- Identify entity type ...",
#   "## 3. Process": "1. Read the input ...",
#   "## 4. Constraints": "MUST NOT ...",
#   "## 5. Output Format": "Return JSON with ...",
#   "## 6. Edge Cases": "If input is empty ...",
# }
```

The markdown loader uses ATX header lines as section keys verbatim (e.g., `"## 1. Role"`). The frontmatter block is stored under the `"frontmatter"` key; pre-header body text is stored under `"body"` when present.

### Artifact type: skill

Skills use a 2-field YAML frontmatter and eight numbered markdown body sections.

```python
seed_candidate = load_markdown_artifact("skills/my-skill/SKILL.md")
# Resulting keys (example):
# {
#   "frontmatter": "name: my-skill\ndescription: ...",
#   "## 1. Purpose and Scope": "Use this skill when ...",
#   "## 2. Core Principles": "1. Principle one ...",
#   ...
#   "## 8. References Usage": "Consult reference files ...",
# }
```

Target section-level keys in the evaluator when measuring skill quality criteria (completeness, actionability of principles, accuracy of checklist items).

### Artifact type: command

Commands use a 2-field YAML frontmatter and five body sections.

```python
seed_candidate = load_markdown_artifact("commands/my-command.md")
# Resulting keys (example):
# {
#   "frontmatter": "name: my-command\ndescription: ...",
#   "## Input Handling": "Accept ...",
#   "## Mode Detection": "Detect ...",
#   "## Execution Flow": "1. Parse input ...",
#   "## Failure Handling": "On error ...",
#   "## Output Contract": "Return ...",
# }
```

### Artifact type: CSV

CSV artifacts map to column-keyed or row-keyed sections.

```python
from optimize_anything import load_csv_artifact

# Default mode="columns": each column becomes a section
seed_candidate = load_csv_artifact("data/prompts.csv")
# Resulting keys match column headers:
# {
#   "instruction": "Classify this text.\nLabel the sentiment.\n...",
#   "format_hint": "Output one word.\nUse lowercase.\n...",
# }

# mode="rows": each row becomes a section
seed_candidate = load_csv_artifact("data/prompts.csv", mode="rows")
# Resulting keys are positional:
# {
#   "row_0": "instruction=Classify this text.\nformat_hint=Output one word.",
#   "row_1": "instruction=Label the sentiment.\nformat_hint=Use lowercase.",
# }
```

Use `mode="columns"` when optimizing column-level content that applies across all rows (e.g., column descriptions or instructions). Use `mode="rows"` when each row represents a distinct configuration to optimize independently.

---

## 4. Optimization Modes

### Single-task optimization

Maximize performance on one narrowly defined task with one objective function and one dataset.

**When to use:** The artifact has one purpose, the evaluator measures one thing, and all dataset examples share the same schema and evaluation logic.

```python
from optimize_anything import run_optimization, llm_classification_evaluator, standard_preset

evaluator = llm_classification_evaluator(
    model="openai/gpt-4.1-mini",
    label_key="label",
    input_key="text",
    prompt_key="system_prompt",
)

dataset = [
    {"text": "This product is amazing!", "label": "positive"},
    {"text": "Terrible experience.", "label": "negative"},
    {"text": "It arrived on time.", "label": "neutral"},
    # ... more examples
]

result = run_optimization(
    seed_candidate={"system_prompt": "Classify the sentiment of the text."},
    evaluator=evaluator,
    dataset=dataset,
    objective="Maximize exact-match accuracy on three-class sentiment labels.",
    background="Labels are 'positive', 'negative', 'neutral'. Return only the label string.",
    preset="standard",
)
```

### Multi-task optimization

Balance performance across multiple related tasks sharing one candidate representation.

**When to use:** One artifact must satisfy multiple task families simultaneously. The candidate structure offers cross-task leverage — a shared system prompt or policy text that affects all task branches. Multi-task mode requires mixed dataset examples with task routing in the evaluator.

```python
from optimize_anything import run_optimization

def multi_task_evaluator(
    candidate: dict[str, str], example: dict[str, Any]
) -> tuple[float, dict[str, Any]]:
    task = example["task"]
    if task == "sentiment":
        return _score_sentiment(candidate, example)
    if task == "routing":
        return _score_routing(candidate, example)
    return 0.0, {"error": f"unknown task: {task}"}

mixed_dataset = [
    {"task": "sentiment", "text": "Love it!", "label": "positive"},
    {"task": "routing", "text": "Cancel my order", "label": "returns"},
    # ... balanced across task families
]

result = run_optimization(
    seed_candidate={
        "system_prompt": "Act as a customer support classifier.",
        "task_instructions": "For sentiment tasks, output positive/negative/neutral. "
                             "For routing tasks, output the department name.",
    },
    evaluator=multi_task_evaluator,
    dataset=mixed_dataset,
    objective="Maximize accuracy across sentiment classification and request routing tasks.",
    background="Both task families share one system prompt. Routing labels: billing, returns, technical.",
    preset="standard",
)
```

Keep task examples balanced in the dataset. Unbalanced datasets bias the optimizer toward the dominant task.

### Generalization optimization

Optimize for transfer quality on held-out examples, not only in-sample fit.

**When to use:** Production conditions differ from training distribution. The artifact must handle linguistic diversity, domain shift, or edge-case inputs that are not fully represented in the training set. Generalization mode requires a `valset` that is strictly held out from search feedback.

```python
from optimize_anything import run_optimization

train_examples = [
    {"text": "Absolutely loved it.", "label": "positive"},
    {"text": "Awful product.", "label": "negative"},
    # ... representative training distribution
]

val_examples = [
    {"text": "Meh, it's okay I guess.", "label": "neutral"},     # hedged language
    {"text": "Not bad for the price.", "label": "neutral"},       # negation
    {"text": "DO NOT BUY THIS", "label": "negative"},            # all-caps emphasis
    # ... distribution-shifted examples
]

result = run_optimization(
    seed_candidate={"system_prompt": "Classify the sentiment."},
    evaluator=evaluator,
    dataset=train_examples,
    valset=val_examples,
    objective="Maximize accuracy on held-out examples including hedged, negated, and emphatic language.",
    background="Labels are 'positive', 'negative', 'neutral'. "
               "Training set lacks hedged phrasing and negation patterns.",
    preset="thorough",
)
```

Include transfer failure indicators in ASI when using generalization mode. Structured ASI fields like `failure_category` or `negation_detected` help the reflection loop target linguistic patterns that cause transfer failures.

---

## 5. Result Object

`optimize_anything` returns a result object containing the best candidate found and associated scoring information. The exact schema is defined by the GEPA library upstream; access the following fields reliably.

### `result.best_candidate`

The optimized artifact as `dict[str, str]`. Keys match those of the original `seed_candidate`. This is the primary output of any optimization run.

```python
result = run_optimization(...)

# Extract optimized sections
best = result.best_candidate
optimized_prompt = best["system_prompt"]
print(optimized_prompt)
```

### Score access

Score field names vary by GEPA version. Check available attributes before assuming a specific name.

```python
# Common score fields — check availability before accessing
if hasattr(result, "best_score"):
    print(f"Best training score: {result.best_score:.4f}")

if hasattr(result, "score"):
    print(f"Score: {result.score:.4f}")
```

When `valset` is provided, the result may include validation-specific score fields. Inspect the result object's attributes or summary fields to identify what is available.

### Applying the best candidate

**In-memory application:**

```python
from optimize_anything import run_optimization, write_markdown_artifact

result = run_optimization(...)
best = result.best_candidate

# Write back to the original file path
write_markdown_artifact(best, "agents/classifier-agent.md")
```

**File-based flow with write-back:**

```python
from optimize_anything import run_from_file

result = run_from_file(
    path="agents/classifier-agent.md",
    evaluator=evaluator,
    dataset=train_examples,
    objective="...",
    preset="standard",
    write_back=True,              # writes best_candidate to path on completion
)
```

**Manual section extraction:**

```python
result = run_optimization(...)
best = result.best_candidate

# Apply individual sections selectively
print("Optimized system prompt:")
print(best["system_prompt"])

print("Optimized task instructions:")
print(best.get("task_instructions", ""))
```

---

## 6. Evaluator Protocol

Consult `skills/optimize-anything/references/evaluator-implementations.md` for the full evaluator protocol, template evaluators, implementation patterns, and common mistakes.

The evaluator signature is `(candidate: dict[str, str], example: dict[str, Any]) -> tuple[float, dict[str, Any]]`. Template evaluators (`llm_classification_evaluator`, `rubric_evaluator`, `mock_evaluator`) are importable from `optimize_anything`.

---

## 7. Public Import Surface

All public names are importable from the package root `optimize_anything`. Prefer root imports in scripts and external workflows.

```python
from optimize_anything import (
    # runners
    run_optimization,
    run_from_file,
    # loaders
    load_markdown_artifact,
    load_csv_artifact,
    write_markdown_artifact,
    write_csv_artifact,
    # evaluators
    EvaluatorFn,
    llm_classification_evaluator,
    rubric_evaluator,
    mock_evaluator,
    # config presets
    quick_preset,
    standard_preset,
    thorough_preset,
)
```

Import `GEPAConfig`, `EngineConfig`, and `ReflectionConfig` directly from `gepa.optimize_anything` when constructing custom configurations not covered by the preset factories.

```python
from gepa.optimize_anything import GEPAConfig, EngineConfig, ReflectionConfig
```
