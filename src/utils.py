"""Shared utilities for paths, random seeds, validation, and output handling."""

from __future__ import annotations

from pathlib import Path
import random
from typing import Iterable

import numpy as np
import pandas as pd


DEFAULT_RANDOM_SEED = 42


def set_random_seed(seed: int = DEFAULT_RANDOM_SEED) -> None:
    """Set reproducible random seeds for Python and NumPy."""
    random.seed(seed)
    np.random.seed(seed)


def get_project_root(start: Path | None = None) -> Path:
    """Return the repository root from the current working directory."""
    current = (start or Path.cwd()).resolve()
    if current.name in {"src", "notebooks"}:
        return current.parent
    return current


def ensure_directories(paths: Iterable[Path]) -> None:
    """Create output directories when they do not already exist."""
    for path in paths:
        path.mkdir(parents=True, exist_ok=True)


def require_columns(data: pd.DataFrame, columns: Iterable[str]) -> None:
    """Raise a clear error when required columns are missing."""
    missing = [column for column in columns if column not in data.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


def save_dataframe(
    data: pd.DataFrame,
    path: Path,
    *,
    index: bool = False,
) -> None:
    """Save a DataFrame to CSV or Excel based on the file suffix."""
    path.parent.mkdir(parents=True, exist_ok=True)

    suffix = path.suffix.lower()
    if suffix == ".csv":
        data.to_csv(path, index=index)
    elif suffix in {".xlsx", ".xls"}:
        data.to_excel(path, index=index)
    else:
        raise ValueError(f"Unsupported output format: {suffix}")
