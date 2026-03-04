from __future__ import annotations

import json
from math import isclose, sqrt
from pathlib import Path

import pytest

from embedding_cohesion.callback import CohesionRecord, EmbeddingCohesionCallback
from embedding_cohesion.metrics import (
    centroid_cosine,
    compute_all_metrics,
    cosine_similarity,
    coverage,
    max_similarity,
    mean_pairwise,
    min_similarity,
)


def mock_embed_fn(text: str) -> list[float]:
    """Map text to a deterministic four-dimensional embedding."""
    base = sum(ord(ch) for ch in text)
    return [
        (base % 7) / 7.0,
        (base % 11) / 11.0,
        (base % 13) / 13.0,
        (base % 17) / 17.0,
    ]


def test_cosine_similarity_known_vectors() -> None:
    assert isclose(cosine_similarity([1.0, 0.0], [1.0, 0.0]), 1.0)
    assert isclose(cosine_similarity([1.0, 0.0], [0.0, 1.0]), 0.0)

    expected = 1 / sqrt(2)
    assert isclose(cosine_similarity([1.0, 1.0], [1.0, 0.0]), expected)


def test_metric_functions_with_simple_vectors() -> None:
    prompt = [1.0, 0.0]
    val_embeddings = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]
    centroid = [2 / 3, 2 / 3]

    assert isclose(centroid_cosine(prompt, centroid), 1 / sqrt(2), rel_tol=1e-9)
    assert isclose(mean_pairwise(prompt, val_embeddings), (1 + 0 + 1 / sqrt(2)) / 3, rel_tol=1e-9)
    assert isclose(max_similarity(prompt, val_embeddings), 1.0)
    assert isclose(min_similarity(prompt, val_embeddings), 0.0)
    assert isclose(coverage(prompt, val_embeddings, threshold=0.6), 2 / 3)


def test_compute_all_metrics_subset_and_validation() -> None:
    prompt = [1.0, 0.0]
    val_embeddings = [[1.0, 0.0], [0.0, 1.0]]
    centroid = [0.5, 0.5]

    out = compute_all_metrics(
        prompt_emb=prompt,
        val_embeddings=val_embeddings,
        val_centroid=centroid,
        metrics_list=["mean_pairwise", "coverage"],
        coverage_threshold=0.4,
    )
    assert set(out.keys()) == {"mean_pairwise", "coverage"}
    assert isclose(out["mean_pairwise"], 0.5)
    assert isclose(out["coverage"], 0.5)

    with pytest.raises(ValueError):
        compute_all_metrics(
            prompt_emb=prompt,
            val_embeddings=val_embeddings,
            val_centroid=centroid,
            metrics_list=["unknown"],
            coverage_threshold=0.5,
        )


def test_callback_lifecycle_tracks_records_and_scores() -> None:
    callback = EmbeddingCohesionCallback(
        valset=[{"text": "alpha"}, {"text": "beta"}],
        embed_fn=mock_embed_fn,
        text_extractor=lambda item: item["text"],
    )

    callback.on_optimization_start(
        {
            "seed_candidate": {"system": "seed"},
            "trainset_size": 10,
            "valset_size": 2,
            "config": {},
        }
    )
    callback.on_proposal_end(
        {
            "iteration": 1,
            "new_instructions": {"system": "s1", "user": "u1"},
        }
    )
    callback.on_valset_evaluated(
        {
            "iteration": 1,
            "candidate_idx": 3,
            "average_score": 0.82,
        }
    )
    callback.on_candidate_accepted(
        {
            "iteration": 1,
            "new_candidate_idx": 3,
            "new_score": 0.82,
        }
    )

    assert len(callback.records) == 1
    record = callback.records[0]
    assert isinstance(record, CohesionRecord)
    assert record.iteration == 1
    assert record.candidate_idx == 3
    assert record.eval_score == 0.82
    assert record.accepted is True
    assert record.candidate_text == "s1\nu1"
    assert set(record.section_metrics.keys()) == {"system", "user"}
    assert record.full_metrics


def test_section_level_metrics_are_computed_per_section() -> None:
    callback = EmbeddingCohesionCallback(
        valset=["x", "y"],
        embed_fn=mock_embed_fn,
        metrics=["mean_pairwise"],
    )
    callback.on_optimization_start(
        {
            "seed_candidate": {"system": "seed"},
            "trainset_size": 1,
            "valset_size": 2,
            "config": {},
        }
    )
    callback.on_proposal_end(
        {
            "iteration": 2,
            "new_instructions": {"a": "left", "b": "right"},
        }
    )

    record = callback.records[0]
    assert set(record.section_metrics.keys()) == {"a", "b"}
    assert set(record.section_metrics["a"].keys()) == {"mean_pairwise"}
    assert set(record.section_metrics["b"].keys()) == {"mean_pairwise"}


def test_empty_valset_and_single_item_valset_edge_cases() -> None:
    empty_callback = EmbeddingCohesionCallback(
        valset=[],
        embed_fn=mock_embed_fn,
        metrics=["centroid_cosine", "coverage"],
    )
    empty_callback.on_optimization_start(
        {
            "seed_candidate": {"system": "seed"},
            "trainset_size": 0,
            "valset_size": 0,
            "config": {},
        }
    )
    empty_callback.on_proposal_end(
        {
            "iteration": 1,
            "new_instructions": {"system": "hello"},
        }
    )

    empty_metrics = empty_callback.records[0].full_metrics
    assert empty_metrics["centroid_cosine"] == 0.0
    assert empty_metrics["coverage"] == 0.0

    single_callback = EmbeddingCohesionCallback(
        valset=["hello"],
        embed_fn=mock_embed_fn,
        metrics=["max_similarity", "min_similarity"],
    )
    single_callback.on_optimization_start(
        {
            "seed_candidate": {"system": "seed"},
            "trainset_size": 1,
            "valset_size": 1,
            "config": {},
        }
    )
    single_callback.on_proposal_end(
        {
            "iteration": 1,
            "new_instructions": {"system": "hello"},
        }
    )

    single_metrics = single_callback.records[0].full_metrics
    assert isclose(single_metrics["max_similarity"], single_metrics["min_similarity"])


def test_identical_and_orthogonal_embedding_cases() -> None:
    assert isclose(cosine_similarity([1.0, 0.0], [1.0, 0.0]), 1.0)
    assert isclose(cosine_similarity([1.0, 0.0], [0.0, 1.0]), 0.0)


def test_output_file_written_on_optimization_end(tmp_path: Path) -> None:
    output_path = tmp_path / "cohesion.json"
    callback = EmbeddingCohesionCallback(
        valset=["alpha", "beta"],
        embed_fn=mock_embed_fn,
        output_path=str(output_path),
    )

    callback.on_optimization_start(
        {
            "seed_candidate": {"system": "seed"},
            "trainset_size": 1,
            "valset_size": 2,
            "config": {},
        }
    )
    callback.on_proposal_end(
        {
            "iteration": 1,
            "new_instructions": {"system": "candidate"},
        }
    )
    callback.on_valset_evaluated(
        {
            "iteration": 1,
            "candidate_idx": 9,
            "average_score": 0.7,
        }
    )
    callback.on_candidate_rejected(
        {
            "iteration": 1,
            "old_score": 0.8,
            "new_score": 0.7,
            "reason": "worse",
        }
    )
    callback.on_optimization_end(
        {
            "best_candidate_idx": 1,
            "total_iterations": 1,
            "total_metric_calls": 1,
            "final_state": {},
        }
    )

    assert output_path.exists()
    payload = json.loads(output_path.read_text(encoding="utf-8"))
    assert "records" in payload
    assert "summary" in payload
    assert payload["records"][0]["accepted"] is False


def test_summary_generation_with_multiple_records_and_correlation_hook(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    callback = EmbeddingCohesionCallback(
        valset=["a", "b"],
        embed_fn=mock_embed_fn,
        metrics=["mean_pairwise"],
    )
    callback.on_optimization_start(
        {
            "seed_candidate": {"system": "seed"},
            "trainset_size": 1,
            "valset_size": 2,
            "config": {},
        }
    )

    callback.on_proposal_end({"iteration": 1, "new_instructions": {"system": "x"}})
    callback.on_valset_evaluated({"iteration": 1, "candidate_idx": 1, "average_score": 0.2})

    callback.on_proposal_end({"iteration": 2, "new_instructions": {"system": "y"}})
    callback.on_valset_evaluated({"iteration": 2, "candidate_idx": 2, "average_score": 0.9})

    monkeypatch.setattr(
        "embedding_cohesion.callback._pearson_correlations",
        lambda metrics_by_name, eval_scores: {"mean_pairwise": 0.5},
    )

    out = callback.summary()
    assert out["num_records"] == 2
    assert out["num_scored_records"] == 2
    assert out["correlations"]["mean_pairwise"] == 0.5


def test_callback_ignores_events_without_matching_iteration() -> None:
    callback = EmbeddingCohesionCallback(valset=["a"], embed_fn=mock_embed_fn)
    callback.on_optimization_start(
        {
            "seed_candidate": {"system": "seed"},
            "trainset_size": 1,
            "valset_size": 1,
            "config": {},
        }
    )

    callback.on_valset_evaluated({"iteration": 99, "candidate_idx": 1, "average_score": 0.3})
    callback.on_candidate_rejected(
        {
            "iteration": 99,
            "old_score": 0.7,
            "new_score": 0.3,
            "reason": "missing",
        }
    )

    assert callback.records == []
