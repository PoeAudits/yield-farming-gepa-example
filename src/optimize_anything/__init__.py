from __future__ import annotations

__version__ = "0.1.0"

from optimize_anything.config import (
    DEFAULT_REFLECTION_LM,
    DEFAULT_TASK_LM,
    ENV_TASK_LM,
    quick_preset,
    standard_preset,
    thorough_preset,
)
from optimize_anything.evaluators import (
    EvaluatorFn,
    extract_response_text,
    llm_classification_evaluator,
    mock_evaluator,
    rubric_evaluator,
)
from optimize_anything.interactive import (
    HandoffManager,
    InteractiveProposer,
    IterationScoreRecord,
    ReportGenerator,
    SessionState,
    load_session_state,
    save_session_state,
)
from optimize_anything.loaders import (
    load_csv_artifact,
    load_markdown_artifact,
    write_csv_artifact,
    write_markdown_artifact,
)
from optimize_anything.runners import run_from_file, run_optimization

__all__ = [
    # version
    "__version__",
    # loaders
    "load_markdown_artifact",
    "load_csv_artifact",
    "write_markdown_artifact",
    "write_csv_artifact",
    # evaluators
    "EvaluatorFn",
    "extract_response_text",
    "llm_classification_evaluator",
    "rubric_evaluator",
    "mock_evaluator",
    # config presets and constants
    "quick_preset",
    "standard_preset",
    "thorough_preset",
    "DEFAULT_TASK_LM",
    "DEFAULT_REFLECTION_LM",
    "ENV_TASK_LM",
    # runners
    "run_optimization",
    "run_from_file",
    # interactive proposer
    "InteractiveProposer",
    "ReportGenerator",
    "SessionState",
    "HandoffManager",
    "IterationScoreRecord",
    "load_session_state",
    "save_session_state",
]
