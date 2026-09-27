"""SCM-GATE-004 independent-replication contract utilities.

A replication package describes protocol identity, software/data integrity,
environment capture, exclusions and scoring before a second team evaluates data.
It is infrastructure only and makes no anomalous-source claim.
"""
from __future__ import annotations
from dataclasses import dataclass
import hashlib, json
from typing import Mapping, Sequence

@dataclass(frozen=True)
class ReplicationManifest:
    protocol_id: str
    protocol_version: str
    code_commit: str
    data_sha256: str
    schema_version: str
    randomization_method: str
    scoring_rule: str
    exclusion_rules: tuple[str, ...]
    environment_fields: tuple[str, ...]
    evidence_class: str = "REPLICATION_INFRASTRUCTURE_ONLY"

REQUIRED_ENVIRONMENT_FIELDS = (
    "utc_start", "utc_end", "location_code", "hardware_ids",
    "software_commit", "operator_roles", "network_state",
    "rf_log", "acoustic_log", "thermal_log", "power_log",
)

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def canonical_manifest_bytes(m: ReplicationManifest) -> bytes:
    payload = {
        "protocol_id": m.protocol_id, "protocol_version": m.protocol_version,
        "code_commit": m.code_commit, "data_sha256": m.data_sha256,
        "schema_version": m.schema_version,
        "randomization_method": m.randomization_method,
        "scoring_rule": m.scoring_rule,
        "exclusion_rules": list(m.exclusion_rules),
        "environment_fields": list(m.environment_fields),
        "evidence_class": m.evidence_class,
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()

def validate_manifest(m: ReplicationManifest) -> tuple[str, ...]:
    errors = []
    for name in ("protocol_id","protocol_version","code_commit","data_sha256",
                 "schema_version","randomization_method","scoring_rule"):
        if not getattr(m, name):
            errors.append(f"missing:{name}")
    if len(m.data_sha256) != 64 or any(c not in "0123456789abcdef" for c in m.data_sha256.lower()):
        errors.append("invalid:data_sha256")
    missing_env = sorted(set(REQUIRED_ENVIRONMENT_FIELDS) - set(m.environment_fields))
    errors.extend(f"missing_environment:{x}" for x in missing_env)
    if not m.exclusion_rules:
        errors.append("missing:exclusion_rules")
    return tuple(errors)

def verify_dataset(m: ReplicationManifest, data: bytes) -> bool:
    return not validate_manifest(m) and sha256_bytes(data) == m.data_sha256

def compare_replications(
    first: Mapping[str, str], second: Mapping[str, str], invariant_fields: Sequence[str]
) -> tuple[str, ...]:
    """Return preregistered invariant fields that differ across replication packages."""
    return tuple(k for k in invariant_fields if first.get(k) != second.get(k))
