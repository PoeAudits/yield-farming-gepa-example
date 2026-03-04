# optimize-anything

A Python library for iterative text artifact optimization using the GEPA `optimize_anything` API. Define a seed candidate as a dictionary of named text sections, supply an evaluator that scores outputs, and let the optimization loop improve the artifact against your dataset. Supports system prompts, instruction templates, rubric text, and any markdown or CSV artifact that can be decomposed into structured sections.

## Installation

```bash
uv sync
```

## Quick Start

Run the classification prototype with a deterministic mock evaluator (no API key required):

```bash
make optimize-mock
```

Run the same prototype with a real LLM evaluator (requires an API key):

```bash
make optimize
```

The prototype optimizes a sentiment classification prompt against a small train/val dataset and prints the best candidate and score.

## Library API

### Loaders

```python
from optimize_anything.io.loaders import load_markdown_artifact, load_csv_artifact

candidate = load_markdown_artifact("prompt.md")   # dict[str, str] keyed by heading
rows = load_csv_artifact("examples.csv")          # list[dict[str, str]]
```

### Writers

```python
from optimize_anything.io.writers import write_markdown_artifact, write_csv_artifact

write_markdown_artifact(candidate, "output.md")
write_csv_artifact(rows, "output.csv")
```

### Evaluators

```python
from optimize_anything.evaluators import (
    llm_classification_evaluator,
    rubric_evaluator,
    mock_evaluator,
)
```

- `llm_classification_evaluator` — scores candidates via LLM classification against expected labels
- `rubric_evaluator` — scores candidates against a rubric using LLM judgment
- `mock_evaluator` — deterministic evaluator for local testing without API calls

### Configuration Presets

```python
from optimize_anything.config.presets import quick_preset, standard_preset, thorough_preset

config = quick_preset()      # fast iteration, low budget
config = standard_preset()   # stable development runs
config = thorough_preset()   # quality-focused sweep, higher budget
```

### Runner

```python
from optimize_anything.runners.optimize import run_optimization, run_from_file

result = run_optimization(
    seed_candidate={"system_prompt": "Classify the text as positive, negative, or neutral."},
    evaluator=evaluator,
    dataset=train_set,
    valset=val_set,
    objective="Maximize exact-match classification accuracy.",
    background="Small prototype dataset for quick iteration.",
    config=quick_preset(),
)

# Or load the full workflow from a config file
result = run_from_file("workflow.yaml")
```

## Makefile Commands

| Command            | Description                                     |
|--------------------|-------------------------------------------------|
| `make install`     | Install dependencies                            |
| `make sync`        | Sync dependencies (alias for install)           |
| `make lock`        | Update lock file                                |
| `make optimize`    | Run classification prototype with real evaluator|
| `make optimize-mock` | Run classification prototype with mock evaluator|
| `make test`        | Run tests (pytest)                              |
| `make lint`        | Lint code (ruff check)                          |
| `make fmt`         | Format code (ruff format)                       |
| `make clean`       | Clean build artifacts                           |
| `make help`        | Show all available commands                     |

## Development

```bash
make test   # run pytest
make lint   # run ruff check
make fmt    # run ruff format
```

## Agent Documentation

See [`skills/optimize-anything/SKILL.md`](skills/optimize-anything/SKILL.md) for the agent-facing operating guide covering candidate representation, evaluator protocol, configuration presets, and multi-task optimization patterns.
