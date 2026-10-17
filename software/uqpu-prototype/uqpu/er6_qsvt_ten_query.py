"""Execute the immutable ten-query ER6 QSVT boundary contract.

This module consumes QOS-AUDIT-010B14 without changing its thresholds.  It
performs independent recurrence, 64-sector logical/decomposed checks and
resource accounting in pinned Qiskit.  The result remains generic SDK
simulation and never authorizes provider submission.
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
from .er6_qsvt_eight_query import _matmul2, _phase, _signal
from .er6_qsvt_next_boundary_preregistration import ROOT, validate_preregistration
from .qos_d23_phase_reconstruction_v040 import FROZEN_PHASES_V040


WORK_ID = "QOS-AUDIT-010B15"
QUERY_COUNT = 10
PREREGISTRATION = (
    ROOT / "benchmarks/results/cycle008-delta13-er6-qsvt-next-boundary-preregistration.json"
)


def explicit_ten_query_matrix(eigenvalue: float):
    if not -1.0 <= eigenvalue <= 1.0:
        raise ValueError("block-encoded eigenvalue must lie in [-1, 1]")
    phases = FROZEN_PHASES_V040[: QUERY_COUNT + 1]
    product = _phase(phases[0])
    for index in range(1, QUERY_COUNT + 1):
        product = _matmul2(product, _signal(eigenvalue))
        product = _matmul2(product, _phase(phases[index]))
    return product


def independent_ten_query_state(eigenvalue: float) -> tuple[complex, complex]:
    if not -1.0 <= eigenvalue <= 1.0:
        raise ValueError("block-encoded eigenvalue must lie in [-1, 1]")
    phases = FROZEN_PHASES_V040[: QUERY_COUNT + 1]
    top = cmath.exp(1j * phases[-1])
    bottom = 0j
    complement = max(0.0, 1.0 - eigenvalue * eigenvalue) ** 0.5
    for index in range(QUERY_COUNT - 1, -1, -1):
        top, bottom = (
            eigenvalue * top + complement * bottom,
            complement * top - eigenvalue * bottom,
        )
        top *= cmath.exp(1j * phases[index])
        bottom *= cmath.exp(-1j * phases[index])
    return top, bottom


def build_ten_query_circuit():
    from qiskit import QuantumCircuit

    phases = FROZEN_PHASES_V040[: QUERY_COUNT + 1]
    circuit = QuantumCircuit(10, name=f"{WORK_ID}-10q")
    select = list(range(4))
    _append_projector_phase(circuit, phases[-1], select)
    block = build_qiskit_block_encoding()
    for index in range(QUERY_COUNT - 1, -1, -1):
        circuit.compose(block, inplace=True)
        _append_projector_phase(circuit, phases[index], select)
    return circuit


def evaluate_result(contract: dict[str, Any], result: dict[str, Any]) -> dict[str, Any]:
    acceptance = contract["acceptance"]
    deterministic = acceptance["deterministic_metric_model_limits"]
    absolute = acceptance["absolute_safety_ceilings"]
    model_failures = [
        metric for metric, limit in deterministic.items() if result[metric] > limit
    ]
    absolute_failures = [
        metric for metric, limit in absolute.items() if result[metric] > limit
    ]
    residual_passed = result["max_raw_residual"] <= acceptance["raw_residual_tolerance"]
    authorization_passed = result["provider_jobs"] == 0 and result["shots"] == 0
    return {
        "deterministic_model_failures": model_failures,
        "absolute_safety_failures": absolute_failures,
        "residual_passed": residual_passed,
        "authorization_passed": authorization_passed,
        "experiment_accepted": (
            not model_failures
            and not absolute_failures
            and residual_passed
            and authorization_passed
        ),
    }


def reproduce_with_qiskit() -> dict[str, Any]:
    import numpy as np
    import qiskit
    from qiskit import qasm2, transpile
    from qiskit.quantum_info import Operator

    if qiskit.__version__ != "2.5.2":
        raise RuntimeError(f"expected {SDK_REQUIREMENT}, got qiskit=={qiskit.__version__}")
    contract = json.loads(PREREGISTRATION.read_text(encoding="utf-8"))
    errors = validate_preregistration(contract)
    if errors:
        raise RuntimeError(f"invalid preregistration: {errors}")
    if contract["selection"]["selected_query_count"] != QUERY_COUNT:
        raise RuntimeError("preregistered query count changed")

    bounded = json.loads(
        (ROOT / "benchmarks/results/cycle008-delta10-er6-lcu-qsvt-bounded-prefix-contract.json")
        .read_text(encoding="utf-8")
    )
    eigenvalues = [float(value) for value in bounded["workload_eigenvalues"]]
    expected = np.asarray([explicit_ten_query_matrix(value)[0][0] for value in eigenvalues])
    recurrence_residual = max(
        max(
            abs(explicit_ten_query_matrix(value)[0][0] - independent_ten_query_state(value)[0]),
            abs(explicit_ten_query_matrix(value)[1][0] - independent_ten_query_state(value)[1]),
        )
        for value in sorted(set(eigenvalues))
    )
    indices = np.asarray([system_index << 4 for system_index in range(64)])
    tracemalloc.start()
    started = perf_counter_ns()
    circuit = build_ten_query_circuit()
    logical = Operator(circuit).data[np.ix_(indices, indices)]
    logical_diag = float(np.max(np.abs(np.diag(logical) - expected)))
    logical_offdiag = float(np.max(np.abs(logical - np.diag(np.diag(logical)))))
    decomposed = transpile(
        circuit,
        basis_gates=list(BASIS_GATES),
        optimization_level=0,
        seed_transpiler=1015,
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
        "queries": QUERY_COUNT,
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
    evaluation = evaluate_result(contract, flat_result)
    basis_passed = set(counts).issubset(BASIS_GATES)
    passed = evaluation["experiment_accepted"] and basis_passed
    return {
        "schema": "uqpu-er6-qsvt-ten-query-qiskit-v1",
        "work_id": WORK_ID,
        "upstream_work_id": contract["work_id"],
        "preregistration_sha256": contract["contract_sha256"],
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
            "tolerance": contract["acceptance"]["raw_residual_tolerance"],
        },
        "resources": {
            **flat_result,
            "logical_qubits": circuit.num_qubits,
            "logical_depth": int(circuit.depth()),
            "logical_size": int(circuit.size()),
            "logical_projector_phases": QUERY_COUNT + 1,
            "decomposed_operation_counts": counts,
            "provider_cost": None,
            "provider_execution_id": None,
            "energy_j": None,
        },
        "evaluation": evaluation,
        "basis_gate_check_passed": basis_passed,
        "passed": passed,
        "limitations": contract["nonclaims"] + [
            "generic basis decomposition is not a dated backend target or calibrated schedule",
            "a passing ten-query prefix does not authorize degree-81 synthesis, eleven queries, or provider execution",
        ],
    }
