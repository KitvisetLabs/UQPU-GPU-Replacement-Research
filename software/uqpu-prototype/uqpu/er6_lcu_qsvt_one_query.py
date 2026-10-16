"""One-query ER6 LCU composition with the frozen QSVT phase convention.

This module checks the bounded fragment ``P(phi_0) U_ER6 P(phi_1)`` where
``P(phi) = exp(i phi (2 Pi - I))`` and ``Pi`` projects all four select
qubits onto zero.  It intentionally does not synthesize or estimate the full
degree-81 sequence.
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

from .er6_lcu_prep_select_qiskit import (
    BASIS_GATES,
    SDK_REQUIREMENT,
    TOLERANCE,
    build_provider_neutral_contract as build_prep_select_contract,
    build_qiskit_block_encoding,
)
from .qos_d23_phase_reconstruction_v040 import (
    FROZEN_PHASES_V040,
    phase_fingerprint,
)


CONTRACT_ID = "QOS-AUDIT-010B8"
ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "benchmarks/experiments/cycle002-delta01-er6-frozen-contract.json"
PHASE_INDICES = (0, 1)


def _sha256(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def _load_source() -> dict[str, Any]:
    return json.loads(SOURCE.read_text(encoding="utf-8"))


def build_one_query_contract(frozen: dict[str, Any]) -> dict[str, Any]:
    upstream = build_prep_select_contract(frozen)
    phase_left = FROZEN_PHASES_V040[PHASE_INDICES[0]]
    phase_right = FROZEN_PHASES_V040[PHASE_INDICES[1]]
    contract = {
        "schema": "uqpu-er6-lcu-qsvt-one-query-v1",
        "work_id": CONTRACT_ID,
        "upstream_work_id": upstream["work_id"],
        "upstream_contract_sha256": upstream["contract_sha256"],
        "phase_source": {
            "work_id": "QOS-AUDIT-010B3",
            "phase_count": len(FROZEN_PHASES_V040),
            "phase_fingerprint": phase_fingerprint(),
            "selected_indices": list(PHASE_INDICES),
            "selected_values": [phase_left, phase_right],
        },
        "projector_phase": {
            "select_qubits": 4,
            "projector": "Pi=|0000><0000| tensor I_system",
            "definition": "P(phi)=exp(i*phi*(2*Pi-I))",
            "projected_eigenvalue": "exp(+i*phi)",
            "complement_eigenvalue": "exp(-i*phi)",
        },
        "composition": {
            "mathematical_order": ["P(phi_0)", "U_ER6", "P(phi_1)"],
            "block_queries": 1,
            "projector_phases": 2,
            "expected_projected_scalar": {
                "real": math.cos(phase_left + phase_right),
                "imag": math.sin(phase_left + phase_right),
            },
            "expected_projected_diagonal": upstream["block_encoding"][
                "expected_projected_diagonal"
            ],
        },
        "authorization": {"provider_submission": False, "paid_execution": False},
        "evidence_class": "SIMULATION_PROVIDER_NEUTRAL_ONE_QUERY_CONTRACT",
        "nonclaims": [
            "not a full degree-81 QSVT circuit",
            "not proof that the frozen scalar convention transfers beyond this bounded fragment",
            "not target-aware transpilation or provider execution",
            "not fault-tolerant, energy, cost, advantage, or replacement evidence",
        ],
    }
    contract["contract_sha256"] = _sha256(contract)
    return contract


def validate_one_query_contract(contract: dict[str, Any]) -> list[str]:
    errors = []
    if contract.get("work_id") != CONTRACT_ID:
        errors.append("work_id_mismatch")
    phase_source = contract.get("phase_source", {})
    if phase_source.get("phase_count") != 82:
        errors.append("phase_count_mismatch")
    if phase_source.get("phase_fingerprint") != phase_fingerprint():
        errors.append("phase_fingerprint_mismatch")
    if phase_source.get("selected_indices") != [0, 1]:
        errors.append("phase_indices_mismatch")
    if contract.get("composition", {}).get("block_queries") != 1:
        errors.append("query_count_mismatch")
    auth = contract.get("authorization", {})
    if auth.get("provider_submission") is not False or auth.get("paid_execution") is not False:
        errors.append("authorization_must_fail_closed")
    digest = contract.get("contract_sha256")
    body = {key: value for key, value in contract.items() if key != "contract_sha256"}
    if digest != _sha256(body):
        errors.append("contract_digest_mismatch")
    return sorted(set(errors))


def _append_projector_phase(circuit, phase: float, select: list[int]) -> None:
    """Append exp(i phi (2 Pi-I)) with Pi selecting the all-zero address."""
    from qiskit.circuit.library import MCPhaseGate

    for qubit in select:
        circuit.x(qubit)
    circuit.append(MCPhaseGate(2.0 * phase, num_ctrl_qubits=len(select) - 1), select)
    for qubit in reversed(select):
        circuit.x(qubit)
    circuit.global_phase -= phase


def build_qiskit_one_query_circuit(frozen: dict[str, Any] | None = None):
    """Build P(phi_0) U_ER6 P(phi_1) without provider/backend surfaces."""
    from qiskit import QuantumCircuit

    phases = [FROZEN_PHASES_V040[index] for index in PHASE_INDICES]
    circuit = QuantumCircuit(10, name=CONTRACT_ID)
    select = list(range(4))
    _append_projector_phase(circuit, phases[1], select)
    circuit.compose(build_qiskit_block_encoding(frozen), inplace=True)
    _append_projector_phase(circuit, phases[0], select)
    return circuit


def _max_residual(left, right) -> float:
    import numpy as np

    return float(np.max(np.abs(left - right)))


def reproduce_with_qiskit() -> dict[str, Any]:
    import numpy as np
    import qiskit
    from qiskit import qasm2, transpile
    from qiskit.quantum_info import Operator

    if qiskit.__version__ != "2.5.2":
        raise RuntimeError(f"expected {SDK_REQUIREMENT}, got qiskit=={qiskit.__version__}")
    contract = build_one_query_contract(_load_source())
    scalar_fields = contract["composition"]["expected_projected_scalar"]
    scalar = complex(scalar_fields["real"], scalar_fields["imag"])
    expected = scalar * np.diag(np.asarray(
        contract["composition"]["expected_projected_diagonal"], dtype=complex
    ))

    tracemalloc.start()
    started = perf_counter_ns()
    circuit = build_qiskit_one_query_circuit()
    operator = Operator(circuit).data
    indices = np.asarray([system_index << 4 for system_index in range(64)])
    projected = operator[np.ix_(indices, indices)]
    projected_residual = _max_residual(projected, expected)

    decomposed = transpile(
        circuit,
        basis_gates=list(BASIS_GATES),
        optimization_level=0,
        seed_transpiler=811,
    )
    decomposed_operator = Operator(decomposed).data
    decomposed_projected = decomposed_operator[np.ix_(indices, indices)]
    decomposed_projected_residual = _max_residual(decomposed_projected, expected)
    full_operator_residual = _max_residual(decomposed_operator, operator)
    qasm = qasm2.dumps(decomposed)
    runtime_ns = perf_counter_ns() - started
    _, peak_bytes = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    counts = {str(key): int(value) for key, value in decomposed.count_ops().items()}
    passed = (
        projected_residual <= TOLERANCE
        and decomposed_projected_residual <= TOLERANCE
        and full_operator_residual <= TOLERANCE
        and set(counts).issubset(BASIS_GATES)
    )
    return {
        "schema": "uqpu-er6-lcu-qsvt-one-query-qiskit-v1",
        "work_id": CONTRACT_ID,
        "contract_sha256": contract["contract_sha256"],
        "sdk": {"name": "qiskit", "version": qiskit.__version__, "requirement": SDK_REQUIREMENT},
        "environment": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
        },
        "operator_agreement": {
            "projected_fragment_max_abs_residual": projected_residual,
            "decomposed_projected_fragment_max_abs_residual": decomposed_projected_residual,
            "decomposed_vs_logical_full_operator_max_abs_residual": full_operator_residual,
            "tolerance": TOLERANCE,
        },
        "resources": {
            "logical_qubits": circuit.num_qubits,
            "logical_block_queries": 1,
            "logical_projector_phases": 2,
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
        "evidence_class": "SIMULATION_INDEPENDENT_SDK_ONE_QUERY_CHECK",
        "limitations": contract["nonclaims"] + [
            "Generic basis decomposition is not a backend target, schedule, calibration, or bill.",
            "Host runtime and traced memory are CI-environment measurements only.",
        ],
    }


def dumps_reproduction() -> str:
    return json.dumps(reproduce_with_qiskit(), indent=2, sort_keys=True)
