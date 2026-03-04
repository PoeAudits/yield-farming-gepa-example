"""Tests for config preset construction and env-var override behavior."""

from __future__ import annotations

import pytest
from gepa.optimize_anything import GEPAConfig

from optimize_anything.config.presets import quick_preset, standard_preset, thorough_preset


def test_quick_preset_sets_max_metric_calls_to_30() -> None:
    config = quick_preset()

    assert isinstance(config, GEPAConfig)
    assert config.engine.max_metric_calls == 30


def test_standard_preset_sets_max_metric_calls_to_100() -> None:
    config = standard_preset()

    assert isinstance(config, GEPAConfig)
    assert config.engine.max_metric_calls == 100


def test_thorough_preset_sets_max_metric_calls_to_300() -> None:
    config = thorough_preset()

    assert isinstance(config, GEPAConfig)
    assert config.engine.max_metric_calls == 300


def test_default_reflection_lm_is_used_when_env_var_is_unset(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("OPTIMIZE_REFLECTION_LM", raising=False)

    config = quick_preset()

    assert config.reflection.reflection_lm == "openai/gpt-4.1-mini"


def test_env_var_override_is_used_for_reflection_lm(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPTIMIZE_REFLECTION_LM", "openai/gpt-4.1")

    config = standard_preset()

    assert config.reflection.reflection_lm == "openai/gpt-4.1"
