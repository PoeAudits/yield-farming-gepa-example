# Examples

This directory contains self-contained examples demonstrating how to use optimize-anything
for different optimization use cases.

## Structure

- `classification/` - Hyperparameter optimization for classification models

## Running Examples

Each example can be run directly from the project root:

```bash
python examples/classification/<script>.py
```

Dependencies are managed via the project's standard environment. Run `make install` first.

## Adding Examples

Place new examples in a subdirectory named after the task type (e.g., `regression/`,
`clustering/`). Each subdirectory should include an `__init__.py` and a brief description
of the use case in comments at the top of each script.
