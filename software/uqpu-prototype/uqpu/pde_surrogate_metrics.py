"""Conservation/bound metrics for supplied PDE-surrogate trajectories.

These checks score supplied discrete fields only. They do not establish that a
quantity is physically conserved for a given PDE, authenticate data, validate a
solver, or establish a physical law or technology advantage.
"""
from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
import math


@dataclass(frozen=True)
class ConservativeTrajectoryMetrics:
    """Metrics for one trajectory against a declared discrete invariant."""

    time_step_count: int
    cell_count: int
    initial_conserved_total: float
    predicted_conserved_totals: tuple[float, ...]
    max_absolute_conservation_drift: float
    mean_absolute_conservation_drift: float
    max_normalized_conservation_drift: float
    mean_normalized_conservation_drift: float
    normalized_conservation_tolerance: float
    conservation_pass: bool
    bounds_applicable: bool
    bound_violation_count: int
    bound_violation_rate: float
    max_bound_violation: float
    bound_tolerance: float
    bounds_pass: bool | None


def _finite_sequence(name: str, values: Sequence[float]) -> tuple[float, ...]:
    if isinstance(values, (str, bytes)) or not isinstance(values, Sequence):
        raise ValueError(f"{name} must be a nonempty numeric sequence")
    if not values:
        raise ValueError(f"{name} must be a nonempty numeric sequence")
    result: list[float] = []
    for index, value in enumerate(values):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"{name}[{index}] must be a finite number")
        try:
            number = float(value)
        except (OverflowError, ValueError) as exc:
            raise ValueError(f"{name}[{index}] must be a finite number") from exc
        if not math.isfinite(number):
            raise ValueError(f"{name}[{index}] must be a finite number")
        result.append(number)
    return tuple(result)


def _nonnegative_scalar(name: str, value: float) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be finite and >= 0")
    try:
        number = float(value)
    except (OverflowError, ValueError) as exc:
        raise ValueError(f"{name} must be finite and >= 0") from exc
    if not math.isfinite(number) or number < 0:
        raise ValueError(f"{name} must be finite and >= 0")
    return number


def _positive_scalar(name: str, value: float) -> float:
    number = _nonnegative_scalar(name, value)
    if number <= 0:
        raise ValueError(f"{name} must be finite and > 0")
    return number


def _finite_sum(name: str, values: Sequence[float]) -> float:
    try:
        total = math.fsum(values)
    except OverflowError as exc:
        raise ValueError(f"{name} must be finite") from exc
    if not math.isfinite(total):
        raise ValueError(f"{name} must be finite")
    return total


def score_conservative_bounded_trajectory(
    initial_field: Sequence[float],
    predicted_fields: Sequence[Sequence[float]],
    *,
    cell_weights: Sequence[float] | None = None,
    lower_bound: float | None = None,
    upper_bound: float | None = None,
    conservation_scale: float | None = None,
    normalized_conservation_tolerance: float = 1e-6,
    bound_tolerance: float = 0.0,
) -> ConservativeTrajectoryMetrics:
    """Score a trajectory against a caller-declared discrete conservation law.

    Cell weights are positive cell measures (for example, cell volumes); if
    omitted, each cell has unit weight. Conservation scale has the same units as
    the conserved total and makes normalized drift dimensionless. When omitted,
    it is derived only from the initial field as sum(abs(value*weight)); a
    zero-magnitude initial field therefore requires an explicit positive scale.

    Bounds are optional and must be physically justified by the caller. A value
    is counted as violating a bound only when its raw violation exceeds
    bound_tolerance. This helper does not infer whether the PDE truly conserves
    the supplied quantity or whether a bound is appropriate.
    """
    initial = _finite_sequence("initial_field", initial_field)
    if isinstance(predicted_fields, (str, bytes)) or not isinstance(predicted_fields, Sequence):
        raise ValueError("predicted_fields must be a nonempty sequence of fields")
    if not predicted_fields:
        raise ValueError("predicted_fields must be a nonempty sequence of fields")

    frames = tuple(
        _finite_sequence(f"predicted_fields[{index}]", frame)
        for index, frame in enumerate(predicted_fields)
    )
    cell_count = len(initial)
    for index, frame in enumerate(frames):
        if len(frame) != cell_count:
            raise ValueError(f"predicted_fields[{index}] must match initial_field length")

    if cell_weights is None:
        weights = (1.0,) * cell_count
    else:
        weights = _finite_sequence("cell_weights", cell_weights)
        if len(weights) != cell_count:
            raise ValueError("cell_weights must match initial_field length")
        if any(weight <= 0 for weight in weights):
            raise ValueError("cell_weights must be > 0")

    lower = None if lower_bound is None else _finite_bound("lower_bound", lower_bound)
    upper = None if upper_bound is None else _finite_bound("upper_bound", upper_bound)
    if lower is not None and upper is not None and lower > upper:
        raise ValueError("lower_bound must be <= upper_bound")
    bound_tol = _nonnegative_scalar("bound_tolerance", bound_tolerance)
    conservation_tol = _nonnegative_scalar(
        "normalized_conservation_tolerance", normalized_conservation_tolerance
    )

    initial_products = tuple(value * weight for value, weight in zip(initial, weights))
    if any(not math.isfinite(value) for value in initial_products):
        raise ValueError("weighted initial field values must be finite")
    initial_total = _finite_sum("initial conserved total", initial_products)

    if conservation_scale is None:
        scale = _finite_sum(
            "initial conservation scale", tuple(abs(value) for value in initial_products)
        )
        if scale <= 0:
            raise ValueError(
                "conservation_scale must be supplied and > 0 for a zero-magnitude initial field"
            )
    else:
        scale = _positive_scalar("conservation_scale", conservation_scale)

    totals: list[float] = []
    absolute_drifts: list[float] = []
    normalized_drifts: list[float] = []
    for index, frame in enumerate(frames):
        products = tuple(value * weight for value, weight in zip(frame, weights))
        if any(not math.isfinite(value) for value in products):
            raise ValueError(f"weighted predicted field values at time index {index} must be finite")
        total = _finite_sum(f"predicted conserved total at time index {index}", products)
        drift = abs(total - initial_total)
        normalized = drift / scale
        if not math.isfinite(drift) or not math.isfinite(normalized):
            raise ValueError(f"conservation drift at time index {index} must be finite")
        totals.append(total)
        absolute_drifts.append(drift)
        normalized_drifts.append(normalized)

    violating_count = 0
    max_violation = 0.0
    for frame in frames:
        for value in frame:
            violation = 0.0
            if lower is not None and value < lower:
                violation = max(violation, lower - value)
            if upper is not None and value > upper:
                violation = max(violation, value - upper)
            if not math.isfinite(violation):
                raise ValueError("bound violation must be finite")
            max_violation = max(max_violation, violation)
            if violation > bound_tol:
                violating_count += 1

    bounds_applicable = lower is not None or upper is not None
    total_values = len(frames) * cell_count
    return ConservativeTrajectoryMetrics(
        time_step_count=len(frames),
        cell_count=cell_count,
        initial_conserved_total=initial_total,
        predicted_conserved_totals=tuple(totals),
        max_absolute_conservation_drift=max(absolute_drifts),
        mean_absolute_conservation_drift=_finite_sum("mean absolute drift", absolute_drifts) / len(absolute_drifts),
        max_normalized_conservation_drift=max(normalized_drifts),
        mean_normalized_conservation_drift=_finite_sum("mean normalized drift", normalized_drifts) / len(normalized_drifts),
        normalized_conservation_tolerance=conservation_tol,
        conservation_pass=max(normalized_drifts) <= conservation_tol,
        bounds_applicable=bounds_applicable,
        bound_violation_count=violating_count,
        bound_violation_rate=violating_count / total_values,
        max_bound_violation=max_violation,
        bound_tolerance=bound_tol,
        bounds_pass=(violating_count == 0) if bounds_applicable else None,
    )


def _finite_bound(name: str, value: float) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be finite")
    try:
        number = float(value)
    except (OverflowError, ValueError) as exc:
        raise ValueError(f"{name} must be finite") from exc
    if not math.isfinite(number):
        raise ValueError(f"{name} must be finite")
    return number
