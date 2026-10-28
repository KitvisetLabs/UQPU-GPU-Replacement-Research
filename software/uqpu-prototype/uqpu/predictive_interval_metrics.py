"""Scoring helpers for held-out predictive intervals.

These metrics assess interval coverage and sharpness on supplied observations.
They do not establish model calibration, equation validity, or physical truth.
"""
from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
import math


@dataclass(frozen=True)
class PredictiveIntervalMetrics:
    """Summary metrics for one nominal level on a held-out sample."""

    sample_count: int
    nominal_coverage: float
    empirical_coverage: float
    coverage_error: float
    mean_width: float
    mean_interval_score: float


def _finite_sequence(name: str, values: Sequence[float]) -> tuple[float, ...]:
    if isinstance(values, (str, bytes)) or not isinstance(values, Sequence):
        raise ValueError(f"{name} must be a nonempty numeric sequence")
    if len(values) == 0:
        raise ValueError(f"{name} must be a nonempty numeric sequence")

    result: list[float] = []
    for index, value in enumerate(values):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"{name}[{index}] must be a finite number")
        number = float(value)
        if not math.isfinite(number):
            raise ValueError(f"{name}[{index}] must be a finite number")
        result.append(number)
    return tuple(result)


def score_prediction_intervals(
    observations: Sequence[float],
    lower_bounds: Sequence[float],
    upper_bounds: Sequence[float],
    nominal_coverage: float,
) -> PredictiveIntervalMetrics:
    """Score central prediction intervals at one preregistered coverage level.

    The central interval score is
        width + (2 / alpha) * distance_outside_interval,
    where alpha = 1 - nominal_coverage. Lower scores are better at a fixed
    nominal level. Coverage is inclusive at both endpoints.

    A single sample's empirical coverage is not a calibration proof. Evaluate
    preregistered nominal levels on held-out samples and report coverage jointly
    with width and this proper interval score.
    """
    actual = _finite_sequence("observations", observations)
    lower = _finite_sequence("lower_bounds", lower_bounds)
    upper = _finite_sequence("upper_bounds", upper_bounds)

    if len(actual) != len(lower) or len(actual) != len(upper):
        raise ValueError(
            "observations and interval-bound sequences must have equal lengths"
        )
    if (
        isinstance(nominal_coverage, bool)
        or not isinstance(nominal_coverage, (int, float))
    ):
        raise ValueError(
            "nominal_coverage must be finite and strictly between 0 and 1"
        )
    nominal = float(nominal_coverage)
    if not math.isfinite(nominal) or not 0.0 < nominal < 1.0:
        raise ValueError(
            "nominal_coverage must be finite and strictly between 0 and 1"
        )

    alpha = 1.0 - nominal
    hits = 0
    widths: list[float] = []
    scores: list[float] = []

    for index, (value, lo, hi) in enumerate(zip(actual, lower, upper)):
        if lo > hi:
            raise ValueError(
                f"lower_bounds[{index}] must be <= upper_bounds[{index}]"
            )
        width = hi - lo
        if not math.isfinite(width):
            raise ValueError(f"interval width at index {index} must be finite")

        distance = lo - value if value < lo else value - hi if value > hi else 0.0
        score = width + (2.0 / alpha) * distance
        if not math.isfinite(score):
            raise ValueError(f"interval score at index {index} must be finite")

        widths.append(width)
        scores.append(score)
        if lo <= value <= hi:
            hits += 1

    try:
        mean_width = math.fsum(widths) / len(actual)
        mean_score = math.fsum(scores) / len(actual)
    except OverflowError as exc:
        raise ValueError("aggregate interval metrics must be finite") from exc
    if not math.isfinite(mean_width) or not math.isfinite(mean_score):
        raise ValueError("aggregate interval metrics must be finite")

    empirical = hits / len(actual)
    return PredictiveIntervalMetrics(
        sample_count=len(actual),
        nominal_coverage=nominal,
        empirical_coverage=empirical,
        coverage_error=empirical - nominal,
        mean_width=mean_width,
        mean_interval_score=mean_score,
    )
