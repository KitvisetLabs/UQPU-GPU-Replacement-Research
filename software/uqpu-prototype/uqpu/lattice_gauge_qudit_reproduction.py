"""FND-007B: reproducible 2D-QED qudit resource and plaquette gate.

Research Attribution
--------------------
Research Owner / Principal Investigator / Research Direction: Kanutsanan Pongpanna
Facebook: https://www.facebook.com/LoveMoneyTH
YouTube: https://www.youtube.com/@LoveMoneyTHOfficial
AI Research Agent: OpenAI GPT-5.6 Sol
AI-assisted contribution: literature/interface audit, exact small-Hilbert-space
reproduction, resource-ledger implementation, tests and documentation.

This module reproduces two source-v3 results from Meth et al., Nature Physics
21, 570-576 (2025), arXiv:2310.12110v3:

1. the mixed qubit-qutrit single-plaquette Hamiltonian of Eqs. (9)-(10),
   restricted to the zero-total-charge sector and solved by deterministic
   exact finite-dimensional linear algebra;
2. the cross-platform CNOT/register resource formulas reported in Appendix G.

Evidence boundary: this is an independent classical reproduction of a small
published model and its resource formulas. It is not a real-QPU reproduction,
a quantum-advantage result, or an elementary-particle computing device.
"""

from __future__ import annotations

import itertools
import math
from dataclasses import dataclass

E_VALUES = (1.0, 0.0, -1.0)


def _zero_charge_basis() -> tuple[tuple[tuple[int, int, int, int], int], ...]:
    basis: list[tuple[tuple[int, int, int, int], int]] = []
    for bits in itertools.product((0, 1), repeat=4):
        if sum(bits) == 2:
            for e_index in range(3):
                basis.append((bits, e_index))
    return tuple(basis)


BASIS = _zero_charge_basis()
INDEX = {state: index for index, state in enumerate(BASIS)}


def _z(bit: int) -> float:
    # Paper convention: down -> -1, up -> +1.
    return 1.0 if bit else -1.0


def _apply_operator_sequence(
    state: tuple[tuple[int, int, int, int], int],
    operators: tuple[tuple[str, int | None], ...],
) -> tuple[tuple[int, int, int, int], int] | None:
    bits = list(state[0])
    e_index = state[1]
    for operator, qubit in reversed(operators):
        if operator == "sp":
            assert qubit is not None
            if bits[qubit] != 0:
                return None
            bits[qubit] = 1
        elif operator == "sm":
            assert qubit is not None
            if bits[qubit] != 1:
                return None
            bits[qubit] = 0
        elif operator == "Udag":
            # E basis is (+1, 0, -1); U^dag raises E.
            if e_index <= 0:
                return None
            e_index -= 1
        elif operator == "U":
            if e_index >= 2:
                return None
            e_index += 1
        else:
            raise ValueError(f"unknown operator: {operator}")
    output = (tuple(bits), e_index)
    return output if output in INDEX else None


def single_plaquette_hamiltonian(
    inverse_g_squared: float,
    mass: float = 0.1,
    omega: float = 5.0,
) -> list[list[float]]:
    """Build the real-symmetric Eq. (9) Hamiltonian in the zero-charge sector.

    The source eliminates three of four gauge links with Gauss' law, leaving
    four matter qubits and one qutrit. The zero-charge sector contains
    C(4,2)*3 = 18 basis states.
    """
    if inverse_g_squared <= 0:
        raise ValueError("inverse_g_squared must be positive")

    g_squared = 1.0 / inverse_g_squared
    size = len(BASIS)
    hamiltonian = [[0.0 for _ in range(size)] for _ in range(size)]

    for column, (bits, e_index) in enumerate(BASIS):
        z1, z2, z3, z4 = (_z(bit) for bit in bits)
        electric_field = E_VALUES[e_index]
        h_e = 0.25 * (
            8.0 * electric_field**2
            + 2.0
            * electric_field
            * (-2.0 * z1 + z2 - z4 - 2.0)
            + z1
            - z2
            + z1 * z4
            + 3.0
        )
        h_m = 0.5 * (z1 - z2 + z3 - z4)
        hamiltonian[column][column] += g_squared * h_e + mass * h_m

        # H_B = -(U + U^dag)/2, multiplied by inverse_g_squared.
        if e_index < 2:
            row = INDEX[(bits, e_index + 1)]
            hamiltonian[row][column] += -0.5 * inverse_g_squared
        if e_index > 0:
            row = INDEX[(bits, e_index - 1)]
            hamiltonian[row][column] += -0.5 * inverse_g_squared

    kinetic_terms = (
        ((('sp', 0), ('Udag', None), ('sm', 1)), 1.0),
        ((('sp', 1), ('sm', 2)), 1.0),
        ((('sp', 3), ('sm', 2)), -1.0),
        ((('sp', 0), ('sm', 3)), -1.0),
    )
    adjoint = {"sp": "sm", "sm": "sp", "Udag": "U", "U": "Udag"}

    for state in BASIS:
        column = INDEX[state]
        for operators, sign in kinetic_terms:
            output = _apply_operator_sequence(state, operators)
            if output is not None:
                hamiltonian[INDEX[output]][column] += omega * sign

            adjoint_operators = tuple(
                (adjoint[operator], qubit)
                for operator, qubit in reversed(operators)
            )
            output = _apply_operator_sequence(state, adjoint_operators)
            if output is not None:
                hamiltonian[INDEX[output]][column] += omega * sign

    return hamiltonian


def _dot(left: list[float], right: list[float]) -> float:
    return sum(a * b for a, b in zip(left, right))


def _norm(vector: list[float]) -> float:
    return math.sqrt(_dot(vector, vector))


def _matvec(matrix: list[list[float]], vector: list[float]) -> list[float]:
    return [sum(value * component for value, component in zip(row, vector)) for row in matrix]


def ground_state(
    hamiltonian: list[list[float]],
    tolerance: float = 1e-13,
    max_iterations: int = 10_000,
) -> tuple[float, list[float], int]:
    """Return the lowest eigenpair using shifted deterministic power iteration."""
    size = len(hamiltonian)
    if not size or any(len(row) != size for row in hamiltonian):
        raise ValueError("hamiltonian must be non-empty and square")

    # Gershgorin row-sum bound guarantees shift > largest eigenvalue.
    shift = max(sum(abs(value) for value in row) for row in hamiltonian) + 1.0
    vector = [1.0 / math.sqrt(size) for _ in range(size)]
    previous_energy: float | None = None

    for iteration in range(1, max_iterations + 1):
        h_vector = _matvec(hamiltonian, vector)
        shifted = [
            shift * component - h_component
            for component, h_component in zip(vector, h_vector)
        ]
        length = _norm(shifted)
        if length == 0.0:
            raise RuntimeError("shifted power iteration encountered zero vector")
        vector = [component / length for component in shifted]
        h_vector = _matvec(hamiltonian, vector)
        energy = _dot(vector, h_vector)
        if previous_energy is not None and abs(energy - previous_energy) < tolerance:
            return energy, vector, iteration
        previous_energy = energy

    raise RuntimeError("ground-state iteration did not converge")


def plaquette_expectation(state_vector: list[float]) -> float:
    """Evaluate square = (U + U^dag)/2 for the single-plaquette encoding."""
    if len(state_vector) != len(BASIS):
        raise ValueError("state vector has wrong dimension")

    expectation = 0.0
    for column, (bits, e_index) in enumerate(BASIS):
        if e_index < 2:
            expectation += (
                0.5
                * state_vector[INDEX[(bits, e_index + 1)]]
                * state_vector[column]
            )
        if e_index > 0:
            expectation += (
                0.5
                * state_vector[INDEX[(bits, e_index - 1)]]
                * state_vector[column]
            )
    return expectation


@dataclass(frozen=True)
class ResourceLedger:
    dimension: int
    qudit_register_size: int
    qudit_cnot_count: int
    qubit_register_size: int
    qubit_cnot_count: int
    qudit_approx_circuit_fidelity: float
    qubit_approx_circuit_fidelity: float


def full_gauge_resource_ledger(
    dimension: int,
    cnot_fidelity: float = 0.99,
) -> ResourceLedger:
    """Reproduce Appendix-G full-gauge one-plaquette resource formulas."""
    if dimension < 3 or dimension % 2 == 0:
        raise ValueError("dimension must be an odd integer >= 3")
    if not 0.0 < cnot_fidelity <= 1.0:
        raise ValueError("cnot_fidelity must be in (0, 1]")

    qudit_cnot_count = 18 + 4 * (dimension - 1)
    qubit_cnot_count = 18 + 36 * (dimension - 1)
    return ResourceLedger(
        dimension=dimension,
        qudit_register_size=5,
        qudit_cnot_count=qudit_cnot_count,
        qubit_register_size=4 + dimension,
        qubit_cnot_count=qubit_cnot_count,
        qudit_approx_circuit_fidelity=cnot_fidelity**qudit_cnot_count,
        qubit_approx_circuit_fidelity=cnot_fidelity**qubit_cnot_count,
    )


def pure_gauge_resource_ledger(
    dimension: int,
    cnot_fidelity: float = 0.99,
) -> ResourceLedger:
    """Reproduce Appendix-G pure-gauge periodic-plaquette resource formulas."""
    if dimension < 3 or dimension % 2 == 0:
        raise ValueError("dimension must be an odd integer >= 3")
    if not 0.0 < cnot_fidelity <= 1.0:
        raise ValueError("cnot_fidelity must be in (0, 1]")

    qudit_cnot_count = 8
    qubit_cnot_count = 48 + 12 * dimension
    return ResourceLedger(
        dimension=dimension,
        qudit_register_size=3,
        qudit_cnot_count=qudit_cnot_count,
        qubit_register_size=3 * dimension,
        qubit_cnot_count=qubit_cnot_count,
        qudit_approx_circuit_fidelity=cnot_fidelity**qudit_cnot_count,
        qubit_approx_circuit_fidelity=cnot_fidelity**qubit_cnot_count,
    )


def reproduce_single_plaquette_curve(
    inverse_g_squared_values: tuple[float, ...] = (0.01, 0.1, 1.0, 10.0, 100.0),
    mass: float = 0.1,
    omega: float = 5.0,
) -> list[dict[str, float | int]]:
    """Exact finite-dimensional reproduction of the source single-plaquette curve."""
    rows: list[dict[str, float | int]] = []
    for inverse_g_squared in inverse_g_squared_values:
        hamiltonian = single_plaquette_hamiltonian(
            inverse_g_squared=inverse_g_squared,
            mass=mass,
            omega=omega,
        )
        energy, state, iterations = ground_state(hamiltonian)
        rows.append(
            {
                "inverse_g_squared": inverse_g_squared,
                "ground_energy": energy,
                "plaquette_expectation": plaquette_expectation(state),
                "iterations": iterations,
            }
        )
    return rows


def classification() -> dict[str, object]:
    return {
        "classification": "LATTICE_QED_QUDIT_RESOURCE_AND_PLAQUETTE_REPRODUCTION",
        "evidence_level": "INDEPENDENT_CLASSICAL_REPRODUCTION_OF_PUBLISHED_SMALL_MODEL",
        "hilbert_sector_dimension": len(BASIS),
        "non_claims": {
            "real_qpu_reproduction": False,
            "quantum_advantage": False,
            "direct_elementary_particle_device": False,
            "qcd_or_quark_computer": False,
            "gpu_npu_ram_hbm_replacement": False,
            "one_hundred_million_x_saving": False,
            "new_physical_law": False,
        },
    }
