"""Freeze an independent-SDK routed-semantics experiment for ER6 QSVT."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
WORK_ID = "QOS-AUDIT-010B21"
UPSTREAM_WORK_ID = "QOS-AUDIT-010B20"
SOURCE_CERTIFICATE = ROOT / "benchmarks/results/cycle008-delta18-er6-qsvt-routed-probe.json"
PERSISTED_PREREGISTRATION = ROOT / "benchmarks/results/cycle008-delta19-er6-qsvt-independent-routed-preregistration.json"
SOURCE_CERTIFICATE_SHA256 = "bcb7618ac7d4bfc20ed03c5aa9d5d4481b5da1b86d267878a1bb9cda998c7640"


def _canonical_sha256(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def build_preregistration() -> dict[str, Any]:
    if hashlib.sha256(SOURCE_CERTIFICATE.read_bytes()).hexdigest() != SOURCE_CERTIFICATE_SHA256:
        raise RuntimeError("Delta 18 routed-probe certificate digest changed")
    source = json.loads(SOURCE_CERTIFICATE.read_text(encoding="utf-8"))
    if source.get("passed") is not True:
        raise RuntimeError("accepted Delta 18 bounded-probe source missing")
    if source.get("evaluation", {}).get("full_operator_equivalence_accepted") is not False:
        raise RuntimeError("source evidence boundary changed")
    result = {
        "schema": "uqpu-er6-qsvt-independent-routed-preregistration-v1",
        "work_id": WORK_ID,
        "upstream_work_id": UPSTREAM_WORK_ID,
        "date": "2026-10-18",
        "evidence_class": "MODEL_ONLY_PREREGISTRATION",
        "inputs": {
            "bounded_same_sdk_result": {
                "path": str(SOURCE_CERTIFICATE.relative_to(ROOT)),
                "sha256": SOURCE_CERTIFICATE_SHA256,
                "work_id": source["work_id"],
                "target_identity_sha256": source["target_identity_sha256"],
                "observed_final_index_layout": source["resources"]["observed_final_index_layout"],
                "compact_routed_size": source["resources"]["compact_routed_size"],
            }
        },
        "method": {
            "reference_sdk": "qiskit==2.5.2",
            "independent_simulator": "qulacs==0.6.14",
            "backend_package": "qiskit-ibm-runtime==0.48.0",
            "reproduce_frozen_saved_target_route": True,
            "active_physical_qubits": list(range(10)),
            "apply_inverse_final_layout": True,
            "gate_translation": {
                "x": "explicit complex128 matrix [[0,1],[1,0]]",
                "sx": "explicit Qiskit-definition complex128 matrix; do not use SDK alias",
                "rz": "explicit diag(exp(-i*theta/2),exp(i*theta/2)); do not use SDK rotation convention",
                "cz": "explicit diag(1,1,1,-1) in verified little-endian target order",
                "barrier": "omit",
                "unknown_operation": "fail_closed",
            },
            "probe_source": "reuse the four immutable QOS-AUDIT-010B19 preparations",
            "reference_path": "Qiskit logical statevector",
            "candidate_path": "manual gate translation plus Qulacs statevector",
            "global_phase_alignment": "inner_product",
            "counterexamples": [
                "mutate one RZ sign and require rejection",
                "swap one CZ endpoint ordering and require rejection when observable",
                "omit final-layout inversion and require rejection",
                "perturb one SX matrix entry and require rejection",
            ],
        },
        "acceptance": {
            "maximum_phase_aligned_l2_residual_per_probe": 1e-9,
            "minimum_state_norm": 0.999999999,
            "maximum_state_norm": 1.000000001,
            "maximum_host_runtime_seconds": 1800,
            "maximum_host_peak_traced_bytes": 1_500_000_000,
            "all_four_probes_must_complete": True,
            "all_counterexamples_must_be_detected": True,
            "gate_set_must_equal": ["cz", "rz", "sx", "x"],
            "no_threshold_change_after_execution": True,
            "stop_on_any_failure": True,
        },
        "authorization": {
            "credentials_used": False,
            "live_service_initialized": False,
            "network_submission_attempted": False,
            "provider_jobs": 0,
            "shots": 0,
            "paid_execution_authorized": False,
        },
        "required_outputs": [
            "observed_gate_set",
            "observed_final_index_layout",
            "per_probe_phase_aligned_l2_residual",
            "per_probe_state_norms",
            "counterexample_detection",
            "host_runtime_ns",
            "host_peak_traced_bytes",
        ],
        "nonclaims": [
            "four probes do not prove full operator equivalence",
            "independent simulation is not hardware fidelity evidence",
            "not live calibration, provider execution, energy, cost, or advantage evidence",
            "not eleven-query or degree-81 feasibility",
            "not GPU, CPU, NPU, RAM, VRAM, or storage replacement evidence",
        ],
    }
    result["contract_sha256"] = _canonical_sha256(result)
    return result


def validate_preregistration(contract: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if contract.get("work_id") != WORK_ID:
        errors.append("work_id")
    if contract.get("inputs", {}).get("bounded_same_sdk_result", {}).get("sha256") != SOURCE_CERTIFICATE_SHA256:
        errors.append("source_certificate_sha256")
    method = contract.get("method", {})
    if method.get("independent_simulator") != "qulacs==0.6.14":
        errors.append("independent_simulator")
    if method.get("active_physical_qubits") != list(range(10)):
        errors.append("active_physical_qubits")
    if set(method.get("gate_translation", {})) != {"x", "sx", "rz", "cz", "barrier", "unknown_operation"}:
        errors.append("gate_translation")
    if len(method.get("counterexamples", [])) != 4:
        errors.append("counterexamples")
    acceptance = contract.get("acceptance", {})
    if acceptance.get("maximum_phase_aligned_l2_residual_per_probe") != 1e-9:
        errors.append("residual_threshold")
    if acceptance.get("gate_set_must_equal") != ["cz", "rz", "sx", "x"]:
        errors.append("gate_set")
    if acceptance.get("all_counterexamples_must_be_detected") is not True:
        errors.append("counterexample_gate")
    if acceptance.get("no_threshold_change_after_execution") is not True:
        errors.append("threshold_freeze")
    if any(contract.get("authorization", {}).values()):
        errors.append("authorization")
    digest = contract.get("contract_sha256")
    body = {key: value for key, value in contract.items() if key != "contract_sha256"}
    if digest != _canonical_sha256(body):
        errors.append("contract_sha256")
    return sorted(set(errors))
