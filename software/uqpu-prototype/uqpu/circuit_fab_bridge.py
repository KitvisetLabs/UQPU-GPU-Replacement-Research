"""Fail-closed bridge from circuit resource reports to device/fab/economic review.

Completeness validation only. A ready status is not a physical or economic claim.
"""
from __future__ import annotations

import math
import re
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_ALLOWED_EVIDENCE = {
    "CONCEPT",
    "THEORY",
    "LITERATURE_ONLY",
    "MODEL_ONLY",
    "SIMULATION",
    "LAB_RESULT",
    "PUBLISHED_EXPERIMENT",
    "HARDWARE_MEASURED",
}
_ALLOWED_EQUIVALENCE = {"PASS_INDEPENDENT", "PASS_SAME_IMPLEMENTATION", "NOT_RUN", "FAIL"}

_STAGE_FIELDS = (
    (
        "CIRCUIT_CERTIFICATE",
        (
            "workload_contract_id",
            "quality_contract_id",
            "candidate_circuit_sha256",
            "reference_circuit_sha256",
            "evidence_class",
            "equivalence_status",
            "output_equivalence_certificate_id",
            "logical_qubits",
            "native_gate_counts",
            "routed_depth",
            "shots_per_accepted_task",
        ),
    ),
    (
        "TARGET_MAPPING",
        (
            "target_id",
            "target_snapshot_sha256",
            "calibration_snapshot_id",
            "native_gate_set_id",
            "routing_profile_id",
            "qec_profile_id",
            "physical_qubits",
            "readout_profile_id",
            "control_power_w",
            "cryogenic_load_w",
            "latency_s",
        ),
    ),
    (
        "DEVICE_PROCESS",
        (
            "device_architecture_id",
            "process_window_id",
            "yield_fraction",
            "fab_cost_per_good_die_usd",
            "package_test_cost_per_device_usd",
            "lifetime_tasks_per_device",
        ),
    ),
    (
        "LIFECYCLE_ECONOMICS",
        (
            "uqpu_cost_target_id",
            "baseline_stack_id",
            "baseline_workload_contract_id",
            "baseline_quality_contract_id",
            "measurement_window_id",
            "baseline_measurement_window_id",
            "provider_cost_per_task_usd",
            "host_cost_per_task_usd",
            "energy_kwh_per_task",
            "maintenance_cost_per_task_usd",
            "reconstruction_cost_per_task_usd",
            "baseline_cost_per_task_usd",
            "uqpu_cost_per_task_usd",
            "accepted_output_count",
            "uncertainty_manifest_id",
        ),
    ),
)

_POSITIVE_NUMBERS = {
    "logical_qubits",
    "routed_depth",
    "shots_per_accepted_task",
    "physical_qubits",
    "latency_s",
    "lifetime_tasks_per_device",
    "baseline_cost_per_task_usd",
    "uqpu_cost_per_task_usd",
    "accepted_output_count",
}
_NONNEGATIVE_NUMBERS = {
    "control_power_w",
    "cryogenic_load_w",
    "fab_cost_per_good_die_usd",
    "package_test_cost_per_device_usd",
    "provider_cost_per_task_usd",
    "host_cost_per_task_usd",
    "energy_kwh_per_task",
    "maintenance_cost_per_task_usd",
    "reconstruction_cost_per_task_usd",
}
_HASH_FIELDS = {
    "candidate_circuit_sha256",
    "reference_circuit_sha256",
    "target_snapshot_sha256",
}


@dataclass(frozen=True)
class BridgeAssessment:
    status: str
    first_blocked_stage: str | None
    missing_fields: tuple[str, ...]
    context_mismatches: tuple[str, ...]
    evidence_class: str | None
    claim_boundary: str = (
        "Completeness and input-sanity gate only; no physical advantage, "
        "fabrication feasibility, memory equivalence, or economic advantage is established."
    )

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "first_blocked_stage": self.first_blocked_stage,
            "missing_fields": list(self.missing_fields),
            "context_mismatches": list(self.context_mismatches),
            "evidence_class": self.evidence_class,
            "claim_boundary": self.claim_boundary,
        }


def _missing(payload: Mapping[str, Any], field: str) -> bool:
    if field not in payload or payload[field] is None:
        return True
    value = payload[field]
    if isinstance(value, str) and not value.strip():
        return True
    if isinstance(value, Mapping) and not value:
        return True
    return False


def _require_int(name: str, value: Any, *, positive: bool) -> None:
    if type(value) is not int or (value <= 0 if positive else value < 0):
        relation = "positive integer" if positive else "non-negative integer"
        raise ValueError(f"{name} must be a {relation}")


def _require_number(name: str, value: Any, *, positive: bool) -> None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be numeric")
    number = float(value)
    if not math.isfinite(number) or (number <= 0 if positive else number < 0):
        relation = "finite and > 0" if positive else "finite and >= 0"
        raise ValueError(f"{name} must be {relation}")


def _validate_present_values(payload: Mapping[str, Any]) -> None:
    evidence = payload.get("evidence_class")
    if evidence is not None and evidence not in _ALLOWED_EVIDENCE:
        raise ValueError(f"unsupported evidence_class: {evidence}")

    equivalence = payload.get("equivalence_status")
    if equivalence is not None and equivalence not in _ALLOWED_EQUIVALENCE:
        raise ValueError(f"unsupported equivalence_status: {equivalence}")

    for field in _HASH_FIELDS:
        value = payload.get(field)
        if value is not None and (not isinstance(value, str) or not _SHA256.fullmatch(value)):
            raise ValueError(f"{field} must be a lowercase SHA-256 hex digest")

    for field in _POSITIVE_NUMBERS:
        if field in payload and payload[field] is not None:
            _require_int(field, payload[field], positive=True) if field in {
                "logical_qubits", "routed_depth", "shots_per_accepted_task",
                "physical_qubits", "accepted_output_count",
            } else _require_number(field, payload[field], positive=True)

    for field in _NONNEGATIVE_NUMBERS:
        if field in payload and payload[field] is not None:
            _require_number(field, payload[field], positive=False)

    if "native_gate_counts" in payload and payload["native_gate_counts"] is not None:
        counts = payload["native_gate_counts"]
        if not isinstance(counts, Mapping) or not counts:
            raise ValueError("native_gate_counts must be a non-empty mapping")
        for gate, count in counts.items():
            if not isinstance(gate, str) or not gate.strip():
                raise ValueError("native gate names must be non-empty strings")
            _require_int(f"native_gate_counts[{gate}]", count, positive=False)

    if "yield_fraction" in payload and payload["yield_fraction"] is not None:
        value = payload["yield_fraction"]
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("yield_fraction must be numeric")
        value = float(value)
        if not math.isfinite(value) or not 0 < value <= 1:
            raise ValueError("yield_fraction must be finite and in (0, 1]")


def _context_mismatches(payload: Mapping[str, Any]) -> tuple[str, ...]:
    checks = (
        ("uqpu_cost_target_id", "target_id"),
        ("baseline_workload_contract_id", "workload_contract_id"),
        ("baseline_quality_contract_id", "quality_contract_id"),
        ("baseline_measurement_window_id", "measurement_window_id"),
    )
    mismatches = []
    for left, right in checks:
        if left in payload and right in payload and payload[left] and payload[right]:
            if payload[left] != payload[right]:
                mismatches.append(f"{left}!={right}")
    return tuple(mismatches)


def assess_circuit_fab_bridge(payload: Mapping[str, Any]) -> BridgeAssessment:
    """Return the first missing/failed integration stage without promoting claims."""
    if not isinstance(payload, Mapping):
        raise TypeError("payload must be a mapping")
    _validate_present_values(payload)
    evidence = payload.get("evidence_class")
    mismatches = _context_mismatches(payload)
    if mismatches:
        return BridgeAssessment(
            "REJECTED_CONTEXT_MISMATCH", None, (), mismatches, evidence
        )

    for stage, fields in _STAGE_FIELDS:
        missing = tuple(field for field in fields if _missing(payload, field))
        if missing:
            return BridgeAssessment(
                f"BLOCKED_{stage}", stage, missing, (), evidence
            )
        if stage == "CIRCUIT_CERTIFICATE":
            if payload["equivalence_status"] != "PASS_INDEPENDENT":
                return BridgeAssessment(
                    "BLOCKED_EQUIVALENCE", stage, (), (), evidence
                )
            if payload["output_equivalence_certificate_id"] in {
                "NOT_RUN", "UNVERIFIED", "MODEL_ONLY"
            }:
                return BridgeAssessment(
                    "BLOCKED_EQUIVALENCE", stage,
                    ("independent output-equivalence certificate",), (), evidence
                )

    return BridgeAssessment("READY_FOR_INTEGRATION_REVIEW", None, (), (), evidence)
