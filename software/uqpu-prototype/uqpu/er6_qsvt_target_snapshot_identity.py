"""Deterministic identity gate for the ER6 QSVT saved target snapshot.

This is a pre-transpilation, no-submit gate.  It fingerprints only the pinned
local fake-backend snapshot and its declared target structure.  It never opens
an IBM service, selects a live backend, submits a circuit, or estimates
hardware fidelity from instruction errors.
"""

from __future__ import annotations

from collections import Counter
import hashlib
import importlib.metadata
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
WORK_ID = "QOS-AUDIT-010B16"
UPSTREAM_WORK_ID = "QOS-AUDIT-010B15"
SOURCE_CERTIFICATE = ROOT / "benchmarks/results/cycle008-delta14-er6-qsvt-ten-query-qiskit.json"
SOURCE_CERTIFICATE_SHA256 = "edcf6e7606336ab55095df44ae03a72e999f863f341033b402a8fbf327f1c899"
SDK_REQUIREMENTS = {
    "qiskit": "2.5.2",
    "qiskit-aer": "0.17.1",
    "qiskit-ibm-runtime": "0.48.0",
}


def _canonical_sha256(payload: dict[str, Any]) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    return hashlib.sha256(encoded).hexdigest()


def _coupling_edges(backend: Any) -> list[list[int]]:
    coupling = getattr(backend, "coupling_map", None)
    if coupling is None:
        return []
    return sorted([int(a), int(b)] for a, b in coupling.get_edges())


def build_target_identity(backend: Any, package_versions: dict[str, str]) -> dict[str, Any]:
    """Return an order-stable structural fingerprint for a saved backend target."""
    target = backend.target
    instruction_signatures: Counter[tuple[str, int]] = Counter()
    for operation, qargs in target.instructions:
        # Qiskit Target uses qargs=None for globally defined instructions.
        # Preserve their declared arity without pretending they are bound to a
        # concrete physical tuple.
        arity = int(operation.num_qubits) if qargs is None else len(qargs)
        instruction_signatures[(str(operation.name), arity)] += 1
    identity = {
        "schema": "uqpu-er6-target-snapshot-identity-v1",
        "work_id": WORK_ID,
        "upstream_work_id": UPSTREAM_WORK_ID,
        "source_certificate_sha256": SOURCE_CERTIFICATE_SHA256,
        "target": {
            "kind": "SAVED_FAKE_BACKEND_SNAPSHOT",
            "class": type(backend).__name__,
            "module": type(backend).__module__,
            "name": str(getattr(backend, "name", "unknown")),
            "num_qubits": int(backend.num_qubits),
            "operation_names": sorted(str(name) for name in target.operation_names),
            "coupling_edges": _coupling_edges(backend),
            "instruction_signature_counts": [
                {"operation": name, "arity": arity, "instances": count}
                for (name, arity), count in sorted(instruction_signatures.items())
            ],
        },
        "environment": {"packages": dict(sorted(package_versions.items()))},
        "authorization": {
            "credentials_used": False,
            "live_service_initialized": False,
            "network_submission_attempted": False,
            "provider_jobs": 0,
            "shots": 0,
            "paid_execution_authorized": False,
        },
        "evidence_class": "CALIBRATION_SNAPSHOT_IDENTITY_ONLY",
        "limitations": [
            "saved fake-backend structure is not current or live calibration",
            "identity collection is not target-aware transpilation or scheduling",
            "no circuit was submitted or executed and no provider cost or energy was measured",
            "instruction properties are not multiplied into a circuit-fidelity claim",
            "this artifact does not authorize eleven queries, degree-81 synthesis, or paid execution",
        ],
    }
    identity["target_identity_sha256"] = _canonical_sha256(identity)
    return identity


def validate_identity(identity: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    payload = dict(identity)
    observed_digest = payload.pop("target_identity_sha256", None)
    if observed_digest != _canonical_sha256(payload):
        errors.append("target_identity_sha256")
    if identity.get("source_certificate_sha256") != SOURCE_CERTIFICATE_SHA256:
        errors.append("source_certificate_sha256")
    if identity.get("target", {}).get("kind") != "SAVED_FAKE_BACKEND_SNAPSHOT":
        errors.append("target.kind")
    if identity.get("environment", {}).get("packages") != SDK_REQUIREMENTS:
        errors.append("environment.packages")
    authorization = identity.get("authorization", {})
    forbidden = (
        authorization.get("credentials_used"),
        authorization.get("live_service_initialized"),
        authorization.get("network_submission_attempted"),
        authorization.get("provider_jobs"),
        authorization.get("shots"),
        authorization.get("paid_execution_authorized"),
    )
    if any(forbidden):
        errors.append("authorization")
    return errors


def reproduce_target_identity() -> dict[str, Any]:
    from qiskit_ibm_runtime.fake_provider import FakeKingston

    source_sha = hashlib.sha256(SOURCE_CERTIFICATE.read_bytes()).hexdigest()
    if source_sha != SOURCE_CERTIFICATE_SHA256:
        raise RuntimeError("ten-query source certificate digest changed")
    packages = {name: importlib.metadata.version(name) for name in SDK_REQUIREMENTS}
    if packages != SDK_REQUIREMENTS:
        raise RuntimeError(f"pinned SDK mismatch: {packages!r}")
    identity = build_target_identity(FakeKingston(), packages)
    errors = validate_identity(identity)
    if errors:
        raise RuntimeError(f"invalid target identity: {errors}")
    return identity
