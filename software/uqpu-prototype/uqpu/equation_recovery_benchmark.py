"""Small deterministic baseline for equation-structure recovery.

EQN-002 starts by rediscovering known laws under held-out evaluation before the
project trusts any AI-assisted search on unknown physics.  This module is a
calibration baseline, not a new-law generator.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Iterable, Sequence


Dimension = tuple[int, int, int]  # exponents for (mass, length, time)


@dataclass(frozen=True)
class PowerLawFit:
    power: int
    coefficient: float
    train_rmse: float
    holdout_rmse: float
    dimensionally_allowed: bool


def combine_dimensions(factors: Sequence[tuple[Dimension, int]]) -> Dimension:
    m = l = t = 0
    for dimension, power in factors:
        if len(dimension) != 3:
            raise ValueError("dimension must be an (M,L,T) exponent tuple")
        m += dimension[0] * power
        l += dimension[1] * power
        t += dimension[2] * power
    return (m, l, t)


def _rmse(actual: Sequence[float], predicted: Sequence[float]) -> float:
    if len(actual) != len(predicted) or not actual:
        raise ValueError("RMSE inputs must be non-empty and equal length")
    return math.sqrt(sum((a - p) ** 2 for a, p in zip(actual, predicted)) / len(actual))


def fit_scalar_power_law(
    x: Sequence[float],
    y: Sequence[float],
    *,
    power: int,
    train_indices: Sequence[int],
    holdout_indices: Sequence[int],
    dimensionally_allowed: bool = True,
) -> PowerLawFit:
    """Fit y ~= c*x**power on train rows and evaluate a disjoint holdout."""
    if len(x) != len(y) or not x:
        raise ValueError("x and y must be non-empty and equal length")
    if not train_indices or not holdout_indices:
        raise ValueError("train and holdout sets are required")
    if set(train_indices) & set(holdout_indices):
        raise ValueError("train and holdout indices must be disjoint")
    all_indices = tuple(train_indices) + tuple(holdout_indices)
    if any(i < 0 or i >= len(x) for i in all_indices):
        raise ValueError("index outside dataset")

    phi = [float(v) ** power for v in x]
    denom = sum(phi[i] ** 2 for i in train_indices)
    if denom == 0:
        raise ValueError("candidate basis is zero on all training points")
    coefficient = sum(phi[i] * float(y[i]) for i in train_indices) / denom

    train_actual = [float(y[i]) for i in train_indices]
    train_pred = [coefficient * phi[i] for i in train_indices]
    holdout_actual = [float(y[i]) for i in holdout_indices]
    holdout_pred = [coefficient * phi[i] for i in holdout_indices]

    return PowerLawFit(
        power=power,
        coefficient=coefficient,
        train_rmse=_rmse(train_actual, train_pred),
        holdout_rmse=_rmse(holdout_actual, holdout_pred),
        dimensionally_allowed=bool(dimensionally_allowed),
    )


def recover_power_law(
    x: Sequence[float],
    y: Sequence[float],
    *,
    candidate_powers: Iterable[int],
    train_indices: Sequence[int],
    holdout_indices: Sequence[int],
    allowed_powers: set[int] | None = None,
) -> PowerLawFit:
    """Return the lowest held-out-error candidate after optional physics gate."""
    fits: list[PowerLawFit] = []
    for power in candidate_powers:
        allowed = allowed_powers is None or power in allowed_powers
        fit = fit_scalar_power_law(
            x,
            y,
            power=power,
            train_indices=train_indices,
            holdout_indices=holdout_indices,
            dimensionally_allowed=allowed,
        )
        if allowed:
            fits.append(fit)
    if not fits:
        raise ValueError("no dimensionally allowed candidate")
    return min(fits, key=lambda item: (item.holdout_rmse, item.train_rmse, abs(item.power), item.power))


def kinetic_energy_calibration() -> dict[str, object]:
    """Recover E = c*v^p for fixed mass from hidden p=2 data.

    The coefficient absorbs the fixed 0.5*m factor.  A separate dimensional
    gate checks that, if the coefficient is only allowed to carry mass units,
    velocity must appear with power 2 to match energy dimensions.
    """
    velocities = (0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0)
    mass = 3.0
    energies = tuple(0.5 * mass * v * v for v in velocities)
    train = (0, 1, 3, 5)
    holdout = (2, 4, 6)

    mass_dim: Dimension = (1, 0, 0)
    velocity_dim: Dimension = (0, 1, -1)
    energy_dim: Dimension = (1, 2, -2)
    allowed = {
        p
        for p in range(1, 5)
        if combine_dimensions(((mass_dim, 1), (velocity_dim, p))) == energy_dim
    }
    fit = recover_power_law(
        velocities,
        energies,
        candidate_powers=(1, 2, 3, 4),
        train_indices=train,
        holdout_indices=holdout,
        allowed_powers=allowed,
    )
    return {
        "law": "kinetic_energy_fixed_mass",
        "hidden_structure": "E proportional to v^2",
        "selected_power": fit.power,
        "coefficient": fit.coefficient,
        "train_rmse": fit.train_rmse,
        "holdout_rmse": fit.holdout_rmse,
        "dimensionally_allowed_powers": sorted(allowed),
        "evidence_level": "MODEL_ONLY",
        "new_physical_law_claim": False,
    }
