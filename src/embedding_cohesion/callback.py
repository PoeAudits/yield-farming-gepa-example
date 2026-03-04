from __future__ import annotations

import json
from collections.abc import Callable
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, TypedDict

from embedding_cohesion.metrics import VALID_METRICS, compute_all_metrics


class OptimizationStartEvent(TypedDict):
    """Subset of GEPA optimization-start event fields."""

    seed_candidate: dict[str, str]
    trainset_size: int
    valset_size: int
    config: dict[str, Any]


class ProposalEndEvent(TypedDict):
    """Subset of GEPA proposal-end event fields."""

    iteration: int
    new_instructions: dict[str, str]


class ValsetEvaluatedEvent(TypedDict):
    """Subset of GEPA valset-evaluated event fields."""

    iteration: int
    candidate_idx: int
    average_score: float


class CandidateAcceptedEvent(TypedDict):
    """Subset of GEPA candidate-accepted event fields."""

    iteration: int
    new_candidate_idx: int
    new_score: float


class CandidateRejectedEvent(TypedDict):
    """Subset of GEPA candidate-rejected event fields."""

    iteration: int
    old_score: float
    new_score: float
    reason: str


class OptimizationEndEvent(TypedDict):
    """Subset of GEPA optimization-end event fields."""

    best_candidate_idx: int
    total_iterations: int
    total_metric_calls: int
    final_state: Any


@dataclass
class CohesionRecord:
    iteration: int
    candidate_idx: int | None
    candidate_text: str
    section_metrics: dict[str, dict[str, float]]
    full_metrics: dict[str, float]
    eval_score: float | None
    accepted: bool | None


class EmbeddingCohesionCallback:
    """Observe embedding cohesion between candidates and the validation set."""

    def __init__(
        self,
        valset: list[Any],
        embed_fn: Callable[[str], list[float]],
        text_extractor: Callable[[Any], str] | None = None,
        metrics: list[str] | None = None,
        coverage_threshold: float = 0.5,
        output_path: str | None = None,
    ) -> None:
        self._valset = valset
        self._embed_fn = embed_fn
        self._text_extractor = text_extractor or str
        selected_metrics = list(VALID_METRICS) if metrics is None else metrics
        self._metrics = self._validate_metrics(selected_metrics)
        self._coverage_threshold = coverage_threshold
        self._output_path = Path(output_path) if output_path is not None else None

        self._val_embeddings: list[list[float]] = []
        self._val_centroid: list[float] = []
        self._record_by_iteration: dict[int, CohesionRecord] = {}

        self.records: list[CohesionRecord] = []
        self._summary_cache: dict[str, Any] = {}

    def on_optimization_start(self, event: OptimizationStartEvent) -> None:
        del event
        self._val_embeddings = [self._embed_fn(self._text_extractor(item)) for item in self._valset]
        self._val_centroid = _compute_centroid(self._val_embeddings)

    def on_proposal_end(self, event: ProposalEndEvent) -> None:
        candidate_sections = event["new_instructions"]
        candidate_text = "\n".join(candidate_sections.values())

        full_emb = self._embed_fn(candidate_text)
        full_metrics = compute_all_metrics(
            prompt_emb=full_emb,
            val_embeddings=self._val_embeddings,
            val_centroid=self._val_centroid,
            metrics_list=self._metrics,
            coverage_threshold=self._coverage_threshold,
        )

        section_metrics: dict[str, dict[str, float]] = {}
        for section_name, section_text in candidate_sections.items():
            section_emb = self._embed_fn(section_text)
            section_metrics[section_name] = compute_all_metrics(
                prompt_emb=section_emb,
                val_embeddings=self._val_embeddings,
                val_centroid=self._val_centroid,
                metrics_list=self._metrics,
                coverage_threshold=self._coverage_threshold,
            )

        record = CohesionRecord(
            iteration=event["iteration"],
            candidate_idx=None,
            candidate_text=candidate_text,
            section_metrics=section_metrics,
            full_metrics=full_metrics,
            eval_score=None,
            accepted=None,
        )
        self.records.append(record)
        self._record_by_iteration[event["iteration"]] = record

    def on_valset_evaluated(self, event: ValsetEvaluatedEvent) -> None:
        record = self._record_by_iteration.get(event["iteration"])
        if record is None:
            return
        record.candidate_idx = event["candidate_idx"]
        record.eval_score = event["average_score"]

    def on_candidate_accepted(self, event: CandidateAcceptedEvent) -> None:
        record = self._record_by_iteration.get(event["iteration"])
        if record is None:
            return
        record.accepted = True
        record.candidate_idx = event["new_candidate_idx"]

    def on_candidate_rejected(self, event: CandidateRejectedEvent) -> None:
        record = self._record_by_iteration.get(event["iteration"])
        if record is None:
            return
        record.accepted = False

    def on_optimization_end(self, event: OptimizationEndEvent) -> None:
        del event
        self._summary_cache = self.summary()
        if self._output_path is None:
            return

        payload = {
            "records": [asdict(record) for record in self.records],
            "summary": self._summary_cache,
        }
        self._output_path.parent.mkdir(parents=True, exist_ok=True)
        self._output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def summary(self) -> dict[str, Any]:
        scored_records = [record for record in self.records if record.eval_score is not None]
        eval_scores = [record.eval_score for record in scored_records]

        metrics_by_name: dict[str, list[float]] = {metric: [] for metric in self._metrics}
        for record in scored_records:
            for metric_name in self._metrics:
                metrics_by_name[metric_name].append(record.full_metrics.get(metric_name, 0.0))

        correlations: dict[str, float | None] = {}
        if len(eval_scores) < 2:
            correlations = {metric: None for metric in self._metrics}
        else:
            correlations = _pearson_correlations(metrics_by_name, eval_scores)

        accepted_count = len([record for record in self.records if record.accepted is True])
        rejected_count = len([record for record in self.records if record.accepted is False])

        return {
            "num_records": len(self.records),
            "num_scored_records": len(scored_records),
            "accepted_count": accepted_count,
            "rejected_count": rejected_count,
            "metrics": list(self._metrics),
            "correlations": correlations,
        }

    @staticmethod
    def _validate_metrics(metrics: list[str]) -> list[str]:
        unknown = [metric for metric in metrics if metric not in VALID_METRICS]
        if unknown:
            msg = f"Unsupported cohesion metrics: {unknown}"
            raise ValueError(msg)
        return metrics


def _compute_centroid(embeddings: list[list[float]]) -> list[float]:
    if not embeddings:
        return []

    dims = len(embeddings[0])
    centroid = [0.0 for _ in range(dims)]
    for emb in embeddings:
        if len(emb) != dims:
            msg = "Validation embeddings must have matching dimensions"
            raise ValueError(msg)
        for i, value in enumerate(emb):
            centroid[i] += value
    total = float(len(embeddings))
    return [value / total for value in centroid]


def _pearson_correlations(
    metrics_by_name: dict[str, list[float]], eval_scores: list[float | None]
) -> dict[str, float | None]:
    try:
        from scipy.stats import pearsonr  # type: ignore[import-not-found]
    except Exception:
        return {metric: None for metric in metrics_by_name}

    filtered_eval_scores = [score for score in eval_scores if score is not None]
    correlations: dict[str, float | None] = {}
    for metric_name, values in metrics_by_name.items():
        if len(values) < 2 or len(filtered_eval_scores) < 2:
            correlations[metric_name] = None
            continue
        try:
            corr, _ = pearsonr(values, filtered_eval_scores)
        except Exception:
            correlations[metric_name] = None
        else:
            correlations[metric_name] = float(corr)
    return correlations
