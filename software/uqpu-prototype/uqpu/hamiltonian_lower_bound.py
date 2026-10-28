"""Scoped coefficient-tail trade-off proxy for Hamiltonian-simulation lower bounds.

The cited theorem is asymptotic and applies only to specified hard-instance and
access models. This module computes the displayed coefficient-profile proxy;
it is not a finite-instance gate lower bound, physical-time bound, energy model,
or economic result.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from collections.abc import Sequence


@dataclass(frozen=True)
class CoefficientTailPoint:
    """One candidate cut K in the asymptotic trade-off expression."""

    cut: int
    tail_weight: float
    proxy_value: float


@dataclass(frozen=True)
class CoefficientTailTradeoff:
    """Auditable coefficient-tail trade-off envelope, never a measured bound."""

    coefficient_count: int
    simulation_time: float
    trace_distance_error: float
    candidates: tuple[CoefficientTailPoint, ...]
    minimizing_cut: int
    minimum_proxy_value: float
    evidence_label: str = "ASYMPTOTIC_TRADEOFF_PROXY_ONLY"


def coefficient_tail_tradeoff_proxy(
    coefficients: Sequence[float],
    simulation_time: float,
    trace_distance_error: float,
) -> CoefficientTailTradeoff:
    """Compute min_K [K*t + t^2 * lambda_K^2 / epsilon], K=0..L.

    Preconditions follow the normalized coefficient convention used in the
    scoped preprint: coefficients are positive, non-increasing and sum to one.
    lambda_K is the sum of coefficients with index greater than K. K=0 retains
    the full tail; K=L has zero tail. The result is only the expression's
    numerical proxy under the supplied inputs, not the asymptotic Omega bound's
    hidden constants or a claim that a workload satisfies the theorem.
    """
    if isinstance(coefficients, (str, bytes)):
        raise ValueError("coefficients must be a nonempty numeric sequence")
    try:
        raw = tuple(coefficients)
        if any(isinstance(value, bool) for value in raw):
            raise ValueError("coefficients must be numeric, not booleans")
        values = tuple(float(value) for value in raw)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError("coefficients must be a nonempty numeric sequence") from exc

    if not values:
        raise ValueError("coefficients must not be empty")
    if any(not math.isfinite(value) or value <= 0.0 for value in values):
        raise ValueError("coefficients must be finite and > 0")
    if any(values[index] < values[index + 1] for index in range(len(values) - 1)):
        raise ValueError("coefficients must be sorted in non-increasing order")
    if not math.isclose(math.fsum(values), 1.0, rel_tol=1e-9, abs_tol=1e-12):
        raise ValueError("coefficients must be normalized to sum to 1")

    time_value = float(simulation_time)
    if not math.isfinite(time_value) or time_value <= 0.0:
        raise ValueError("simulation_time must be finite and > 0")
    epsilon = float(trace_distance_error)
    if not math.isfinite(epsilon) or not 0.0 < epsilon < 1.0:
        raise ValueError("trace_distance_error must be finite and in (0, 1)")

    count = len(values)
    tails = [0.0] * (count + 1)
    for index in range(count - 1, -1, -1):
        tails[index] = math.fsum((values[index], tails[index + 1]))

    candidates = tuple(
        CoefficientTailPoint(
            cut=cut,
            tail_weight=tails[cut],
            proxy_value=(cut * time_value)
            + (time_value * time_value * tails[cut] * tails[cut] / epsilon),
        )
        for cut in range(count + 1)
    )
    best = min(candidates, key=lambda point: (point.proxy_value, point.cut))
    return CoefficientTailTradeoff(
        coefficient_count=count,
        simulation_time=time_value,
        trace_distance_error=epsilon,
        candidates=candidates,
        minimizing_cut=best.cut,
        minimum_proxy_value=best.proxy_value,
    )
