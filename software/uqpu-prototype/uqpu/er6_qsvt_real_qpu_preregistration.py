"""Build a fail-closed contract for a future bounded real-QPU pilot.

The contract intentionally authorizes no provider access or submission.  It
defines the evidence that must be supplied in a later, explicitly authorized
execution record.  Delta 20 remains simulation evidence and is used only as a
bound upstream reference; it is not promoted to hardware evidence here.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


WORK_ID = "QOS-AUDIT-010B23"
UPSTREAM_WORK_ID = "QOS-AUDIT-010B22"
ROOT = Path(__file__).resolve().parents[3]
UPSTREAM_CERTIFICATE = (
    ROOT / "benchmarks/results/cycle008-delta20-er6-qsvt-independent-routed-probe.json"
)
PERSISTED_PREREGISTRATION = (
    ROOT / "benchmarks/results/cycle008-delta21-er6-qsvt-real-qpu-preregistration.json"
)

REQUIRED_EXECUTION_FIELDS = [
    "provider",
    "target_id",
    "target_snapshot_timestamp_utc",
    "target_snapshot_sha256",
    "pricing_source_url",
    "pricing_observed_at_utc",
    "currency",
    "maximum_authorized_cost",
    "estimated_cost_before_submission",
    "actual_billable_cost",
    "job_ids",
    "shots_requested",
    "shots_completed",
    "queue_latency_seconds",
    "execution_latency_seconds",
    "end_to_end_latency_seconds",
    "host_preprocess_seconds",
    "host_postprocess_seconds",
    "host_peak_memory_bytes",
    "payload_bytes_sent",
    "result_bytes_received",
    "retry_count",
    "accepted_output_count",
    "quality_metric_name",
    "quality_metric_value",
    "quality_threshold",
    "quality_gate_passed",
    "energy_measurement_status",
]


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _sha256_json(value: Any) -> str:
    return _sha256_bytes(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    )


def build_preregistration() -> dict[str, Any]:
    upstream = json.loads(UPSTREAM_CERTIFICATE.read_text(encoding="utf-8"))
    if upstream.get("passed") is not True:
        raise ValueError("Delta 20 upstream certificate did not pass")
    if upstream.get("work_id") != UPSTREAM_WORK_ID:
        raise ValueError("Delta 20 upstream work ID mismatch")
    authorization = upstream["resources"]["authorization"]
    if any(
        authorization.get(key)
        for key in (
            "credentials_used",
            "live_service_initialized",
            "network_submission_attempted",
            "paid_execution_authorized",
            "provider_jobs",
            "shots",
        )
    ):
        raise ValueError("upstream certificate crossed the no-provider boundary")

    result: dict[str, Any] = {
        "schema": "uqpu-er6-qsvt-real-qpu-preregistration-v1",
        "work_id": WORK_ID,
        "upstream_work_id": UPSTREAM_WORK_ID,
        "date": "2026-10-19",
        "evidence_class": "MODEL_ONLY_PREREGISTRATION",
        "upstream": {
            "path": str(UPSTREAM_CERTIFICATE.relative_to(ROOT)),
            "sha256": _sha256_bytes(UPSTREAM_CERTIFICATE.read_bytes()),
            "target_identity_sha256": upstream["target_identity_sha256"],
            "evidence_class": upstream["evidence_class"],
        },
        "phases": [
            {
                "id": "NO_SUBMIT_PREFLIGHT",
                "provider_service_initialization": False,
                "network_submission": False,
                "paid_execution": False,
                "required_outputs": [
                    "provider_and_target_selected",
                    "fresh_target_snapshot_captured_and_hashed",
                    "target_specific_route_rebuilt",
                    "native_gate_and_topology_conformance_passed",
                    "ideal_reference_recomputed_for_exact_submitted_circuit",
                    "shot_plan_and_quality_threshold_frozen",
                    "pricing_source_and_cost_ceiling_frozen",
                ],
            },
            {
                "id": "AUTHORIZED_EXECUTION",
                "enabled": False,
                "enablement_requires_all": [
                    "explicit_user_consent_recorded",
                    "credentials_available_without_secret_capture",
                    "provider_target_and_region_fixed",
                    "maximum_jobs_fixed",
                    "maximum_shots_fixed",
                    "maximum_authorized_cost_fixed",
                    "estimated_cost_not_above_authorized_cost",
                    "NO_SUBMIT_PREFLIGHT_passed",
                ],
            },
        ],
        "authorization": {
            "explicit_user_consent_recorded": False,
            "credentials_used": False,
            "live_service_initialized": False,
            "network_submission_attempted": False,
            "paid_execution_authorized": False,
            "maximum_jobs": 0,
            "maximum_shots": 0,
            "maximum_authorized_cost": None,
            "currency": None,
        },
        "measurement_contract": {
            "same_provider_target_pricing_and_result_record_required": True,
            "cross_provider_probability_price_join_forbidden": True,
            "execution_success_is_not_quality_acceptance": True,
            "required_execution_fields": REQUIRED_EXECUTION_FIELDS,
            "quality_threshold_change_after_submission_forbidden": True,
            "accepted_useful_output_denominator": "accepted_output_count",
            "cost_per_accepted_useful_output_formula": (
                "actual_billable_cost / accepted_output_count"
            ),
            "zero_accepted_output_result": "REJECT_AND_REPORT_UNDEFINED_COST_PER_ACCEPTED_OUTPUT",
        },
        "stop_conditions": [
            "missing explicit consent or bounded budget",
            "estimated cost exceeds the authorized ceiling",
            "target snapshot or exact submitted circuit lacks a digest",
            "target-specific conformance failure",
            "pricing provenance missing or from another provider/target",
            "requested jobs or shots exceed the frozen ceilings",
            "any required execution field cannot be recorded",
        ],
        "nonclaims": [
            "not real-QPU execution or hardware-quality evidence",
            "not authorization to initialize a live provider service",
            "not authorization to submit a free or paid provider job",
            "not quantum advantage, GPU replacement, or Data-Center-to-Phone evidence",
            "not RAM, VRAM, storage, material, bio-oil, fusion, WACC, or new-law evidence",
            "Delta 20 saved-target simulation cannot substitute for a fresh live target snapshot",
        ],
    }
    result["contract_sha256"] = _sha256_json(result)
    return result


def validate_preregistration(contract: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if contract.get("work_id") != WORK_ID:
        errors.append("work_id")
    if contract.get("evidence_class") != "MODEL_ONLY_PREREGISTRATION":
        errors.append("evidence_class")
    phases = contract.get("phases", [])
    if [phase.get("id") for phase in phases] != [
        "NO_SUBMIT_PREFLIGHT",
        "AUTHORIZED_EXECUTION",
    ]:
        errors.append("phases")
    elif phases[1].get("enabled") is not False:
        errors.append("execution_enabled")
    authorization = contract.get("authorization", {})
    expected_disabled = {
        "explicit_user_consent_recorded": False,
        "credentials_used": False,
        "live_service_initialized": False,
        "network_submission_attempted": False,
        "paid_execution_authorized": False,
        "maximum_jobs": 0,
        "maximum_shots": 0,
        "maximum_authorized_cost": None,
        "currency": None,
    }
    if authorization != expected_disabled:
        errors.append("authorization")
    measurement = contract.get("measurement_contract", {})
    if measurement.get("required_execution_fields") != REQUIRED_EXECUTION_FIELDS:
        errors.append("required_execution_fields")
    if measurement.get("cross_provider_probability_price_join_forbidden") is not True:
        errors.append("cross_provider_join")
    if measurement.get("execution_success_is_not_quality_acceptance") is not True:
        errors.append("quality_gate")
    digest = contract.get("contract_sha256")
    body = {key: value for key, value in contract.items() if key != "contract_sha256"}
    if digest != _sha256_json(body):
        errors.append("contract_digest")
    return sorted(set(errors))
