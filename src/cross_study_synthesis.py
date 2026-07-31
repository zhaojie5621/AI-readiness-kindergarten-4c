"""Cross-study synthesis utilities.

Respondent-level datasets must never be pooled in this module.
"""

from __future__ import annotations

import pandas as pd


def validate_aggregate_only(data: pd.DataFrame) -> None:
    """Reject obvious respondent-level identifiers in synthesis inputs."""
    prohibited = {
        "respondent_id",
        "participant_id",
        "name",
        "email",
        "phone",
    }
    overlap = prohibited.intersection({column.lower() for column in data.columns})
    if overlap:
        raise ValueError(
            f"Respondent-level or identifying fields detected: {sorted(overlap)}"
        )


def borda_rank(
    rankings: pd.DataFrame,
    *,
    alternative_column: str,
    rank_columns: list[str],
) -> pd.DataFrame:
    """Aggregate multiple rank columns using a lower-is-better Borda total."""
    result = rankings[[alternative_column] + rank_columns].copy()
    result["borda_total"] = result[rank_columns].sum(axis=1)
    result["final_rank"] = (
        result["borda_total"]
        .rank(method="min", ascending=True)
        .astype(int)
    )
    return result.sort_values(["final_rank", "borda_total"])


def build_convergence_matrix(*args, **kwargs):
    """Placeholder for the verified evidence-convergence framework."""
    raise NotImplementedError(
        "Insert the verified construct, effect, profile, and priority synthesis."
    )
