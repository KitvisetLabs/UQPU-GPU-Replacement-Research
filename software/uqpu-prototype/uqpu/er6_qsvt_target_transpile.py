"""Run the preregistered ER6 ten-query saved-target transpilation.

This module compiles locally against a pinned FakeKingston snapshot and records
routed resource facts.  It never creates a provider service or executes the
circuit.  Successful transpilation is not useful-output or fidelity acceptance.
"""

from __future__ import annotations

from collections import Counter
import hashlib
import json
import platform
from time import perf_counter_ns
import tracemalloc
from typing import Any

from .er6_qsvt_target_snapshot_identity import reproduce_target_identity
from .er6_qsvt_target_transpile_preregistration import (
    PERSISTED_PREREGISTRATION,
    TARGET_IDENTITY_SHA256,
    validate_preregistration,
)
from .er6_qsvt_ten_query import build_ten_query_circuit


WORK_ID = "QOS-AUDIT-010B18"
UPSTREAM_WORK_ID = "QOS-AUDIT-010B17"


def _canonical_sha256(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def evaluate_result(contract: dict[str, Any], resources: dict[str, Any]) -> dict[str, Any]:
    acceptance = contract["acceptance"]
    failures: list[str] = []
    limit_map = {
        "host_runtime_seconds": "maximum_host_runtime_seconds",
        "host_peak_traced_bytes": "maximum_host_peak_traced_bytes",
        "routed_depth": "maximum_routed_depth",
        "routed_size": "maximum_routed_size",
        "two_qubit_operations": "maximum_two_qubit_operations",
        "serialized_qasm2_bytes": "maximum_serialized_qasm2_bytes",
    }
    for metric, limit_name in limit_map.items():
        if resources[metric] > acceptance[limit_name]:
            failures.append(metric)
    if resources["logical_qubits"] < acceptance["minimum_logical_qubits_preserved"]:
        failures.append("logical_qubits")
    if resources["target_conformance_failures"]:
        failures.append("target_conformance")
    authorization = resources["authorization"]
    if any(authorization.values()):
        failures.append("authorization")
    return {
        "failures": sorted(set(failures)),
        "resource_and_authorization_gate_passed": not failures,
        "useful_output_quality_accepted": False,
    }


def _instruction_facts(circuit: Any, target: Any) -> tuple[dict[str, int], list[int], list[dict[str, Any]], str]:
    counts: Counter[str] = Counter()
    active: set[int] = set()
    unsupported: list[dict[str, Any]] = []
    stream: list[dict[str, Any]] = []
    for item in circuit.data:
        operation = item.operation
        qargs = tuple(circuit.find_bit(bit).index for bit in item.qubits)
        name = str(operation.name)
        counts[name] += 1
        active.update(qargs)
        stream.append({"operation": name, "qargs": list(qargs)})
        if name == "barrier":
            continue
        if not target.instruction_supported(operation_name=name, qargs=qargs):
            unsupported.append({"operation": name, "qargs": list(qargs)})
    return dict(sorted(counts.items())), sorted(active), unsupported, _canonical_sha256(stream)


def reproduce_with_qiskit() -> dict[str, Any]:
    import qiskit
    from qiskit import qasm2, transpile
    from qiskit_ibm_runtime.fake_provider import FakeKingston

    contract = json.loads(PERSISTED_PREREGISTRATION.read_text(encoding="utf-8"))
    errors = validate_preregistration(contract)
    if errors:
        raise RuntimeError(f"invalid transpilation preregistration: {errors}")
    identity = reproduce_target_identity()
    if identity["target_identity_sha256"] != TARGET_IDENTITY_SHA256:
        raise RuntimeError("saved target identity changed before transpilation")
    backend = FakeKingston()
    settings = contract["transpiler"]
    tracemalloc.start()
    started = perf_counter_ns()
    logical = build_ten_query_circuit()
    routed = transpile(
        logical,
        target=backend.target,
        optimization_level=settings["optimization_level"],
        seed_transpiler=settings["seed_transpiler"],
        initial_layout=settings["initial_layout"],
        layout_method=settings["layout_method"],
        routing_method=settings["routing_method"],
        scheduling_method=settings["scheduling_method"],
    )
    serialized = qasm2.dumps(routed)
    runtime_ns = perf_counter_ns() - started
    _, peak_bytes = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    counts, active, unsupported, layout_fingerprint = _instruction_facts(routed, backend.target)
    two_qubit = sum(
        1 for item in routed.data if len(item.qubits) == 2 and item.operation.name != "barrier"
    )
    authorization = dict(contract["authorization"])
    resources = {
        "logical_qubits": int(logical.num_qubits),
        "target_width_qubits": int(routed.num_qubits),
        "active_physical_qubits": active,
        "routed_operation_counts": counts,
        "routed_depth": int(routed.depth()),
        "routed_size": int(routed.size()),
        "two_qubit_operations": int(two_qubit),
        "serialized_qasm2_bytes": len(serialized.encode("utf-8")),
        "host_runtime_ns": int(runtime_ns),
        "host_runtime_seconds": runtime_ns / 1_000_000_000,
        "host_peak_traced_bytes": int(peak_bytes),
        "layout_fingerprint": layout_fingerprint,
        "target_conformance_failures": unsupported,
        "authorization": authorization,
        "provider_cost": None,
        "energy_j": None,
    }
    evaluation = evaluate_result(contract, resources)
    return {
        "schema": "uqpu-er6-qsvt-target-transpile-v1",
        "work_id": WORK_ID,
        "upstream_work_id": UPSTREAM_WORK_ID,
        "preregistration_sha256": contract["contract_sha256"],
        "target_identity_sha256": TARGET_IDENTITY_SHA256,
        "evidence_class": "SAVED_TARGET_NO_SUBMIT_TRANSPILATION_RESOURCE_CHECK",
        "environment": {
            "qiskit": qiskit.__version__,
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
        },
        "resources": resources,
        "evaluation": evaluation,
        "passed": evaluation["resource_and_authorization_gate_passed"],
        "limitations": contract["nonclaims"] + [
            "routed instruction conformance does not verify logical equivalence after routing",
            "saved instruction properties are not converted into a circuit-fidelity estimate",
        ],
    }
