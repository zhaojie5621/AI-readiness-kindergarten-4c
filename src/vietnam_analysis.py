"""Reusable functions for the Vietnam ECE analysis.

The main explanatory analysis is observed-variable path analysis.
It should not be relabeled as structural equation modeling.
"""

from __future__ import annotations

import pandas as pd

from .utils import require_columns


def audit_vietnam_data(
    data: pd.DataFrame,
    *,
    expected_n: int = 426,
) -> dict[str, int]:
    """Return basic integrity information for the Vietnam ECE dataset."""
    if len(data) != expected_n:
        raise ValueError(
            f"Expected {expected_n} Vietnam ECE records, found {len(data)}."
        )

    return {
        "n_rows": len(data),
        "n_columns": data.shape[1],
        "n_missing_cells": int(data.isna().sum().sum()),
    }


def build_vietnam_scales(
    data: pd.DataFrame,
    scale_map: dict[str, list[str]],
) -> pd.DataFrame:
    """Create mean composite scores from verified item groupings."""
    output = data.copy()

    for scale_name, item_columns in scale_map.items():
        require_columns(output, item_columns)
        output[scale_name] = output[item_columns].mean(axis=1)

    return output


def run_observed_variable_path_model(*args, **kwargs):
    """Placeholder for the verified Vietnam observed-variable path analysis."""
    raise NotImplementedError(
        "Insert only the verified observed-variable path workflow."
    )


def calculate_pd_priority_index(*args, **kwargs):
    """Placeholder for the verified exploratory PD priority index."""
    raise NotImplementedError(
        "Insert the verified PD priority-index formula and sensitivity checks."
    )
