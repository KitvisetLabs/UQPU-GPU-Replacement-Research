"""Offline validator for the QOS-AUDIT-010B25 redacted target snapshot contract.

This module does not contact IBM Quantum, load credentials, initialize a service,
open a session, transpile against a live target, or submit a job. It validates a
caller-supplied metadata snapshot and its separately recorded digest only.
"""
from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
import math
import re
from typing import Any

WORK_ID = "QOS-AUDIT-010B25"
EXPECTED_SCHEMA = "uqpu-er6-authenticated-readonly-target-snapshot-v1"
EXPECTED_PROVIDER = "IBM Quantum Compute"
EXPECTED_TARGET_ID = "ibm_kingston"
MAX_AGE_SECONDS = 900
RFC3339_UTC_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z$")
REQUIRED_TOP_LEVEL_FIELDS = (
    "schema", "provider", "target_id", "captured_at_utc",
    "client_package_versions", "backend_status", "target_structure",
    "timing_constraints", "calibration_provenance", "redaction_report",
)
REQUIRED_NESTED_FIELDS = {
    "client_package_versions": ("qiskit", "qiskit_ibm_runtime"),
    "backend_status": ("operational", "status_message", "pending_jobs", "status_observed_at_utc"),
    "target_structure": (
        "num_qubits", "basis_gates", "instruction_names", "coupling_edges",
        "measurement_map", "dynamic_circuit_capability_if_exposed",
    ),
    "timing_constraints": (
        "dt_seconds_if_exposed", "granularity_if_exposed", "minimum_length_if_exposed",
        "pulse_alignment_if_exposed", "acquire_alignment_if_exposed",
    ),
    "calibration_provenance": (
        "properties_last_update_utc_if_exposed", "target_last_update_utc_if_exposed",
        "per_instruction_error_and_duration_if_exposed",
        "per_qubit_readout_error_and_t1_t2_frequency_if_exposed",
    ),
}
FORBIDDEN_KEY_FRAGMENTS = (
    "token", "credential", "authorization", "accountid", "email", "hub",
    "group", "project", "accountidentifier", "instancecrn", "privateendpoint", "quota",
    "rawexception", "apikey", "accesskey",
)
SECRET_VALUE_PATTERNS = (
    re.compile(r"(?i)\bbearer\s+\S+"),
    re.compile(r"(?i)\b(?:api[_ -]?key|access[_ -]?token|password)\s*[:=]\s*\S+"),
    re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    re.compile(r"(?i)\bcrn:v\d+:[^\s]+"),
)


def _normal_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


def _parse_utc(value: Any) -> datetime:
    if not isinstance(value, str) or RFC3339_UTC_PATTERN.fullmatch(value) is None:
        raise ValueError("timestamp must be an RFC3339 UTC string ending in Z")
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError as exc:
        raise ValueError("timestamp is not parseable RFC3339 UTC") from exc
    if parsed.utcoffset() != timezone.utc.utcoffset(parsed):
        raise ValueError("timestamp must use UTC")
    return parsed.astimezone(timezone.utc)


def _walk(value: Any, path: str = "$"):
    if isinstance(value, dict):
        for key, child in value.items():
            yield path, key, child
            yield from _walk(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from _walk(child, f"{path}[{index}]")


def _has_explanation(container: dict[str, Any], key: str) -> bool:
    if key not in container:
        return False
    if container[key] is not None:
        return True
    reasons = container.get("null_reasons", {})
    return isinstance(reasons, dict) and isinstance(reasons.get(key), str) and bool(reasons[key].strip())


def _normalize_snapshot(snapshot: dict[str, Any]) -> dict[str, Any]:
    normalized = deepcopy(snapshot)
    target = normalized.get("target_structure")
    if not isinstance(target, dict):
        return normalized
    for key in ("basis_gates", "instruction_names"):
        value = target.get(key)
        if isinstance(value, list) and all(isinstance(item, str) for item in value):
            target[key] = sorted(set(value))
    edges = target.get("coupling_edges")
    if isinstance(edges, list) and all(
        isinstance(edge, (list, tuple)) and len(edge) == 2
        and all(isinstance(endpoint, int) and not isinstance(endpoint, bool) for endpoint in edge)
        for edge in edges
    ):
        target["coupling_edges"] = [list(edge) for edge in sorted({tuple(edge) for edge in edges})]
    indices = target.get("qubit_indices")
    if isinstance(indices, list) and all(isinstance(item, int) and not isinstance(item, bool) for item in indices):
        target["qubit_indices"] = sorted(set(indices))
    return normalized


def canonical_snapshot_bytes(snapshot: dict[str, Any]) -> bytes:
    """Return deterministic UTF-8 JSON bytes with field-specific list normalization."""
    normalized = _normalize_snapshot(snapshot)
    encoded = json.dumps(
        normalized, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False,
    ).encode("utf-8")
    return encoded + b"\n"


def snapshot_sha256(snapshot: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_snapshot_bytes(snapshot)).hexdigest()


def _is_finite_tree(value: Any) -> bool:
    if isinstance(value, float):
        return math.isfinite(value)
    if isinstance(value, dict):
        return all(_is_finite_tree(v) for v in value.values())
    if isinstance(value, list):
        return all(_is_finite_tree(v) for v in value)
    return True


def validate_snapshot(
    snapshot: dict[str, Any],
    route_build_time_utc: str,
    recorded_sha256: str,
) -> list[str]:
    """Validate a redacted snapshot; return stable error identifiers, never a truth claim."""
    errors: list[str] = []
    if not isinstance(snapshot, dict):
        return ["snapshot_not_object"]
    if not _is_finite_tree(snapshot):
        errors.append("non_finite_number")
    for key in REQUIRED_TOP_LEVEL_FIELDS:
        if key not in snapshot:
            errors.append(f"missing_top_level:{key}")
    if snapshot.get("schema") != EXPECTED_SCHEMA:
        errors.append("schema_mismatch")
    if snapshot.get("provider") != EXPECTED_PROVIDER:
        errors.append("provider_mismatch")
    if snapshot.get("target_id") != EXPECTED_TARGET_ID:
        errors.append("target_id_mismatch")

    for container_name, required in REQUIRED_NESTED_FIELDS.items():
        container = snapshot.get(container_name)
        if not isinstance(container, dict):
            errors.append(f"container_not_object:{container_name}")
            continue
        for key in required:
            if not _has_explanation(container, key):
                errors.append(f"missing_or_unexplained:{container_name}.{key}")

    for path, key, child in _walk(snapshot):
        normalized_key = _normal_key(key)
        if any(fragment in normalized_key for fragment in FORBIDDEN_KEY_FRAGMENTS):
            errors.append(f"forbidden_key:{path}.{key}")
        if isinstance(child, str) and any(pattern.search(child) for pattern in SECRET_VALUE_PATTERNS):
            errors.append(f"secret_like_value:{path}.{key}")

    redaction = snapshot.get("redaction_report")
    if isinstance(redaction, dict):
        if redaction.get("scan_completed") is not True:
            errors.append("redaction_scan_not_completed")
        if redaction.get("forbidden_fields_detected") != []:
            errors.append("redaction_report_not_clean")

    versions = snapshot.get("client_package_versions")
    if isinstance(versions, dict):
        for name in REQUIRED_NESTED_FIELDS["client_package_versions"]:
            if name in versions and versions[name] is not None and not isinstance(versions[name], str):
                errors.append(f"invalid_package_version:{name}")

    status = snapshot.get("backend_status")
    if isinstance(status, dict):
        if status.get("operational") is not None and not isinstance(status.get("operational"), bool):
            errors.append("invalid_backend_status.operational")
        pending = status.get("pending_jobs")
        if pending is not None and (not isinstance(pending, int) or isinstance(pending, bool) or pending < 0):
            errors.append("invalid_backend_status.pending_jobs")

    target = snapshot.get("target_structure")
    if isinstance(target, dict):
        n = target.get("num_qubits")
        if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
            errors.append("invalid_num_qubits")
            n = None
        for key in ("basis_gates", "instruction_names"):
            value = target.get(key)
            if not isinstance(value, list) or not value or any(not isinstance(x, str) or not x.strip() for x in value):
                errors.append(f"invalid_nonempty_string_list:{key}")
        edges = target.get("coupling_edges")
        if not isinstance(edges, list):
            errors.append("invalid_coupling_edges")
        else:
            seen: set[tuple[int, int]] = set()
            for i, edge in enumerate(edges):
                if not isinstance(edge, (list, tuple)) or len(edge) != 2 or any(
                    not isinstance(endpoint, int) or isinstance(endpoint, bool) for endpoint in edge
                ):
                    errors.append(f"malformed_coupling_edge:{i}")
                    continue
                pair = (edge[0], edge[1])
                if pair in seen:
                    errors.append(f"duplicate_coupling_edge:{pair[0]}->{pair[1]}")
                seen.add(pair)
                if n is not None and any(endpoint < 0 or endpoint >= n for endpoint in pair):
                    errors.append(f"coupling_edge_out_of_range:{pair[0]}->{pair[1]}")
        indices = target.get("qubit_indices")
        if indices is not None:
            if not isinstance(indices, list) or any(
                not isinstance(i, int) or isinstance(i, bool) or i < 0 or (n is not None and i >= n)
                for i in indices
            ):
                errors.append("qubit_indices_out_of_range_or_malformed")
        measurement_map = target.get("measurement_map")
        if measurement_map is not None:
            if not isinstance(measurement_map, list) or any(
                not isinstance(i, int) or isinstance(i, bool) or i < 0 or (n is not None and i >= n)
                for i in measurement_map
            ):
                errors.append("measurement_map_out_of_range_or_malformed")

    try:
        captured = _parse_utc(snapshot.get("captured_at_utc"))
    except ValueError:
        captured = None
        errors.append("invalid_capture_timestamp")
    try:
        route_time = _parse_utc(route_build_time_utc)
    except ValueError:
        route_time = None
        errors.append("invalid_route_build_timestamp")
    if captured is not None and route_time is not None:
        age = (route_time - captured).total_seconds()
        if age < 0:
            errors.append("capture_after_route_build")
        elif age > MAX_AGE_SECONDS:
            errors.append("snapshot_stale")

    status = snapshot.get("backend_status")
    if isinstance(status, dict) and status.get("status_observed_at_utc") is not None:
        try:
            status_stamp = _parse_utc(status["status_observed_at_utc"])
            if captured is not None and status_stamp > captured:
                errors.append("status_observed_after_capture")
        except ValueError:
            errors.append("invalid_status_observed_timestamp")

    calibration = snapshot.get("calibration_provenance")
    if isinstance(calibration, dict) and captured is not None:
        for key in ("properties_last_update_utc_if_exposed", "target_last_update_utc_if_exposed"):
            value = calibration.get(key)
            if value is None:
                continue
            try:
                stamp = _parse_utc(value)
            except ValueError:
                errors.append(f"invalid_calibration_timestamp:{key}")
                continue
            if stamp > captured:
                errors.append(f"calibration_after_capture:{key}")

    try:
        observed_digest = snapshot_sha256(snapshot)
    except (TypeError, ValueError):
        observed_digest = None
        errors.append("canonical_serialization_failed")
    if not isinstance(recorded_sha256, str) or observed_digest != recorded_sha256:
        errors.append("snapshot_digest_mismatch")
    return sorted(set(errors))
