"""Clean missing values in the clinical-trials dataset and compare them visually."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


DATA_PATH = Path(__file__).with_name("clinical_trials_2025_2026.csv")
CLEANED_DATA_PATH = Path(__file__).with_name("clinical_trials_2025_2026_cleaned.csv")
PLOT_PATH = Path(__file__).with_name("missing_values_before_after.png")
PHASE_MISSING_VALUE = -1


def normalize_missing_values(data: pd.DataFrame) -> pd.DataFrame:
    """Convert empty strings and semicolon-only intervention placeholders to NA."""
    normalized = data.copy()
    string_columns = normalized.select_dtypes(include=["object", "string"]).columns

    for column in string_columns:
        values = normalized[column].astype("string").str.strip()
        placeholders = values.eq("") | values.str.fullmatch(r"(?:;\s*)+", na=False)
        normalized.loc[placeholders, column] = pd.NA

    return normalized


def clean_dataset(data: pd.DataFrame) -> pd.DataFrame:
    """Fill missing values without dropping trial records."""
    cleaned = normalize_missing_values(data)
    numeric_columns = cleaned.select_dtypes(include="number").columns
    categorical_columns = cleaned.select_dtypes(
        include=["object", "string", "category"]
    ).columns

    for column in numeric_columns:
        if column == "phase_numeric":
            cleaned[column] = cleaned[column].fillna(PHASE_MISSING_VALUE)
            continue

        median = cleaned[column].median()
        if pd.isna(median):
            raise ValueError(f"Cannot impute '{column}': it has no non-missing values.")
        cleaned[column] = cleaned[column].fillna(median)

    for column in categorical_columns:
        cleaned[column] = cleaned[column].fillna("Unknown")

    remaining_missing = cleaned.isna().sum()
    remaining_missing = remaining_missing[remaining_missing > 0]
    if not remaining_missing.empty:
        raise ValueError(
            "Missing values remain after cleaning: "
            f"{remaining_missing.to_dict()}"
        )

    return cleaned


def plot_missing_values(before: pd.DataFrame, after: pd.DataFrame) -> None:
    """Save side-by-side missing-value percentages for the original and clean data."""
    before_percent = before.isna().mean().mul(100)
    after_percent = after.isna().mean().mul(100)
    max_percent = max(float(before_percent.max()), float(after_percent.max()), 1.0)

    figure, axes = plt.subplots(1, 2, figsize=(16, 7), sharey=True)
    for axis, percentages, title, color in (
        (axes[0], before_percent, "Before cleaning", "indianred"),
        (axes[1], after_percent, "After cleaning", "seagreen"),
    ):
        bars = axis.bar(percentages.index, percentages.values, color=color)
        axis.set_title(title)
        axis.set_ylabel("Missing values (%)")
        axis.set_ylim(0, max_percent * 1.15)
        axis.tick_params(axis="x", labelrotation=90)
        axis.bar_label(bars, fmt="%.1f%%", padding=3, fontsize=7)

    figure.suptitle("Missing Values by Column")
    figure.tight_layout()
    figure.savefig(PLOT_PATH, dpi=150, bbox_inches="tight")
    plt.close(figure)


def main() -> None:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    original = pd.read_csv(DATA_PATH)
    before = normalize_missing_values(original)
    cleaned = clean_dataset(original)

    plot_missing_values(before, cleaned)
    cleaned.to_csv(CLEANED_DATA_PATH, index=False)

    print(f"Rows retained: {len(original):,} / {len(cleaned):,}")
    print(f"Missing values before cleaning: {int(before.isna().sum().sum()):,}")
    print(f"Missing values after cleaning: {int(cleaned.isna().sum().sum()):,}")
    print(f"Cleaned dataset saved to: {CLEANED_DATA_PATH}")
    print(f"Before/after plot saved to: {PLOT_PATH}")


if __name__ == "__main__":
    main()