"""Pinned-Qiskit reproduction of the bounded QOS-AUDIT-010B4 fixture.

This is an independent SDK/operator and serialization check for RG-033.  The
two-qubit dense block encoding is supplied as a unitary instruction and then
decomposed into a declared generic basis.  It is not a scalable block-encoding
construction, target transpilation, provider execution, or economic result.
"""

from __future__ import annotations

import json
import platform
import sys
from time import perf_counter_ns
import tracemalloc

from .qos_d23_phase_reconstruction_v040 import FROZEN_PHASES_V040
from .qos_d23_qsvt_matrix_fixture import (
    TRANSFORM_TOLERANCE,
    fixture_block_encoding,
    target_transformed_matrix,
    transformed_unitary,
)


CONTRACT_ID = "QOS-AUDIT-010B5"
BASIS_GATES = ("rz", "sx", "x", "cx")
SDK_REQUIREMENT = "qiskit==2.5.2"


def _array(matrix):
    import numpy as np

    return np.asarray(matrix, dtype=complex)


def build_qiskit_fixture_circuit(phases=FROZEN_PHASES_V040):
    """Build a circuit whose operator follows the repository matrix order."""
    if len(phases) != 82:
        raise ValueError("the frozen contract requires exactly 82 phases")
    from qiskit import QuantumCircuit
    from qiskit.circuit.library import UnitaryGate

    circuit = QuantumCircuit(2, name=CONTRACT_ID)
    signal = UnitaryGate(_array(fixture_block_encoding()), label="U_A")

    # Qiskit composes appended instructions from right to left.  Appending the
    # mathematical sequence in reverse realizes P0 U_A P1 ... U_A P81.
    circuit.rz(-2.0 * phases[-1], 1)
    for phase in reversed(phases[:-1]):
        circuit.append(signal, [0, 1])
        circuit.rz(-2.0 * phase, 1)
    return circuit


def _max_residual(left, right) -> float:
    import numpy as np

    return float(np.max(np.abs(left - right)))


def reproduce_with_qiskit() -> dict:
    """Run the pinned-SDK operator/decomposition/serialization certificate."""
    import qiskit
    from qiskit import qasm2, transpile
    from qiskit.quantum_info import Operator

    if qiskit.__version__ != "2.5.2":
        raise RuntimeError(f"expected {SDK_REQUIREMENT}, got qiskit=={qiskit.__version__}")

    tracemalloc.start()
    started = perf_counter_ns()
    circuit = build_qiskit_fixture_circuit()
    sdk_operator = Operator(circuit).data
    repository_operator = _array(transformed_unitary())
    target = _array(target_transformed_matrix())
    operator_residual = _max_residual(sdk_operator, repository_operator)
    projected_real_residual = _max_residual(sdk_operator[:2, :2].real, target.real)

    decomposed = transpile(
        circuit,
        basis_gates=list(BASIS_GATES),
        optimization_level=0,
        seed_transpiler=808,
    )
    decomposed_operator_residual = _max_residual(
        Operator(decomposed).data,
        repository_operator,
    )
    qasm = qasm2.dumps(decomposed)
    runtime_ns = perf_counter_ns() - started
    _, peak_bytes = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    operation_counts = {str(key): int(value) for key, value in decomposed.count_ops().items()}
    passed = (
        operator_residual <= TRANSFORM_TOLERANCE
        and projected_real_residual <= TRANSFORM_TOLERANCE
        and decomposed_operator_residual <= TRANSFORM_TOLERANCE
        and set(operation_counts).issubset(BASIS_GATES)
    )
    return {
        "schema": "uqpu-qos-audit-010b5-qiskit-reproduction-v1",
        "contract_id": CONTRACT_ID,
        "upstream_contract_id": "QOS-AUDIT-010B4",
        "sdk": {"name": "qiskit", "version": qiskit.__version__, "requirement": SDK_REQUIREMENT},
        "environment": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
        },
        "operator_agreement": {
            "repository_vs_qiskit_max_abs_residual": operator_residual,
            "projected_real_block_vs_target_max_abs_residual": projected_real_residual,
            "decomposed_vs_repository_max_abs_residual": decomposed_operator_residual,
            "tolerance": TRANSFORM_TOLERANCE,
        },
        "resources": {
            "logical_qubits": circuit.num_qubits,
            "dense_signal_instructions": 81,
            "phase_rotations": 82,
            "basis_gates": list(BASIS_GATES),
            "decomposed_operation_counts": operation_counts,
            "decomposed_depth": int(decomposed.depth()),
            "decomposed_size": int(decomposed.size()),
            "serialized_openqasm2_bytes": len(qasm.encode("utf-8")),
            "host_runtime_ns": runtime_ns,
            "host_peak_traced_bytes": peak_bytes,
            "shots": 0,
            "provider_jobs": 0,
            "provider_execution_id": None,
            "provider_cost": None,
            "energy_j": None,
        },
        "passed": passed,
        "evidence_label": "SIMULATION_INDEPENDENT_SDK_CHECK",
        "limitations": [
            "The dense two-qubit signal unitary is an input instruction, not a scalable block-encoding construction.",
            "Generic-basis decomposition is not target-aware routing, scheduling, calibration, or execution.",
            "Host runtime and traced Python memory are workflow-environment measurements, not QPU resources.",
            "No provider job, shot, bill, energy measurement, quantum advantage, or replacement claim.",
        ],
    }


def dumps_reproduction() -> str:
    return json.dumps(reproduce_with_qiskit(), indent=2, sort_keys=True)
