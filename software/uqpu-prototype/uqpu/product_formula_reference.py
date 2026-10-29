"""First-order Lie-Trotter baseline for a two-term 2x2 Hamiltonian.

The model is H = alpha*Z + beta*X. This dependency-free helper is a
MODEL_ONLY simulator/reference comparator, not a sparse-oracle implementation,
a hardware gate estimate, or evidence of quantum advantage.
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


def _matmul2(left, right):
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def _matrix2(name: str, value: object):
    if isinstance(value, (str, bytes)):
        raise ValueError(f"{name} must be a 2x2 matrix")
    try:
        rows = tuple(tuple(row) for row in value)  # type: ignore[arg-type]
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be a 2x2 matrix") from exc
    if len(rows) != 2 or any(len(row) != 2 for row in rows):
        raise ValueError(f"{name} must be a 2x2 matrix")
    result = []
    for row in rows:
        checked = []
        for item in row:
            if isinstance(item, bool) or not isinstance(item, (int, float, complex)):
                raise ValueError(f"{name} entries must be finite complex numbers")
            try:
                entry = complex(item)
            except (OverflowError, TypeError, ValueError) as exc:
                raise ValueError(f"{name} entries must be finite complex numbers") from exc
            if not math.isfinite(entry.real) or not math.isfinite(entry.imag):
                raise ValueError(f"{name} entries must be finite complex numbers")
            checked.append(entry)
        result.append(tuple(checked))
    return tuple(result)


def evolve_xz_lie_trotter(
    alpha: float, beta: float, time: float, steps: int
) -> tuple[tuple[complex, complex], tuple[complex, complex]]:
    """Return (exp(-i alpha Z dt) exp(-i beta X dt))**steps.

    The exact comparison target is evolve_2x2_hermitian(alpha, -alpha, beta,
    time), for H=[[alpha,beta],[beta,-alpha]]. Steps must be a positive integer.
    The method is first-order Lie-Trotter splitting; the returned matrix is a
    mathematical simulation result only, with no gate/resource accounting.
    """
    a = _finite_real("alpha", alpha)
    b = _finite_real("beta", beta)
    t = _finite_real("time", time)
    if isinstance(steps, bool) or not isinstance(steps, int) or steps < 1:
        raise ValueError("steps must be a positive integer")
    dt = t / steps
    x_angle = b * dt
    z_angle = a * dt
    if not math.isfinite(dt) or not math.isfinite(x_angle) or not math.isfinite(z_angle):
        raise ValueError("time-step angles must remain finite")

    cx, sx = math.cos(x_angle), math.sin(x_angle)
    cz, sz = math.cos(z_angle), math.sin(z_angle)
    u_x = ((complex(cx, 0.0), complex(0.0, -sx)),
           (complex(0.0, -sx), complex(cx, 0.0)))
    u_z = ((complex(cz, -sz), 0j), (0j, complex(cz, sz)))
    step = _matmul2(u_z, u_x)
    result = ((1 + 0j, 0j), (0j, 1 + 0j))
    for _ in range(steps):
        result = _matmul2(step, result)
    return result


def frobenius_distance_2x2(left: object, right: object) -> float:
    """Return the Frobenius norm of the difference between two finite 2x2 matrices."""
    a = _matrix2("left", left)
    b = _matrix2("right", right)
    return math.sqrt(math.fsum(abs(a[i][j] - b[i][j]) ** 2
                               for i in range(2) for j in range(2)))
