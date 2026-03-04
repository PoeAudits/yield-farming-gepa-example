from __future__ import annotations

from pathlib import Path
from typing import Any, Literal

from gepa.optimize_anything import GEPAConfig
from gepa.optimize_anything import optimize_anything as gepa_optimize_anything

from optimize_anything.config import quick_preset, standard_preset, thorough_preset
from optimize_anything.evaluators.base import EvaluatorFn
from optimize_anything.loaders import (
    load_csv_artifact,
    load_markdown_artifact,
    write_csv_artifact,
    write_markdown_artifact,
)

__all__ = ["run_optimization", "run_from_file"]


def run_optimization(
    seed_candidate: dict[str, str],
    evaluator: EvaluatorFn,
    dataset: list[dict[str, Any]],
    objective: str,
    background: str = "",
    valset: list[dict[str, Any]] | None = None,
    config: GEPAConfig | None = None,
    preset: Literal["quick", "standard", "thorough"] = "quick",
) -> Any:
    """Run GEPA optimization for an in-memory candidate and return the raw result."""
    resolved_config = config if config is not None else _resolve_preset_config(preset)
    return gepa_optimize_anything(
        seed_candidate=seed_candidate,
        evaluator=evaluator,
        dataset=dataset,
        valset=valset,
        objective=objective,
        background=background,
        config=resolved_config,
    )


def run_from_file(
    path: str | Path,
    evaluator: EvaluatorFn,
    dataset: list[dict[str, Any]],
    objective: str,
    background: str = "",
    valset: list[dict[str, Any]] | None = None,
    config: GEPAConfig | None = None,
    preset: Literal["quick", "standard", "thorough"] = "quick",
    write_back: bool = False,
) -> Any:
    """Load a candidate artifact from disk, optimize it, and optionally write the best result."""
    artifact_path = Path(path)
    seed_candidate = _load_candidate_for_path(artifact_path)

    result = run_optimization(
        seed_candidate=seed_candidate,
        evaluator=evaluator,
        dataset=dataset,
        objective=objective,
        background=background,
        valset=valset,
        config=config,
        preset=preset,
    )

    if write_back:
        optimized_candidate = result.best_candidate
        _write_candidate_for_path(artifact_path, optimized_candidate)

    return result


def _resolve_preset_config(preset: str) -> GEPAConfig:
    """Return the GEPA config preset for the provided preset name."""
    presets = {
        "quick": quick_preset,
        "standard": standard_preset,
        "thorough": thorough_preset,
    }
    preset_factory = presets.get(preset)
    if preset_factory is None:
        msg = "Invalid preset. Expected one of: quick, standard, thorough."
        raise ValueError(msg)
    return preset_factory()


def _load_candidate_for_path(path: Path) -> dict[str, str]:
    """Load a candidate artifact based on file extension."""
    suffix = path.suffix.lower()
    if suffix in {".md", ".markdown"}:
        return load_markdown_artifact(path)
    if suffix == ".csv":
        return load_csv_artifact(path)

    msg = "Unsupported artifact extension. Expected .md, .markdown, or .csv."
    raise ValueError(msg)


def _write_candidate_for_path(path: Path, candidate: dict[str, str]) -> None:
    """Write an optimized candidate artifact based on file extension."""
    suffix = path.suffix.lower()
    if suffix in {".md", ".markdown"}:
        write_markdown_artifact(candidate, path)
        return
    if suffix == ".csv":
        write_csv_artifact(candidate, path)
        return

    msg = "Unsupported artifact extension. Expected .md, .markdown, or .csv."
    raise ValueError(msg)
