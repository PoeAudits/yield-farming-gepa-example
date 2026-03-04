from __future__ import annotations

import math

VALID_METRICS = {
    "centroid_cosine",
    "mean_pairwise",
    "max_similarity",
    "min_similarity",
    "coverage",
}


def cosine_similarity(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if len(a) != len(b) or not a:
        return 0.0

    dot = sum(x * y for x, y in zip(a, b, strict=True))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0
    return dot / (norm_a * norm_b)


def centroid_cosine(prompt_emb: list[float], val_centroid: list[float]) -> float:
    """Compute cosine similarity between prompt and validation centroid."""
    return cosine_similarity(prompt_emb, val_centroid)


def mean_pairwise(prompt_emb: list[float], val_embeddings: list[list[float]]) -> float:
    """Compute mean cosine similarity to all validation embeddings."""
    if not val_embeddings:
        return 0.0
    similarities = [cosine_similarity(prompt_emb, val_emb) for val_emb in val_embeddings]
    return sum(similarities) / len(similarities)


def max_similarity(prompt_emb: list[float], val_embeddings: list[list[float]]) -> float:
    """Compute maximum cosine similarity to any validation embedding."""
    if not val_embeddings:
        return 0.0
    return max(cosine_similarity(prompt_emb, val_emb) for val_emb in val_embeddings)


def min_similarity(prompt_emb: list[float], val_embeddings: list[list[float]]) -> float:
    """Compute minimum cosine similarity to any validation embedding."""
    if not val_embeddings:
        return 0.0
    return min(cosine_similarity(prompt_emb, val_emb) for val_emb in val_embeddings)


def coverage(prompt_emb: list[float], val_embeddings: list[list[float]], threshold: float) -> float:
    """Compute the fraction of similarities above the threshold."""
    if not val_embeddings:
        return 0.0

    hits = 0
    for val_emb in val_embeddings:
        if cosine_similarity(prompt_emb, val_emb) > threshold:
            hits += 1
    return hits / len(val_embeddings)


def compute_all_metrics(
    prompt_emb: list[float],
    val_embeddings: list[list[float]],
    val_centroid: list[float],
    metrics_list: list[str],
    coverage_threshold: float,
) -> dict[str, float]:
    """Compute a selected set of embedding cohesion metrics."""
    unknown = [metric for metric in metrics_list if metric not in VALID_METRICS]
    if unknown:
        msg = f"Unsupported cohesion metrics: {unknown}"
        raise ValueError(msg)

    output: dict[str, float] = {}
    for metric in metrics_list:
        if metric == "centroid_cosine":
            output[metric] = centroid_cosine(prompt_emb, val_centroid)
        elif metric == "mean_pairwise":
            output[metric] = mean_pairwise(prompt_emb, val_embeddings)
        elif metric == "max_similarity":
            output[metric] = max_similarity(prompt_emb, val_embeddings)
        elif metric == "min_similarity":
            output[metric] = min_similarity(prompt_emb, val_embeddings)
        elif metric == "coverage":
            output[metric] = coverage(prompt_emb, val_embeddings, coverage_threshold)
    return output
