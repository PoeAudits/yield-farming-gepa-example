from __future__ import annotations

from collections import Counter

try:
    from .data import load_train_set, load_unlabeled_set, load_val_set
except ImportError:  # pragma: no cover - allows direct script execution
    from data import load_train_set, load_unlabeled_set, load_val_set


def _truncate_text(text: str, limit: int = 120) -> str:
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    return f"{text[: limit - 3]}..."


def _print_dataset_overview(
    name: str, rows: list[dict[str, str]], *, include_label_stats: bool
) -> None:
    print(f"\n=== {name} ===")
    print(f"Total: {len(rows)}")

    source_counts = Counter(row.get("source_file", "") for row in rows)

    if include_label_stats:
        label_counts = Counter(row.get("label", "") for row in rows)
        print("Label breakdown:")
        print(f"  yes: {label_counts.get('yes', 0)}")
        print(f"  no: {label_counts.get('no', 0)}")
    else:
        print("Label breakdown: unlabeled dataset (label is empty)")

    print("Source breakdown:")
    for source in ("agreed", "disagreed", "low_confidence"):
        print(f"  {source}: {source_counts.get(source, 0)}")

    if include_label_stats:
        print("Cross-tabulation (label per source_file):")
        for source in ("agreed", "disagreed", "low_confidence"):
            subset = [row for row in rows if row.get("source_file") == source]
            source_label_counts = Counter(row.get("label", "") for row in subset)
            print(
                "  "
                f"{source}: yes={source_label_counts.get('yes', 0)}, "
                f"no={source_label_counts.get('no', 0)}"
            )

    print("Sample texts:")
    for index, row in enumerate(rows[:3], start=1):
        text = _truncate_text(row.get("text", ""))
        label = row.get("label", "") or "(empty)"
        source = row.get("source_file", "")
        print(f"  {index}. [{label}] ({source}) {text}")


if __name__ == "__main__":
    train_set = load_train_set()
    val_set = load_val_set()
    unlabeled_set = load_unlabeled_set()

    print("Yield Farming Classifier Data Preview")
    _print_dataset_overview("Train", train_set, include_label_stats=True)
    _print_dataset_overview("Validation", val_set, include_label_stats=True)
    _print_dataset_overview("Unlabeled", unlabeled_set, include_label_stats=False)
