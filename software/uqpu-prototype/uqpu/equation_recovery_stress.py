"""Noise/distractor stress tests for EQN-002 equation recovery.

This module intentionally stays inside a small, transparent expression grammar.
It is a calibration instrument for the discovery workflow, not a new-physics
search engine and not evidence of a new physical law.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import random
import statistics
from typing import Iterable, Sequence


@dataclass(frozen=True)
class CandidateExpression:
    powers: tuple[int, ...]

    @property
    def name(self) -> str:
        return " + ".join(f"z^{power}" for power in self.powers)

    @property
    def complexity(self) -> int:
        return len(self.powers)


@dataclass(frozen=True)
class CandidateFit:
    candidate: CandidateExpression
    coefficients: tuple[float, ...]
    holdout_rmse: float
    extrapolation_rmse: float
    parsimony_score: float


DEFAULT_CANDIDATES: tuple[CandidateExpression, ...] = tuple(
    CandidateExpression(powers)
    for powers in (
        (1,),
        (2,),
        (3,),
        (4,),
        (1, 2),
        (1, 3),
        (2, 3),
        (2, 4),
        (1, 2, 3),
        (1, 2, 4),
        (2, 3, 4),
    )
)


def _solve_linear_system(matrix: Sequence[Sequence[float]], rhs: Sequence[float]) -> tuple[float, ...]:
    if len(matrix) != len(rhs) or not rhs:
        raise ValueError("matrix/rhs dimensions must match and be non-empty")
    size = len(rhs)
    augmented = [list(map(float, matrix[row])) + [float(rhs[row])] for row in range(size)]
    if any(len(row) != size + 1 for row in augmented):
        raise ValueError("matrix must be square")

    for column in range(size):
        pivot = max(range(column, size), key=lambda row: abs(augmented[row][column]))
        if abs(augmented[pivot][column]) < 1e-12:
            raise ValueError("singular candidate basis")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]

        pivot_value = augmented[column][column]
        for j in range(column, size + 1):
            augmented[column][j] /= pivot_value

        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            for j in range(column, size + 1):
                augmented[row][j] -= factor * augmented[column][j]

    return tuple(augmented[row][size] for row in range(size))


def _fit_coefficients(
    z: Sequence[float],
    y: Sequence[float],
    candidate: CandidateExpression,
    indices: Sequence[int],
) -> tuple[float, ...]:
    if not indices:
        raise ValueError("fit indices are required")
    powers = candidate.powers
    gram = [
        [sum((z[i] ** p) * (z[i] ** q) for i in indices) for q in powers]
        for p in powers
    ]
    rhs = [sum((z[i] ** p) * y[i] for i in indices) for p in powers]
    return _solve_linear_system(gram, rhs)


def _predict(z_value: float, candidate: CandidateExpression, coefficients: Sequence[float]) -> float:
    return sum(coefficient * z_value**power for coefficient, power in zip(coefficients, candidate.powers))


def _rmse(
    z: Sequence[float],
    y: Sequence[float],
    candidate: CandidateExpression,
    coefficients: Sequence[float],
    indices: Sequence[int],
) -> float:
    if not indices:
        raise ValueError("evaluation indices are required")
    return math.sqrt(
        sum((y[i] - _predict(z[i], candidate, coefficients)) ** 2 for i in indices) / len(indices)
    )


def fit_candidate(
    z: Sequence[float],
    y: Sequence[float],
    candidate: CandidateExpression,
    *,
    train_indices: Sequence[int],
    holdout_indices: Sequence[int],
    extrapolation_indices: Sequence[int],
    parsimony_penalty_strength: float = 4.0,
) -> CandidateFit:
    """Fit on train rows and score on disjoint holdout/extrapolation rows.

    z is dimensionless. That makes every polynomial distractor in this benchmark
    dimensionally admissible when the fitted output coefficients carry the output
    unit. This prevents dimensional analysis from revealing the hidden exponent.
    """
    if len(z) != len(y) or not z:
        raise ValueError("z and y must be non-empty and equal length")
    groups = [set(train_indices), set(holdout_indices), set(extrapolation_indices)]
    if any(not group for group in groups):
        raise ValueError("train, holdout and extrapolation sets are required")
    if groups[0] & groups[1] or groups[0] & groups[2] or groups[1] & groups[2]:
        raise ValueError("train, holdout and extrapolation sets must be disjoint")
    if any(i < 0 or i >= len(z) for group in groups for i in group):
        raise ValueError("index outside dataset")
    if parsimony_penalty_strength < 0:
        raise ValueError("parsimony_penalty_strength must be non-negative")

    coefficients = _fit_coefficients(z, y, candidate, train_indices)
    holdout_rmse = _rmse(z, y, candidate, coefficients, holdout_indices)
    extrapolation_rmse = _rmse(z, y, candidate, coefficients, extrapolation_indices)

    # BIC-inspired but deliberately named differently because lambda may differ
    # from the canonical BIC coefficient. Evaluation error is measured only on
    # the holdout set; coefficients are fitted only on the train set.
    mse = max(holdout_rmse * holdout_rmse, 1e-18)
    parsimony_score = (
        len(holdout_indices) * math.log(mse)
        + parsimony_penalty_strength * candidate.complexity * math.log(len(holdout_indices))
    )
    return CandidateFit(
        candidate=candidate,
        coefficients=coefficients,
        holdout_rmse=holdout_rmse,
        extrapolation_rmse=extrapolation_rmse,
        parsimony_score=parsimony_score,
    )


def run_noise_trial(
    seed: int,
    noise_sigma: float,
    *,
    candidates: Iterable[CandidateExpression] = DEFAULT_CANDIDATES,
    parsimony_penalty_strength: float = 4.0,
) -> dict[str, CandidateFit]:
    """Run one hidden-law trial with unit-consistent distractor expressions."""
    if noise_sigma < 0:
        raise ValueError("noise_sigma must be non-negative")

    z = (0.25, 0.40, 0.60, 0.85, 1.10, 1.40, 1.75, 2.00, 2.40, 2.80, 3.20, 3.80)
    train = (0, 2, 4, 6, 7)
    holdout = (1, 3, 5)
    extrapolation = (8, 9, 10, 11)
    rng = random.Random(seed)

    # Hidden structure: y = 1.5*z^2. Multiplicative Gaussian noise scales with
    # signal magnitude. This is synthetic MODEL_ONLY evidence.
    y = tuple(1.5 * value * value * (1.0 + rng.gauss(0.0, noise_sigma)) for value in z)
    fits = [
        fit_candidate(
            z,
            y,
            candidate,
            train_indices=train,
            holdout_indices=holdout,
            extrapolation_indices=extrapolation,
            parsimony_penalty_strength=parsimony_penalty_strength,
        )
        for candidate in candidates
    ]
    if not fits:
        raise ValueError("at least one candidate is required")

    error_only = min(
        fits,
        key=lambda fit: (fit.holdout_rmse, fit.candidate.complexity, fit.candidate.powers),
    )
    parsimony_regularized = min(
        fits,
        key=lambda fit: (
            fit.parsimony_score,
            fit.holdout_rmse,
            fit.candidate.complexity,
            fit.candidate.powers,
        ),
    )
    return {
        "error_only": error_only,
        "parsimony_regularized": parsimony_regularized,
    }


def run_stress_suite(
    *,
    seed_count: int = 256,
    noise_levels: Sequence[float] = (0.01, 0.05, 0.10, 0.20),
    parsimony_penalty_strength: float = 4.0,
) -> dict[str, object]:
    """Aggregate repeated-seed structure recovery and false-discovery metrics."""
    if seed_count <= 0:
        raise ValueError("seed_count must be positive")
    if not noise_levels:
        raise ValueError("noise_levels are required")

    truth = (2,)
    rows: list[dict[str, object]] = []
    for noise_sigma in noise_levels:
        by_selector: dict[str, list[CandidateFit]] = {
            "error_only": [],
            "parsimony_regularized": [],
        }
        for seed in range(seed_count):
            result = run_noise_trial(
                seed,
                float(noise_sigma),
                parsimony_penalty_strength=parsimony_penalty_strength,
            )
            for selector, fit in result.items():
                by_selector[selector].append(fit)

        row: dict[str, object] = {"noise_sigma": float(noise_sigma)}
        for selector, fits in by_selector.items():
            recovery_rate = sum(fit.candidate.powers == truth for fit in fits) / seed_count
            row[selector] = {
                "exact_structure_recovery_rate": recovery_rate,
                "false_discovery_rate": 1.0 - recovery_rate,
                "median_holdout_rmse": statistics.median(fit.holdout_rmse for fit in fits),
                "median_extrapolation_rmse": statistics.median(
                    fit.extrapolation_rmse for fit in fits
                ),
            }
        rows.append(row)

    return {
        "program": "INV-035/EQN-002/RG-031",
        "evidence_level": "MODEL_ONLY_SYNTHETIC",
        "new_physical_law_claim": False,
        "truth": "y = 1.5*z^2",
        "dimension_contract": "z is dimensionless; all candidate polynomial terms are unit-consistent",
        "seed_count": seed_count,
        "parsimony_penalty_strength": parsimony_penalty_strength,
        "noise_levels": rows,
    }
