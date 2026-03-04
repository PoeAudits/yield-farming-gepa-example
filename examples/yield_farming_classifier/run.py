from __future__ import annotations

import argparse

from gepa.optimize_anything import EngineConfig, GEPAConfig, ReflectionConfig

from optimize_anything.runners.optimize import run_optimization
from optimize_anything.runners.results import (
    extract_best_score,
    extract_summary,
    is_probable_missing_api_key,
)

try:
    from .config import BEST_PROMPT_PATH, MAX_METRIC_CALLS, REFLECTION_LM, REFLECTION_MINIBATCH_SIZE
    from .data import load_train_set, load_val_set
    from .evaluator import mock_evaluator, real_evaluator
except ImportError:
    from config import BEST_PROMPT_PATH, MAX_METRIC_CALLS, REFLECTION_LM, REFLECTION_MINIBATCH_SIZE
    from data import load_train_set, load_val_set
    from evaluator import mock_evaluator, real_evaluator

__all__ = ["main"]

_OBJECTIVE = (
    "Maximize exact-match classification accuracy for identifying genuine, actionable "
    "yield farming opportunities in crypto messages. Labels are yes and no."
)

_BACKGROUND = (
    "Messages come from crypto Telegram and Discord channels. A yield farming opportunity "
    "is a message that presents a concrete, actionable way to earn passive yield on crypto "
    "assets - including staking, liquidity provision, vault deposits, savings products, and "
    "earn programs with stated APY/APR. Messages that are general news, require active "
    "trading, are competitions or lotteries, or lack specifics are not yield farming "
    "opportunities. The dataset includes messages where ML models agreed, disagreed, or had "
    "low confidence, so edge cases are heavily represented."
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run yield farming classifier prompt optimization.",
    )
    parser.add_argument(
        "--mock",
        action="store_true",
        help="Use deterministic mock evaluator (no external API calls).",
    )
    return parser.parse_args()


def _report_results(result: object) -> str:
    best_candidate = getattr(result, "best_candidate", {})
    optimized_prompt = ""
    if isinstance(best_candidate, dict):
        optimized_prompt = str(best_candidate.get("system_prompt", ""))

    if optimized_prompt:
        BEST_PROMPT_PATH.write_text(optimized_prompt, encoding="utf-8")
        print(f"\nBest prompt saved to: {BEST_PROMPT_PATH}")

    best_score = extract_best_score(result)
    summary = extract_summary(result)

    print("\nOptimized prompt:")
    print(optimized_prompt if optimized_prompt else "<missing system_prompt>")
    print("\nBest score:")
    print(f"{best_score:.4f}" if best_score is not None else "<unavailable>")
    print("\nSummary:")
    print(summary)
    return optimized_prompt


def main() -> int:
    args = parse_args()

    seed_candidate: dict[str, str] = {
        "system_prompt": BEST_PROMPT_PATH.read_text(encoding="utf-8").strip()
    }
    train_set = load_train_set()
    val_set = load_val_set()

    evaluator = mock_evaluator if args.mock else real_evaluator
    mode = "mock" if args.mock else "real"
    config = GEPAConfig(
        engine=EngineConfig(max_metric_calls=MAX_METRIC_CALLS),
        reflection=ReflectionConfig(
            reflection_lm=REFLECTION_LM,
            reflection_minibatch_size=REFLECTION_MINIBATCH_SIZE,
        ),
    )

    print("=== Yield Farming Classifier Optimization Prototype ===")
    print(f"Mode: {mode}")
    print(f"Training examples: {len(train_set)}")
    print(f"Validation examples: {len(val_set)}")
    print("\nSeed prompt:")
    print(seed_candidate["system_prompt"])

    try:
        result = run_optimization(
            seed_candidate=seed_candidate,
            evaluator=evaluator,
            dataset=train_set,
            valset=val_set,
            objective=_OBJECTIVE,
            background=_BACKGROUND,
            config=config,
        )
    except Exception as exc:
        if not args.mock and is_probable_missing_api_key(exc):
            print("\nOptimization failed: missing or invalid API credentials.")
            print("Set the provider API key (for example OPENAI_API_KEY) and retry.")
            return 1
        print(f"\nOptimization failed: {exc}")
        return 1

    _report_results(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
