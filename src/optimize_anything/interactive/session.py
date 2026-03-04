from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

SESSION_STATE_FILENAME = "session_state.json"


@dataclass
class IterationScoreRecord:
    iteration: int
    aggregate_accuracy: float
    false_positive_count: int
    false_negative_count: int
    delta_from_previous: float | None = None


@dataclass
class SessionState:
    current_iteration: int
    score_history: list[IterationScoreRecord] = field(default_factory=list)
    handoff_dir: Path = field(default_factory=Path)
    run_dir: Path = field(default_factory=Path)
    session_metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "current_iteration": self.current_iteration,
            "score_history": [
                {
                    "iteration": score.iteration,
                    "aggregate_accuracy": score.aggregate_accuracy,
                    "false_positive_count": score.false_positive_count,
                    "false_negative_count": score.false_negative_count,
                    "delta_from_previous": score.delta_from_previous,
                }
                for score in self.score_history
            ],
            "handoff_dir": str(self.handoff_dir),
            "run_dir": str(self.run_dir),
            "session_metadata": self.session_metadata,
        }

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> SessionState:
        score_history = [
            IterationScoreRecord(**entry) for entry in payload.get("score_history", [])
        ]
        return cls(
            current_iteration=payload["current_iteration"],
            score_history=score_history,
            handoff_dir=Path(payload["handoff_dir"]),
            run_dir=Path(payload["run_dir"]),
            session_metadata=payload.get("session_metadata", {}),
        )


def save_session_state(state: SessionState, path: str | Path) -> Path:
    state_path = _ensure_state_file_path(path)
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(state.to_dict(), indent=2, sort_keys=True), encoding="utf-8")
    return state_path


def load_session_state(path: str | Path) -> SessionState:
    state_path = _ensure_state_file_path(path)
    raw_payload = json.loads(state_path.read_text(encoding="utf-8"))
    return SessionState.from_dict(raw_payload)


class HandoffManager:
    def __init__(self, base_handoff_dir: str | Path, state: SessionState) -> None:
        self.base_handoff_dir = Path(base_handoff_dir)
        self.state = state
        self.base_handoff_dir.mkdir(parents=True, exist_ok=True)

    def resolve_iteration_dir(self, iteration: int | None = None) -> Path:
        iteration_value = self.state.current_iteration if iteration is None else iteration
        iteration_dir = self.base_handoff_dir / f"iteration_{iteration_value:03d}"
        iteration_dir.mkdir(parents=True, exist_ok=True)
        return iteration_dir

    def resolve_report_path(self) -> Path:
        return self.resolve_iteration_dir() / "report.md"

    def resolve_prompt_used_path(self) -> Path:
        return self.resolve_iteration_dir() / "prompt_used.md"

    def resolve_new_prompt_path(self) -> Path:
        return self.resolve_iteration_dir() / "new_prompt.md"

    def advance_iteration(self) -> Path:
        self.state.current_iteration += 1
        return self.resolve_iteration_dir()


def _ensure_state_file_path(path: str | Path) -> Path:
    target_path = Path(path)
    if target_path.suffix.lower() == ".json":
        return target_path
    return target_path / SESSION_STATE_FILENAME


__all__ = [
    "IterationScoreRecord",
    "SessionState",
    "save_session_state",
    "load_session_state",
    "HandoffManager",
]
