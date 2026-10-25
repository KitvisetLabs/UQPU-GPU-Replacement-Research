"""Numerical prototype of the published M-QSP constructivity decision recursion.

Reference: Ito, Mori, Sakamoto & Fujii, Quantum 10, 2102 (2026),
Algorithm 1, DOI 10.22331/q-2026-05-12-2102.

This implementation uses floating-point complex coefficients and a tolerance.
It is not an exact-arithmetic or formally verified reproduction of the theorem.
A positive result is a candidate factorization that must be independently
reconstructed; a negative result near tolerance boundaries is not a proof of
infeasibility. No hardware, application, cost, or quantum-advantage claim is
made.
"""
from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Mapping
import cmath
import math
from typing import TypeAlias

Exponent: TypeAlias = tuple[int, ...]
LaurentPolynomial: TypeAlias = Mapping[Exponent, complex]


@dataclass(frozen=True)
class MQSPDecision:
    """Numerical feasibility candidate and one constructive witness."""

    candidate_feasible: bool
    signal_indices: tuple[int, ...]
    phase_angles: tuple[float, ...]
    reason: str
    tolerance: float


def _clean(poly: dict[Exponent, complex], tolerance: float) -> dict[Exponent, complex]:
    return {exp: value for exp, value in poly.items() if abs(value) > tolerance}


def _normalize(
    poly: LaurentPolynomial, variable_count: int, tolerance: float
) -> dict[Exponent, complex]:
    if not isinstance(poly, Mapping):
        raise ValueError("polynomial must be a mapping from exponent tuples to coefficients")
    out: dict[Exponent, complex] = {}
    for exponent, raw_value in poly.items():
        if (
            not isinstance(exponent, tuple)
            or len(exponent) != variable_count
            or any(not isinstance(k, int) or isinstance(k, bool) for k in exponent)
        ):
            raise ValueError("each exponent must be an integer tuple of variable_count length")
        try:
            value = complex(raw_value)
        except (TypeError, ValueError) as exc:
            raise ValueError("polynomial coefficients must be finite complex numbers") from exc
        if not math.isfinite(value.real) or not math.isfinite(value.imag):
            raise ValueError("polynomial coefficients must be finite complex numbers")
        out[exponent] = out.get(exponent, 0j) + value
    return _clean(out, tolerance)


def _degree(poly: dict[Exponent, complex], axis: int) -> int:
    return max((abs(exponent[axis]) for exponent in poly), default=0)


def _positive_slice(
    poly: dict[Exponent, complex], axis: int, degree: int
) -> dict[tuple[int, ...], complex]:
    return {
        exponent[:axis] + exponent[axis + 1:]: value
        for exponent, value in poly.items()
        if exponent[axis] == degree
    }


def _phase_if_proportional_unit(
    p_slice: dict[tuple[int, ...], complex],
    q_slice: dict[tuple[int, ...], complex],
    tolerance: float,
) -> float | None:
    if not p_slice or not q_slice:
        return None
    reference = next(iter(q_slice))
    ratio = p_slice.get(reference, 0j) / q_slice[reference]
    if abs(abs(ratio) - 1.0) > tolerance:
        return None
    for key in set(p_slice) | set(q_slice):
        p_value = p_slice.get(key, 0j)
        q_value = ratio * q_slice.get(key, 0j)
        if abs(p_value - q_value) > tolerance * max(1.0, abs(p_value), abs(q_value)):
            return None
    return 0.5 * cmath.phase(ratio)


def _shift(
    poly: dict[Exponent, complex], axis: int, amount: int
) -> dict[Exponent, complex]:
    shifted: dict[Exponent, complex] = {}
    for exponent, value in poly.items():
        key = exponent[:axis] + (exponent[axis] + amount,) + exponent[axis + 1:]
        shifted[key] = shifted.get(key, 0j) + value
    return shifted


def _combine(
    terms: tuple[tuple[dict[Exponent, complex], complex], ...],
    tolerance: float,
) -> dict[Exponent, complex]:
    result: dict[Exponent, complex] = {}
    for poly, scale in terms:
        for exponent, value in poly.items():
            result[exponent] = result.get(exponent, 0j) + scale * value
    return _clean(result, tolerance)


def _remove_last_signal(
    p: dict[Exponent, complex],
    q: dict[Exponent, complex],
    axis: int,
    phase: float,
    tolerance: float,
) -> tuple[dict[Exponent, complex], dict[Exponent, complex]]:
    p_plus, p_minus = _shift(p, axis, 1), _shift(p, axis, -1)
    q_plus, q_minus = _shift(q, axis, 1), _shift(q, axis, -1)
    half = 0.5
    p_reduced = _combine(
        (
            (p_plus, half * cmath.exp(-1j * phase)),
            (p_minus, half * cmath.exp(-1j * phase)),
            (q_plus, -half * cmath.exp(1j * phase)),
            (q_minus, half * cmath.exp(1j * phase)),
        ),
        tolerance,
    )
    q_reduced = _combine(
        (
            (q_plus, half * cmath.exp(1j * phase)),
            (q_minus, half * cmath.exp(1j * phase)),
            (p_plus, -half * cmath.exp(-1j * phase)),
            (p_minus, half * cmath.exp(-1j * phase)),
        ),
        tolerance,
    )
    return p_reduced, q_reduced


def _base_phase(
    p: dict[Exponent, complex],
    q: dict[Exponent, complex],
    variable_count: int,
    tolerance: float,
) -> float | None:
    zero = (0,) * variable_count
    if q or len(p) != 1 or zero not in p:
        return None
    value = p[zero]
    if abs(abs(value) - 1.0) > tolerance:
        return None
    return cmath.phase(value)


def mqsp_constructivity_decision(
    p: LaurentPolynomial,
    q: LaurentPolynomial,
    variable_count: int,
    n_steps: int,
    tolerance: float = 1e-9,
) -> MQSPDecision:
    """Run a floating-point transcription of M-QSP-CDA Algorithm 1.

    signal_indices are zero-based variable indices. phase_angles has one more
    element than the witness signal sequence when feasible. Inputs use exponent
    tuples such as (1, -2) for a_1 * a_2**-2.
    """
    if (
        not isinstance(variable_count, int)
        or isinstance(variable_count, bool)
        or variable_count <= 0
    ):
        raise ValueError("variable_count must be a positive integer")
    if (
        not isinstance(n_steps, int)
        or isinstance(n_steps, bool)
        or n_steps < 0
    ):
        raise ValueError("n_steps must be a nonnegative integer")
    try:
        tol = float(tolerance)
    except (TypeError, ValueError) as exc:
        raise ValueError("tolerance must be finite and positive") from exc
    if not math.isfinite(tol) or tol <= 0:
        raise ValueError("tolerance must be finite and positive")

    p0 = _normalize(p, variable_count, tol)
    q0 = _normalize(q, variable_count, tol)

    def recurse(
        p_current: dict[Exponent, complex],
        q_current: dict[Exponent, complex],
        remaining: int,
    ) -> tuple[bool, tuple[int, ...], tuple[float, ...], str]:
        if remaining == 0:
            phase0 = _base_phase(p_current, q_current, variable_count, tol)
            if phase0 is not None:
                return True, (), (phase0,), "constant unit-modulus base pair accepted numerically"
            return False, (), (), "zero-step base pair failed unit-modulus/zero-Q check"

        degrees = [_degree(p_current, axis) for axis in range(variable_count)]
        degree_sum = sum(degrees)
        if degree_sum <= remaining - 2:
            return recurse(p_current, q_current, remaining - 2)

        if degree_sum == remaining:
            for axis, degree in enumerate(degrees):
                phase = _phase_if_proportional_unit(
                    _positive_slice(p_current, axis, degree),
                    _positive_slice(q_current, axis, degree),
                    tol,
                )
                if phase is None:
                    continue
                p_reduced, q_reduced = _remove_last_signal(
                    p_current, q_current, axis, phase, tol
                )
                ok, indices, angles, reason = recurse(
                    p_reduced, q_reduced, remaining - 1
                )
                if not ok:
                    return False, (), (), reason
                return True, indices + (axis,), angles + (phase,), (
                    "recursive numerical factorization candidate accepted"
                )

        return False, (), (), "degree/leading-coefficient recursion rejected the pair"

    feasible, indices, angles, reason = recurse(p0, q0, n_steps)
    return MQSPDecision(feasible, indices, angles, reason, tol)
