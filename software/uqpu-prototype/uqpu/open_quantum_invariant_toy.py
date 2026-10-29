"""Exact toy checks for invariant observable structures in a one-qubit dephasing model.

This deliberately small standard-library fixture checks two distinct properties:
invariance under a declared generator and closure under operator multiplication.
It is MODEL_ONLY mathematics/software, not an experimental or hardware result.
"""
from __future__ import annotations

import math
from collections.abc import Iterable


def _matrix_rank(matrix: list[list[complex]], tolerance: float) -> int:
    """Return a tolerance-based row rank using Gaussian elimination."""
    if not matrix:
        return 0
    rows = [row[:] for row in matrix]
    row_count = len(rows)
    column_count = len(rows[0])
    pivot_row = 0
    for column in range(column_count):
        if pivot_row >= row_count:
            break
        pivot = max(range(pivot_row, row_count), key=lambda index: abs(rows[index][column]))
        if abs(rows[pivot][column]) <= tolerance:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = rows[pivot_row][column]
        rows[pivot_row] = [value / scale for value in rows[pivot_row]]
        for index in range(row_count):
            if index == pivot_row:
                continue
            factor = rows[index][column]
            if abs(factor) > tolerance:
                rows[index] = [
                    left - factor * right
                    for left, right in zip(rows[index], rows[pivot_row])
                ]
        pivot_row += 1
    return pivot_row


def _validated_basis(
    basis: Iterable[Iterable[object]], tolerance: object
) -> tuple[tuple[tuple[complex, ...], ...], float]:
    """Validate independent coefficient vectors in the ordered basis I, X, Y, Z."""
    if isinstance(basis, (str, bytes)):
        raise ValueError("basis must be a non-string iterable of coefficient vectors")
    try:
        vectors = tuple(tuple(vector) for vector in basis)
    except TypeError as exc:
        raise ValueError("basis must be an iterable of coefficient vectors") from exc
    if not vectors:
        raise ValueError("basis must not be empty")

    clean: list[tuple[complex, ...]] = []
    for vector in vectors:
        if len(vector) != 4:
            raise ValueError("each Pauli coefficient vector must have length 4 (I, X, Y, Z)")
        values: list[complex] = []
        for value in vector:
            if isinstance(value, bool) or not isinstance(value, (int, float, complex)):
                raise ValueError("coefficients must be numeric and not boolean")
            number = complex(value)
            if not math.isfinite(number.real) or not math.isfinite(number.imag):
                raise ValueError("coefficients must be finite")
            values.append(number)
        clean.append(tuple(values))

    if isinstance(tolerance, bool) or not isinstance(tolerance, (int, float)):
        raise ValueError("tolerance must be positive and finite")
    if not math.isfinite(tolerance) or tolerance <= 0:
        raise ValueError("tolerance must be positive and finite")
    if len(clean) > 4:
        raise ValueError("a linearly independent Pauli coefficient basis has dimension at most four")

    rows = [[clean[column][row] for column in range(len(clean))] for row in range(4)]
    if _matrix_rank(rows, float(tolerance)) != len(clean):
        raise ValueError("basis vectors must be linearly independent")
    return tuple(clean), float(tolerance)


def _in_span(
    vector: tuple[complex, ...],
    basis: tuple[tuple[complex, ...], ...],
    tolerance: float,
) -> bool:
    """Check whether a coefficient vector belongs to the candidate linear span."""
    rows = [[basis[column][row] for column in range(len(basis))] for row in range(4)]
    augmented = [row + [vector[index]] for index, row in enumerate(rows)]
    return _matrix_rank(rows, tolerance) == _matrix_rank(augmented, tolerance)


def _pauli_product(
    left: tuple[complex, ...], right: tuple[complex, ...]
) -> tuple[complex, ...]:
    """Multiply operators encoded as coefficients in the Pauli basis I, X, Y, Z."""
    identity, x, y, z = left
    other_identity, other_x, other_y, other_z = right
    return (
        identity * other_identity + x * other_x + y * other_y + z * other_z,
        identity * other_x + x * other_identity + 1j * (y * other_z - z * other_y),
        identity * other_y + y * other_identity + 1j * (z * other_x - x * other_z),
        identity * other_z + z * other_identity + 1j * (x * other_y - y * other_x),
    )


def evaluate_pure_dephasing_candidate(
    basis: Iterable[Iterable[object]],
    gamma: object = 1.0,
    tolerance: object = 1e-10,
) -> dict[str, object]:
    """Check invariance and algebra closure for a declared one-qubit pure-dephasing toy model.

    Coefficients use the Pauli basis ordered as (I, X, Y, Z). The declared
    Heisenberg-picture generator maps I and Z to zero, and maps X and Y to
    -gamma times themselves. Passing these checks does not establish that a
    structure is identifiable from measurements or decoherence-free.
    """
    vectors, tol = _validated_basis(basis, tolerance)
    if isinstance(gamma, bool) or not isinstance(gamma, (int, float)):
        raise ValueError("gamma must be finite and nonnegative")
    if not math.isfinite(gamma) or gamma < 0:
        raise ValueError("gamma must be finite and nonnegative")

    images = tuple((0j, -gamma * vector[1], -gamma * vector[2], 0j) for vector in vectors)
    invariant = all(_in_span(image, vectors, tol) for image in images)
    algebra_closed = all(
        _in_span(_pauli_product(left, right), vectors, tol)
        for left in vectors
        for right in vectors
    )
    return {
        "model": "one-qubit pure-dephasing generator in the Pauli basis",
        "evidence_class": "MODEL_ONLY",
        "basis_dimension": len(vectors),
        "invariant_under_declared_generator": invariant,
        "closed_under_operator_product": algebra_closed,
        "passes_exact_toy_checks": invariant and algebra_closed,
        "claim_boundary": (
            "Deterministic finite-dimensional toy check only; not an experimental result, "
            "new physical law, decoherence-free claim, quantum advantage, memory replacement, "
            "or UQPU mission-level result."
        ),
    }
