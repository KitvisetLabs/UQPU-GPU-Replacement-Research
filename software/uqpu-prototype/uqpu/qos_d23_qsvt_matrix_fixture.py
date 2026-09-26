"""Bounded matrix/QSVT fixture for QOS-AUDIT-010B4.

This is a dense numerical convention check, not a circuit execution.  It lifts
the Batch-055 scalar Wx convention to a one-ancilla Hermitian block encoding and
compares the transformed projected block with spectral polynomial calculus.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import asdict, dataclass

from .qos_d23_phase_reconstruction_v040 import FROZEN_PHASES_V040, target_polynomial

Matrix = tuple[tuple[complex, ...], ...]

CONTRACT_ID = "QOS-AUDIT-010B4"
FIXTURE_EIGENVALUES = (0.2, 0.8)
FIXTURE_ROTATION_RADIANS = 0.37
TRANSFORM_TOLERANCE = 2e-12
UNITARITY_TOLERANCE = 2e-13


def _identity(size: int) -> Matrix:
    return tuple(tuple(complex(row == column) for column in range(size)) for row in range(size))


def _matmul(left: Matrix, right: Matrix) -> Matrix:
    if not left or len(left[0]) != len(right):
        raise ValueError("incompatible matrix dimensions")
    return tuple(
        tuple(
            sum(left[row][inner] * right[inner][column] for inner in range(len(right)))
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def _dagger(matrix: Matrix) -> Matrix:
    return tuple(tuple(matrix[row][column].conjugate() for row in range(len(matrix)))
                 for column in range(len(matrix[0])))


def _spectral_2x2(values: tuple[float, float], angle: float) -> Matrix:
    cosine, sine = math.cos(angle), math.sin(angle)
    rotation: Matrix = ((cosine, -sine), (sine, cosine))
    diagonal: Matrix = ((values[0], 0j), (0j, values[1]))
    return _matmul(_matmul(rotation, diagonal), _dagger(rotation))


def fixture_matrix() -> Matrix:
    return _spectral_2x2(FIXTURE_EIGENVALUES, FIXTURE_ROTATION_RADIANS)


def fixture_block_encoding() -> Matrix:
    """Return U_A=[[A,i sqrt(I-A^2)],[i sqrt(I-A^2),A]]."""
    matrix = fixture_matrix()
    complement_values = tuple(math.sqrt(1.0 - value * value) for value in FIXTURE_EIGENVALUES)
    complement = _spectral_2x2(complement_values, FIXTURE_ROTATION_RADIANS)
    return tuple(
        tuple(
            matrix[row % 2][column % 2]
            if (row < 2) == (column < 2)
            else 1j * complement[row % 2][column % 2]
            for column in range(4)
        )
        for row in range(4)
    )


def _phase_rotation(phase: float) -> Matrix:
    positive = cmath.exp(1j * phase)
    negative = positive.conjugate()
    return (
        (positive, 0j, 0j, 0j),
        (0j, positive, 0j, 0j),
        (0j, 0j, negative, 0j),
        (0j, 0j, 0j, negative),
    )


def transformed_unitary(phases: tuple[float, ...] = FROZEN_PHASES_V040) -> Matrix:
    if not phases or not all(math.isfinite(phase) for phase in phases):
        raise ValueError("phases must be finite and nonempty")
    signal = fixture_block_encoding()
    result = _phase_rotation(phases[0])
    for phase in phases[1:]:
        result = _matmul(_matmul(result, signal), _phase_rotation(phase))
    return result


def target_transformed_matrix() -> Matrix:
    return _spectral_2x2(
        tuple(target_polynomial(value) for value in FIXTURE_EIGENVALUES),
        FIXTURE_ROTATION_RADIANS,
    )


def _unitarity_residual(matrix: Matrix) -> float:
    product = _matmul(_dagger(matrix), matrix)
    identity = _identity(len(matrix))
    return max(
        abs(product[row][column] - identity[row][column])
        for row in range(len(matrix))
        for column in range(len(matrix))
    )


@dataclass(frozen=True)
class MatrixFixtureCertificate:
    contract_id: str
    fixture_eigenvalues: tuple[float, float]
    fixture_rotation_radians: float
    block_encoding_dimension: int
    block_encoding_top_left_residual: float
    block_encoding_unitarity_residual: float
    transformed_real_block_residual: float
    transformed_unitarity_residual: float
    transform_tolerance: float
    unitarity_tolerance: float
    phase_count: int
    passed: bool
    evidence_label: str


def verify_matrix_fixture(
    phases: tuple[float, ...] = FROZEN_PHASES_V040,
    transform_tolerance: float = TRANSFORM_TOLERANCE,
    unitarity_tolerance: float = UNITARITY_TOLERANCE,
) -> MatrixFixtureCertificate:
    matrix = fixture_matrix()
    block = fixture_block_encoding()
    transformed = transformed_unitary(phases)
    target = target_transformed_matrix()
    block_residual = max(abs(block[row][column] - matrix[row][column])
                         for row in range(2) for column in range(2))
    transform_residual = max(abs(transformed[row][column].real - target[row][column].real)
                             for row in range(2) for column in range(2))
    block_unitarity = _unitarity_residual(block)
    transformed_unitarity = _unitarity_residual(transformed)
    passed = (
        len(phases) == 82
        and block_residual <= transform_tolerance
        and transform_residual <= transform_tolerance
        and block_unitarity <= unitarity_tolerance
        and transformed_unitarity <= unitarity_tolerance
    )
    return MatrixFixtureCertificate(
        contract_id=CONTRACT_ID,
        fixture_eigenvalues=FIXTURE_EIGENVALUES,
        fixture_rotation_radians=FIXTURE_ROTATION_RADIANS,
        block_encoding_dimension=4,
        block_encoding_top_left_residual=block_residual,
        block_encoding_unitarity_residual=block_unitarity,
        transformed_real_block_residual=transform_residual,
        transformed_unitarity_residual=transformed_unitarity,
        transform_tolerance=transform_tolerance,
        unitarity_tolerance=unitarity_tolerance,
        phase_count=len(phases),
        passed=passed,
        evidence_label="SIMULATION",
    )


def resource_ledger() -> dict[str, object]:
    return {
        "contract_id": CONTRACT_ID,
        "accounting_scope": "BOUNDED_DENSE_FIXTURE_MODEL_ONLY",
        "polynomial_degree": 81,
        "signal_or_block_encoding_queries": 81,
        "phase_rotations": 82,
        "signal_ancillas": 1,
        "logical_system_qubits_fixture": 1,
        "logical_qubits_fixture_total": 2,
        "phase_payload_binary64_bytes": 82 * 8,
        "dense_statevector_complex128_bytes": 4 * 16,
        "dense_operator_complex128_bytes": 4 * 4 * 16,
        "shots": 0,
        "provider_jobs": 0,
        "gate_decomposition_status": "NOT_PERFORMED",
        "energy_and_cost_status": "NOT_MEASURED",
    }


def matrix_fixture_artifact() -> dict[str, object]:
    return {
        "certificate": asdict(verify_matrix_fixture()),
        "resource_ledger": resource_ledger(),
        "warning": (
            "Dense numerical matrix validation only; not a provider circuit, real-QPU result, "
            "competitive workload, hardware requirement, or economic advantage."
        ),
    }
