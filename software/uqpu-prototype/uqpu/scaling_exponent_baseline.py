"""Classical log-linear baseline for known positive power-law fixtures.

This is a synthetic/reference baseline, not the MSN-PINN method and not a
physical-law detector. Its identifiability flag is conditional on the
predeclared pure-power-law model y = amplitude * x**exponent and positive data.
"""
from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Iterable
import math


def _positive_finite_vector(name: str, values: Iterable[object]) -> tuple[float, ...]:
    if isinstance(values, (str, bytes)):
        raise ValueError(f"{name} must be a non-string iterable")
    try:
        raw = tuple(values)
    except TypeError as exc:
        raise ValueError(f"{name} must be iterable") from exc
    if len(raw) < 3:
        raise ValueError(f"{name} must contain at least three observations")
    converted = []
    for value in raw:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"{name} values must be numeric and not boolean")
        number = float(value)
        if not math.isfinite(number) or number <= 0.0:
            raise ValueError(f"{name} values must be finite and strictly positive")
        converted.append(number)
    return tuple(converted)


@dataclass(frozen=True)
class PowerLawFit:
    amplitude: float
    exponent: float
    r_squared: float
    n_observations: int
    log_x_span: float

    def predict(self, x: float) -> float:
        if isinstance(x, bool) or not isinstance(x, (int, float)):
            raise ValueError("prediction x must be numeric and not boolean")
        x = float(x)
        if not math.isfinite(x) or x <= 0.0:
            raise ValueError("prediction x must be finite and strictly positive")
        try:
            value = self.amplitude * math.exp(self.exponent * math.log(x))
        except OverflowError as exc:
            raise ValueError("power-law prediction overflowed") from exc
        if not math.isfinite(value):
            raise ValueError("power-law prediction must be finite")
        return value


def fit_power_law(
    x_values: Iterable[object],
    y_values: Iterable[object],
    *,
    min_log_x_span: float = 1e-6,
) -> PowerLawFit:
    """Fit log(y) = log(amplitude) + exponent*log(x) by ordinary least squares.

    min_log_x_span is a predeclared design threshold. Passing this check means
    only that the slope is numerically estimable for this restricted model;
    it does not establish global identifiability among alternative laws.
    """
    xs = _positive_finite_vector("x_values", x_values)
    ys = _positive_finite_vector("y_values", y_values)
    if len(xs) != len(ys):
        raise ValueError("x_values and y_values must have equal lengths")
    if isinstance(min_log_x_span, bool) or not isinstance(min_log_x_span, (int, float)):
        raise ValueError("min_log_x_span must be numeric and not boolean")
    min_log_x_span = float(min_log_x_span)
    if not math.isfinite(min_log_x_span) or min_log_x_span <= 0.0:
        raise ValueError("min_log_x_span must be finite and strictly positive")

    lx = tuple(math.log(x) for x in xs)
    ly = tuple(math.log(y) for y in ys)
    log_x_span = max(lx) - min(lx)
    if log_x_span <= min_log_x_span:
        raise ValueError("power-law exponent is not identifiable: insufficient log-x span")

    mean_x = math.fsum(lx) / len(lx)
    mean_y = math.fsum(ly) / len(ly)
    sxx = math.fsum((value - mean_x) ** 2 for value in lx)
    if sxx <= 0.0 or not math.isfinite(sxx):
        raise ValueError("power-law exponent is not identifiable: singular design")
    exponent = math.fsum((x - mean_x) * (y - mean_y) for x, y in zip(lx, ly)) / sxx
    intercept = mean_y - exponent * mean_x
    try:
        amplitude = math.exp(intercept)
    except OverflowError as exc:
        raise ValueError("fitted amplitude overflowed") from exc
    if not all(math.isfinite(v) for v in (amplitude, exponent)) or amplitude <= 0.0:
        raise ValueError("fitted power-law parameters must be finite and amplitude positive")

    residual_sum = math.fsum((y - (intercept + exponent * x)) ** 2 for x, y in zip(lx, ly))
    total_sum = math.fsum((y - mean_y) ** 2 for y in ly)
    r_squared = 1.0 if total_sum == 0.0 and residual_sum == 0.0 else (
        0.0 if total_sum == 0.0 else 1.0 - residual_sum / total_sum
    )
    if not math.isfinite(r_squared):
        raise ValueError("fit score must be finite")
    return PowerLawFit(
        amplitude=amplitude,
        exponent=exponent,
        r_squared=r_squared,
        n_observations=len(xs),
        log_x_span=log_x_span,
    )
