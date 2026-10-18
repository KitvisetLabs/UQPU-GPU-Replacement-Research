"""Execute QOS-AUDIT-010B21 with explicit matrices in Qulacs.

Qiskit reconstructs the frozen logical circuit and route.  Qulacs receives
only explicit complex matrices; no Qulacs named X/SX/RZ/CZ aliases are used.
The finite probes remain a bounded semantic check, not operator equivalence.
"""

from __future__ import annotations

import cmath
import json
import math
import platform
from time import perf_counter_ns
import tracemalloc
from typing import Any

from .er6_qsvt_independent_routed_preregistration import (
    PERSISTED_PREREGISTRATION,
    ROOT,
    validate_preregistration,
)
from .er6_qsvt_routed_probe import (
    _compact_routed,
    _probe_circuit,
    inverse_layout_state,
    phase_aligned_l2,
)
from .er6_qsvt_routed_probe_preregistration import (
    PERSISTED_PREREGISTRATION as PROBE_PREREGISTRATION,
)
from .er6_qsvt_target_snapshot_identity import reproduce_target_identity
from .er6_qsvt_target_transpile_preregistration import TARGET_IDENTITY_SHA256
from .er6_qsvt_ten_query import build_ten_query_circuit


WORK_ID = "QOS-AUDIT-010B22"
UPSTREAM_WORK_ID = "QOS-AUDIT-010B21"
PERSISTED_CERTIFICATE = ROOT / "benchmarks/results/cycle008-delta20-er6-qsvt-independent-routed-probe.json"


X_MATRIX = ((0j, 1 + 0j), (1 + 0j, 0j))
SX_MATRIX = (
    ((1 + 1j) / 2, (1 - 1j) / 2),
    ((1 - 1j) / 2, (1 + 1j) / 2),
)
CZ_MATRIX = (
    (1 + 0j, 0j, 0j, 0j),
    (0j, 1 + 0j, 0j, 0j),
    (0j, 0j, 1 + 0j, 0j),
    (0j, 0j, 0j, -1 + 0j),
)


def rz_matrix(theta: float) -> tuple[tuple[complex, complex], tuple[complex, complex]]:
    return ((cmath.exp(-0.5j * theta), 0j), (0j, cmath.exp(0.5j * theta)))


def _route() -> tuple[Any, Any, list[int]]:
    from qiskit import transpile
    from qiskit_ibm_runtime.fake_provider import FakeKingston
    from .er6_qsvt_target_transpile_preregistration import (
        PERSISTED_PREREGISTRATION as ROUTING_PREREGISTRATION,
    )

    if reproduce_target_identity()["target_identity_sha256"] != TARGET_IDENTITY_SHA256:
        raise RuntimeError("saved target identity changed")
    routing = json.loads(ROUTING_PREREGISTRATION.read_text(encoding="utf-8"))
    settings = routing["transpiler"]
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
    final_layout = [int(value) for value in routed.layout.final_index_layout(filter_ancillas=True)]
    return logical, _compact_routed(routed, list(range(10))), final_layout


def _explicit_gate(name: str, qargs: list[int], params: list[Any], mutation: str | None, mutation_used: bool) -> tuple[Any, bool]:
    import numpy as np
    from qulacs.gate import DenseMatrix

    if name == "x":
        return DenseMatrix(qargs, np.asarray(X_MATRIX, dtype=np.complex128)), mutation_used
    if name == "sx":
        matrix = np.asarray(SX_MATRIX, dtype=np.complex128)
        if mutation == "sx_entry" and not mutation_used:
            matrix = matrix.copy()
            matrix[0, 0] += 1e-3
            mutation_used = True
        return DenseMatrix(qargs, matrix), mutation_used
    if name == "rz":
        theta = float(params[0])
        if mutation == "rz_sign" and not mutation_used and abs(theta) > 1e-15:
            theta = -theta
            mutation_used = True
        return DenseMatrix(qargs, np.asarray(rz_matrix(theta), dtype=np.complex128)), mutation_used
    if name == "cz":
        targets = list(qargs)
        if mutation == "cz_endpoint_order" and not mutation_used:
            targets.reverse()
            mutation_used = True
        elif mutation == "cz_mapping" and not mutation_used:
            replacement = next(q for q in range(10) if q not in targets)
            targets[1] = replacement
            mutation_used = True
        return DenseMatrix(targets, np.asarray(CZ_MATRIX, dtype=np.complex128)), mutation_used
    raise RuntimeError(f"unknown routed operation: {name}")


def _qulacs_circuit(compact: Any, mutation: str | None = None) -> tuple[Any, list[str], bool]:
    from qulacs import QuantumCircuit

    circuit = QuantumCircuit(compact.num_qubits)
    observed: set[str] = set()
    mutation_used = False
    for item in compact.data:
        name = item.operation.name
        if name == "barrier":
            continue
        qargs = [compact.find_bit(bit).index for bit in item.qubits]
        gate, mutation_used = _explicit_gate(name, qargs, list(item.operation.params), mutation, mutation_used)
        circuit.add_gate(gate)
        observed.add(name)
    if mutation is not None and not mutation_used:
        raise RuntimeError(f"requested mutation had no target: {mutation}")
    return circuit, sorted(observed), mutation_used


def _prepare_qulacs(probe: dict[str, Any], qubits: int) -> Any:
    import numpy as np
    from qulacs import QuantumState
    from qulacs.gate import DenseMatrix

    matrices = {
        "x": np.asarray(X_MATRIX, dtype=np.complex128),
        "h": np.asarray(((1, 1), (1, -1)), dtype=np.complex128) / math.sqrt(2),
        "s": np.asarray(((1, 0), (0, 1j)), dtype=np.complex128),
        "t": np.asarray(((1, 0), (0, cmath.exp(0.25j * math.pi))), dtype=np.complex128),
    }
    state = QuantumState(qubits)
    for instruction in probe["preparation"]:
        for qubit in instruction["qubits"]:
            DenseMatrix([qubit], matrices[instruction["gate"]]).update_quantum_state(state)
    return state


def _candidate(compiled: Any, probe: dict[str, Any], final_layout: list[int], invert_layout: bool = True) -> list[complex]:
    state = _prepare_qulacs(probe, len(final_layout))
    compiled.update_quantum_state(state)
    vector = state.get_vector()
    return inverse_layout_state(vector, final_layout) if invert_layout else [complex(value) for value in vector]


def evaluate_result(contract: dict[str, Any], resources: dict[str, Any]) -> dict[str, Any]:
    acceptance = contract["acceptance"]
    failures: list[str] = []
    if resources["observed_gate_set"] != acceptance["gate_set_must_equal"]:
        failures.append("observed_gate_set")
    if sorted(resources["observed_final_index_layout"]) != list(range(10)):
        failures.append("final_index_layout")
    if resources["completed_probe_count"] != 4:
        failures.append("completed_probe_count")
    if resources["host_runtime_seconds"] > acceptance["maximum_host_runtime_seconds"]:
        failures.append("host_runtime_seconds")
    if resources["host_peak_traced_bytes"] > acceptance["maximum_host_peak_traced_bytes"]:
        failures.append("host_peak_traced_bytes")
    for probe in resources["probes"]:
        if probe["phase_aligned_l2_residual"] > acceptance["maximum_phase_aligned_l2_residual_per_probe"]:
            failures.append(f"probe:{probe['id']}:residual")
        for key in ("reference_state_norm", "candidate_state_norm"):
            if not acceptance["minimum_state_norm"] <= probe[key] <= acceptance["maximum_state_norm"]:
                failures.append(f"probe:{probe['id']}:{key}")
    if not all(item["contract_requirement_satisfied"] for item in resources["counterexamples"]):
        failures.append("counterexample_detection")
    if any(resources["authorization"].values()):
        failures.append("authorization")
    return {
        "failures": sorted(set(failures)),
        "independent_sdk_bounded_probe_gate_passed": not failures,
        "full_operator_equivalence_accepted": False,
        "hardware_fidelity_accepted": False,
        "useful_output_quality_accepted": False,
    }


def reproduce_with_qulacs() -> dict[str, Any]:
    import numpy as np
    import qiskit
    import qulacs
    from qiskit.quantum_info import Statevector

    contract = json.loads(PERSISTED_PREREGISTRATION.read_text(encoding="utf-8"))
    errors = validate_preregistration(contract)
    if errors:
        raise RuntimeError(f"invalid independent-routed preregistration: {errors}")
    probes_contract = json.loads(PROBE_PREREGISTRATION.read_text(encoding="utf-8"))
    probes = probes_contract["method"]["probes"]

    tracemalloc.start()
    started = perf_counter_ns()
    logical, compact, final_layout = _route()
    compiled, observed_gates, _ = _qulacs_circuit(compact)
    results: list[dict[str, Any]] = []
    references: dict[str, Any] = {}
    for probe in probes:
        reference = Statevector.from_instruction(_probe_circuit(probe, 10).compose(logical)).data
        references[probe["id"]] = reference
        candidate = _candidate(compiled, probe, final_layout)
        results.append({
            "id": probe["id"],
            "phase_aligned_l2_residual": phase_aligned_l2(reference, candidate),
            "reference_state_norm": float(np.linalg.norm(reference)),
            "candidate_state_norm": float(np.linalg.norm(candidate)),
        })

    diagnostic_probe = next(probe for probe in probes if probe["id"] == "complex_product")
    reference = references["complex_product"]
    counterexamples: list[dict[str, Any]] = []
    threshold = contract["acceptance"]["maximum_phase_aligned_l2_residual_per_probe"]
    for mutation in ("rz_sign", "sx_entry", "cz_mapping"):
        mutated, _, _ = _qulacs_circuit(compact, mutation)
        residual = phase_aligned_l2(reference, _candidate(mutated, diagnostic_probe, final_layout))
        counterexamples.append({
            "id": mutation,
            "probe": "complex_product",
            "phase_aligned_l2_residual": residual,
            "contract_requirement_satisfied": residual > threshold,
            "outcome": "REJECTED" if residual > threshold else "NOT_DETECTED",
        })
    omitted = phase_aligned_l2(reference, _candidate(compiled, diagnostic_probe, final_layout, invert_layout=False))
    counterexamples.append({
        "id": "omit_layout_inversion",
        "probe": "complex_product",
        "phase_aligned_l2_residual": omitted,
        "contract_requirement_satisfied": omitted > threshold,
        "outcome": "REJECTED" if omitted > threshold else "NOT_DETECTED",
    })

    # A CZ is invariant under endpoint reversal: diag(1,1,1,-1) is symmetric.
    # Record this preregistered conditional case explicitly and test the
    # observable altered-mapping variant above instead of fabricating a signal.
    reversed_cz, _, _ = _qulacs_circuit(compact, "cz_endpoint_order")
    endpoint_residual = phase_aligned_l2(reference, _candidate(reversed_cz, diagnostic_probe, final_layout))
    counterexamples.append({
        "id": "cz_endpoint_order",
        "probe": "complex_product",
        "phase_aligned_l2_residual": endpoint_residual,
        "observable": False,
        "contract_requirement_satisfied": endpoint_residual <= threshold,
        "outcome": "NOT_OBSERVABLE_BY_CZ_SYMMETRY",
        "algebraic_reason": "CZ(q0,q1) = CZ(q1,q0)",
    })

    runtime_ns = perf_counter_ns() - started
    _, peak_bytes = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    resources = {
        "observed_gate_set": observed_gates,
        "observed_final_index_layout": final_layout,
        "compact_routed_qubits": int(compact.num_qubits),
        "compact_routed_size": int(compact.size()),
        "completed_probe_count": len(results),
        "probes": results,
        "counterexamples": counterexamples,
        "host_runtime_ns": int(runtime_ns),
        "host_runtime_seconds": runtime_ns / 1_000_000_000,
        "host_peak_traced_bytes": int(peak_bytes),
        "authorization": dict(contract["authorization"]),
        "provider_cost": None,
        "energy_j": None,
    }
    evaluation = evaluate_result(contract, resources)
    return {
        "schema": "uqpu-er6-qsvt-independent-routed-probe-v1",
        "work_id": WORK_ID,
        "upstream_work_id": UPSTREAM_WORK_ID,
        "preregistration_sha256": contract["contract_sha256"],
        "target_identity_sha256": TARGET_IDENTITY_SHA256,
        "evidence_class": "SIMULATION_INDEPENDENT_SDK_BOUNDED_ROUTED_PROBE_CHECK",
        "environment": {
            "qiskit": qiskit.__version__,
            "qulacs": qulacs.__version__,
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
        },
        "resources": resources,
        "evaluation": evaluation,
        "passed": evaluation["independent_sdk_bounded_probe_gate_passed"],
        "limitations": contract["nonclaims"] + [
            "finite independent-simulator probes cannot exclude defects on unprobed states",
            "Qiskit still reconstructs the frozen source and route",
            "tracemalloc excludes some native-library allocations",
        ],
    }
