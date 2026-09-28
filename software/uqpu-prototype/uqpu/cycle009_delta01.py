"""Cycle 009 Delta 01 reproducibility and falsification gates.

All positive fixtures in this module are synthetic or local software checks.
The functions return bounded acceptance metadata and do not authorize provider
submission, purchases, measurements, capital, or evidence promotion.
"""

from __future__ import annotations

from datetime import date
from decimal import Decimal, InvalidOperation, localcontext
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import random
import subprocess
import sys
import tempfile
from typing import Any

from .cycle007_delta01 import validate_content_range


LANES = ("A", "B", "C", "D", "E", "F", "G", "H", "FND/EQN", "SCM", "AI-COST", "QOS/QSVT")


def canonical_json_sha256(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _cut_value(mask: int, edges: list[tuple[int, int, int]]) -> int:
    return sum(weight for left, right, weight in edges if ((mask >> left) & 1) != ((mask >> right) & 1))


def _greedy_cut(n: int, edges: list[tuple[int, int, int]], initial_mask: int) -> tuple[int, int]:
    mask = initial_mask
    while True:
        current = _cut_value(mask, edges)
        candidate, best = mask, current
        for node in range(n):
            flipped = mask ^ (1 << node)
            score = _cut_value(flipped, edges)
            if score > best:
                candidate, best = flipped, score
        if candidate == mask:
            return current, mask
        mask = candidate


def compare_preregistered_restart_budgets(
    *, seed: int = 1, node_count: int = 8, edge_probability: float = 0.4,
    budgets: tuple[int, ...] = (1, 4, 16), state_cap: int = 1024,
) -> dict[str, Any]:
    """Exact-enumerate a seeded graph and compare nested deterministic restarts."""
    if type(node_count) is not int or node_count < 2 or (1 << node_count) > state_cap:
        raise ValueError("graph state space exceeds the declared exact-enumeration cap")
    if not budgets or tuple(sorted(set(budgets))) != budgets or any(type(x) is not int or x < 1 for x in budgets):
        raise ValueError("restart budgets must be strictly increasing positive integers")
    graph_rng = random.Random(seed)
    edges = [(u, v, 1) for u in range(node_count) for v in range(u + 1, node_count)
             if graph_rng.random() < edge_probability]
    if not edges:
        raise ValueError("generated graph must contain at least one edge")
    exact = max(_cut_value(mask, edges) for mask in range(1 << node_count))
    # Use one saved restart sequence so larger budgets extend the same trial set.
    rows = []
    score_sequence = []
    for restart in range(budgets[-1]):
        initial = random.Random(seed * 1_000_003 + restart).randrange(1 << node_count)
        score, _ = _greedy_cut(node_count, edges, initial)
        score_sequence.append(score)
    for budget in budgets:
        rows.append({
            "restarts": budget,
            "objective": max(score_sequence[:budget]),
            "gap_to_exact": exact - max(score_sequence[:budget]),
            "restart_objectives": score_sequence[:budget],
        })
    return {
        "schema": "uqpu-cycle009-preregistered-restart-sweep-v1",
        "evidence_class": "LOCAL_SEEDED_CLASSICAL_SOFTWARE_COMPARISON",
        "fixture": {"generator": "seeded_erdos_renyi_maxcut", "seed": seed,
                    "node_count": node_count, "edge_probability": edge_probability,
                    "edge_list": [[u, v, w] for u, v, w in edges]},
        "exact_control": {"complete": True, "states_evaluated": 1 << node_count,
                           "state_cap": state_cap, "best_objective": exact},
        "budget_results": rows,
        "falsification_fixture": any(row["gap_to_exact"] > 0 for row in rows),
        "nonclaims": ["Finite local fixtures do not establish competitiveness or scaling.",
                      "No GPU, QPU, energy, provider, or hardware comparison is made."],
    }


def build_versioned_request_receipt(request: dict[str, Any], *, source_commit: str) -> dict[str, Any]:
    canonical = canonical_json_sha256(request)
    receipt = {"schema": "uqpu-synthetic-receipt-v2", "request_sha256": canonical,
               "client_token": request.get("client_token"), "submitted": False,
               "execution_id": None, "actual_bill": None,
               "evidence_class": "SYNTHETIC_SCHEMA_FIXTURE"}
    receipt["receipt_sha256"] = canonical_json_sha256(receipt)
    return {"schema": "uqpu-request-envelope-v2", "canonicalization": "JSON_SORTED_KEYS_COMPACT_V1",
            "source_commit": source_commit, "evidence_class": "SYNTHETIC_SCHEMA_FIXTURE",
            "request": request, "receipt": receipt}


def validate_versioned_request_envelope(envelope: dict[str, Any]) -> dict[str, Any]:
    errors = []
    request, receipt = envelope.get("request"), envelope.get("receipt")
    if envelope.get("schema") != "uqpu-request-envelope-v2":
        errors.append("envelope_schema_unsupported")
    if envelope.get("canonicalization") != "JSON_SORTED_KEYS_COMPACT_V1":
        errors.append("canonicalization_version_missing_or_unsupported")
    if not isinstance(envelope.get("source_commit"), str) or len(envelope["source_commit"]) < 7:
        errors.append("source_commit_missing")
    if envelope.get("evidence_class") != "SYNTHETIC_SCHEMA_FIXTURE":
        errors.append("envelope_evidence_class_invalid")
    if not isinstance(request, dict) or not isinstance(receipt, dict):
        errors.append("request_or_receipt_missing")
        request, receipt = {}, {}
    for field in ("client_token", "operation", "payload_sha256", "payload"):
        if not request.get(field):
            errors.append(f"request_field_missing:{field}")
    if isinstance(request.get("payload"), (dict, list)) and request.get("payload_sha256") != canonical_json_sha256(request["payload"]):
        errors.append("request_payload_hash_mismatch")
    if receipt.get("schema") != "uqpu-synthetic-receipt-v2":
        errors.append("receipt_schema_unsupported")
    if receipt.get("request_sha256") != canonical_json_sha256(request):
        errors.append("request_hash_mismatch")
    if receipt.get("client_token") != request.get("client_token"):
        errors.append("receipt_token_mismatch")
    body = {key: value for key, value in receipt.items() if key != "receipt_sha256"}
    if receipt.get("receipt_sha256") != canonical_json_sha256(body):
        errors.append("receipt_hash_mismatch")
    if receipt.get("submitted") is not False or receipt.get("execution_id") is not None or receipt.get("actual_bill") is not None:
        errors.append("synthetic_receipt_claims_execution_or_bill")
    return {"valid": not errors, "errors": sorted(set(errors)),
            "evidence_class": "SYNTHETIC_VERSIONED_REQUEST_RECEIPT_GATE",
            "provider_submission_enabled": False}


def validate_versioned_request_replay(original: dict[str, Any], replay: dict[str, Any]) -> dict[str, Any]:
    errors = []
    if original.get("client_token") != replay.get("client_token"):
        errors.append("replay_client_token_changed")
    if canonical_json_sha256(original) != canonical_json_sha256(replay):
        errors.append("same_token_payload_mutated")
    return {"valid": not errors, "errors": errors,
            "evidence_class": "SYNTHETIC_CLIENT_ENVELOPE_REPLAY_COMPARISON",
            "provider_idempotency_claim": False}


def validate_io_process_record(record: dict[str, Any]) -> list[str]:
    errors = []
    if record.get("process_scope") not in {"REPEATED_PROCESS", "FRESH_PROCESS"}:
        errors.append("process_scope_invalid")
    if record.get("cache_state") != "UNCONTROLLED":
        errors.append("cache_state_must_remain_uncontrolled")
    if record.get("device_flush_claim") and record.get("device_flush_attested") is not True:
        errors.append("device_flush_claim_unattested")
    if record.get("power_loss_claim") and record.get("power_loss_tested") is not True:
        errors.append("power_loss_claim_untested")
    if record.get("readback_sha256") != record.get("expected_sha256"):
        errors.append("readback_hash_mismatch")
    return errors


def simulate_interrupted_atomic_publication(
    old_payload: bytes, new_payload: bytes, *, interrupt_after: str,
) -> dict[str, Any]:
    """Inject a software exception at a publication boundary in a temp dir."""
    if interrupt_after not in {"before_write", "after_staging_fsync", "after_replace"}:
        raise ValueError("unknown interruption boundary")
    with tempfile.TemporaryDirectory(prefix="uqpu-cycle009-atomic-") as directory:
        final = Path(directory) / "published.bin"
        staging = Path(directory) / "staging.bin"
        final.write_bytes(old_payload)
        replaced = False
        try:
            if interrupt_after == "before_write":
                raise InterruptedError("injected before write")
            with staging.open("wb") as handle:
                handle.write(new_payload)
                handle.flush()
                os.fsync(handle.fileno())
            if interrupt_after == "after_staging_fsync":
                raise InterruptedError("injected after staging fsync")
            os.replace(staging, final)
            replaced = True
            if interrupt_after == "after_replace":
                raise InterruptedError("injected after replace")
        except InterruptedError:
            pass
        state = final.read_bytes()
        expected = new_payload if replaced else old_payload
        return {"injected_boundary": interrupt_after, "replace_completed": replaced,
                "old_or_new_payload_preserved": state == expected,
                "final_sha256": hashlib.sha256(state).hexdigest(),
                "evidence_class": "LOCAL_FAULT_INJECTION_SOFTWARE_SCREEN_ONLY"}


def measure_local_io_scope_screen(payload: Any) -> dict[str, Any]:
    """Hash-check repeated same-process and fresh-process reads of one local file."""
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")
    expected = hashlib.sha256(encoded).hexdigest()
    with tempfile.TemporaryDirectory(prefix="uqpu-cycle009-io-scope-") as directory:
        root = Path(directory)
        staging, final = root / "staging.bin", root / "published.bin"
        with staging.open("wb") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(staging, final)
        directory_fsync_supported = hasattr(os, "O_DIRECTORY")
        directory_fsync_completed = False
        directory_fsync_errno = None
        if directory_fsync_supported:
            try:
                descriptor = os.open(directory, os.O_RDONLY | os.O_DIRECTORY)
                try:
                    os.fsync(descriptor)
                    directory_fsync_completed = True
                finally:
                    os.close(descriptor)
            except OSError as error:
                directory_fsync_errno = error.errno
        rows = []
        for _ in range(2):
            recovered = final.read_bytes()
            rows.append({"process_scope": "REPEATED_PROCESS", "process_id": os.getpid(),
                         "readback_bytes": len(recovered),
                         "readback_sha256": hashlib.sha256(recovered).hexdigest(),
                         "sha256_matches": hashlib.sha256(recovered).hexdigest() == expected})
        child = subprocess.run(
            [sys.executable, "-c",
             "import hashlib,pathlib,sys; b=pathlib.Path(sys.argv[1]).read_bytes(); "
             "print(len(b)); print(hashlib.sha256(b).hexdigest())", str(final)],
            capture_output=True, text=True, timeout=30, check=False)
        if child.returncode != 0:
            raise RuntimeError(f"fresh-process readback failed: {child.stderr[-1000:]}")
        values = child.stdout.strip().splitlines()
        if len(values) != 2:
            raise RuntimeError("fresh-process readback returned malformed metadata")
        rows.append({"process_scope": "FRESH_PROCESS", "process_id": None,
                     "readback_bytes": int(values[0]), "readback_sha256": values[1],
                     "sha256_matches": values[1] == expected})
    return {"payload_sha256": expected, "payload_bytes": len(encoded), "rows": rows,
            "platform_capabilities": {"directory_fsync_supported": directory_fsync_supported,
                                      "directory_fsync_completed": directory_fsync_completed,
                                      "directory_fsync_error_errno": directory_fsync_errno},
            "cache_state": "UNCONTROLLED",
            "evidence_class": "LOCAL_REPEATED_AND_FRESH_PROCESS_FILESYSTEM_SCREEN_ONLY",
            "nonclaims": ["No cold-cache label, device-flush attestation, remote durability, or power-loss evidence."]}


def validate_offline_zip_metadata(record: dict[str, Any]) -> list[str]:
    errors = []
    size, start, end = record.get("archive_size_bytes"), record.get("central_start"), record.get("central_end")
    if any(type(value) is not int for value in (size, start, end)):
        return ["zip_metadata_coordinates_must_be_integers"]
    if size < 1 or start < 0 or end < start or end > size:
        errors.append("zip_directory_bounds_invalid")
    declared = record.get("declared_archive_size_bytes")
    if type(declared) is not int or declared != size:
        errors.append("zip_declared_archive_size_mismatch")
    entries = record.get("entries")
    if not isinstance(entries, list) or not entries:
        errors.append("zip_entries_missing")
        entries = []
    for index, entry in enumerate(entries):
        offset, compressed = entry.get("local_header_offset"), entry.get("compressed_size_bytes")
        if type(offset) is not int or offset < 0 or offset >= start:
            errors.append(f"zip_local_header_offset_invalid:{index}")
        if type(compressed) is not int or compressed < 0:
            errors.append(f"zip_compressed_size_invalid:{index}")
        elif type(offset) is int and offset + 30 + compressed > start:
            errors.append(f"zip_entry_truncated_before_central_directory:{index}")
    if record.get("archive_downloaded") is not False or record.get("payload_read") is not False:
        errors.append("zip_metadata_fixture_must_remain_offline")
    return sorted(set(errors))


def validate_synthetic_material_provenance(record: dict[str, Any], *, as_of: date) -> dict[str, Any]:
    errors = []
    required = ("sample_id", "control_id", "measurand", "unit_code", "method_id",
                "calibration_id", "calibration_scope", "valid_until", "uncertainty",
                "uncertainty_unit", "evidence_class")
    errors.extend(f"field_missing:{field}" for field in required if record.get(field) in (None, ""))
    if record.get("sample_id") == record.get("control_id"):
        errors.append("sample_control_identity_collision")
    if record.get("unit_code") != record.get("uncertainty_unit"):
        errors.append("uncertainty_unit_mismatch")
    try:
        valid_until = date.fromisoformat(record["valid_until"])
        if valid_until < as_of:
            errors.append("calibration_expired")
    except (KeyError, TypeError, ValueError):
        errors.append("calibration_valid_until_invalid")
    if record.get("synthetic") is not True or record.get("physical_measurement") is not False:
        errors.append("material_fixture_must_remain_synthetic")
    if not record.get("calibration_scope") or record.get("calibration_scope") != record.get("method_id"):
        errors.append("calibration_scope_mismatch")
    try:
        value = Fraction(str(record.get("uncertainty")))
        if value < 0:
            errors.append("uncertainty_must_be_nonnegative")
    except (ValueError, ZeroDivisionError, TypeError):
        errors.append("uncertainty_invalid")
    return {"valid": not errors, "errors": sorted(set(errors)),
            "evidence_class": "SYNTHETIC_MATERIAL_PROVENANCE_MUTATION_GATE",
            "physical_measurement_claim": False}


def compute_cost_interval_with_uncertainty(record: dict[str, Any]) -> dict[str, Any]:
    errors = []
    currency = record.get("currency")
    accepted_outputs = record.get("accepted_outputs")
    contract_hash = record.get("accepted_output_contract_sha256")
    required = record.get("required_components", [])
    components = record.get("components", {})
    if not isinstance(required, list) or not required:
        errors.append("required_components_missing")
        required = []
    if not isinstance(currency, str) or not currency:
        errors.append("currency_missing")
    if not isinstance(components, dict):
        errors.append("components_invalid")
        components = {}
    if type(accepted_outputs) is not int or accepted_outputs <= 0:
        errors.append("accepted_outputs_must_be_positive_integer")
    if not isinstance(contract_hash, str) or len(contract_hash) != 64 or any(c not in "0123456789abcdef" for c in contract_hash.lower()):
        errors.append("accepted_output_contract_hash_invalid")
    contract = record.get("accepted_output_contract")
    if not isinstance(contract, dict) or contract_hash != canonical_json_sha256(contract):
        errors.append("accepted_output_contract_hash_mismatch")
    lows, highs, sigmas = [], [], []
    for name in required:
        row = components.get(name)
        if not isinstance(row, dict):
            errors.append(f"component_missing:{name}")
            continue
        if row.get("currency") != currency:
            errors.append(f"component_currency_mismatch:{name}")
        try:
            low, high, sigma = (Fraction(str(row.get(key))) for key in ("low", "high", "standard_uncertainty"))
            if low < 0 or high < low or sigma < 0:
                raise ValueError
        except (ValueError, ZeroDivisionError, TypeError):
            errors.append(f"component_interval_or_uncertainty_invalid:{name}")
            continue
        lows.append(low); highs.append(high); sigmas.append(sigma)
    try:
        coverage_factor = Decimal(str(record.get("coverage_factor")))
        if not coverage_factor.is_finite() or coverage_factor <= 0:
            raise InvalidOperation
    except (InvalidOperation, TypeError, ValueError):
        errors.append("coverage_factor_invalid")
        coverage_factor = Decimal(0)
    complete = not errors and len(lows) == len(required)
    result = {"complete": complete, "errors": sorted(set(errors)), "currency": currency if complete else None,
              "accepted_output_contract_sha256": contract_hash if complete else None,
              "evidence_class": "SYNTHETIC_COST_INTERVAL_WITH_UNCERTAINTY",
              "uncertainty_assumption": "INDEPENDENT_COMPONENTS_ROOT_SUM_SQUARES_FOR_MODEL_ONLY",
              "financial_claim_admissible": False}
    if not complete:
        result.update({"total_interval": None, "per_accepted_output_interval": None,
                       "variance_sum_exact": None, "expanded_uncertainty_model_only": None})
        return result
    total_low, total_high = sum(lows, Fraction()), sum(highs, Fraction())
    variance = sum((sigma * sigma for sigma in sigmas), Fraction())
    with localcontext() as ctx:
        ctx.prec = 28
        rss = (Decimal(variance.numerator) / Decimal(variance.denominator)).sqrt()
    result.update({
        "total_interval": [str(total_low), str(total_high)],
        "per_accepted_output_interval": [str(total_low / accepted_outputs), str(total_high / accepted_outputs)],
        "variance_sum_exact": str(variance),
        "expanded_uncertainty_model_only": str(rss * coverage_factor),
    })
    return result


def validate_synthetic_uncertainty_budget(record: dict[str, Any], *, as_of: date) -> dict[str, Any]:
    errors = []
    if record.get("evidence_class") != "SYNTHETIC_UNCERTAINTY_BUDGET":
        errors.append("uncertainty_evidence_class_invalid")
    if record.get("scope_id") != record.get("required_scope_id") or not record.get("scope_id"):
        errors.append("uncertainty_scope_mismatch")
    try:
        if date.fromisoformat(record["valid_until"]) < as_of:
            errors.append("uncertainty_budget_expired")
    except (KeyError, TypeError, ValueError):
        errors.append("uncertainty_valid_until_invalid")
    components = record.get("components")
    reported = record.get("reported_component_ids")
    if not isinstance(components, list) or not components:
        errors.append("uncertainty_components_missing")
        components = []
    ids = [row.get("component_id") for row in components]
    if not isinstance(reported, list) or set(reported) != set(ids):
        errors.append("unreported_uncertainty_component")
    unit = record.get("unit_code")
    sigmas = []
    for index, row in enumerate(components):
        if not row.get("component_id") or row.get("unit_code") != unit:
            errors.append(f"uncertainty_component_unit_or_id_invalid:{index}")
        try:
            sigma = Decimal(str(row.get("standard_uncertainty")))
            if not sigma.is_finite() or sigma < 0:
                raise InvalidOperation
            sigmas.append(sigma)
        except (InvalidOperation, TypeError, ValueError):
            errors.append(f"uncertainty_component_value_invalid:{index}")
    method = record.get("combination_method")
    coverage = record.get("coverage_factor")
    if method not in {"ROOT_SUM_SQUARES_UNCORRELATED", "LINEAR_WORST_CASE"}:
        errors.append("uncertainty_combination_method_missing")
    try:
        k = Decimal(str(coverage))
        if not k.is_finite() or k <= 0:
            raise InvalidOperation
    except (InvalidOperation, TypeError, ValueError):
        errors.append("coverage_factor_invalid")
        k = Decimal(1)
    combined = None
    if not errors:
        if method == "LINEAR_WORST_CASE":
            standard = sum(sigmas, Decimal(0))
        else:
            with localcontext() as ctx:
                ctx.prec = 28
                standard = sum((sigma * sigma for sigma in sigmas), Decimal(0)).sqrt()
        combined = str(standard * k)
    return {"valid": not errors, "errors": sorted(set(errors)),
            "combination_method": method, "coverage_factor": str(coverage),
            "expanded_uncertainty_model_only": combined,
            "evidence_class": "SYNTHETIC_UNCERTAINTY_BUDGET",
            "measured_uncertainty_claim": False}


def rank_evidence_gate_sensitivity_grid(
    gates: list[dict[str, Any]], scenarios: list[dict[str, Any]],
) -> dict[str, Any]:
    if not gates or not scenarios:
        raise ValueError("a gate set and at least one assumption scenario are required")
    gate_ids = [row.get("gate_id") for row in gates]
    if any(not gate for gate in gate_ids) or len(set(gate_ids)) != len(gate_ids):
        raise ValueError("gate IDs must be unique and non-empty")
    rankings = []
    for scenario in scenarios:
        effort, impact = scenario.get("effort_cost"), scenario.get("blocker_impact")
        if not isinstance(effort, dict) or not isinstance(impact, dict):
            raise ValueError("each scenario needs explicit effort and impact assumptions")
        scores = []
        for gate_id in gate_ids:
            e, i = effort.get(gate_id), impact.get(gate_id)
            if not isinstance(e, (int, float)) or isinstance(e, bool) or e <= 0 or not isinstance(i, (int, float)) or isinstance(i, bool) or i < 0:
                raise ValueError("effort must be positive and impact non-negative")
            scores.append((i / e, gate_id))
        scores.sort(key=lambda row: (-row[0], row[1]))
        rankings.append({"scenario_id": scenario.get("scenario_id"),
                         "ranking": [gate for _, gate in scores],
                         "scores": {gate: score for score, gate in scores}})
    base = next((row for row in rankings if row["scenario_id"] == "base"), rankings[0])
    pairs = [(a, b) for i, a in enumerate(gate_ids) for b in gate_ids[i + 1:]]
    comparisons = 0
    stable = 0
    for row in rankings:
        positions = {gate: index for index, gate in enumerate(row["ranking"])}
        for a, b in pairs:
            comparisons += 1
            stable += positions[a] < positions[b] if base["ranking"].index(a) < base["ranking"].index(b) else positions[b] < positions[a]
    total = len(rankings) * len(pairs)
    return {"schema": "uqpu-cycle009-assumption-grid-ranking-v1", "rankings": rankings,
            "base_ranking": base["ranking"], "pairwise_order_stability": stable / total if total else 1.0,
            "pairwise_comparisons": comparisons, "assumptions_measured": False,
            "capital_authorized": False, "capital_amount": None,
            "evidence_class": "ILLUSTRATIVE_ASSUMPTION_GRID_ONLY"}


def validate_typed_quantity_declaration(record: dict[str, Any], unit_registry: dict[str, dict[str, Any]]) -> dict[str, Any]:
    errors = []
    unit, vector = record.get("unit_code"), record.get("dimension_vector")
    if not record.get("quantity_id"):
        errors.append("quantity_id_missing")
    if not record.get("source_locator"):
        errors.append("source_locator_missing")
    if not record.get("evidence_type"):
        errors.append("evidence_type_missing")
    if unit not in unit_registry:
        errors.append("unit_unclassified_or_unregistered")
    elif unit_registry[unit] != vector:
        errors.append("dimension_vector_does_not_match_registered_unit")
    if not isinstance(vector, dict) or not vector:
        errors.append("dimension_vector_unclassified")
    else:
        for axis, exponent in vector.items():
            try:
                Fraction(str(exponent))
            except (ValueError, ZeroDivisionError):
                errors.append(f"dimension_exponent_invalid:{axis}")
    return {"valid": not errors, "errors": sorted(set(errors)),
            "quantity_id": record.get("quantity_id"),
            "evidence_class": "BOUNDED_SOURCE_LINKED_TYPED_DECLARATION_AUDIT"}


def validate_fictional_state_transition(record: dict[str, Any], *, states: set[str], equations: set[str], used_nonces: set[str]) -> dict[str, Any]:
    errors = []
    if record.get("domain_sort") != "FICTION_CANON":
        errors.append("transition_domain_sort_invalid")
    if record.get("from_state") not in states or record.get("to_state") not in states:
        errors.append("transition_state_unknown")
    if record.get("equation_id") not in equations:
        errors.append("transition_equation_reference_unknown")
    if not record.get("canon_version") or record.get("source_version") != record.get("target_version") or record.get("canon_version") != record.get("source_version"):
        errors.append("transition_canon_version_mismatch")
    if record.get("cross_domain_cast") is not False:
        errors.append("transition_cross_domain_cast_forbidden")
    nonce = record.get("consent_nonce")
    if record.get("consent") is not True or not nonce:
        errors.append("transition_consent_required")
    if nonce in used_nonces:
        errors.append("transition_consent_nonce_replayed")
    volume_links = record.get("volume_equation_links")
    if not isinstance(volume_links, dict) or set(volume_links) != {"V1", "V2", "V3", "V4", "V5"}:
        errors.append("five_volume_links_incomplete")
    elif any(reference not in equations for reference in volume_links.values()):
        errors.append("five_volume_equation_reference_unknown")
    return {"valid": not errors, "errors": sorted(set(errors)),
            "evidence_class": "FICTIONAL_VERSIONED_TRANSITION_MUTATION_GATE",
            "empirical_coupling": None}


def build_three_way_ai_manifest(
    split_ids: dict[str, list[str]], source_hashes: dict[str, str], required_metrics: list[str],
) -> dict[str, Any]:
    return {
        "schema": "uqpu-ai-three-way-split-manifest-v1",
        "split_ids": split_ids,
        "split_hashes": {name: canonical_json_sha256(sorted(ids)) for name, ids in split_ids.items()},
        "source_hashes": source_hashes,
        "required_metrics": required_metrics,
        "metric_values": {name: {metric: None for metric in required_metrics} for name in split_ids},
        "evidence_class": "SYNTHETIC_MANIFEST_FIXTURE",
    }


def validate_three_way_ai_manifest(manifest: dict[str, Any], *, expected_source_hashes: dict[str, str]) -> dict[str, Any]:
    errors = []
    ids = manifest.get("split_ids")
    if not isinstance(ids, dict) or set(ids) != {"train", "validation", "test"}:
        errors.append("three_way_split_names_required")
        ids = {}
    normalized = {}
    for name in ("train", "validation", "test"):
        values = ids.get(name, []) if isinstance(ids.get(name, []), list) else []
        if not values or any(not isinstance(value, str) or not value for value in values) or len(set(values)) != len(values):
            errors.append(f"split_ids_invalid:{name}")
        normalized[name] = set(values)
        if manifest.get("split_hashes", {}).get(name) != canonical_json_sha256(sorted(values)):
            errors.append(f"split_hash_mismatch:{name}")
    for left, right in (("train", "validation"), ("train", "test"), ("validation", "test")):
        if normalized.get(left, set()) & normalized.get(right, set()):
            errors.append(f"split_overlap:{left}:{right}")
    if manifest.get("source_hashes") != expected_source_hashes:
        errors.append("source_hash_map_mismatch")
    if not isinstance(expected_source_hashes, dict) or any(
        not isinstance(v, str) or len(v) != 64 or any(c not in "0123456789abcdef" for c in v.lower())
        for v in expected_source_hashes.values()
    ):
        errors.append("source_hash_invalid")
    metrics = manifest.get("required_metrics")
    report = manifest.get("metric_values")
    if not isinstance(metrics, list) or not metrics:
        errors.append("required_metrics_missing")
        metrics = []
    completeness = {}
    for split in ("train", "validation", "test"):
        values = report.get(split, {}) if isinstance(report, dict) else {}
        missing = [metric for metric in metrics if not isinstance(values, dict) or values.get(metric) is None]
        completeness[split] = {"complete": not missing, "missing_metrics": missing}
        if missing:
            errors.append(f"metrics_incomplete:{split}")
    return {"valid": not errors, "errors": sorted(set(errors)), "completeness": completeness,
            "evidence_class": "SYNTHETIC_THREE_WAY_MANIFEST_GATE", "scoring_performed": False}


def validate_er6_semantic_certificate(source: dict[str, Any], candidate: dict[str, Any], bounds: dict[str, int]) -> dict[str, Any]:
    errors = []
    for field in ("register_map", "measurement_destinations"):
        if source.get(field) != candidate.get(field):
            errors.append(f"er6_semantics_changed:{field}")
    if not source.get("grammar_subset_id") or source.get("grammar_subset_id") != candidate.get("grammar_subset_id"):
        errors.append("er6_grammar_subset_changed")
    for field in ("logical_qubits", "gate_count", "depth"):
        value = candidate.get("resources", {}).get(field)
        bound = bounds.get(field)
        if type(value) is not int or value < 0:
            errors.append(f"er6_resource_invalid:{field}")
        if type(bound) is not int or bound < 0 or (type(value) is int and value > bound):
            errors.append(f"er6_resource_bound_exceeded:{field}")
    digest = candidate.get("source_sha256")
    if not isinstance(digest, str) or len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest.lower()):
        errors.append("er6_source_hash_invalid")
    elif digest != canonical_json_sha256(source):
        errors.append("er6_source_hash_mismatch")
    return {"valid": not errors, "errors": sorted(set(errors)),
            "evidence_class": "FROZEN_ER6_SEMANTIC_AND_RESOURCE_CERTIFICATE",
            "provider_transpile_receipt": None, "hardware_receipt": None}
