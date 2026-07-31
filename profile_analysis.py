"""Profile-analysis utilities."""

from __future__ import annotations

import pandas as pd
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler


def fit_gmm_candidates(
    data: pd.DataFrame,
    variables: list[str],
    *,
    min_components: int = 1,
    max_components: int = 6,
    random_seed: int = 42,
) -> pd.DataFrame:
    """Fit candidate Gaussian mixture models and return AIC/BIC diagnostics."""
    matrix = data[variables].dropna()
    scaled = StandardScaler().fit_transform(matrix)

    rows: list[dict[str, float | int]] = []

    for n_components in range(min_components, max_components + 1):
        model = GaussianMixture(
            n_components=n_components,
            covariance_type="full",
            random_state=random_seed,
            n_init=20,
        )
        model.fit(scaled)

        rows.append(
            {
                "n_components": n_components,
                "aic": model.aic(scaled),
                "bic": model.bic(scaled),
                "converged": int(model.converged_),
            }
        )

    return pd.DataFrame(rows)


def fit_selected_profile_model(*args, **kwargs):
    """Placeholder for the verified final profile solution and labeling."""
    raise NotImplementedError(
        "Add the verified profile-selection and labeling workflow."
    )
