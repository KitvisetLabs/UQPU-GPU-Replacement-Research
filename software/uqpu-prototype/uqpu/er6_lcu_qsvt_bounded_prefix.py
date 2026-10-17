"""Fail-closed three- and five-query ER6 QSVT prefix experiment.

Each prefix is checked first by two independent two-dimensional spectral-sector
recurrences over all 64 workload eigenvalues.  An optional pinned-Qiskit path
then compares the logical and generic-basis circuits with those sector results
and records measured host resources.  This is bounded simulation evidence, not
degree-81 synthesis, provider execution, advantage, or replacement evidence.
"""

from __future__ import annotations

import cmath
import hashlib
import json
import math
import platform
from pathlib import Path
from time import perf_counter_ns
import tracemalloc
from typing import Any

from .er6_lcu_prep_select_qiskit import (
    BASIS_GATES,
    SDK_REQUIREMENT,
    TOLERANCE,
    build_provider_neutral_contract,
    build_qiskit_block_encoding,
)
from .er6_lcu_qsvt_one_query import _append_projector_phase
from .qos_d23_phase_reconstruction_v040 import FROZEN_PHASES_V040, phase_fingerprint


CONTRACT_ID = "QOS-AUDIT-010B11"
ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "benchmarks/experiments/cycle002-delta01-er6-frozen-contract.json"
QUERY_COUNTS = (3, 5)
MAX_HOST_RUNTIME_NS = 900_000_000_000
MAX_HOST_PEAK_TRACED_BYTES = 750_000_000
MAX_SERIALIZED_OPENQASM2_BYTES = 500_000


def _sha256(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def _load_source() -> dict[str, Any]:
    return json.loads(SOURCE.read_text(encoding="utf-8"))


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
    if not -1.0 <= eigenvalue <= 1.0:
        raise ValueError("block-encoded eigenvalue must lie in [-1, 1]")
    complement = math.sqrt(max(0.0, 1.0 - eigenvalue * eigenvalue))
    return ((eigenvalue, complement), (complement, -eigenvalue))


def _phase(value: float):
    return ((cmath.exp(1j * value), 0j), (0j, cmath.exp(-1j * value)))


def explicit_prefix_matrix(eigenvalue: float, queries: int):
    if queries not in QUERY_COUNTS:
        raise ValueError(f"queries must be one of {QUERY_COUNTS}")
    phases = FROZEN_PHASES_V040[: queries + 1]
    product = _phase(phases[0])
    for index in range(1, queries + 1):
        product = _matmul2(product, _signal(eigenvalue))
        product = _matmul2(product, _phase(phases[index]))
    return product


def independent_prefix_state(eigenvalue: float, queries: int) -> tuple[complex, complex]:
    """Apply factors right-to-left to |0> without matrix-matrix recurrence."""
    if queries not in QUERY_COUNTS:
        raise ValueError(f"queries must be one of {QUERY_COUNTS}")
    phases = FROZEN_PHASES_V040[: queries + 1]
    top = cmath.exp(1j * phases[-1])
    bottom = 0j
    complement = math.sqrt(max(0.0, 1.0 - eigenvalue * eigenvalue))
    for index in range(queries - 1, -1, -1):
        top, bottom = (
            eigenvalue * top + complement * bottom,
            complement * top - eigenvalue * bottom,
        )
        top *= cmath.exp(1j * phases[index])
        bottom *= cmath.exp(-1j * phases[index])
    return top, bottom


def build_bounded_prefix_contract(frozen: dict[str, Any]) -> dict[str, Any]:
    upstream = build_provider_neutral_contract(frozen)
    eigenvalues = [float(value) for value in upstream["block_encoding"]["expected_projected_diagonal"]]
    prefixes = []
    overall_max = 0.0
    for queries in QUERY_COUNTS:
        rows = []
        for eigenvalue in sorted(set(eigenvalues)):
            matrix = explicit_prefix_matrix(eigenvalue, queries)
            state = independent_prefix_state(eigenvalue, queries)
            residual = max(abs(matrix[0][0] - state[0]), abs(matrix[1][0] - state[1]))
            overall_max = max(overall_max, residual)
            rows.append({
                "normalized_eigenvalue": eigenvalue,
                "projected_amplitude": [matrix[0][0].real, matrix[0][0].imag],
                "leakage_amplitude": [matrix[1][0].real, matrix[1][0].imag],
                "matrix_vs_state_max_abs_residual": residual,
            })
        prefixes.append({
            "queries": queries,
            "projector_phases": queries + 1,
            "selected_phase_indices": list(range(queries + 1)),
            "unique_eigenvalues_checked": len(rows),
            "rows": rows,
        })
    contract = {
        "schema": "uqpu-er6-lcu-qsvt-bounded-prefix-v1",
        "work_id": CONTRACT_ID,
        "upstream_work_id": "QOS-AUDIT-010B10",
        "upstream_prep_select_sha256": upstream["contract_sha256"],
        "phase_source": {
            "phase_count": len(FROZEN_PHASES_V040),
            "phase_fingerprint": phase_fingerprint(),
        },
        "workload_sectors": len(eigenvalues),
        "workload_eigenvalues": eigenvalues,
        "prefixes": prefixes,
        "acceptance": {
            "matrix_vs_state_max_abs_residual": overall_max,
            "tolerance": TOLERANCE,
            "max_host_runtime_ns_per_prefix": MAX_HOST_RUNTIME_NS,
            "max_host_peak_traced_bytes_per_prefix": MAX_HOST_PEAK_TRACED_BYTES,
            "max_serialized_openqasm2_bytes_per_prefix": MAX_SERIALIZED_OPENQASM2_BYTES,
            "stop_on_failure": True,
            "passed": overall_max <= TOLERANCE,
        },
        "authorization": {"provider_submission": False, "paid_execution": False},
        "evidence_class": "SIMULATION_BOUNDED_PREFIX_CONTRACT",
        "nonclaims": [
            "not full degree-81 synthesis or accepted transformed-workload output",
            "not target-aware transpilation or provider execution",
            "not fault-tolerant, energy, cost, advantage, or replacement evidence",
        ],
    }
    contract["contract_sha256"] = _sha256(contract)
    return contract


def validate_bounded_prefix_contract(contract: dict[str, Any]) -> list[str]:
    errors = []
    if contract.get("work_id") != CONTRACT_ID:
        errors.append("work_id_mismatch")
    if contract.get("phase_source", {}).get("phase_fingerprint") != phase_fingerprint():
        errors.append("phase_fingerprint_mismatch")
    prefixes = contract.get("prefixes", [])
    if [item.get("queries") for item in prefixes] != list(QUERY_COUNTS):
        errors.append("query_ladder_mismatch")
    if contract.get("workload_sectors") != 64 or len(contract.get("workload_eigenvalues", [])) != 64:
        errors.append("sector_coverage_mismatch")
    for item in prefixes:
        queries = item.get("queries")
        rows = item.get("rows", [])
        if len(rows) != 7 or item.get("unique_eigenvalues_checked") != 7:
            errors.append(f"unique_spectrum_mismatch_{queries}")
        if item.get("projector_phases") != queries + 1:
            errors.append(f"phase_count_mismatch_{queries}")
    acceptance = contract.get("acceptance", {})
    if acceptance.get("passed") is not True:
        errors.append("acceptance_failed")
    if acceptance.get("stop_on_failure") is not True:
        errors.append("stop_on_failure_missing")
    auth = contract.get("authorization", {})
    if auth.get("provider_submission") is not False or auth.get("paid_execution") is not False:
        errors.append("authorization_must_fail_closed")
    digest = contract.get("contract_sha256")
    body = {key: value for key, value in contract.items() if key != "contract_sha256"}
    if digest != _sha256(body):
        errors.append("contract_digest_mismatch")
    return sorted(set(errors))


def build_qiskit_prefix_circuit(queries: int, frozen: dict[str, Any] | None = None):
    from qiskit import QuantumCircuit

    if queries not in QUERY_COUNTS:
        raise ValueError(f"queries must be one of {QUERY_COUNTS}")
    phases = FROZEN_PHASES_V040[: queries + 1]
    circuit = QuantumCircuit(10, name=f"{CONTRACT_ID}-{queries}q")
    select = list(range(4))
    _append_projector_phase(circuit, phases[-1], select)
    block = build_qiskit_block_encoding(frozen)
    for index in range(queries - 1, -1, -1):
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
    frozen = _load_source()
    contract = build_bounded_prefix_contract(frozen)
    indices = np.asarray([system_index << 4 for system_index in range(64)])
    prefix_results = []
    all_passed = True
    for prefix in contract["prefixes"]:
        queries = prefix["queries"]
        expected = np.asarray([
            explicit_prefix_matrix(float(eigenvalue), queries)[0][0]
            for eigenvalue in contract["workload_eigenvalues"]
        ])
        tracemalloc.start()
        started = perf_counter_ns()
        circuit = build_qiskit_prefix_circuit(queries)
        logical = Operator(circuit).data[np.ix_(indices, indices)]
        logical_diagonal_residual = float(np.max(np.abs(np.diag(logical) - expected)))
        logical_offdiagonal_residual = float(np.max(np.abs(logical - np.diag(np.diag(logical)))))
        decomposed = transpile(
            circuit,
            basis_gates=list(BASIS_GATES),
            optimization_level=0,
            seed_transpiler=812,
        )
        decomposed_projected = Operator(decomposed).data[np.ix_(indices, indices)]
        decomposed_diagonal_residual = float(
            np.max(np.abs(np.diag(decomposed_projected) - expected))
        )
        decomposed_offdiagonal_residual = float(
            np.max(np.abs(decomposed_projected - np.diag(np.diag(decomposed_projected))))
        )
        serialized = qasm2.dumps(decomposed)
        runtime_ns = perf_counter_ns() - started
        _, peak_bytes = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        counts = {str(key): int(value) for key, value in decomposed.count_ops().items()}
        residuals = (
            logical_diagonal_residual,
            logical_offdiagonal_residual,
            decomposed_diagonal_residual,
            decomposed_offdiagonal_residual,
        )
        resource_gate = (
            runtime_ns <= MAX_HOST_RUNTIME_NS
            and peak_bytes <= MAX_HOST_PEAK_TRACED_BYTES
            and len(serialized.encode("utf-8")) <= MAX_SERIALIZED_OPENQASM2_BYTES
        )
        passed = max(residuals) <= TOLERANCE and set(counts).issubset(BASIS_GATES) and resource_gate
        all_passed = all_passed and passed
        prefix_results.append({
            "queries": queries,
            "workload_sectors_checked": 64,
            "agreement": {
                "logical_projected_diagonal_vs_2x2_max_abs_residual": logical_diagonal_residual,
                "logical_projected_offdiagonal_max_abs_residual": logical_offdiagonal_residual,
                "decomposed_projected_diagonal_vs_2x2_max_abs_residual": decomposed_diagonal_residual,
                "decomposed_projected_offdiagonal_max_abs_residual": decomposed_offdiagonal_residual,
                "tolerance": TOLERANCE,
            },
            "resources": {
                "logical_qubits": circuit.num_qubits,
                "logical_block_queries": queries,
                "logical_projector_phases": queries + 1,
                "logical_depth": int(circuit.depth()),
                "logical_size": int(circuit.size()),
                "decomposed_operation_counts": counts,
                "decomposed_depth": int(decomposed.depth()),
                "decomposed_size": int(decomposed.size()),
                "serialized_openqasm2_bytes": len(serialized.encode("utf-8")),
                "host_runtime_ns": runtime_ns,
                "host_peak_traced_bytes": peak_bytes,
                "shots": 0,
                "provider_jobs": 0,
                "provider_execution_id": None,
                "provider_cost": None,
                "energy_j": None,
            },
            "resource_gate_passed": resource_gate,
            "passed": passed,
        })
        if not passed:
            break
    return {
        "schema": "uqpu-er6-lcu-qsvt-bounded-prefix-qiskit-v1",
        "work_id": CONTRACT_ID,
        "contract_sha256": contract["contract_sha256"],
        "sdk": {"name": "qiskit", "version": qiskit.__version__, "requirement": SDK_REQUIREMENT},
        "environment": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
        },
        "prefix_results": prefix_results,
        "passed": all_passed and len(prefix_results) == len(QUERY_COUNTS),
        "evidence_class": "SIMULATION_INDEPENDENT_SDK_BOUNDED_PREFIX_CHECK",
        "limitations": contract["nonclaims"] + [
            "The sector reference reuses the verified ER6 eigenvalue contract.",
            "Generic basis decomposition is not a backend target, schedule, calibration, or bill.",
            "Host runtime and traced memory are CI-environment measurements only.",
        ],
    }


def dumps_reproduction() -> str:
    return json.dumps(reproduce_with_qiskit(), indent=2, sort_keys=True)
