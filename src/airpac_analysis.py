"""Reusable functions for AIRPAC-Q analysis.

Final functions must be verified against the frozen manuscript,
Supplementary Material, and analytical dataset before public release.
"""

from __future__ import annotations

import pandas as pd

from .utils import require_columns


def audit_airpac_data(
    data: pd.DataFrame,
    *,
    expected_n: int = 528,
) -> dict[str, int]:
    """Return basic integrity information for the AIRPAC-Q dataset."""
    if len(data) != expected_n:
        raise ValueError(
            f"Expected {expected_n} AIRPAC-Q records, found {len(data)}."
        )

    return {
        "n_rows": len(data),
        "n_columns": data.shape[1],
        "n_missing_cells": int(data.isna().sum().sum()),
    }


def build_airpac_scales(
    data: pd.DataFrame,
    scale_map: dict[str, list[str]],
) -> pd.DataFrame:
    """Create mean composite scores using a verified scale-to-item map."""
    output = data.copy()

    for scale_name, item_columns in scale_map.items():
        require_columns(output, item_columns)
        output[scale_name] = output[item_columns].mean(axis=1)

    return output


def run_airpac_models(*args, **kwargs):
    """Placeholder for the verified CFA, SEM, mediation, profile, and ML workflow."""
    raise NotImplementedError(
        "Insert only the verified AIRPAC-Q analytical workflow."
    )
