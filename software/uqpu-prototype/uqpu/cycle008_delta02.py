"""Cycle 008 Delta 02: fail-closed cross-lane evidence gates.

These validators make the Cycle 008 work packet executable.  They validate
synthetic contracts and provenance; they do not create provider, material,
device, economic, or physical evidence.
"""

from __future__ import annotations

from datetime import date
from fractions import Fraction
import hashlib
import json
from typing import Any


LANES = ("A", "B", "C", "D", "E", "F", "G", "H", "FND/EQN", "SCM", "AI-COST", "QOS/QSVT")
DIMENSIONS = ("length", "mass", "time", "electric_current", "temperature",
              "amount_of_substance", "luminous_intensity", "currency",
              "information", "count")


def canonical_sha256(value: Any) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def validate_solver_comparison(rows: list[dict]) -> list[str]:
    errors: list[str] = []
    ids = []
    for index, row in enumerate(rows):
        prefix = f"row[{index}]"
        ids.append(row.get("fixture_id"))
        for field in ("fixture_id", "solver_id", "completion", "objective", "runtime_ns", "states_examined"):
            if row.get(field) is None:
                errors.append(f"{prefix}:{field}_missing")
        if row.get("completion") not in {"COMPLETE", "INCOMPLETE"}:
            errors.append(f"{prefix}:completion_invalid")
        if not isinstance(row.get("runtime_ns"), int) or isinstance(row.get("runtime_ns"), bool) or row.get("runtime_ns", 0) <= 0:
            errors.append(f"{prefix}:runtime_ns_invalid")
        if row.get("gpu_extrapolation") or row.get("qpu_extrapolation"):
            errors.append(f"{prefix}:hardware_extrapolation_forbidden")
    if len(ids) != len(set(ids)):
        errors.append("fixture_id_duplicate")
    return sorted(set(errors))


def validate_request_receipt(request: dict, receipt: dict | None) -> list[str]:
    errors = []
    request_hash = canonical_sha256(request)
    if request.get("submission_authorized") is not False:
        errors.append("submission_must_remain_disabled")
    if not request.get("idempotency_key"):
        errors.append("idempotency_key_missing")
    if receipt is not None:
        if receipt.get("request_sha256") != request_hash:
            errors.append("receipt_request_hash_mismatch")
        expected = canonical_sha256({key: value for key, value in receipt.items() if key != "receipt_sha256"})
        if receipt.get("receipt_sha256") != expected:
            errors.append("receipt_hash_mismatch")
        if receipt.get("idempotency_key") != request.get("idempotency_key"):
            errors.append("idempotency_replay_mismatch")
    return sorted(set(errors))


def validate_storage_measurement(record: dict) -> list[str]:
    errors = []
    required = ("platform", "filesystem", "process_mode", "cache_control_attempted", "device_flush_attested", "power_loss_tested")
    errors.extend(f"{field}_missing" for field in required if field not in record)
    if record.get("process_mode") not in {"FRESH_PROCESS", "REPEATED_PROCESS"}:
        errors.append("process_mode_invalid")
    if record.get("cache_label") in {"COLD", "WARM"} and not record.get("cache_control_attempted"):
        errors.append("cache_label_requires_control")
    return sorted(set(errors))


def full_download_decision(*, bytes_total: int, byte_limit: int, publisher_checksum: str | None, computed_checksum: str | None) -> dict:
    allowed = 0 < bytes_total <= byte_limit and bool(publisher_checksum)
    verified = allowed and computed_checksum is not None and computed_checksum == publisher_checksum
    return {"download_allowed": allowed, "checksum_verified": verified,
            "state": "VERIFIED" if verified else ("ALLOWED_NOT_VERIFIED" if allowed else "BLOCKED")}


def validate_material_measurement(record: dict) -> list[str]:
    required = ("function_id", "sample_lot_id", "control_lot_id", "value", "unit_code", "calibration_id", "uncertainty", "method_id")
    errors = [f"{field}_missing" for field in required if record.get(field) is None]
    if record.get("sample_lot_id") == record.get("control_lot_id"):
        errors.append("sample_control_collision")
    if not isinstance(record.get("uncertainty"), (int, float)) or isinstance(record.get("uncertainty"), bool) or record.get("uncertainty", -1) < 0:
        errors.append("uncertainty_invalid")
    return sorted(set(errors))


def validate_cost_interval(record: dict) -> list[str]:
    errors = []
    for field in ("currency", "amount_unit", "lower", "upper", "accepted_output_count", "accepted_output_provenance"):
        if record.get(field) is None:
            errors.append(f"{field}_missing")
    if record.get("currency") != record.get("amount_unit"):
        errors.append("currency_unit_mismatch")
    if isinstance(record.get("lower"), (int, float)) and isinstance(record.get("upper"), (int, float)) and record["lower"] > record["upper"]:
        errors.append("interval_inverted")
    if not isinstance(record.get("accepted_output_count"), int) or isinstance(record.get("accepted_output_count"), bool) or record.get("accepted_output_count", 0) <= 0:
        errors.append("accepted_output_count_invalid")
    return sorted(set(errors))


def validate_calibration_certificate(certificate: dict, *, as_of: date, required_scope: str) -> list[str]:
    errors = []
    for field in ("certificate_id", "scope_id", "valid_until", "uncertainty_budget", "issuer", "reviewer"):
        if not certificate.get(field):
            errors.append(f"{field}_missing")
    if certificate.get("scope_id") != required_scope:
        errors.append("scope_mismatch")
    try:
        if date.fromisoformat(certificate.get("valid_until", "")) < as_of:
            errors.append("certificate_expired")
    except (TypeError, ValueError):
        errors.append("valid_until_invalid")
    if certificate.get("issuer") == certificate.get("reviewer"):
        errors.append("issuer_reviewer_collision")
    if not isinstance(certificate.get("uncertainty_budget"), dict) or not certificate.get("uncertainty_budget"):
        errors.append("uncertainty_budget_invalid")
    return sorted(set(errors))


def rank_decisive_gates(gates: list[dict]) -> list[dict]:
    required = {"gate_id", "sensitivity_abs", "evidence_gap", "falsifier"}
    if any(not required.issubset(gate) for gate in gates):
        raise ValueError("decisive gate fields incomplete")
    return sorted(gates, key=lambda row: (-row["sensitivity_abs"], row["gate_id"]))


def validate_dimension_equation(terms: list[dict]) -> list[str]:
    errors = []
    vectors = []
    for index, term in enumerate(terms):
        vector = term.get("dimension_vector")
        if not term.get("quantity_kind") or not term.get("unit_code"):
            errors.append(f"term[{index}]:classification_missing")
        if not isinstance(vector, dict) or set(vector) != set(DIMENSIONS):
            errors.append(f"term[{index}]:dimension_vector_invalid")
            continue
        try:
            vectors.append(tuple(Fraction(vector[key]) for key in DIMENSIONS))
        except (ValueError, ZeroDivisionError, TypeError):
            errors.append(f"term[{index}]:dimension_vector_invalid")
    if vectors and any(vector != vectors[0] for vector in vectors[1:]):
        errors.append("equation_dimension_mismatch")
    return sorted(set(errors))


def validate_fictional_state(record: dict) -> list[str]:
    errors = []
    if record.get("domain") != "FICTIONAL_PROTOCOL":
        errors.append("fictional_domain_required")
    if record.get("real_world_coupling") is not None:
        errors.append("real_world_coupling_must_be_null")
    if record.get("human_study_authorized") is not False:
        errors.append("human_study_must_be_disabled")
    if record.get("consent_state") != "NOT_APPLICABLE_FICTIONAL":
        errors.append("fictional_consent_state_invalid")
    quantities = record.get("quantities", {})
    if sum(quantities.get("inputs", [])) != sum(quantities.get("outputs", [])):
        errors.append("fictional_conservation_failed")
    return sorted(set(errors))


def validate_ai_candidate(candidate: dict) -> list[str]:
    errors = []
    for field in ("candidate_id", "train_hash", "heldout_hash", "quality", "runtime_ns", "energy_j", "cost"):
        if candidate.get(field) is None:
            errors.append(f"{field}_missing")
    if candidate.get("train_hash") == candidate.get("heldout_hash"):
        errors.append("train_heldout_leakage")
    return sorted(set(errors))


def validate_qos_certificate(certificate: dict) -> list[str]:
    errors = []
    required = ("contract_id", "source_semantics_sha256", "lowered_semantics_sha256", "logical_qubits", "two_qubit_gates", "measurements")
    errors.extend(f"{field}_missing" for field in required if certificate.get(field) is None)
    if certificate.get("source_semantics_sha256") != certificate.get("lowered_semantics_sha256"):
        errors.append("semantic_equivalence_failed")
    if certificate.get("provider_execution_id") is not None or certificate.get("provider_cost") is not None:
        errors.append("provider_fields_must_be_null")
    return sorted(set(errors))


def build_integrated_checkpoint() -> dict:
    """Return the deterministic, synthetic Cycle 008 gate checkpoint."""
    zero = {axis: "0" for axis in DIMENSIONS}
    fixtures = {
        "A": validate_solver_comparison([{"fixture_id": "f8", "solver_id": "exact-control", "completion": "COMPLETE", "objective": -65, "runtime_ns": 1, "states_examined": 256}]),
        "B": validate_request_receipt({"idempotency_key": "SYNTHETIC-008", "submission_authorized": False}, None),
        "C": validate_storage_measurement({"platform": "portable", "filesystem": "unspecified", "process_mode": "FRESH_PROCESS", "cache_control_attempted": False, "device_flush_attested": False, "power_loss_tested": False}),
        "D": [] if full_download_decision(bytes_total=145469232, byte_limit=1000000, publisher_checksum="md5:publisher-only", computed_checksum=None)["state"] == "BLOCKED" else ["guard_failed"],
        "E": validate_material_measurement({"function_id": "conductivity", "sample_lot_id": "SYNTHETIC-S", "control_lot_id": "SYNTHETIC-C", "value": 1, "unit_code": "S/m", "calibration_id": "SYNTHETIC-CAL", "uncertainty": 0.1, "method_id": "SYNTHETIC-M"}),
        "F": validate_cost_interval({"currency": "USD", "amount_unit": "USD", "lower": 1, "upper": 2, "accepted_output_count": 1, "accepted_output_provenance": "synthetic://accepted/1"}),
        "G": validate_calibration_certificate({"certificate_id": "SYNTHETIC-CAL", "scope_id": "SYNTHETIC-SCOPE", "valid_until": "2027-01-01", "uncertainty_budget": {"type_b": 0.1}, "issuer": "issuer", "reviewer": "reviewer"}, as_of=date(2026, 10, 15), required_scope="SYNTHETIC-SCOPE"),
        "H": [] if rank_decisive_gates([{"gate_id": "G1", "sensitivity_abs": 1.0, "evidence_gap": "real data", "falsifier": "measured failure"}])[0]["gate_id"] == "G1" else ["rank_failed"],
        "FND/EQN": validate_dimension_equation([{"quantity_kind": "count", "unit_code": "1", "dimension_vector": zero}, {"quantity_kind": "count", "unit_code": "1", "dimension_vector": zero}]),
        "SCM": validate_fictional_state({"domain": "FICTIONAL_PROTOCOL", "real_world_coupling": None, "human_study_authorized": False, "consent_state": "NOT_APPLICABLE_FICTIONAL", "quantities": {"inputs": [1, 2], "outputs": [3]}}),
        "AI-COST": validate_ai_candidate({"candidate_id": "SYNTHETIC-AI", "train_hash": "a", "heldout_hash": "b", "quality": 0, "runtime_ns": 1, "energy_j": 0, "cost": 0}),
        "QOS/QSVT": validate_qos_certificate({"contract_id": "ER6", "source_semantics_sha256": "a", "lowered_semantics_sha256": "a", "logical_qubits": 1, "two_qubit_gates": 0, "measurements": 1, "provider_execution_id": None, "provider_cost": None}),
    }
    return {
        "schema": "uqpu-cycle008-delta02-integrated-gates-v1",
        "date": "2026-10-15",
        "evidence_class": "SYNTHETIC_SCHEMA_AND_NEGATIVE_TEST_EVIDENCE",
        "lane_count": len(LANES),
        "lanes": {lane: {"passing": not errors, "errors": errors} for lane, errors in fixtures.items()},
        "all_synthetic_gates_pass": all(not errors for errors in fixtures.values()),
        "capital_amount": None,
        "owner_authorization": False,
        "provider_submission_authorized": False,
        "nonclaims": [
            "No real-QPU, provider, material, fuel, fusion, factory, or economic result.",
            "No quantum advantage, GPU replacement, physical law, or Data-Center-to-Phone result.",
            "SCM remains a fictional protocol domain with no human study or real-world coupling.",
        ],
    }
