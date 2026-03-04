from __future__ import annotations

from pathlib import Path

from optimize_anything.interactive import ReportGenerator, SessionState
from tests.conftest import build_score_record, build_session_state


def test_report_generator_renders_required_sections_with_rich_data(tmp_path: Path) -> None:
    session_state = build_session_state(
        tmp_path,
        iteration=3,
        score_history=[
            build_score_record(1, 0.70, fp_count=4, fn_count=3, delta=None),
            build_score_record(2, 0.76, fp_count=3, fn_count=2, delta=0.06),
        ],
    )
    reflective_dataset = {
        "system_prompt": [
            {
                "Inputs": "Earn APY from liquidity pools now!",
                "Generated Outputs": "yes",
                "Feedback": "expected: no, got: yes. false positive due to marketing hype.",
            },
            {
                "Inputs": "Stake token for rewards each epoch.",
                "Generated Outputs": "no",
                "Feedback": "expected: yes, got: no. ambiguous wording in instructions.",
            },
        ]
    }
    raw_asi = {
        "system_prompt": [
            {
                "response": "yes",
                "expected": "no",
                "explanation": "Mentions APY but not protocol mechanics.",
                "confidence": "0.38",
                "source_file": "discord_dump_01.jsonl",
            },
            {
                "response": "no",
                "expected": "yes",
                "explanation": "Contains staking intent.",
                "confidence": "0.55",
                "source_file": "telegram_dump_02.jsonl",
            },
        ]
    }

    report = ReportGenerator(raw_evaluation_asi=raw_asi).generate(
        candidate={"system_prompt": "Classifier instructions"},
        reflective_dataset=reflective_dataset,
        session_state=session_state,
    )

    assert "## Header" in report
    assert "## Aggregate scores" in report
    assert "## Score history" in report
    assert "## False positives" in report
    assert "## False negatives" in report
    assert "## Edge cases / ambiguous examples" in report
    assert "## Prompt refinement suggestions" in report
    assert "## GEPA acceptance note" in report
    assert "Earn APY from liquidity pools now!" in report
    assert "Stake token for rewards each epoch." in report
    assert "discord_dump_01.jsonl" in report
    assert "telegram_dump_02.jsonl" in report
    assert "| 2 | 0.7600 | +0.0600 | 3 | 2 |" in report
    assert "new_sum > old_sum" in report


def test_report_generator_degrades_gracefully_with_minimal_dataset(tmp_path: Path) -> None:
    session_state = SessionState(
        current_iteration=1, handoff_dir=tmp_path / "handoff", run_dir=tmp_path / "run"
    )
    reflective_dataset = {
        "system_prompt": [
            {
                "Inputs": "Generic text",
                "Generated Outputs": "yes",
                "Feedback": "expected: no, got: yes",
            }
        ]
    }

    report = ReportGenerator().generate(
        candidate={"system_prompt": "Seed prompt"},
        reflective_dataset=reflective_dataset,
        session_state=session_state,
    )

    assert "- Accuracy: n/a" in report
    assert "### Source: unknown" in report
    assert "Confidence:" not in report
    assert "Explanation:" not in report
    assert "No low-confidence or ambiguous examples identified." in report


def test_report_generator_write_report_creates_parent_directories(tmp_path: Path) -> None:
    generator = ReportGenerator()
    report_path = tmp_path / "handoff" / "iteration_001" / "report.md"

    generator.write_report("# Report\n", report_path)

    assert report_path.exists()
    assert report_path.read_text(encoding="utf-8") == "# Report\n"
