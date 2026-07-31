"""Machine-learning utilities for predictive validation."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import KFold, cross_val_predict


@dataclass(frozen=True)
class RegressionMetrics:
    rmse: float
    mae: float
    r2: float


def regression_metrics(
    y_true: np.ndarray | pd.Series,
    y_pred: np.ndarray | pd.Series,
) -> RegressionMetrics:
    """Calculate RMSE, MAE, and R²."""
    return RegressionMetrics(
        rmse=float(np.sqrt(mean_squared_error(y_true, y_pred))),
        mae=float(mean_absolute_error(y_true, y_pred)),
        r2=float(r2_score(y_true, y_pred)),
    )


def cross_validated_predictions(
    estimator,
    features: pd.DataFrame,
    target: pd.Series,
    *,
    n_splits: int = 10,
    random_seed: int = 42,
) -> tuple[np.ndarray, RegressionMetrics]:
    """Generate shuffled K-fold out-of-fold predictions."""
    cv = KFold(
        n_splits=n_splits,
        shuffle=True,
        random_state=random_seed,
    )
    predictions = cross_val_predict(
        clone(estimator),
        features,
        target,
        cv=cv,
        n_jobs=-1,
    )
    return predictions, regression_metrics(target, predictions)


def run_verified_model_comparison(*args, **kwargs):
    """Placeholder for the manuscript-verified model comparison."""
    raise NotImplementedError(
        "Insert the verified candidate models, tuning method, and CV design."
    )
