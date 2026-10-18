"""Freeze a bounded routed-semantics probe experiment for ER6 ten-query QSVT.

The contract binds the accepted logical source and saved-target routing
certificate before any statevector probe residual is observed.  Passing this
experiment can reject some routing defects, but a finite probe ensemble is not
a proof of full operator equivalence and is never hardware evidence.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
WORK_ID = "QOS-AUDIT-010B19"
UPSTREAM_WORK_ID = "QOS-AUDIT-010B18"
SOURCE_CERTIFICATE = ROOT / "benchmarks/results/cycle008-delta14-er6-qsvt-ten-query-qiskit.json"
ROUTING_CERTIFICATE = ROOT / "benchmarks/results/cycle008-delta16-er6-qsvt-target-transpile.json"
PERSISTED_PREREGISTRATION = ROOT / "benchmarks/results/cycle008-delta17-er6-qsvt-routed-probe-preregistration.json"
SOURCE_CERTIFICATE_SHA256 = "edcf6e7606336ab55095df44ae03a72e999f863f341033b402a8fbf327f1c899"
ROUTING_CERTIFICATE_SHA256 = "5e3612dc420b3763655e26aac7f1388073f7228a913179d605c66895601332ff"
TARGET_IDENTITY_SHA256 = "88419f3cb82b6d2bf21cb40ef59ae3ac9fbca0c37b0425bd0d8f561cb905ca4e"


def _canonical_sha256(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_preregistration() -> dict[str, Any]:
    if _file_sha256(SOURCE_CERTIFICATE) != SOURCE_CERTIFICATE_SHA256:
        raise RuntimeError("ten-query source certificate digest changed")
    if _file_sha256(ROUTING_CERTIFICATE) != ROUTING_CERTIFICATE_SHA256:
        raise RuntimeError("saved-target routing certificate digest changed")
    source = json.loads(SOURCE_CERTIFICATE.read_text(encoding="utf-8"))
    routing = json.loads(ROUTING_CERTIFICATE.read_text(encoding="utf-8"))
    if source.get("passed") is not True or source.get("resources", {}).get("queries") != 10:
        raise RuntimeError("accepted ten-query source contract missing")
    if routing.get("passed") is not True:
        raise RuntimeError("accepted routing resource certificate missing")
    if routing.get("target_identity_sha256") != TARGET_IDENTITY_SHA256:
        raise RuntimeError("saved-target identity changed")
    result = {
        "schema": "uqpu-er6-qsvt-routed-probe-preregistration-v1",
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
            },
            "saved_target_routing": {
                "path": str(ROUTING_CERTIFICATE.relative_to(ROOT)),
                "sha256": ROUTING_CERTIFICATE_SHA256,
                "work_id": routing["work_id"],
                "target_identity_sha256": TARGET_IDENTITY_SHA256,
                "layout_fingerprint": routing["resources"]["layout_fingerprint"],
                "active_physical_qubits": routing["resources"]["active_physical_qubits"],
            },
        },
        "method": {
            "sdk": "qiskit==2.5.2",
            "backend_package": "qiskit-ibm-runtime==0.48.0",
            "reproduce_routing_from_frozen_b17_contract": True,
            "compact_only_frozen_active_physical_qubits": list(range(10)),
            "require_final_index_layout_bijection": True,
            "apply_inverse_final_layout_before_comparison": True,
            "statevector_qubits": 10,
            "global_phase_alignment": "inner_product",
            "probes": [
                {"id": "computational_zero", "preparation": []},
                {"id": "computational_one", "preparation": [{"gate": "x", "qubits": list(range(10))}]},
                {"id": "alternating_odd", "preparation": [{"gate": "x", "qubits": [1, 3, 5, 7, 9]}]},
                {"id": "complex_product", "preparation": [
                    {"gate": "h", "qubits": list(range(10))},
                    {"gate": "s", "qubits": [1, 2, 5, 7]},
                    {"gate": "t", "qubits": [0, 3, 6, 9]},
                ]},
            ],
        },
        "acceptance": {
            "maximum_phase_aligned_l2_residual_per_probe": 1e-9,
            "minimum_state_norm": 0.999999999,
            "maximum_state_norm": 1.000000001,
            "maximum_host_runtime_seconds": 1800,
            "maximum_host_peak_traced_bytes": 1_500_000_000,
            "layout_must_be_bijective": True,
            "active_wire_set_must_match": True,
            "all_probes_must_complete": True,
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
            "observed_final_index_layout",
            "observed_active_physical_qubits",
            "per_probe_phase_aligned_l2_residual",
            "per_probe_logical_state_norm",
            "per_probe_routed_state_norm",
            "host_runtime_ns",
            "host_peak_traced_bytes",
        ],
        "nonclaims": [
            "finite probes do not prove full operator equivalence",
            "same-SDK statevector comparison is not an independent-SDK proof",
            "not live calibration, hardware execution, sampling, or fidelity evidence",
            "not eleven-query or degree-81 feasibility",
            "not provider cost, energy, quantum advantage, or subsystem replacement evidence",
        ],
    }
    result["contract_sha256"] = _canonical_sha256(result)
    return result


def validate_preregistration(contract: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if contract.get("work_id") != WORK_ID:
        errors.append("work_id")
    inputs = contract.get("inputs", {})
    if inputs.get("logical_source", {}).get("sha256") != SOURCE_CERTIFICATE_SHA256:
        errors.append("source_certificate_sha256")
    routed = inputs.get("saved_target_routing", {})
    if routed.get("sha256") != ROUTING_CERTIFICATE_SHA256:
        errors.append("routing_certificate_sha256")
    if routed.get("target_identity_sha256") != TARGET_IDENTITY_SHA256:
        errors.append("target_identity_sha256")
    method = contract.get("method", {})
    if method.get("compact_only_frozen_active_physical_qubits") != list(range(10)):
        errors.append("active_physical_qubits")
    if method.get("require_final_index_layout_bijection") is not True:
        errors.append("layout_bijection")
    if len(method.get("probes", [])) != 4:
        errors.append("probe_ensemble")
    acceptance = contract.get("acceptance", {})
    if acceptance.get("maximum_phase_aligned_l2_residual_per_probe") != 1e-9:
        errors.append("residual_threshold")
    if acceptance.get("stop_on_any_failure") is not True:
        errors.append("stop_on_failure")
    if acceptance.get("no_threshold_change_after_execution") is not True:
        errors.append("threshold_freeze")
    if any(contract.get("authorization", {}).values()):
        errors.append("authorization")
    digest = contract.get("contract_sha256")
    body = {key: value for key, value in contract.items() if key != "contract_sha256"}
    if digest != _canonical_sha256(body):
        errors.append("contract_sha256")
    return sorted(set(errors))
