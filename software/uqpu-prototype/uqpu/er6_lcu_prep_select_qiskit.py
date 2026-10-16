"""Provider-neutral PREP/SELECT circuit and pinned-Qiskit check for ER6.

The contract turns QOS-AUDIT-010B6's algebraic LCU into an explicit circuit:
PREP -> SELECT -> PREP†.  It remains a generic logical circuit, not a dated
target transpilation, provider execution, fault-tolerant resource estimate, or
performance/economic claim.
"""

from __future__ import annotations

import hashlib
import json
import math
import platform
from pathlib import Path
from time import perf_counter_ns
import tracemalloc
from typing import Any

from .er6_sparse_lcu_block_encoding import build_lcu_contract


CONTRACT_ID = "QOS-AUDIT-010B7"
SDK_REQUIREMENT = "qiskit==2.5.2"
BASIS_GATES = ("rz", "sx", "x", "cx")
TOLERANCE = 2e-12
ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "benchmarks/experiments/cycle002-delta01-er6-frozen-contract.json"


def _sha256(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def _load_source() -> dict[str, Any]:
    return json.loads(SOURCE.read_text(encoding="utf-8"))


def build_provider_neutral_contract(frozen: dict[str, Any]) -> dict[str, Any]:
    upstream = build_lcu_contract(frozen)
    probabilities = upstream["operator"]["prep_probabilities"]
    padded = upstream["operator"]["padded_select_terms"]
    amplitudes = [math.sqrt(value) for value in probabilities]
    amplitudes.extend([0.0] * (padded - len(amplitudes)))
    branches = []
    for index, term in enumerate(upstream["operator"]["terms"]):
        branches.append({
            "select_index": index,
            "coefficient_sign": 1 if term["coefficient"] >= 0 else -1,
            "pauli_z_system_qubits": term["pauli_z_qubits"],
        })
    contract = {
        "schema": "uqpu-er6-lcu-prep-select-circuit-v1",
        "work_id": CONTRACT_ID,
        "upstream_work_id": upstream["work_id"],
        "upstream_contract_sha256": upstream["contract_sha256"],
        "registers": {
            "select_qubits": 4,
            "system_qubits": 6,
            "total_logical_qubits": 10,
            "select_is_little_endian": True,
            "system_is_little_endian": True,
        },
        "prep": {
            "definition": "PREP|0^4>=sum_l sqrt(|c_l|/alpha)|l>",
            "amplitudes": amplitudes,
            "amplitude_norm_residual": abs(math.fsum(a * a for a in amplitudes) - 1.0),
            "inverse_required_after_select": True,
        },
        "select": {
            "definition": "sum_l |l><l| tensor sign(c_l)P_l",
            "branches": branches,
            "padded_identity_indices": list(range(len(branches), padded)),
        },
        "block_encoding": {
            "sequence": ["PREP", "SELECT", "PREP_DAGGER"],
            "projected_select_state": 0,
            "normalization_alpha": upstream["operator"]["alpha"],
            "expected_projected_diagonal": [
                sum(((index >> u) & 1) != ((index >> v) & 1)
                    for u, v in upstream["operator"]["edges"])
                / upstream["operator"]["alpha"]
                for index in range(64)
            ],
        },
        "authorization": {"provider_submission": False, "paid_execution": False},
        "evidence_class": "SIMULATION_PROVIDER_NEUTRAL_CIRCUIT_CONTRACT",
        "nonclaims": [
            "not target-aware transpilation",
            "not provider execution",
            "not fault-tolerant resource evidence",
            "not QSVT end-to-end execution",
            "not quantum advantage or replacement evidence",
        ],
    }
    contract["contract_sha256"] = _sha256(contract)
    return contract


def validate_provider_neutral_contract(contract: dict[str, Any]) -> list[str]:
    errors = []
    if contract.get("work_id") != CONTRACT_ID:
        errors.append("work_id_mismatch")
    if contract.get("registers", {}).get("total_logical_qubits") != 10:
        errors.append("logical_qubit_count_mismatch")
    if len(contract.get("select", {}).get("branches", [])) != 10:
        errors.append("select_branch_count_mismatch")
    if contract.get("prep", {}).get("amplitude_norm_residual", 1.0) > 1e-15:
        errors.append("prep_normalization_failed")
    auth = contract.get("authorization", {})
    if auth.get("provider_submission") is not False or auth.get("paid_execution") is not False:
        errors.append("authorization_must_fail_closed")
    digest = contract.get("contract_sha256")
    body = {key: value for key, value in contract.items() if key != "contract_sha256"}
    if digest != _sha256(body):
        errors.append("contract_digest_mismatch")
    return sorted(set(errors))


def build_qiskit_block_encoding(frozen: dict[str, Any] | None = None):
    """Build PREP SELECT PREP† without provider or backend surfaces."""
    from qiskit import QuantumCircuit
    from qiskit.circuit.library import MCPhaseGate, StatePreparation, ZGate

    contract = build_provider_neutral_contract(frozen or _load_source())
    select_count = contract["registers"]["select_qubits"]
    circuit = QuantumCircuit(10, name=CONTRACT_ID)
    select = list(range(select_count))
    prep = StatePreparation(contract["prep"]["amplitudes"], normalize=False)
    circuit.append(prep, select)

    branch_phase = MCPhaseGate(math.pi, num_ctrl_qubits=select_count - 1)
    controlled_z = ZGate().control(select_count, annotated=False)
    for branch in contract["select"]["branches"]:
        if branch["coefficient_sign"] > 0 and not branch["pauli_z_system_qubits"]:
            continue
        index = branch["select_index"]
        zero_controls = [bit for bit in select if ((index >> bit) & 1) == 0]
        for bit in zero_controls:
            circuit.x(bit)
        if branch["coefficient_sign"] < 0:
            circuit.append(branch_phase, select)
        for system_qubit in branch["pauli_z_system_qubits"]:
            circuit.append(controlled_z, select + [select_count + system_qubit])
        for bit in reversed(zero_controls):
            circuit.x(bit)
    circuit.append(prep.inverse(), select)
    return circuit


def reproduce_with_qiskit() -> dict[str, Any]:
    import numpy as np
    import qiskit
    from qiskit import qasm2, transpile
    from qiskit.quantum_info import Operator

    if qiskit.__version__ != "2.5.2":
        raise RuntimeError(f"expected {SDK_REQUIREMENT}, got qiskit=={qiskit.__version__}")
    contract = build_provider_neutral_contract(_load_source())
    expected = np.diag(np.asarray(
        contract["block_encoding"]["expected_projected_diagonal"], dtype=complex
    ))

    tracemalloc.start()
    started = perf_counter_ns()
    circuit = build_qiskit_block_encoding()
    operator = Operator(circuit).data
    indices = np.asarray([system_index << 4 for system_index in range(64)])
    projected = operator[np.ix_(indices, indices)]
    projected_residual = float(np.max(np.abs(projected - expected)))

    decomposed = transpile(
        circuit,
        basis_gates=list(BASIS_GATES),
        optimization_level=0,
        seed_transpiler=810,
    )
    decomposed_operator = Operator(decomposed).data
    decomposed_projected = decomposed_operator[np.ix_(indices, indices)]
    decomposed_raw_residual = float(np.max(np.abs(decomposed_projected - expected)))
    full_operator_raw_residual = float(np.max(np.abs(decomposed_operator - operator)))
    overlap = np.vdot(operator.ravel(), decomposed_operator.ravel())
    global_phase_offset = float(np.angle(overlap))
    phase_aligned_operator = decomposed_operator * np.exp(-1j * global_phase_offset)
    phase_aligned_projected = phase_aligned_operator[np.ix_(indices, indices)]
    decomposed_phase_aligned_residual = float(
        np.max(np.abs(phase_aligned_projected - expected))
    )
    full_operator_phase_aligned_residual = float(
        np.max(np.abs(phase_aligned_operator - operator))
    )
    qasm = qasm2.dumps(decomposed)
    runtime_ns = perf_counter_ns() - started
    _, peak_bytes = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    counts = {str(key): int(value) for key, value in decomposed.count_ops().items()}
    passed = (
        projected_residual <= TOLERANCE
        and decomposed_phase_aligned_residual <= TOLERANCE
        and full_operator_phase_aligned_residual <= TOLERANCE
        and set(counts).issubset(BASIS_GATES)
    )
    return {
        "schema": "uqpu-er6-lcu-prep-select-qiskit-v1",
        "work_id": CONTRACT_ID,
        "contract_sha256": contract["contract_sha256"],
        "sdk": {"name": "qiskit", "version": qiskit.__version__, "requirement": SDK_REQUIREMENT},
        "environment": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
        },
        "operator_agreement": {
            "projected_block_max_abs_residual": projected_residual,
            "decomposed_projected_block_raw_max_abs_residual": decomposed_raw_residual,
            "decomposed_vs_logical_full_operator_raw_max_abs_residual": full_operator_raw_residual,
            "decomposition_global_phase_offset_rad": global_phase_offset,
            "decomposed_projected_block_phase_aligned_max_abs_residual": decomposed_phase_aligned_residual,
            "decomposed_vs_logical_full_operator_phase_aligned_max_abs_residual": full_operator_phase_aligned_residual,
            "tolerance": TOLERANCE,
        },
        "resources": {
            "logical_qubits": circuit.num_qubits,
            "logical_depth": int(circuit.depth()),
            "logical_size": int(circuit.size()),
            "decomposed_operation_counts": counts,
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
        "evidence_class": "SIMULATION_INDEPENDENT_SDK_CIRCUIT_CHECK",
        "limitations": contract["nonclaims"] + [
            "Generic basis decomposition is not a backend target, schedule, calibration, or bill.",
            "Raw and phase-aligned residuals are separate; controlled/QSVT composition remains blocked until the relative-phase convention is fixed.",
            "Host runtime and traced memory are CI-environment measurements only.",
        ],
    }


def dumps_reproduction() -> str:
    return json.dumps(reproduce_with_qiskit(), indent=2, sort_keys=True)
