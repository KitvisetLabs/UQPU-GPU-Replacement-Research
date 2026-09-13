"""FND-007B2: independent operator-algebra cross-check for the 2D-QED plaquette.

Research Attribution
--------------------
Research Owner / Principal Investigator / Research Direction: Kanutsanan Pongpanna
Facebook: https://www.facebook.com/LoveMoneyTH
YouTube: https://www.youtube.com/@LoveMoneyTHOfficial
AI Research Agent: OpenAI GPT-5.6 Sol
AI-assisted contribution: independent operator-algebra implementation, deterministic
Jacobi eigensolver, numerical cross-check design, evidence classification and docs.

This module intentionally does not import the Batch-042 Hamiltonian builder. It
reconstructs Meth et al. (Nature Physics 21, 570-576 (2025),
arXiv:2310.12110v3) Eqs. (9)-(10) through explicit tensor-product operators in
the full 2^4 * 3 = 48 dimensional qubit-qutrit Hilbert space and only then
projects to the zero-total-magnetization sector.

The independent diagonalization path is a classical symmetric Jacobi method.
The purpose is to test implementation agreement and numerical convergence, not
to claim an independent experimental reproduction or quantum advantage.
"""

from __future__ import annotations

import itertools
import math
from dataclasses import dataclass

Matrix = list[list[float]]

I2: Matrix = [[1.0, 0.0], [0.0, 1.0]]
Z: Matrix = [[-1.0, 0.0], [0.0, 1.0]]
SIGMA_PLUS: Matrix = [[0.0, 0.0], [1.0, 0.0]]
SIGMA_MINUS: Matrix = [[0.0, 1.0], [0.0, 0.0]]
I3: Matrix = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
E: Matrix = [[1.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, -1.0]]
U: Matrix = [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]
U_DAGGER: Matrix = [list(row) for row in zip(*U)]


def _zeros(rows: int, columns: int) -> Matrix:
    return [[0.0 for _ in range(columns)] for _ in range(rows)]


def _identity(size: int) -> Matrix:
    return [[1.0 if row == column else 0.0 for column in range(size)] for row in range(size)]


def _transpose(matrix: Matrix) -> Matrix:
    return [list(row) for row in zip(*matrix)]


def _add(*matrices: Matrix) -> Matrix:
    rows = len(matrices[0])
    columns = len(matrices[0][0])
    output = _zeros(rows, columns)
    for matrix in matrices:
        if len(matrix) != rows or any(len(row) != columns for row in matrix):
            raise ValueError("all matrices must have equal shape")
        for row in range(rows):
            for column in range(columns):
                output[row][column] += matrix[row][column]
    return output


def _scale(matrix: Matrix, scalar: float) -> Matrix:
    return [[scalar * value for value in row] for row in matrix]


def _matmul(left: Matrix, right: Matrix) -> Matrix:
    if len(left[0]) != len(right):
        raise ValueError("matrix dimensions do not align")
    rows = len(left)
    inner = len(right)
    columns = len(right[0])
    output = _zeros(rows, columns)
    for row in range(rows):
        for pivot in range(inner):
            coefficient = left[row][pivot]
            if coefficient == 0.0:
                continue
            for column in range(columns):
                output[row][column] += coefficient * right[pivot][column]
    return output


def _kron(left: Matrix, right: Matrix) -> Matrix:
    left_rows = len(left)
    left_columns = len(left[0])
    right_rows = len(right)
    right_columns = len(right[0])
    output = _zeros(left_rows * right_rows, left_columns * right_columns)
    for left_row in range(left_rows):
        for left_column in range(left_columns):
            coefficient = left[left_row][left_column]
            if coefficient == 0.0:
                continue
            for right_row in range(right_rows):
                for right_column in range(right_columns):
                    output[left_row * right_rows + right_row][
                        left_column * right_columns + right_column
                    ] = coefficient * right[right_row][right_column]
    return output


def _tensor_operator(
    qubit_operators: dict[int, Matrix] | None = None,
    gauge_operator: Matrix | None = None,
) -> Matrix:
    qubit_operators = qubit_operators or {}
    output: Matrix = [[1.0]]
    for qubit in range(4):
        output = _kron(output, qubit_operators.get(qubit, I2))
    return _kron(output, gauge_operator if gauge_operator is not None else I3)


FULL_IDENTITY = _tensor_operator()
Z_OPERATORS = tuple(_tensor_operator({qubit: Z}) for qubit in range(4))
E_OPERATOR = _tensor_operator(gauge_operator=E)
E_SQUARED_OPERATOR = _matmul(E_OPERATOR, E_OPERATOR)
U_OPERATOR = _tensor_operator(gauge_operator=U)
U_DAGGER_OPERATOR = _tensor_operator(gauge_operator=U_DAGGER)
PLAQUETTE_FULL_OPERATOR = _scale(_add(U_OPERATOR, U_DAGGER_OPERATOR), 0.5)


def _full_basis_index(bits: tuple[int, int, int, int], gauge_index: int) -> int:
    index = 0
    for bit in bits:
        index = 2 * index + bit
    return 3 * index + gauge_index


ZERO_MAGNETIZATION_FULL_INDICES = tuple(
    _full_basis_index(bits, gauge_index)
    for bits in itertools.product((0, 1), repeat=4)
    if sum(bits) == 2
    for gauge_index in range(3)
)


def project_zero_magnetization(matrix: Matrix) -> Matrix:
    """Project a 48x48 full-space operator to the 18-state physical sector."""
    if len(matrix) != 48 or any(len(row) != 48 for row in matrix):
        raise ValueError("full-space matrix must be 48x48")
    return [
        [matrix[row][column] for column in ZERO_MAGNETIZATION_FULL_INDICES]
        for row in ZERO_MAGNETIZATION_FULL_INDICES
    ]


def full_space_hamiltonian(
    inverse_g_squared: float,
    mass: float = 0.1,
    omega: float = 5.0,
) -> Matrix:
    """Construct source-v3 Eqs. (9)-(10) in the full 48-dimensional space."""
    if inverse_g_squared <= 0.0:
        raise ValueError("inverse_g_squared must be positive")

    g_squared = 1.0 / inverse_g_squared
    z1, z2, z3, z4 = Z_OPERATORS

    electric_linear = _add(
        _scale(z1, -2.0),
        z2,
        _scale(z4, -1.0),
        _scale(FULL_IDENTITY, -2.0),
    )
    h_e = _scale(
        _add(
            _scale(E_SQUARED_OPERATOR, 8.0),
            _scale(_matmul(E_OPERATOR, electric_linear), 2.0),
            z1,
            _scale(z2, -1.0),
            _matmul(z1, z4),
            _scale(FULL_IDENTITY, 3.0),
        ),
        0.25,
    )
    h_b = _scale(_add(U_OPERATOR, U_DAGGER_OPERATOR), -0.5)
    h_m = _scale(_add(z1, _scale(z2, -1.0), z3, _scale(z4, -1.0)), 0.5)

    kinetic_forward = _add(
        _tensor_operator({0: SIGMA_PLUS, 1: SIGMA_MINUS}, U_DAGGER),
        _tensor_operator({1: SIGMA_PLUS, 2: SIGMA_MINUS}),
        _scale(_tensor_operator({3: SIGMA_PLUS, 2: SIGMA_MINUS}), -1.0),
        _scale(_tensor_operator({0: SIGMA_PLUS, 3: SIGMA_MINUS}), -1.0),
    )
    h_k = _add(kinetic_forward, _transpose(kinetic_forward))

    return _add(
        _scale(h_e, g_squared),
        _scale(h_b, inverse_g_squared),
        _scale(h_m, mass),
        _scale(h_k, omega),
    )


def projected_hamiltonian(
    inverse_g_squared: float,
    mass: float = 0.1,
    omega: float = 5.0,
) -> Matrix:
    return project_zero_magnetization(
        full_space_hamiltonian(
            inverse_g_squared=inverse_g_squared,
            mass=mass,
            omega=omega,
        )
    )


PROJECTED_PLAQUETTE_OPERATOR = project_zero_magnetization(PLAQUETTE_FULL_OPERATOR)


def symmetric_jacobi_eigendecomposition(
    matrix: Matrix,
    tolerance: float = 1e-12,
    max_rotations: int = 200_000,
) -> tuple[list[float], list[list[float]], int]:
    """Return ascending eigenvalues and eigenvectors for a real-symmetric matrix."""
    size = len(matrix)
    if not size or any(len(row) != size for row in matrix):
        raise ValueError("matrix must be non-empty and square")
    if tolerance <= 0.0:
        raise ValueError("tolerance must be positive")
    if max_rotations <= 0:
        raise ValueError("max_rotations must be positive")
    for row in range(size):
        for column in range(row + 1, size):
            if abs(matrix[row][column] - matrix[column][row]) > 1e-12:
                raise ValueError("matrix must be symmetric")

    working = [row[:] for row in matrix]
    eigenvectors = _identity(size)

    for rotation in range(max_rotations + 1):
        pivot_row = 0
        pivot_column = 0
        max_off_diagonal = 0.0
        for row in range(size):
            for column in range(row + 1, size):
                magnitude = abs(working[row][column])
                if magnitude > max_off_diagonal:
                    max_off_diagonal = magnitude
                    pivot_row = row
                    pivot_column = column

        if max_off_diagonal < tolerance:
            raw_eigenvalues = [working[index][index] for index in range(size)]
            order = sorted(range(size), key=lambda index: raw_eigenvalues[index])
            values = [raw_eigenvalues[index] for index in order]
            vectors = [
                [eigenvectors[row][index] for row in range(size)]
                for index in order
            ]
            return values, vectors, rotation

        p = pivot_row
        q = pivot_column
        app = working[p][p]
        aqq = working[q][q]
        apq = working[p][q]

        tau = (aqq - app) / (2.0 * apq)
        tangent = 1.0 / (abs(tau) + math.sqrt(1.0 + tau * tau))
        if tau < 0.0:
            tangent = -tangent
        cosine = 1.0 / math.sqrt(1.0 + tangent * tangent)
        sine = tangent * cosine

        for index in range(size):
            if index in (p, q):
                continue
            aip = working[index][p]
            aiq = working[index][q]
            working[index][p] = working[p][index] = cosine * aip - sine * aiq
            working[index][q] = working[q][index] = sine * aip + cosine * aiq

        working[p][p] = app - tangent * apq
        working[q][q] = aqq + tangent * apq
        working[p][q] = working[q][p] = 0.0

        for row in range(size):
            vip = eigenvectors[row][p]
            viq = eigenvectors[row][q]
            eigenvectors[row][p] = cosine * vip - sine * viq
            eigenvectors[row][q] = sine * vip + cosine * viq

    raise RuntimeError("Jacobi eigendecomposition did not converge")


def _matvec(matrix: Matrix, vector: list[float]) -> list[float]:
    return [
        sum(value * component for value, component in zip(row, vector))
        for row in matrix
    ]


def _dot(left: list[float], right: list[float]) -> float:
    return sum(a * b for a, b in zip(left, right))


def _norm(vector: list[float]) -> float:
    return math.sqrt(_dot(vector, vector))


def operator_expectation(operator: Matrix, state: list[float]) -> float:
    if len(operator) != len(state) or any(len(row) != len(state) for row in operator):
        raise ValueError("operator and state dimensions do not align")
    return _dot(state, _matvec(operator, state))


def eigenpair_residual(matrix: Matrix, eigenvalue: float, state: list[float]) -> float:
    if len(matrix) != len(state) or any(len(row) != len(state) for row in matrix):
        raise ValueError("matrix and state dimensions do not align")
    transformed = _matvec(matrix, state)
    return _norm(
        [value - eigenvalue * component for value, component in zip(transformed, state)]
    )


@dataclass(frozen=True)
class IndependentGroundState:
    inverse_g_squared: float
    energy: float
    plaquette_expectation: float
    residual_norm: float
    jacobi_rotations: int


def independent_ground_state(
    inverse_g_squared: float,
    mass: float = 0.1,
    omega: float = 5.0,
) -> IndependentGroundState:
    hamiltonian = projected_hamiltonian(
        inverse_g_squared=inverse_g_squared,
        mass=mass,
        omega=omega,
    )
    eigenvalues, eigenvectors, rotations = symmetric_jacobi_eigendecomposition(hamiltonian)
    state = eigenvectors[0]
    energy = eigenvalues[0]
    return IndependentGroundState(
        inverse_g_squared=inverse_g_squared,
        energy=energy,
        plaquette_expectation=operator_expectation(PROJECTED_PLAQUETTE_OPERATOR, state),
        residual_norm=eigenpair_residual(hamiltonian, energy, state),
        jacobi_rotations=rotations,
    )


def full_spectrum(
    inverse_g_squared: float,
    mass: float = 0.1,
    omega: float = 5.0,
) -> list[float]:
    eigenvalues, _, _ = symmetric_jacobi_eigendecomposition(
        projected_hamiltonian(
            inverse_g_squared=inverse_g_squared,
            mass=mass,
            omega=omega,
        )
    )
    return eigenvalues


def classification() -> dict[str, object]:
    return {
        "classification": "LATTICE_QED_INDEPENDENT_OPERATOR_CROSSCHECK",
        "evidence_level": "INTERNAL_INDEPENDENT_IMPLEMENTATION_CROSSCHECK",
        "full_hilbert_dimension": 48,
        "projected_sector_dimension": len(ZERO_MAGNETIZATION_FULL_INDICES),
        "independence_boundary": (
            "Independent code path and eigensolver inside UQPU; not an independent "
            "external team, experiment, or hardware reproduction."
        ),
        "non_claims": {
            "real_qpu_reproduction": False,
            "quantum_advantage": False,
            "direct_elementary_particle_device": False,
            "qcd_or_quark_computer": False,
            "universal_qudit_advantage": False,
            "gpu_npu_ram_hbm_replacement": False,
            "one_hundred_million_x_saving": False,
            "new_physical_law": False,
        },
    }
