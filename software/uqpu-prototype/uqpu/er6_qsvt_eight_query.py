"""Execute the preregistered eight-query ER6 QSVT prefix.

The experiment is bound to QOS-AUDIT-010B12 before execution.  A model-growth
rejection is retained as a valid negative result; residual, absolute-resource,
authorization, or basis-gate failures stop acceptance.  This remains generic
independent-SDK simulation, not target or real-QPU evidence.
"""

from __future__ import annotations

import cmath
import json
from pathlib import Path
import platform
from time import perf_counter_ns
import tracemalloc
from typing import Any

from .er6_lcu_prep_select_qiskit import BASIS_GATES, SDK_REQUIREMENT, build_qiskit_block_encoding
from .er6_lcu_qsvt_one_query import _append_projector_phase
from .er6_qsvt_prefix_growth_falsifier import (
    NEXT_QUERY_COUNT,
    ROOT,
    evaluate_eight_query_result,
    validate_preregistration,
)
from .qos_d23_phase_reconstruction_v040 import FROZEN_PHASES_V040


WORK_ID = "QOS-AUDIT-010B13"
PREREGISTRATION = ROOT / "benchmarks/results/cycle008-delta11-er6-qsvt-prefix-growth-preregistration.json"


def _matmul2(left, right):
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def _signal(eigenvalue: float):
    complement = max(0.0, 1.0 - eigenvalue * eigenvalue) ** 0.5
    return ((eigenvalue, complement), (complement, -eigenvalue))


def _phase(value: float):
    return ((cmath.exp(1j * value), 0j), (0j, cmath.exp(-1j * value)))


def explicit_eight_query_matrix(eigenvalue: float):
    if not -1.0 <= eigenvalue <= 1.0:
        raise ValueError("block-encoded eigenvalue must lie in [-1, 1]")
    phases = FROZEN_PHASES_V040[: NEXT_QUERY_COUNT + 1]
    product = _phase(phases[0])
    for index in range(1, NEXT_QUERY_COUNT + 1):
        product = _matmul2(product, _signal(eigenvalue))
        product = _matmul2(product, _phase(phases[index]))
    return product


def independent_eight_query_state(eigenvalue: float) -> tuple[complex, complex]:
    phases = FROZEN_PHASES_V040[: NEXT_QUERY_COUNT + 1]
    top = cmath.exp(1j * phases[-1])
    bottom = 0j
    complement = max(0.0, 1.0 - eigenvalue * eigenvalue) ** 0.5
    for index in range(NEXT_QUERY_COUNT - 1, -1, -1):
        top, bottom = (
            eigenvalue * top + complement * bottom,
            complement * top - eigenvalue * bottom,
        )
        top *= cmath.exp(1j * phases[index])
        bottom *= cmath.exp(-1j * phases[index])
    return top, bottom


def build_eight_query_circuit():
    from qiskit import QuantumCircuit

    phases = FROZEN_PHASES_V040[: NEXT_QUERY_COUNT + 1]
    circuit = QuantumCircuit(10, name=f"{WORK_ID}-8q")
    select = list(range(4))
    _append_projector_phase(circuit, phases[-1], select)
    block = build_qiskit_block_encoding()
    for index in range(NEXT_QUERY_COUNT - 1, -1, -1):
        circuit.compose(block, inplace=True)
        _append_projector_phase(circuit, phases[index], select)
    return circuit


def reproduce_with_qiskit() -> dict[str, Any]:
    import numpy as np
    import qiskit
    from qiskit import qasm2, transpile
    from qiskit.quantum_info import Operator

    if qiskit.__version__ != "2.5.2":
        raise RuntimeError(f"expected {SDK_REQUIREMENT}, got qiskit=={qiskit.__version__}")
    preregistration = json.loads(PREREGISTRATION.read_text(encoding="utf-8"))
    errors = validate_preregistration(preregistration)
    if errors:
        raise RuntimeError(f"invalid preregistration: {errors}")
    # The full 64-sector sequence is frozen in the upstream measured contract.
    bounded = json.loads(
        (ROOT / "benchmarks/results/cycle008-delta10-er6-lcu-qsvt-bounded-prefix-contract.json")
        .read_text(encoding="utf-8")
    )
    eigenvalues = [float(value) for value in bounded["workload_eigenvalues"]]
    expected = np.asarray([explicit_eight_query_matrix(value)[0][0] for value in eigenvalues])
    recurrence_residual = max(
        max(
            abs(explicit_eight_query_matrix(value)[0][0] - independent_eight_query_state(value)[0]),
            abs(explicit_eight_query_matrix(value)[1][0] - independent_eight_query_state(value)[1]),
        )
        for value in sorted(set(eigenvalues))
    )
    indices = np.asarray([system_index << 4 for system_index in range(64)])
    tracemalloc.start()
    started = perf_counter_ns()
    circuit = build_eight_query_circuit()
    logical = Operator(circuit).data[np.ix_(indices, indices)]
    logical_diag = float(np.max(np.abs(np.diag(logical) - expected)))
    logical_offdiag = float(np.max(np.abs(logical - np.diag(np.diag(logical)))))
    decomposed = transpile(
        circuit,
        basis_gates=list(BASIS_GATES),
        optimization_level=0,
        seed_transpiler=812,
    )
    projected = Operator(decomposed).data[np.ix_(indices, indices)]
    decomposed_diag = float(np.max(np.abs(np.diag(projected) - expected)))
    decomposed_offdiag = float(np.max(np.abs(projected - np.diag(np.diag(projected)))))
    serialized = qasm2.dumps(decomposed)
    runtime_ns = perf_counter_ns() - started
    _, peak_bytes = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    counts = {str(key): int(value) for key, value in decomposed.count_ops().items()}
    max_raw_residual = max(
        recurrence_residual,
        logical_diag,
        logical_offdiag,
        decomposed_diag,
        decomposed_offdiag,
    )
    flat_result = {
        "queries": NEXT_QUERY_COUNT,
        "decomposed_depth": int(decomposed.depth()),
        "decomposed_size": int(decomposed.size()),
        "serialized_openqasm2_bytes": len(serialized.encode("utf-8")),
        "host_runtime_ns": runtime_ns,
        "host_peak_traced_bytes": peak_bytes,
        "cx": counts.get("cx", 0),
        "rz": counts.get("rz", 0),
        "sx": counts.get("sx", 0),
        "x": counts.get("x", 0),
        "max_raw_residual": max_raw_residual,
        "provider_jobs": 0,
        "shots": 0,
    }
    evaluation = evaluate_eight_query_result(preregistration, flat_result)
    basis_passed = set(counts).issubset(BASIS_GATES)
    passed = evaluation["experiment_accepted"] and basis_passed
    return {
        "schema": "uqpu-er6-qsvt-eight-query-qiskit-v1",
        "work_id": WORK_ID,
        "upstream_work_id": preregistration["work_id"],
        "preregistration_sha256": preregistration["contract_sha256"],
        "evidence_class": "SIMULATION_INDEPENDENT_SDK_BOUNDED_PREFIX_CHECK",
        "sdk": {"name": "qiskit", "requirement": SDK_REQUIREMENT, "version": qiskit.__version__},
        "environment": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
        },
        "agreement": {
            "matrix_vs_state_max_abs_residual": recurrence_residual,
            "logical_projected_diagonal_max_abs_residual": logical_diag,
            "logical_projected_offdiagonal_max_abs_residual": logical_offdiag,
            "decomposed_projected_diagonal_max_abs_residual": decomposed_diag,
            "decomposed_projected_offdiagonal_max_abs_residual": decomposed_offdiag,
            "tolerance": preregistration["acceptance"]["raw_residual_tolerance"],
        },
        "resources": {
            **flat_result,
            "logical_qubits": circuit.num_qubits,
            "logical_depth": int(circuit.depth()),
            "logical_size": int(circuit.size()),
            "logical_projector_phases": NEXT_QUERY_COUNT + 1,
            "decomposed_operation_counts": counts,
            "provider_cost": None,
            "provider_execution_id": None,
            "energy_j": None,
        },
        "growth_evaluation": evaluation,
        "basis_gate_check_passed": basis_passed,
        "passed": passed,
        "limitations": preregistration["nonclaims"] + [
            "generic basis decomposition is not a dated backend target or calibrated schedule",
            "a passing eight-query prefix does not authorize degree-81 synthesis or provider execution",
        ],
    }

