"""Tiny exact reference for two-dimensional Hermitian Hamiltonians.

This is a deterministic analytic reference fixture for small-instance validation.
It is not a sparse-oracle implementation, a quantum algorithm, a gate-count model,
or evidence of a physical or economic advantage.
"""
from __future__ import annotations

import math
from collections.abc import Sequence


def _finite_real(name: str, value: object) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a finite real number")
    try:
        result = float(value)
    except (OverflowError, TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be a finite real number") from exc
    if not math.isfinite(result):
        raise ValueError(f"{name} must be a finite real number")
    return result


def _finite_complex(name: str, value: object) -> complex:
    if isinstance(value, bool) or not isinstance(value, (int, float, complex)):
        raise ValueError(f"{name} must be a finite complex number")
    try:
        result = complex(value)
    except (OverflowError, TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be a finite complex number") from exc
    if not math.isfinite(result.real) or not math.isfinite(result.imag):
        raise ValueError(f"{name} must be a finite complex number")
    return result


def hamiltonian_2x2_contract(
    h00: float, h11: float, h01: complex
) -> dict[str, object]:
    """Return exact 2x2 Hermitian sparsity and row/column norm metadata.

    H is parameterized as [[h00, h01], [conj(h01), h11]], so Hermiticity
    is structural. Norms are Euclidean row/column norms, not operator norms.
    The output remains MODEL_ONLY metadata.
    """
    a = _finite_real("h00", h00)
    d = _finite_real("h11", h11)
    b = _finite_complex("h01", h01)
    row_norms = (math.hypot(a, abs(b)), math.hypot(d, abs(b)))
    row_sparsities = (
        int(a != 0.0) + int(b != 0j),
        int(d != 0.0) + int(b != 0j),
    )
    return {
        "dimension": 2,
        "max_row_sparsity": max(row_sparsities),
        "row_euclidean_norms": row_norms,
        "column_euclidean_norms": row_norms,
        "eta": max(row_norms),
        "evidence_level": "MODEL_ONLY",
        "interpretation": (
            "analytic 2x2 reference metadata only; no sparse oracle or query "
            "complexity is instantiated"
        ),
    }


def evolve_2x2_hermitian(
    h00: float, h11: float, h01: complex, time: float
) -> tuple[tuple[complex, complex], tuple[complex, complex]]:
    """Compute exp(-i H t) analytically for H=[[h00,h01],[conj(h01),h11]].

    The closed form uses H = mu*I + K, K^2 = delta^2*I. The delta=0
    branch uses the continuous limit sin(delta*t)/delta -> t.
    """
    a = _finite_real("h00", h00)
    d = _finite_real("h11", h11)
    b = _finite_complex("h01", h01)
    t = _finite_real("time", time)

    mu = (a + d) / 2.0
    z = (a - d) / 2.0
    delta = math.sqrt(z * z + abs(b) ** 2)
    cosine = math.cos(delta * t)
    sine_over_delta = t if delta == 0.0 else math.sin(delta * t) / delta
    phase = complex(math.cos(mu * t), -math.sin(mu * t))

    u00 = phase * complex(cosine, -sine_over_delta * z)
    u01 = phase * (-1j * sine_over_delta * b)
    u10 = phase * (-1j * sine_over_delta * b.conjugate())
    u11 = phase * complex(cosine, sine_over_delta * z)
    return ((u00, u01), (u10, u11))


def max_unitarity_residual(
    unitary: Sequence[Sequence[complex]],
) -> float:
    """Return max_ij |(U†U - I)_ij| for a finite 2x2 matrix."""
    try:
        rows = tuple(tuple(row) for row in unitary)
    except TypeError as exc:
        raise ValueError("unitary must be a 2x2 sequence") from exc
    if len(rows) != 2 or any(len(row) != 2 for row in rows):
        raise ValueError("unitary must be a 2x2 sequence")
    matrix = tuple(
        tuple(_finite_complex("unitary entry", value) for value in row)
        for row in rows
    )
    worst = 0.0
    for i in range(2):
        for j in range(2):
            inner = sum(
                matrix[k][i].conjugate() * matrix[k][j]
                for k in range(2)
            )
            residual = inner - (1.0 if i == j else 0.0)
            worst = max(worst, abs(residual))
    return worst
