"""Pinned-SDK semantic cross-check for the signed Max-Cut score operator.

This module verifies a finite, tiny-instance algebraic contract. It does not
build QAOA circuits, query a provider, or claim physical or economic advantage.
"""
from __future__ import annotations

import math

from .signed_maxcut_objective import SignedMaxCutLowering

PINNED_QISKIT_VERSION = "2.5.2"
DEFAULT_TOLERANCE = 1e-12
MAX_EXHAUSTIVE_VERTICES = 8


def tiny_signed_maxcut_fixtures() -> tuple[tuple[str, int, tuple[tuple[int, int, float], ...]], ...]:
    """Return the frozen small-graph fixtures shared by tests and certificate runner."""
    return (
        ("empty_one_vertex", 1, ()),
        ("signed_triangle", 3, ((0, 1, 2.0), (1, 2, -3.0), (0, 2, 0.5))),
        ("negative_only", 3, ((0, 1, -2.0), (1, 2, -1.0))),
        ("tied_positive_cycle", 4, ((0, 1, 1.0), (1, 2, 1.0), (2, 3, 1.0), (3, 0, 1.0))),
        ("disconnected_mixed", 5, ((0, 1, 1.25), (1, 2, -0.75), (3, 4, 2.0), (0, 2, 0.0))),
        ("all_zero_triangle", 3, ((0, 1, 0.0), (1, 2, 0.0), (0, 2, 0.0))),
    )


def build_qiskit_signed_maxcut_operator(lowering: SignedMaxCutLowering):
    """Build C-hat = c I + sum J_uv Z_u Z_v in Qiskit Pauli-label order.

    Qiskit Pauli strings place qubit 0 at the rightmost character. The constant
    is preserved in the returned score operator, even if an optimizer removes it.
    """
    try:
        from qiskit.quantum_info import SparsePauliOp
    except ImportError as exc:
        raise RuntimeError(
            "Qiskit is optional; install verification-optional-requirements.txt"
        ) from exc

    n = lowering.vertex_count
    terms: list[tuple[str, complex]] = [("I" * n, complex(lowering.ising_constant))]
    for u, v, coefficient in lowering.ising_couplings:
        label = ["I"] * n
        label[n - 1 - u] = "Z"
        label[n - 1 - v] = "Z"
        terms.append(("".join(label), complex(coefficient)))
    return SparsePauliOp.from_list(terms)


def qiskit_signed_maxcut_scores(
    lowering: SignedMaxCutLowering, tolerance: float = DEFAULT_TOLERANCE
) -> tuple[float, ...]:
    """Return all operator diagonal scores in computational-basis order.

    Basis index k maps to bits x_q = (k >> q) & 1. Exhaustive matrix allocation
    is capped so the verification helper cannot silently become a state-space
    benchmark or allocate a large dense matrix.
    """
    if (
        isinstance(tolerance, bool)
        or not isinstance(tolerance, (int, float))
        or not math.isfinite(tolerance)
        or tolerance < 0
    ):
        raise ValueError("tolerance must be a finite nonnegative real number")
    if lowering.vertex_count > MAX_EXHAUSTIVE_VERTICES:
        raise ValueError(
            f"exhaustive SDK verification is limited to {MAX_EXHAUSTIVE_VERTICES} vertices"
        )

    import numpy as np

    matrix = build_qiskit_signed_maxcut_operator(lowering).to_matrix()
    if float(np.max(np.abs(matrix - matrix.conj().T))) > tolerance:
        raise AssertionError("SDK score operator is not Hermitian within tolerance")
    diagonal = np.diag(matrix)
    off_diagonal = matrix - np.diag(diagonal)
    if float(np.max(np.abs(off_diagonal))) > tolerance:
        raise AssertionError("signed Max-Cut score operator must be diagonal")
    if float(np.max(np.abs(diagonal.imag))) > tolerance:
        raise AssertionError("SDK score operator has non-real computational-basis scores")

    scores = tuple(float(value.real) for value in diagonal)
    for basis_index, actual in enumerate(scores):
        bits = tuple((basis_index >> qubit) & 1 for qubit in range(lowering.vertex_count))
        expected = lowering.direct_score(bits)
        if not math.isclose(actual, expected, rel_tol=0.0, abs_tol=tolerance):
            raise AssertionError(
                f"SDK operator mismatch at basis index {basis_index}: "
                f"SDK={actual!r}, direct={expected!r}, bits={bits!r}"
            )
    return scores
