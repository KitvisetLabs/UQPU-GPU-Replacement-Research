"""Execute the preregistered bounded routed-semantics probes for ER6 QSVT.

This is a local, same-SDK statevector check on four frozen product states.  It
can expose routing/layout defects but cannot establish full operator
equivalence, hardware fidelity, or useful-output advantage.
"""

from __future__ import annotations

import json
import platform
from time import perf_counter_ns
import tracemalloc
from typing import Any

from .er6_qsvt_routed_probe_preregistration import (
    PERSISTED_PREREGISTRATION,
    ROOT,
    validate_preregistration,
)
from .er6_qsvt_target_snapshot_identity import reproduce_target_identity
from .er6_qsvt_target_transpile_preregistration import TARGET_IDENTITY_SHA256
from .er6_qsvt_ten_query import build_ten_query_circuit


WORK_ID = "QOS-AUDIT-010B20"
UPSTREAM_WORK_ID = "QOS-AUDIT-010B19"
PERSISTED_CERTIFICATE = ROOT / "benchmarks/results/cycle008-delta18-er6-qsvt-routed-probe.json"


def inverse_layout_state(data: Any, final_index_layout: list[int]) -> Any:
    """Return amplitudes in logical-qubit order from physical-wire order.

    ``final_index_layout[i]`` is the physical output position of logical qubit
    ``i``.  Explicit bit-index movement avoids relying on SDK permutation
    conventions and is bounded here to ten qubits.
    """
    values = [complex(value) for value in data]
    qubits = len(final_index_layout)
    if sorted(final_index_layout) != list(range(qubits)):
        raise ValueError("final index layout is not a bijection")
    if len(values) != 1 << qubits:
        raise ValueError("statevector width does not match final index layout")
    logical = [0j] * len(values)
    for logical_index in range(1 << qubits):
        physical_index = 0
        for logical_qubit, physical_qubit in enumerate(final_index_layout):
            physical_index |= ((logical_index >> logical_qubit) & 1) << physical_qubit
        logical[logical_index] = values[physical_index]
    return logical


def phase_aligned_l2(reference: Any, candidate: Any) -> float:
    """Compute L2 residual after removing one global phase."""
    import math

    reference_array = [complex(value) for value in reference]
    candidate_array = [complex(value) for value in candidate]
    if len(reference_array) != len(candidate_array):
        raise ValueError("statevector lengths differ")
    overlap = sum(left.conjugate() * right for left, right in zip(reference_array, candidate_array))
    if abs(overlap) == 0:
        return math.sqrt(sum(abs(left - right) ** 2 for left, right in zip(reference_array, candidate_array)))
    phase = overlap / abs(overlap)
    return math.sqrt(sum(abs(left - right / phase) ** 2 for left, right in zip(reference_array, candidate_array)))


def evaluate_result(contract: dict[str, Any], resources: dict[str, Any]) -> dict[str, Any]:
    acceptance = contract["acceptance"]
    failures: list[str] = []
    if resources["observed_active_physical_qubits"] != contract["method"]["compact_only_frozen_active_physical_qubits"]:
        failures.append("active_physical_qubits")
    if sorted(resources["observed_final_index_layout"]) != list(range(contract["method"]["statevector_qubits"])):
        failures.append("final_index_layout")
    if resources["host_runtime_seconds"] > acceptance["maximum_host_runtime_seconds"]:
        failures.append("host_runtime_seconds")
    if resources["host_peak_traced_bytes"] > acceptance["maximum_host_peak_traced_bytes"]:
        failures.append("host_peak_traced_bytes")
    if resources["completed_probe_count"] != len(contract["method"]["probes"]):
        failures.append("completed_probe_count")
    for probe in resources["probes"]:
        if probe["phase_aligned_l2_residual"] > acceptance["maximum_phase_aligned_l2_residual_per_probe"]:
            failures.append(f"probe:{probe['id']}:residual")
        for state_name in ("logical_state_norm", "routed_state_norm"):
            if not acceptance["minimum_state_norm"] <= probe[state_name] <= acceptance["maximum_state_norm"]:
                failures.append(f"probe:{probe['id']}:{state_name}")
    if any(resources["authorization"].values()):
        failures.append("authorization")
    return {
        "failures": sorted(set(failures)),
        "bounded_probe_gate_passed": not failures,
        "full_operator_equivalence_accepted": False,
        "independent_sdk_equivalence_accepted": False,
        "useful_output_quality_accepted": False,
    }


def _probe_circuit(probe: dict[str, Any], qubits: int) -> Any:
    from qiskit import QuantumCircuit

    circuit = QuantumCircuit(qubits)
    for instruction in probe["preparation"]:
        gate = getattr(circuit, instruction["gate"])
        for qubit in instruction["qubits"]:
            gate(qubit)
    return circuit


def _compact_routed(circuit: Any, active: list[int]) -> Any:
    from qiskit import QuantumCircuit

    active_map = {physical: compact for compact, physical in enumerate(active)}
    compact = QuantumCircuit(len(active))
    compact.global_phase = circuit.global_phase
    for item in circuit.data:
        if item.operation.name == "barrier":
            continue
        physical_qargs = [circuit.find_bit(bit).index for bit in item.qubits]
        if any(index not in active_map for index in physical_qargs):
            raise RuntimeError(f"routed instruction escaped frozen active wires: {physical_qargs}")
        if item.clbits:
            raise RuntimeError("unexpected classical bit in unitary routed circuit")
        compact.append(item.operation, [active_map[index] for index in physical_qargs])
    return compact


def reproduce_with_qiskit() -> dict[str, Any]:
    import numpy as np
    import qiskit
    from qiskit import transpile
    from qiskit.quantum_info import Statevector
    from qiskit_ibm_runtime.fake_provider import FakeKingston

    contract = json.loads(PERSISTED_PREREGISTRATION.read_text(encoding="utf-8"))
    errors = validate_preregistration(contract)
    if errors:
        raise RuntimeError(f"invalid routed-probe preregistration: {errors}")
    identity = reproduce_target_identity()
    if identity["target_identity_sha256"] != TARGET_IDENTITY_SHA256:
        raise RuntimeError("saved target identity changed before routed probes")

    from .er6_qsvt_target_transpile_preregistration import PERSISTED_PREREGISTRATION as transpile_contract_path

    routing_contract = json.loads(transpile_contract_path.read_text(encoding="utf-8"))
    settings = routing_contract["transpiler"]
    active = contract["method"]["compact_only_frozen_active_physical_qubits"]
    tracemalloc.start()
    started = perf_counter_ns()
    logical = build_ten_query_circuit()
    routed = transpile(
        logical,
        target=FakeKingston().target,
        optimization_level=settings["optimization_level"],
        seed_transpiler=settings["seed_transpiler"],
        initial_layout=settings["initial_layout"],
        layout_method=settings["layout_method"],
        routing_method=settings["routing_method"],
        scheduling_method=settings["scheduling_method"],
    )
    observed_active = sorted({routed.find_bit(bit).index for item in routed.data for bit in item.qubits})
    final_layout = [int(value) for value in routed.layout.final_index_layout(filter_ancillas=True)]
    compact = _compact_routed(routed, active)
    probes: list[dict[str, Any]] = []
    for probe in contract["method"]["probes"]:
        preparation = _probe_circuit(probe, logical.num_qubits)
        logical_state = Statevector.from_instruction(preparation.compose(logical)).data
        physical_state = Statevector.from_instruction(preparation.compose(compact)).data
        routed_state = inverse_layout_state(physical_state, final_layout)
        probes.append({
            "id": probe["id"],
            "phase_aligned_l2_residual": phase_aligned_l2(logical_state, routed_state),
            "logical_state_norm": float(np.linalg.norm(logical_state)),
            "routed_state_norm": float(np.linalg.norm(routed_state)),
        })
    runtime_ns = perf_counter_ns() - started
    _, peak_bytes = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    resources = {
        "observed_final_index_layout": final_layout,
        "observed_active_physical_qubits": observed_active,
        "logical_qubits": int(logical.num_qubits),
        "compact_routed_qubits": int(compact.num_qubits),
        "compact_routed_size": int(compact.size()),
        "completed_probe_count": len(probes),
        "probes": probes,
        "host_runtime_ns": int(runtime_ns),
        "host_runtime_seconds": runtime_ns / 1_000_000_000,
        "host_peak_traced_bytes": int(peak_bytes),
        "authorization": dict(contract["authorization"]),
        "provider_cost": None,
        "energy_j": None,
    }
    evaluation = evaluate_result(contract, resources)
    return {
        "schema": "uqpu-er6-qsvt-routed-probe-v1",
        "work_id": WORK_ID,
        "upstream_work_id": UPSTREAM_WORK_ID,
        "preregistration_sha256": contract["contract_sha256"],
        "target_identity_sha256": TARGET_IDENTITY_SHA256,
        "evidence_class": "SAME_SDK_BOUNDED_STATEVECTOR_PROBE_CHECK",
        "environment": {
            "qiskit": qiskit.__version__,
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
        },
        "resources": resources,
        "evaluation": evaluation,
        "passed": evaluation["bounded_probe_gate_passed"],
        "limitations": contract["nonclaims"] + [
            "four passing product-state probes cannot exclude defects on unprobed states",
            "logical and routed paths share the same SDK implementation",
        ],
    }
