from __future__ import annotations

from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any

from optimize_anything.interactive.report import ReportGenerator
from optimize_anything.interactive.session import HandoffManager, SessionState, save_session_state


class InteractiveProposer:
    def __init__(
        self,
        handoff_manager: HandoffManager,
        session_state: SessionState,
        report_generator: ReportGenerator,
    ) -> None:
        self.handoff_manager = handoff_manager
        self.session_state = session_state
        self.report_generator = report_generator

    def __call__(
        self,
        candidate: dict[str, str],
        reflective_dataset: Mapping[str, Sequence[Mapping[str, Any]]],
        components_to_update: list[str],
    ) -> dict[str, str]:
        if not components_to_update:
            raise ValueError("components_to_update must include at least one component name")

        new_prompt_path = self.handoff_manager.resolve_new_prompt_path()
        if new_prompt_path.exists():
            return self._load_resumed_candidate(new_prompt_path, components_to_update)

        if self._resume_mode_requested():
            raise FileNotFoundError(
                f"Resume mode requested but new prompt file does not exist: {new_prompt_path}"
            )

        return self._handle_start_mode(candidate, reflective_dataset)

    def _handle_start_mode(
        self,
        candidate: dict[str, str],
        reflective_dataset: Mapping[str, Sequence[Mapping[str, Any]]],
    ) -> dict[str, str]:
        self._store_reflective_dataset(reflective_dataset)

        report_content = self.report_generator.generate(
            candidate=candidate,
            reflective_dataset=reflective_dataset,
            session_state=self.session_state,
        )
        self.report_generator.write_report(
            report_content, self.handoff_manager.resolve_report_path()
        )

        prompt_used_path = self.handoff_manager.resolve_prompt_used_path()
        prompt_used_path.write_text(self._serialize_candidate(candidate), encoding="utf-8")

        save_session_state(self.session_state, self.handoff_manager.base_handoff_dir)
        return candidate

    def _load_resumed_candidate(
        self, new_prompt_path: Path, components_to_update: list[str]
    ) -> dict[str, str]:
        # Resume mode updates only the first component; all other components
        # retain their previous values.
        target_component = components_to_update[0]
        new_prompt_text = new_prompt_path.read_text(encoding="utf-8")
        return {target_component: new_prompt_text}

    def _store_reflective_dataset(
        self, reflective_dataset: Mapping[str, Sequence[Mapping[str, Any]]]
    ) -> None:
        serialized_dataset: dict[str, list[dict[str, Any]]] = {}
        for component_name, records in reflective_dataset.items():
            serialized_dataset[component_name] = [dict(record) for record in records]

        self.session_state.session_metadata["reflective_dataset"] = serialized_dataset

    def _resume_mode_requested(self) -> bool:
        mode_value = str(self.session_state.session_metadata.get("interactive_mode", "")).lower()
        if mode_value == "resume":
            return True
        return bool(self.session_state.session_metadata.get("resume_mode", False))

    def _serialize_candidate(self, candidate: dict[str, str]) -> str:
        lines: list[str] = []
        for component_name, component_text in candidate.items():
            lines.append(f"## {component_name}")
            lines.append("")
            lines.append(component_text.rstrip("\n"))
            lines.append("")

        if not lines:
            return ""

        return "\n".join(lines).rstrip() + "\n"


__all__ = ["InteractiveProposer"]
