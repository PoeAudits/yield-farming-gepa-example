from __future__ import annotations

from pathlib import Path

__all__ = [
    "REFLECTION_LM",
    "MAX_METRIC_CALLS",
    "REFLECTION_MINIBATCH_SIZE",
    "BEST_PROMPT_PATH",
]

# ---------------------------------------------------------------------------
# Model configuration
# ---------------------------------------------------------------------------

# LLM used for classifying messages during evaluation.
TASK_LM = "openai/gpt-4.1-mini"

# LLM used by the optimizer for reflection and candidate generation.
REFLECTION_LM = "openai/gpt-5.2"

# ---------------------------------------------------------------------------
# Optimization budget
# ---------------------------------------------------------------------------

# Maximum number of evaluator calls the optimizer may make.
MAX_METRIC_CALLS = 1000

# Number of examples sampled per reflection minibatch.
REFLECTION_MINIBATCH_SIZE = 20

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

# Path to save/load the best optimized prompt.
BEST_PROMPT_PATH = Path(__file__).parent / "best_prompt.md"
