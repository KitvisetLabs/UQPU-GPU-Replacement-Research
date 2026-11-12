"""Fail-closed provenance contract for provider-matched QPU execution records.

This module validates record structure and identity consistency only. It does not
contact a provider, verify a bill, certify a result, or promote evidence.
"""
from __future__ import annotations

from datetime import datetime, timezone
import math
import re
from typing import Any, Mapping
from urllib.parse import urlparse

SCHEMA = "uqpu-provider-matched-execution-record-v1"
EVIDENCE_CLASSES = {
    "REAL_QPU",
    "SIMULATION",
    "MODEL_ONLY",
    "DRY_RUN",
    "SYNTHETIC_TEST_FIXTURE",
    "LITERATURE_ONLY",
}
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
CURRENCY_RE = re.compile(r"^[A-Z]{3}$")
IDENTITY_FIELDS = (
    "provider",
    "target_id",
    "region",
    "execution_route_id",
    "workload_contract_id",
    "circuit_sha256",
    "target_snapshot_sha256",
    "target_snapshot_timestamp_utc",
)
EXECUTION_FIELDS = (
    *IDENTITY_FIELDS,
    "calibration_snapshot_sha256",
    "calibration_timestamp_utc",
    "shots_requested",
    "shots_completed",
    "job_ids",
    "queue_latency_seconds",
    "execution_latency_seconds",
    "end_to_end_latency_seconds",
    "host_preprocess_seconds",
    "host_postprocess_seconds",
    "host_peak_memory_bytes",
    "payload_bytes_sent",
    "result_bytes_received",
    "retry_count",
    "energy_measurement_status",
    "energy_joules",
)
QUALITY_FIELDS = (
    *IDENTITY_FIELDS,
    "calibration_snapshot_sha256",
    "calibration_timestamp_utc",
    "success_probability",
    "accepted_output_count",
    "quality_metric_name",
    "quality_metric_value",
    "quality_threshold",
    "quality_direction",
    "quality_gate_passed",
)
BILLING_FIELDS = (
    *IDENTITY_FIELDS,
    "job_ids",
    "pricing_source_url",
    "pricing_observed_at_utc",
    "pricing_record_sha256",
    "currency",
    "actual_billable_cost",
)
UTC_FIELDS = (
    ("execution", "target_snapshot_timestamp_utc"),
    ("execution", "calibration_timestamp_utc"),
    ("quality", "target_snapshot_timestamp_utc"),
    ("quality", "calibration_timestamp_utc"),
    ("billing", "target_snapshot_timestamp_utc"),
    ("billing", "pricing_observed_at_utc"),
)
HASH_FIELDS = (
    ("execution", "circuit_sha256"),
    ("execution", "target_snapshot_sha256"),
    ("execution", "calibration_snapshot_sha256"),
    ("quality", "circuit_sha256"),
    ("quality", "target_snapshot_sha256"),
    ("quality", "calibration_snapshot_sha256"),
    ("billing", "circuit_sha256"),
    ("billing", "target_snapshot_sha256"),
    ("billing", "pricing_record_sha256"),
)


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _utc_timestamp(value: Any) -> bool:
    if not isinstance(value, str) or not value.endswith("Z"):
        return False
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return False
    return parsed.tzinfo is not None and parsed.utcoffset() == timezone.utc.utcoffset(parsed)


def _finite_number(value: Any) -> bool:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        return False
    try:
        return math.isfinite(float(value))
    except (OverflowError, ValueError):
        return False


def _nonnegative_integer(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def validate_execution_record(record: Mapping[str, Any]) -> list[str]:
    """Return stable validation error codes; an empty list means schema-consistent.

    The function does not establish that any supplied evidence is authentic.
    """
    if not isinstance(record, Mapping):
        return ["record_type"]

    errors: list[str] = []
    if "cost_per_accepted_useful_output" not in record:
        errors.append("missing:cost_per_accepted_useful_output")
    if record.get("schema") != SCHEMA:
        errors.append("schema")
    if record.get("evidence_class") not in EVIDENCE_CLASSES:
        errors.append("evidence_class")

    sections: dict[str, Mapping[str, Any]] = {}
    for name, required in (
        ("execution", EXECUTION_FIELDS),
        ("quality", QUALITY_FIELDS),
        ("billing", BILLING_FIELDS),
    ):
        value = record.get(name)
        if not isinstance(value, Mapping):
            errors.append(f"{name}_section")
            sections[name] = {}
            continue
        sections[name] = value
        for field in required:
            if field not in value:
                errors.append(f"missing:{name}.{field}")

    for field in IDENTITY_FIELDS:
        values = [sections[name].get(field) for name in ("execution", "quality", "billing")]
        if any(not _nonempty_string(value) for value in values):
            errors.append(f"identity_missing:{field}")
        elif not (values[0] == values[1] == values[2]):
            for name in ("quality", "billing"):
                if sections[name].get(field) != values[0]:
                    errors.append(f"identity_mismatch:{field}:{name}")

    for section, field in UTC_FIELDS:
        if not _utc_timestamp(sections[section].get(field)):
            errors.append(f"timestamp:{section}.{field}")

    for section, field in HASH_FIELDS:
        value = sections[section].get(field)
        if not isinstance(value, str) or not SHA256_RE.fullmatch(value):
            errors.append(f"sha256:{section}.{field}")

    for section in ("execution", "quality", "billing"):
        value = sections[section]
        for field in ("provider", "target_id", "region", "execution_route_id", "workload_contract_id"):
            if field in value and not _nonempty_string(value[field]):
                errors.append(f"nonempty:{section}.{field}")

    if not _nonempty_string(sections["quality"].get("quality_metric_name")):
        errors.append("quality_metric_name")

    for field in ("calibration_snapshot_sha256", "calibration_timestamp_utc"):
        if sections["execution"].get(field) != sections["quality"].get(field):
            errors.append(f"calibration_mismatch:{field}")

    execution_jobs = sections["execution"].get("job_ids")
    billing_jobs = sections["billing"].get("job_ids")
    for section, jobs in (("execution", execution_jobs), ("billing", billing_jobs)):
        if (
            not isinstance(jobs, list)
            or not jobs
            or any(not _nonempty_string(job) for job in jobs)
            or len(set(jobs)) != len(jobs)
        ):
            errors.append(f"job_ids:{section}")
    if isinstance(execution_jobs, list) and isinstance(billing_jobs, list) and execution_jobs != billing_jobs:
        errors.append("job_ids_mismatch")

    execution = sections["execution"]
    for field in ("shots_requested", "shots_completed", "host_peak_memory_bytes",
                  "payload_bytes_sent", "result_bytes_received", "retry_count"):
        if not _nonnegative_integer(execution.get(field)):
            errors.append(f"integer:{field}")
    if (
        _nonnegative_integer(execution.get("shots_requested"))
        and _nonnegative_integer(execution.get("shots_completed"))
        and execution["shots_completed"] > execution["shots_requested"]
    ):
        errors.append("shots_completed_exceeds_requested")

    for field in ("queue_latency_seconds", "execution_latency_seconds", "end_to_end_latency_seconds",
                  "host_preprocess_seconds", "host_postprocess_seconds"):
        value = execution.get(field)
        if not _finite_number(value) or value < 0:
            errors.append(f"nonnegative_number:{field}")

    energy_status = execution.get("energy_measurement_status")
    energy = execution.get("energy_joules")
    if energy_status not in {"MEASURED", "ESTIMATED", "NOT_MEASURED", "UNAVAILABLE"}:
        errors.append("energy_measurement_status")
    elif energy_status in {"MEASURED", "ESTIMATED"}:
        if not _finite_number(energy) or energy < 0:
            errors.append("energy_joules")
    elif energy is not None:
        errors.append("energy_joules_must_be_null_when_unmeasured")

    quality = sections["quality"]
    probability = quality.get("success_probability")
    if not _finite_number(probability) or not 0 <= float(probability) <= 1:
        errors.append("success_probability")
    accepted = quality.get("accepted_output_count")
    if not _nonnegative_integer(accepted):
        errors.append("accepted_output_count")
    elif _nonnegative_integer(execution.get("shots_completed")) and accepted > execution["shots_completed"]:
        errors.append("accepted_outputs_exceed_shots")

    for field in ("quality_metric_value", "quality_threshold"):
        if not _finite_number(quality.get(field)):
            errors.append(f"finite_number:{field}")
    direction = quality.get("quality_direction")
    if direction not in {"MIN", "MAX"}:
        errors.append("quality_direction")
    passed = quality.get("quality_gate_passed")
    if not isinstance(passed, bool):
        errors.append("quality_gate_passed")
    elif direction in {"MIN", "MAX"} and _finite_number(quality.get("quality_metric_value")) and _finite_number(quality.get("quality_threshold")):
        measured = float(quality["quality_metric_value"])
        threshold = float(quality["quality_threshold"])
        expected_pass = measured <= threshold if direction == "MIN" else measured >= threshold
        if passed != expected_pass:
            errors.append("quality_gate_inconsistent")
    if _nonnegative_integer(accepted) and isinstance(passed, bool):
        if accepted > 0 and not passed:
            errors.append("accepted_outputs_without_quality_pass")
        if accepted == 0 and passed:
            errors.append("quality_pass_without_accepted_outputs")
        if accepted > 0 and _finite_number(probability) and float(probability) == 0:
            errors.append("accepted_outputs_with_zero_probability")

    billing = sections["billing"]
    cost = billing.get("actual_billable_cost")
    if not _finite_number(cost) or cost < 0:
        errors.append("actual_billable_cost")
    currency = billing.get("currency")
    if not isinstance(currency, str) or not CURRENCY_RE.fullmatch(currency):
        errors.append("currency")
    source_url = billing.get("pricing_source_url")
    parsed_url = urlparse(source_url) if isinstance(source_url, str) else None
    if parsed_url is None or parsed_url.scheme != "https" or not parsed_url.netloc:
        errors.append("pricing_source_url")

    reported = record.get("cost_per_accepted_useful_output")
    if _nonnegative_integer(accepted) and accepted == 0:
        if reported is not None:
            errors.append("undefined_cost_must_be_null")
    elif _nonnegative_integer(accepted) and accepted > 0 and _finite_number(cost):
        expected = float(cost) / accepted
        if not _finite_number(reported) or not math.isclose(float(reported), expected, rel_tol=1e-9, abs_tol=1e-12):
            errors.append("cost_per_accepted_output_mismatch")

    return sorted(set(errors))


def billable_cost_per_accepted_output(record: Mapping[str, Any]) -> float | None:
    """Compute actual billable cost per accepted output, or None if none passed.

    This is arithmetic on a validated record, not a judgment that its evidence
    class or source data are authentic or scientifically sufficient.
    """
    errors = validate_execution_record(record)
    if errors:
        raise ValueError("invalid execution record: " + ",".join(errors))
    accepted = record["quality"]["accepted_output_count"]
    if accepted == 0:
        return None
    return float(record["billing"]["actual_billable_cost"]) / accepted
