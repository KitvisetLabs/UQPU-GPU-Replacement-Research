"""Cycle 008 executable protocol gates for non-mathematical tracked lanes.

Measurements are limited to seeded local software and local filesystem probes;
positive provider/material/cost/capital records are synthetic only.
"""
from __future__ import annotations

from datetime import date
from decimal import Decimal, InvalidOperation
import math
from typing import Any

from .cycle003_delta01 import canonical_json_bytes
from .cycle005_delta01 import benchmark_scale_case
import hashlib


def _hash(value: Any) -> str:
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def _nonnegative(value: Any) -> bool:
    return isinstance(value, (int, float, Decimal)) and not isinstance(value, bool) and math.isfinite(float(value)) and value >= 0


def compare_deterministic_solver_restarts(*, node_count: int = 12, seed: int = 80812) -> dict:
    """Compare deterministic greedy restart budgets against complete enumeration."""
    rows = [benchmark_scale_case(node_count, seed, max_states=1 << node_count,
                                 deadline_seconds=30, heuristic_restarts=n)
            for n in (32, 128)]
    fields = ("complete", "states_evaluated", "total_state_space", "best_objective")
    if any(row["exact"][key] != rows[0]["exact"][key] for row in rows[1:] for key in fields):
        raise ValueError("exact-control fixture drift")
    if any(row["node_count"] != node_count or row["seed"] != seed for row in rows):
        raise ValueError("solver fixture identity drift")
    if any(row["heuristic"]["objective"] < row["exact"]["best_objective"] - 1e-12 for row in rows):
        raise ValueError("heuristic beats declared complete optimum")
    return {
        "schema": "uqpu-cycle008-solver-restart-comparison-v1",
        "fixture": {"node_count": node_count, "seed": seed, "generator": rows[0]["generator"]},
        "exact_control": {key: rows[0]["exact"][key] for key in fields},
        "solver_variants": [{
            "method": row["heuristic"]["method"], "restarts": row["heuristic"]["restarts"],
            "objective": row["heuristic"]["objective"],
            "elapsed_seconds": row["heuristic"]["elapsed_seconds"],
            "gap_to_exact": row["heuristic"]["objective_gap_to_exact"],
        } for row in rows],
        "evidence_class": "LOCAL_SEEDED_CLASSICAL_SOFTWARE_COMPARISON",
        "nonclaims": ["One finite generated instance only.", "No scaling-law inference.", "No GPU/QPU/energy result."],
    }


def seal_synthetic_request_receipt(request: dict, receipt: dict) -> dict:
    request_hash = _hash(request)
    receipt_hash = _hash({"request_sha256": request_hash, "receipt": receipt})
    return {"request": request, "request_sha256": request_hash, "receipt": receipt,
            "receipt_envelope_sha256": receipt_hash, "submission_performed": False,
            "provider_task_id": None, "provider_bill_id": None,
            "evidence_class": "SYNTHETIC_PROVENANCE_SCHEMA_FIXTURE"}


def validate_request_receipt_link(envelope: dict) -> list[str]:
    request, receipt = envelope.get("request"), envelope.get("receipt")
    if not isinstance(request, dict) or not isinstance(receipt, dict):
        return ["request_or_receipt_missing"]
    errors = []
    request_hash = _hash(request)
    if envelope.get("request_sha256") != request_hash:
        errors.append("request_hash_mismatch")
    if envelope.get("receipt_envelope_sha256") != _hash({"request_sha256": request_hash, "receipt": receipt}):
        errors.append("receipt_envelope_hash_mismatch")
    if not request.get("client_token"):
        errors.append("client_token_missing")
    if envelope.get("submission_performed") is not False:
        errors.append("synthetic_fixture_must_not_submit")
    if envelope.get("provider_task_id") is not None or envelope.get("provider_bill_id") is not None:
        errors.append("physical_provider_fields_must_be_null")
    return errors


def validate_idempotent_replay(original: dict, replay: dict) -> list[str]:
    errors = []
    if original.get("client_token") != replay.get("client_token"):
        errors.append("client_token_changed")
    if _hash(original) != _hash(replay):
        errors.append("request_payload_changed_under_replay")
    return errors


def validate_io_claim(record: dict) -> list[str]:
    errors = []
    if record.get("process_scope") not in {"FRESH_PROCESS", "SAME_PROCESS"}:
        errors.append("process_scope_invalid")
    state = record.get("cache_state")
    if state not in {"UNCONTROLLED", "COLD_CONTROLLED", "WARM_CONTROLLED"}:
        errors.append("cache_state_required")
    if state != "UNCONTROLLED" and record.get("cache_control_verified") is not True:
        errors.append("cache_label_without_control")
    if record.get("device_flush_claim") and record.get("device_flush_attestation") is not True:
        errors.append("device_flush_claim_unattested")
    if record.get("power_loss_claim") and record.get("power_loss_tested") is not True:
        errors.append("power_loss_claim_untested")
    return errors


def plan_archive_integrity(*, expected_bytes: int, max_download_bytes: int,
                           download_authorized: bool = False) -> dict:
    if type(expected_bytes) is not int or expected_bytes < 1 or type(max_download_bytes) is not int or max_download_bytes < 0:
        raise ValueError("archive sizes must be positive/ non-negative integers")
    if expected_bytes > max_download_bytes:
        state = "BLOCKED_RESOURCE_CAP"
    elif download_authorized:
        state = "READY_NOT_EXECUTED"
    else:
        state = "BLOCKED_NOT_AUTHORIZED"
    return {"state": state, "expected_bytes": expected_bytes, "max_download_bytes": max_download_bytes,
            "download_attempted": False, "full_archive_sha256": None, "payload_read": False,
            "evidence_class": "RESOURCE_GUARDED_RETRIEVAL_PLAN_ONLY"}


def validate_material_measurement_record(record: dict) -> list[str]:
    required = ("sample_lot_id", "control_id", "measurand", "unit_code", "method_id",
                "calibration_certificate_id", "standard_uncertainty", "uncertainty_unit_code", "evidence_class")
    errors = [f"{field}_missing" for field in required if record.get(field) in (None, "")]
    if record.get("unit_code") != record.get("uncertainty_unit_code"):
        errors.append("uncertainty_unit_mismatch")
    if not _nonnegative(record.get("standard_uncertainty")):
        errors.append("standard_uncertainty_invalid")
    if record.get("sample_lot_id") == record.get("control_id"):
        errors.append("sample_control_identity_collision")
    return errors


def cost_interval_per_accepted_output(components: list[dict], *, currency: str,
                                      accepted_outputs: int) -> dict:
    errors, lows, highs = [], [], []
    if not currency:
        errors.append("currency_missing")
    if type(accepted_outputs) is not int or accepted_outputs < 1:
        errors.append("accepted_output_count_invalid")
    for index, row in enumerate(components):
        if row.get("currency") != currency or row.get("unit_code") != currency:
            errors.append(f"component_currency_or_unit_mismatch:{index}")
        try:
            low, high = Decimal(str(row.get("lower"))), Decimal(str(row.get("upper")))
        except (InvalidOperation, TypeError):
            errors.append(f"component_interval_invalid:{index}")
            continue
        if not low.is_finite() or not high.is_finite() or low < 0 or high < low:
            errors.append(f"component_interval_invalid:{index}")
            continue
        lows.append(low)
        highs.append(high)
    complete = not errors and len(lows) == len(components)
    low_total, high_total = (sum(lows, Decimal(0)), sum(highs, Decimal(0))) if complete else (None, None)
    return {"complete": complete, "errors": errors, "currency": currency if complete else None,
            "total_interval": [str(low_total), str(high_total)] if complete else None,
            "per_accepted_output_interval": [str(low_total / accepted_outputs), str(high_total / accepted_outputs)] if complete else None,
            "evidence_class": "SYNTHETIC_COST_INTERVAL_SCHEMA_TEST"}


def validate_calibration_certificate(record: dict, *, as_of: date) -> list[str]:
    fields = ("certificate_id", "issuer", "instrument_id", "method_scope_id", "valid_from", "valid_until", "uncertainty_budget")
    errors = [f"{field}_missing" for field in fields if record.get(field) in (None, "")]
    try:
        start, end = date.fromisoformat(record["valid_from"]), date.fromisoformat(record["valid_until"])
    except (KeyError, TypeError, ValueError):
        return errors + ["certificate_date_invalid"]
    if start > as_of or end < as_of:
        errors.append("certificate_out_of_validity_window")
    budget = record.get("uncertainty_budget")
    if not isinstance(budget, list) or not budget:
        errors.append("uncertainty_budget_empty")
    elif any(not row.get("component") or not row.get("unit_code") or not _nonnegative(row.get("standard_uncertainty")) for row in budget):
        errors.append("uncertainty_component_invalid")
    return errors


def rank_decisive_gates(gates: list[dict]) -> dict:
    rows = []
    for gate in gates:
        effort, reduction = gate.get("effort_cost_sensitivity"), gate.get("blocker_reduction_sensitivity")
        if not gate.get("gate_id") or not isinstance(effort, dict) or not isinstance(reduction, dict):
            raise ValueError("gate ID and low/base/high assumptions are required")
        if any(not _nonnegative(effort.get(k)) or effort[k] == 0 for k in ("low", "base", "high")):
            raise ValueError("effort assumptions must be positive finite quantities")
        if any(not _nonnegative(reduction.get(k)) for k in ("low", "base", "high")):
            raise ValueError("blocker reductions must be non-negative")
        rows.append({"gate_id": gate["gate_id"], "score": {k: reduction[k] / effort[k] for k in ("low", "base", "high")}})
    rows.sort(key=lambda row: row["score"]["base"], reverse=True)
    return {"ranking": rows, "model": "assumed_blocker_reduction_points_per_assumed_effort_cost_unit",
            "assumptions_are_measured": False, "capital_authorized": False, "capital_amount": None}


def validate_ai_cost_candidate(record: dict) -> dict:
    errors = []
    train, held = set(record.get("train_example_ids", [])), set(record.get("held_out_example_ids", []))
    if not train or not held:
        errors.append("train_and_held_out_ids_required")
    if train & held:
        errors.append("train_held_out_leakage")
    required = ("quality", "runtime_seconds", "energy_joules", "cost_amount", "cost_currency", "accepted_outputs")
    errors.extend(f"{key}_missing" for key in required if record.get(key) is None)
    for key in ("quality", "runtime_seconds", "energy_joules", "cost_amount"):
        if record.get(key) is not None and not _nonnegative(record[key]):
            errors.append(f"{key}_invalid")
    if type(record.get("accepted_outputs")) is not int or record.get("accepted_outputs", 0) < 1:
        errors.append("accepted_outputs_invalid")
    complete = not errors
    return {"errors": sorted(set(errors)), "structurally_complete": complete,
            "candidate_claim_admissible": complete and record.get("evidence_class") == "MEASURED_CANDIDATE" and record.get("independent_verification") is True}


def validate_qos_semantic_certificate(record: dict) -> list[str]:
    fields = ("circuit_sha256", "grammar_subset_id", "source_measurement_map", "candidate_measurement_map")
    errors = [f"{field}_missing" for field in fields if record.get(field) in (None, "")]
    if record.get("source_measurement_map") != record.get("candidate_measurement_map"):
        errors.append("measurement_semantics_mismatch")
    if type(record.get("logical_qubits")) is not int or record.get("logical_qubits", 0) < 1:
        errors.append("logical_qubit_count_invalid")
    for field in ("logical_depth", "t_count"):
        if type(record.get(field)) is not int or record.get(field, -1) < 0:
            errors.append(f"{field}_invalid")
    if record.get("provider_task_id") is not None or record.get("hardware_receipt") is not None:
        errors.append("provider_and_hardware_receipts_must_be_null")
    return errors
