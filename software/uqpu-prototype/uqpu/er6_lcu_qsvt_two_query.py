"""Two-query ER6 recurrence under the frozen multi-ancilla QSVT convention.

The bounded fragment is ``P(phi_0) U P(phi_1) U P(phi_2)``.  Its expected
operator is assembled as dense matrix products independently of the circuit
instruction order.  This is a convention/recurrence check, not full QSVT.
"""

from __future__ import annotations

import hashlib
import json
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
from .er6_lcu_qsvt_one_query import _append_projector_phase
from .qos_d23_phase_reconstruction_v040 import FROZEN_PHASES_V040, phase_fingerprint


CONTRACT_ID = "QOS-AUDIT-010B9"
ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "benchmarks/experiments/cycle002-delta01-er6-frozen-contract.json"
PHASE_INDICES = (0, 1, 2)


def _sha256(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def _load_source() -> dict[str, Any]:
    return json.loads(SOURCE.read_text(encoding="utf-8"))


def build_two_query_contract(frozen: dict[str, Any]) -> dict[str, Any]:
    upstream = build_prep_select_contract(frozen)
    contract = {
        "schema": "uqpu-er6-lcu-qsvt-two-query-v1",
        "work_id": CONTRACT_ID,
        "upstream_work_id": "QOS-AUDIT-010B8",
        "upstream_prep_select_sha256": upstream["contract_sha256"],
        "phase_source": {
            "work_id": "QOS-AUDIT-010B3",
            "phase_count": len(FROZEN_PHASES_V040),
            "phase_fingerprint": phase_fingerprint(),
            "selected_indices": list(PHASE_INDICES),
            "selected_values": [FROZEN_PHASES_V040[index] for index in PHASE_INDICES],
        },
        "projector_phase": {
            "select_qubits": 4,
            "projector": "Pi=|0000><0000| tensor I_system",
            "definition": "P(phi)=exp(i*phi*(2*Pi-I))",
        },
        "composition": {
            "mathematical_order": [
                "P(phi_0)", "U_ER6", "P(phi_1)", "U_ER6", "P(phi_2)"
            ],
            "block_queries": 2,
            "projector_phases": 3,
            "independent_reference": "dense diagonal row/column scaling and two matrix products",
        },
        "authorization": {"provider_submission": False, "paid_execution": False},
        "evidence_class": "SIMULATION_PROVIDER_NEUTRAL_TWO_QUERY_CONTRACT",
        "nonclaims": [
            "not a full degree-81 QSVT circuit or transformed-workload result",
            "not target-aware transpilation or provider execution",
            "not fault-tolerant, energy, cost, advantage, or replacement evidence",
        ],
    }
    contract["contract_sha256"] = _sha256(contract)
    return contract


def validate_two_query_contract(contract: dict[str, Any]) -> list[str]:
    errors = []
    if contract.get("work_id") != CONTRACT_ID:
        errors.append("work_id_mismatch")
    phase_source = contract.get("phase_source", {})
    if phase_source.get("phase_count") != 82:
        errors.append("phase_count_mismatch")
    if phase_source.get("phase_fingerprint") != phase_fingerprint():
        errors.append("phase_fingerprint_mismatch")
    if phase_source.get("selected_indices") != [0, 1, 2]:
        errors.append("phase_indices_mismatch")
    composition = contract.get("composition", {})
    if composition.get("block_queries") != 2 or composition.get("projector_phases") != 3:
        errors.append("recurrence_count_mismatch")
    auth = contract.get("authorization", {})
    if auth.get("provider_submission") is not False or auth.get("paid_execution") is not False:
        errors.append("authorization_must_fail_closed")
    digest = contract.get("contract_sha256")
    body = {key: value for key, value in contract.items() if key != "contract_sha256"}
    if digest != _sha256(body):
        errors.append("contract_digest_mismatch")
    return sorted(set(errors))


def build_qiskit_two_query_circuit(frozen: dict[str, Any] | None = None):
    from qiskit import QuantumCircuit

    phases = [FROZEN_PHASES_V040[index] for index in PHASE_INDICES]
    circuit = QuantumCircuit(10, name=CONTRACT_ID)
    select = list(range(4))
    # Circuit instructions act from right to left in the matrix product.
    _append_projector_phase(circuit, phases[2], select)
    block = build_qiskit_block_encoding(frozen)
    circuit.compose(block, inplace=True)
    _append_projector_phase(circuit, phases[1], select)
    circuit.compose(block, inplace=True)
    _append_projector_phase(circuit, phases[0], select)
    return circuit


def _projector_phase_diagonal(phase: float):
    """Independent dense diagonal for P(phi), using Qiskit little-endian indices."""
    import numpy as np

    indices = np.arange(1 << 10, dtype=np.int64)
    projected = (indices & 0xF) == 0
    return np.where(projected, np.exp(1j * phase), np.exp(-1j * phase))


def independently_assembled_operator(block_operator):
    """Assemble P0 U P1 U P2 without using the composed circuit builder."""
    import numpy as np

    u = np.asarray(block_operator, dtype=complex)
    if u.shape != (1024, 1024):
        raise ValueError("expected a 1024x1024 ten-qubit block operator")
    p0, p1, p2 = (
        _projector_phase_diagonal(FROZEN_PHASES_V040[index]) for index in PHASE_INDICES
    )
    right = u * p2[None, :]
    middle = u @ (p1[:, None] * right)
    return p0[:, None] * middle


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
    contract = build_two_query_contract(_load_source())
    from .er6_lcu_qsvt_spectral_sector import (
        CONTRACT_ID as SPECTRAL_CONTRACT_ID,
        build_spectral_sector_contract,
        spectral_sector_amplitudes,
    )
    spectral_contract = build_spectral_sector_contract(_load_source())
    tracemalloc.start()
    started = perf_counter_ns()

    primitive = Operator(build_qiskit_block_encoding()).data
    expected = independently_assembled_operator(primitive)
    circuit = build_qiskit_two_query_circuit()
    logical = Operator(circuit).data
    full_logical_residual = _max_residual(logical, expected)
    indices = np.asarray([system_index << 4 for system_index in range(64)])
    logical_projected = logical[np.ix_(indices, indices)]
    projected_residual = _max_residual(
        logical_projected, expected[np.ix_(indices, indices)]
    )
    sector_amplitudes = np.asarray(spectral_sector_amplitudes(_load_source()))
    logical_sector_diagonal_residual = _max_residual(
        np.diag(logical_projected), sector_amplitudes
    )
    logical_sector_offdiagonal_residual = _max_residual(
        logical_projected, np.diag(np.diag(logical_projected))
    )

    decomposed = transpile(
        circuit,
        basis_gates=list(BASIS_GATES),
        optimization_level=0,
        seed_transpiler=812,
    )
    decomposed_operator = Operator(decomposed).data
    decomposed_full_residual = _max_residual(decomposed_operator, expected)
    decomposed_projected_residual = _max_residual(
        decomposed_operator[np.ix_(indices, indices)], expected[np.ix_(indices, indices)]
    )
    decomposed_projected = decomposed_operator[np.ix_(indices, indices)]
    decomposed_sector_diagonal_residual = _max_residual(
        np.diag(decomposed_projected), sector_amplitudes
    )
    decomposed_sector_offdiagonal_residual = _max_residual(
        decomposed_projected, np.diag(np.diag(decomposed_projected))
    )
    qasm = qasm2.dumps(decomposed)
    runtime_ns = perf_counter_ns() - started
    _, peak_bytes = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    counts = {str(key): int(value) for key, value in decomposed.count_ops().items()}
    passed = (
        full_logical_residual <= TOLERANCE
        and projected_residual <= TOLERANCE
        and decomposed_full_residual <= TOLERANCE
        and decomposed_projected_residual <= TOLERANCE
        and logical_sector_diagonal_residual <= TOLERANCE
        and logical_sector_offdiagonal_residual <= TOLERANCE
        and decomposed_sector_diagonal_residual <= TOLERANCE
        and decomposed_sector_offdiagonal_residual <= TOLERANCE
        and set(counts).issubset(BASIS_GATES)
    )
    return {
        "schema": "uqpu-er6-lcu-qsvt-two-query-qiskit-v1",
        "work_id": CONTRACT_ID,
        "contract_sha256": contract["contract_sha256"],
        "sdk": {"name": "qiskit", "version": qiskit.__version__, "requirement": SDK_REQUIREMENT},
        "environment": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
        },
        "operator_agreement": {
            "logical_vs_independent_full_max_abs_residual": full_logical_residual,
            "logical_vs_independent_projected_max_abs_residual": projected_residual,
            "decomposed_vs_independent_full_max_abs_residual": decomposed_full_residual,
            "decomposed_vs_independent_projected_max_abs_residual": decomposed_projected_residual,
            "tolerance": TOLERANCE,
        },
        "spectral_sector_agreement": {
            "work_id": SPECTRAL_CONTRACT_ID,
            "contract_sha256": spectral_contract["contract_sha256"],
            "workload_sectors_checked": 64,
            "logical_projected_diagonal_vs_2x2_max_abs_residual": logical_sector_diagonal_residual,
            "logical_projected_offdiagonal_max_abs_residual": logical_sector_offdiagonal_residual,
            "decomposed_projected_diagonal_vs_2x2_max_abs_residual": decomposed_sector_diagonal_residual,
            "decomposed_projected_offdiagonal_max_abs_residual": decomposed_sector_offdiagonal_residual,
            "tolerance": TOLERANCE,
        },
        "resources": {
            "logical_qubits": circuit.num_qubits,
            "logical_block_queries": 2,
            "logical_projector_phases": 3,
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
        "evidence_class": "SIMULATION_INDEPENDENT_SDK_SPECTRAL_SECTOR_CHECK",
        "limitations": contract["nonclaims"] + [
            "The independently assembled reference reuses the already verified U_ER6 primitive.",
            "Generic basis decomposition is not a backend target, schedule, calibration, or bill.",
            "Host runtime and traced memory are CI-environment measurements only.",
        ],
    }


def dumps_reproduction() -> str:
    return json.dumps(reproduce_with_qiskit(), indent=2, sort_keys=True)
