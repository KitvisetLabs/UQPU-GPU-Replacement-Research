from __future__ import annotations

from dataclasses import dataclass
import math

from .optimization_baseline import QuboInstance


@dataclass(frozen=True)
class QuboPayload:
    format: str
    payload: dict
    notes: str = ""


def _validate_finite_coefficients(instance: QuboInstance) -> None:
    """Reject non-finite coefficients before producing a provider payload."""
    values = [("constant", instance.constant)]
    values.extend((f"linear[{i}]", weight) for i, weight in instance.linear.items())
    values.extend((f"quadratic[{i},{j}]", weight) for (i, j), weight in instance.quadratic.items())
    for name, value in values:
        try:
            numeric = float(value)
        except (TypeError, ValueError, OverflowError) as exc:
            raise ValueError(f"{name} must be a finite numeric coefficient") from exc
        if not math.isfinite(numeric):
            raise ValueError(f"{name} must be finite")


def to_dwave_qubo(instance: QuboInstance) -> QuboPayload:
    _validate_finite_coefficients(instance)
    q = {}
    for i, weight in instance.linear.items():
        q[(i, i)] = float(weight)
    for (i, j), weight in instance.quadratic.items():
        key = (min(i, j), max(i, j))
        q[key] = q.get(key, 0.0) + float(weight)
    return QuboPayload(
        format="dwave-qubo",
        payload={"Q": q, "offset": float(instance.constant)},
        notes=(
            "Compatible with UQPU DWaveLeapAdapter QUBO payload convention; "
            "offset is metadata unless downstream sampler supports it."
        ),
    )


def to_portable_qubo(instance: QuboInstance) -> QuboPayload:
    _validate_finite_coefficients(instance)
    return QuboPayload(
        format="uqpu-qubo-v1",
        payload={
            "linear": {str(i): float(weight) for i, weight in instance.linear.items()},
            "quadratic": [
                [int(i), int(j), float(weight)]
                for (i, j), weight in sorted(instance.quadratic.items())
            ],
            "constant": float(instance.constant),
        },
        notes="Provider-neutral QUBO representation for routing/lowering.",
    )
