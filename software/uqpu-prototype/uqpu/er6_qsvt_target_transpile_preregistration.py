"""Freeze the ER6 ten-query saved-target transpilation experiment.

The contract binds the accepted ten-query source certificate and the exact
saved-target identity before routed resources are observed.  It authorizes
only local compilation against the pinned snapshot: no provider service,
submission, shots, billing, live calibration, or hardware execution.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
WORK_ID = "QOS-AUDIT-010B17"
UPSTREAM_WORK_ID = "QOS-AUDIT-010B16"
SOURCE_CERTIFICATE = ROOT / "benchmarks/results/cycle008-delta14-er6-qsvt-ten-query-qiskit.json"
IDENTITY_CERTIFICATE = ROOT / "benchmarks/results/cycle008-delta15-er6-qsvt-target-snapshot-identity.json"
PERSISTED_PREREGISTRATION = ROOT / "benchmarks/results/cycle008-delta16-er6-qsvt-target-transpile-preregistration.json"
SOURCE_CERTIFICATE_SHA256 = "edcf6e7606336ab55095df44ae03a72e999f863f341033b402a8fbf327f1c899"
IDENTITY_CERTIFICATE_SHA256 = "06fa59ffd50202a3b6846ae1beb0fdacf6a81fcf129af01765e5ade3ad685612"
TARGET_IDENTITY_SHA256 = "88419f3cb82b6d2bf21cb40ef59ae3ac9fbca0c37b0425bd0d8f561cb905ca4e"


def _sha256_json(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_preregistration() -> dict[str, Any]:
    if _file_sha256(SOURCE_CERTIFICATE) != SOURCE_CERTIFICATE_SHA256:
        raise RuntimeError("ten-query source certificate digest changed")
    if _file_sha256(IDENTITY_CERTIFICATE) != IDENTITY_CERTIFICATE_SHA256:
        raise RuntimeError("saved-target identity certificate digest changed")
    source = json.loads(SOURCE_CERTIFICATE.read_text(encoding="utf-8"))
    identity = json.loads(IDENTITY_CERTIFICATE.read_text(encoding="utf-8"))
    if source.get("passed") is not True or source.get("resources", {}).get("queries") != 10:
        raise RuntimeError("accepted ten-query source contract missing")
    if identity.get("target_identity_sha256") != TARGET_IDENTITY_SHA256:
        raise RuntimeError("saved-target identity digest mismatch")
    result = {
        "schema": "uqpu-er6-qsvt-target-transpile-preregistration-v1",
        "work_id": WORK_ID,
        "upstream_work_id": UPSTREAM_WORK_ID,
        "date": "2026-10-18",
        "evidence_class": "MODEL_ONLY_PREREGISTRATION",
        "inputs": {
            "logical_source": {
                "path": str(SOURCE_CERTIFICATE.relative_to(ROOT)),
                "sha256": SOURCE_CERTIFICATE_SHA256,
                "work_id": source["work_id"],
                "queries": source["resources"]["queries"],
                "logical_qubits": source["resources"]["logical_qubits"],
                "max_raw_residual": source["resources"]["max_raw_residual"],
            },
            "saved_target_identity": {
                "path": str(IDENTITY_CERTIFICATE.relative_to(ROOT)),
                "sha256": IDENTITY_CERTIFICATE_SHA256,
                "target_identity_sha256": TARGET_IDENTITY_SHA256,
                "class": identity["target"]["class"],
                "num_qubits": identity["target"]["num_qubits"],
            },
        },
        "transpiler": {
            "sdk": "qiskit==2.5.2",
            "backend_package": "qiskit-ibm-runtime==0.48.0",
            "optimization_level": 0,
            "seed_transpiler": 1017,
            "initial_layout": list(range(10)),
            "layout_method": None,
            "routing_method": "basic",
            "scheduling_method": None,
            "saved_target_only": True,
        },
        "acceptance": {
            "target_identity_must_match": True,
            "source_certificate_must_match": True,
            "all_routed_instructions_supported_by_saved_target": True,
            "minimum_logical_qubits_preserved": 10,
            "maximum_host_runtime_seconds": 1200,
            "maximum_host_peak_traced_bytes": 1_500_000_000,
            "maximum_routed_depth": 300_000,
            "maximum_routed_size": 600_000,
            "maximum_two_qubit_operations": 150_000,
            "maximum_serialized_qasm2_bytes": 8_000_000,
            "stop_on_any_failure": True,
            "no_threshold_change_after_execution": True,
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
            "routed_operation_counts",
            "routed_depth",
            "routed_size",
            "two_qubit_operations",
            "active_physical_qubits",
            "serialized_qasm2_bytes",
            "host_runtime_ns",
            "host_peak_traced_bytes",
            "layout_fingerprint",
            "target_conformance_failures",
        ],
        "nonclaims": [
            "not live calibration or a live backend selection",
            "not circuit execution, sampling, fidelity, or accepted useful-output evidence",
            "not provider cost or energy evidence",
            "not eleven-query or degree-81 feasibility",
            "not quantum advantage or GPU, CPU, NPU, RAM, VRAM, or storage replacement",
        ],
    }
    result["contract_sha256"] = _sha256_json(result)
    return result


def validate_preregistration(contract: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if contract.get("work_id") != WORK_ID:
        errors.append("work_id")
    inputs = contract.get("inputs", {})
    if inputs.get("logical_source", {}).get("sha256") != SOURCE_CERTIFICATE_SHA256:
        errors.append("source_certificate_sha256")
    if inputs.get("saved_target_identity", {}).get("sha256") != IDENTITY_CERTIFICATE_SHA256:
        errors.append("identity_certificate_sha256")
    if inputs.get("saved_target_identity", {}).get("target_identity_sha256") != TARGET_IDENTITY_SHA256:
        errors.append("target_identity_sha256")
    transpiler = contract.get("transpiler", {})
    expected_transpiler = {
        "sdk": "qiskit==2.5.2",
        "backend_package": "qiskit-ibm-runtime==0.48.0",
        "optimization_level": 0,
        "seed_transpiler": 1017,
        "initial_layout": list(range(10)),
        "layout_method": None,
        "routing_method": "basic",
        "scheduling_method": None,
        "saved_target_only": True,
    }
    if transpiler != expected_transpiler:
        errors.append("transpiler_contract")
    acceptance = contract.get("acceptance", {})
    if acceptance.get("no_threshold_change_after_execution") is not True:
        errors.append("threshold_freeze")
    if acceptance.get("stop_on_any_failure") is not True:
        errors.append("stop_on_failure")
    authorization = contract.get("authorization", {})
    if any(authorization.values()):
        errors.append("authorization")
    digest = contract.get("contract_sha256")
    body = {key: value for key, value in contract.items() if key != "contract_sha256"}
    if digest != _sha256_json(body):
        errors.append("contract_sha256")
    return sorted(set(errors))
