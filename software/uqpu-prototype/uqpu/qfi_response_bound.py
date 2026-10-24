"""Audit a measured first-order observable response against a QFI bound.

The helper checks |d <O>/ds|^2 <= F_Q(s) Var(O) for one observable and one
consistently parameterized physical direction. It does not compute QFI,
establish the assumptions of a paper's full retrained-loss theorem, or
establish quantum advantage or a new physical law.
"""
from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class QFIResponseAudit:
    """Scalar audit record for one observable/direction/sample.

    directional_qfi is v.T @ F_Q @ v for the exact same direction v
    used to calculate observed_slope. observable_variance and the
    slope must use the same state, observable, parameterization and sample.
    """

    directional_qfi: float
    observable_variance: float
    observed_slope: float
    relative_tolerance: float = 1e-10

    def validate(self) -> None:
        """Raise ValueError when inputs are invalid or the bound is violated."""
        try:
            qfi = float(self.directional_qfi)
            variance = float(self.observable_variance)
            slope = float(self.observed_slope)
            tolerance = float(self.relative_tolerance)
        except (TypeError, ValueError, OverflowError) as exc:
            raise ValueError("QFI response inputs must be numeric") from exc

        values = {
            "directional_qfi": qfi,
            "observable_variance": variance,
            "observed_slope": slope,
            "relative_tolerance": tolerance,
        }
        for name, value in values.items():
            if not math.isfinite(value):
                raise ValueError(f"{name} must be finite")
        if qfi < 0.0:
            raise ValueError("directional_qfi must be >= 0")
        if variance < 0.0:
            raise ValueError("observable_variance must be >= 0")
        if tolerance < 0.0:
            raise ValueError("relative_tolerance must be >= 0")

        bound = qfi * variance
        observed = slope * slope
        scale = max(bound, observed, 1e-300)
        if observed > bound + tolerance * scale:
            raise ValueError(
                "QFI response bound violated: observed_slope^2 exceeds "
                "directional_qfi * observable_variance"
            )

    @property
    def bound_squared(self) -> float:
        """Return the squared response envelope F_Q(v) * Var(O)."""
        return float(self.directional_qfi) * float(self.observable_variance)

    @property
    def observed_slope_squared(self) -> float:
        """Return the squared observed first-order response."""
        slope = float(self.observed_slope)
        return slope * slope

    @property
    def response_utilization(self) -> float:
        """Return |slope| / sqrt(bound); 0 or infinity for a zero bound."""
        bound = self.bound_squared
        if bound == 0.0:
            return 0.0 if self.observed_slope == 0.0 else math.inf
        return abs(float(self.observed_slope)) / math.sqrt(bound)
