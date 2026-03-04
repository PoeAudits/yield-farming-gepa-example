from __future__ import annotations

import os
from typing import Any

from gepa.optimize_anything import EngineConfig, GEPAConfig, ReflectionConfig

__all__ = [
    "quick_preset",
    "standard_preset",
    "thorough_preset",
    "DEFAULT_TASK_LM",
    "DEFAULT_REFLECTION_LM",
    "ENV_TASK_LM",
]

DEFAULT_TASK_LM = "openai/gpt-4.1-mini"
DEFAULT_REFLECTION_LM = "openai/gpt-4.1-mini"
ENV_TASK_LM = "OPTIMIZE_TASK_LM"
_DEFAULT_REFLECTION_LM = DEFAULT_REFLECTION_LM  # backward-compat alias
_ENV_REFLECTION_LM = "OPTIMIZE_REFLECTION_LM"
_QUICK_MAX_CALLS = 30  # Fast iteration budget for local development loops.
_STANDARD_MAX_CALLS = 100  # Balanced budget for most optimisation runs.
_THOROUGH_MAX_CALLS = 300  # Extended budget for quality-focused exploration.


def _get_reflection_lm(override: str | None) -> str:
    """Return the reflection LM string, checking override then env var then default."""
    if override is not None:
        return override
    return os.environ.get(_ENV_REFLECTION_LM, _DEFAULT_REFLECTION_LM)


def _build_preset(
    max_metric_calls: int,
    reflection_lm: str | None = None,
    reflection_minibatch_size: int | None = None,
    **overrides: Any,
) -> GEPAConfig:
    """Central factory for preset GEPAConfig instances; **overrides replace any defaults."""
    lm = _get_reflection_lm(reflection_lm)
    engine = EngineConfig(max_metric_calls=max_metric_calls)
    if reflection_minibatch_size is None:
        reflection = ReflectionConfig(reflection_lm=lm)
    else:
        reflection = ReflectionConfig(
            reflection_lm=lm,
            reflection_minibatch_size=reflection_minibatch_size,
        )
    return GEPAConfig(engine=engine, reflection=reflection, **overrides)


def quick_preset(
    reflection_lm: str | None = None,
    reflection_minibatch_size: int | None = None,
    **overrides: Any,
) -> GEPAConfig:
    """Return a GEPAConfig tuned for fast iteration and testing (max_metric_calls=30)."""
    return _build_preset(
        max_metric_calls=_QUICK_MAX_CALLS,
        reflection_lm=reflection_lm,
        reflection_minibatch_size=reflection_minibatch_size,
        **overrides,
    )


def standard_preset(
    reflection_lm: str | None = None,
    reflection_minibatch_size: int | None = None,
    **overrides: Any,
) -> GEPAConfig:
    """Return a GEPAConfig for standard optimisation runs (max_metric_calls=100)."""
    return _build_preset(
        max_metric_calls=_STANDARD_MAX_CALLS,
        reflection_lm=reflection_lm,
        reflection_minibatch_size=reflection_minibatch_size,
        **overrides,
    )


def thorough_preset(
    reflection_lm: str | None = None,
    reflection_minibatch_size: int | None = None,
    **overrides: Any,
) -> GEPAConfig:
    """Return a GEPAConfig for thorough, high-quality optimisation (max_metric_calls=300)."""
    return _build_preset(
        max_metric_calls=_THOROUGH_MAX_CALLS,
        reflection_lm=reflection_lm,
        reflection_minibatch_size=reflection_minibatch_size,
        **overrides,
    )
