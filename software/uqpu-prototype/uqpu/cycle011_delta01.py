"""Cycle 011 bounded, reproducible extensions for all twelve research lanes."""
from __future__ import annotations

import hashlib
import itertools
import json
import math
import os
import random
import re
import subprocess
import sys
import tempfile
import time
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any, Mapping, Sequence


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def canonical_sha256(value: Any) -> str:
    return sha256_bytes(canonical_bytes(value))


# A — fourth preregistered graph and positive integer edge weights.
def weighted_instance(seed: int, node_count: int = 8, density: float = 0.4) -> dict[str, Any]:
    if type(seed) is not int or type(node_count) is not int or not 2 <= node_count <= 12:
        raise ValueError("weighted_graph_seed_or_node_count_invalid")
    if not 0 < density < 1:
        raise ValueError("weighted_graph_density_invalid")
    rng = random.Random(seed)
    edges = [[i, j, rng.randint(1, 5)] for i in range(node_count) for j in range(i + 1, node_count) if rng.random() < density]
    if not edges:
        edges = [[0, node_count - 1, rng.randint(1, 5)]]
    return {"seed": seed, "node_count": node_count, "density": density, "edges": edges, "weight_domain": "INTEGER_1_TO_5"}


def _cut(bits: Sequence[int], edges: Sequence[Sequence[int]]) -> int:
    return sum(weight for left, right, weight in edges if bits[left] != bits[right])


def _greedy(bits: Sequence[int], edges: Sequence[Sequence[int]]) -> tuple[tuple[int, ...], int]:
    state = list(bits)
    score = _cut(state, edges)
    while True:
        found = False
        for index in range(len(state)):
            candidate = state.copy()
            candidate[index] ^= 1
            candidate_score = _cut(candidate, edges)
            if candidate_score > score:
                state, score, found = candidate, candidate_score, True
        if not found:
            return tuple(state), score


def run_weighted_maxcut(seed: int, state_cap: int = 512, budgets: Sequence[int] = (1, 4, 16, 64)) -> dict[str, Any]:
    graph = weighted_instance(seed)
    state_count = 1 << graph["node_count"]
    if type(state_cap) is not int or state_cap < state_count:
        return {"complete": False, "states_evaluated": 0, "error": "exact_state_cap_exceeded"}
    exact = max(_cut(tuple((mask >> bit) & 1 for bit in range(graph["node_count"])), graph["edges"]) for mask in range(state_count))
    rng = random.Random(seed ^ 0xC011)
    starts, scores, elapsed = [], [], []
    for _ in range(max(budgets)):
        start = tuple(rng.randrange(2) for _ in range(graph["node_count"]))
        starts.append(start)
        tick = time.perf_counter_ns()
        scores.append(_greedy(start, graph["edges"])[1])
        elapsed.append(max(0, time.perf_counter_ns() - tick))
    rows = [{"restarts": n, "best_objective": max(scores[:n]), "exact_objective": exact,
             "gap_to_exact": exact - max(scores[:n]), "restart_prefix_sha256": canonical_sha256(starts[:n]),
             "host_elapsed_ns": sum(elapsed[:n])} for n in budgets]
    return {"graph": graph, "graph_sha256": canonical_sha256(graph), "complete": True,
            "states_evaluated": state_count, "state_cap": state_cap, "results": rows,
            "evidence_class": "LOCAL_SEEDED_CLASSICAL_WEIGHTED_SOFTWARE_COMPARISON"}


# B — strict v2 to current-v3 migration with canonical request and token binding.
_V2_KEYS = {"schema_version", "idempotency_token", "source_commit", "request", "payload_sha256"}
_V3_KEYS = _V2_KEYS | {"binding_sha256"}
_REQUEST_KEYS = {"action", "shots", "payload"}


def migrate_request_v2_to_current(envelope: Mapping[str, Any]) -> dict[str, Any]:
    version = envelope.get("schema_version")
    allowed = _V2_KEYS if version == 2 else _V3_KEYS if version == 3 else set()
    if not allowed:
        raise ValueError("unsupported_request_schema")
    if set(envelope) != allowed:
        raise ValueError("request_envelope_fields_not_exact")
    request = envelope.get("request")
    if not isinstance(request, dict) or set(request) != _REQUEST_KEYS:
        raise ValueError("request_fields_not_exact")
    if type(request.get("shots")) is not int or request["shots"] <= 0:
        raise ValueError("request_shots_invalid")
    token, source = envelope.get("idempotency_token"), envelope.get("source_commit")
    if not isinstance(token, str) or not token or not isinstance(source, str) or not re.fullmatch(r"[0-9a-f]{40}", source):
        raise ValueError("request_identity_invalid")
    digest = canonical_sha256(request)
    if envelope.get("payload_sha256") != digest:
        raise ValueError("canonical_payload_binding_mismatch")
    binding = canonical_sha256({"idempotency_token": token, "source_commit": source, "payload_sha256": digest})
    if version == 3 and envelope.get("binding_sha256") != binding:
        raise ValueError("canonical_token_binding_mismatch")
    return {"schema_version": 3, "idempotency_token": token, "source_commit": source,
            "request": request, "payload_sha256": digest, "binding_sha256": binding}


# C — same/fresh-process atomic publication with cleanup and capability capture.
def _directory_fsync(directory: Path) -> bool:
    try:
        fd = os.open(str(directory), os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
        try:
            os.fsync(fd)
        finally:
            os.close(fd)
        return True
    except (OSError, AttributeError):
        return False


def atomic_publish(path: Path, payload: bytes, fail_after_stage: bool = False) -> dict[str, Any]:
    path.parent.mkdir(parents=True, exist_ok=True)
    previous = path.read_bytes() if path.exists() else None
    temp_name = None
    file_fsync = False
    directory_fsync = False
    replaced = False
    error = None
    try:
        with tempfile.NamedTemporaryFile(mode="wb", dir=path.parent, prefix=".uqpu-cycle011-", delete=False) as stream:
            temp_name = stream.name
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
            file_fsync = True
        if fail_after_stage:
            raise OSError("injected_after_stage_before_replace")
        os.replace(temp_name, path)
        replaced = True
        temp_name = None
        directory_fsync = _directory_fsync(path.parent)
    except OSError as exc:
        error = str(exc)
    finally:
        if temp_name and os.path.exists(temp_name):
            os.unlink(temp_name)
    current = path.read_bytes() if path.exists() else None
    leftovers = [name for name in os.listdir(path.parent) if name.startswith(".uqpu-cycle011-")]
    integrity = current == (payload if replaced else previous)
    return {"published": replaced, "integrity_preserved": integrity, "old_sha256": sha256_bytes(previous) if previous is not None else None,
            "new_sha256": sha256_bytes(payload), "final_sha256": sha256_bytes(current) if current is not None else None,
            "file_fsync": file_fsync, "directory_fsync": directory_fsync, "temp_files_remaining": len(leftovers),
            "cache_state": "UNCONTROLLED", "error": error}


_FRESH_WRITE = r'''import hashlib,json,os,pathlib,sys,tempfile
p=pathlib.Path(sys.argv[1]); b=bytes.fromhex(sys.argv[2])
with tempfile.NamedTemporaryFile(mode="wb",dir=p.parent,prefix=".uqpu-cycle011-child-",delete=False) as f:
 n=f.name; f.write(b); f.flush(); os.fsync(f.fileno())
os.replace(n,p)
try:
 d=os.open(str(p.parent),os.O_RDONLY|getattr(os,"O_DIRECTORY",0)); os.fsync(d); os.close(d); directory=True
except (OSError,AttributeError): directory=False
print(json.dumps({"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"file_fsync":True,"directory_fsync":directory}))
'''


def run_atomic_protocol() -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="uqpu-cycle011-io-") as directory:
        path = Path(directory) / "accepted.bin"
        same = []
        for i in range(2):
            payload = f"cycle011-same-{i}".encode()
            row = atomic_publish(path, payload)
            same.append({**row, "process_scope": "same_process", "expected_sha256": sha256_bytes(payload)})
        fresh_payload = b"cycle011-fresh-child"
        child = subprocess.run([sys.executable, "-c", _FRESH_WRITE, str(path), fresh_payload.hex()], capture_output=True, text=True, timeout=10, check=False)
        if child.returncode:
            raise RuntimeError("fresh_process_writer_failed")
        fresh = json.loads(child.stdout)
        fresh["expected_sha256"] = sha256_bytes(fresh_payload)
        fresh["process_scope"] = "fresh_child_process"
        fault = atomic_publish(path, b"cycle011-fault", fail_after_stage=True)
    rows = same + [fresh]
    return {"rows": rows, "injected_failure": fault, "hashes_match": all(row["expected_sha256"] == (row.get("final_sha256") or row.get("sha256")) for row in rows),
            "temp_cleanup_pass": all(row.get("temp_files_remaining", 0) == 0 for row in same + [fault]),
            "cache_state": "UNCONTROLLED", "evidence_class": "LOCAL_FILESYSTEM_ATOMIC_PUBLICATION_SCREEN"}


# D — ordered, bounded multi-entry ZIP64 central-directory metadata.
def validate_zip64_directory(record: Mapping[str, Any]) -> dict[str, Any]:
    errors = []
    start, size, file_size = record.get("central_directory_start"), record.get("central_directory_size"), record.get("file_size")
    scalars = (start, size, file_size)
    if any(type(v) is not int or v < 0 for v in scalars):
        return {"valid": False, "errors": ["central_directory_scalar_invalid"]}
    end = start + size
    if end > file_size:
        errors.append("central_directory_out_of_file")
    entries = record.get("entries")
    if not isinstance(entries, list) or not entries:
        errors.append("central_directory_entries_missing")
        entries = []
    previous_end = start
    previous_offset = -1
    for i, row in enumerate(entries):
        if not isinstance(row, dict):
            errors.append(f"central_directory_entry_invalid:{i}")
            continue
        offset, length, local = row.get("offset"), row.get("record_size"), row.get("local_header_offset")
        if any(type(v) is not int or v < 0 for v in (offset, length, local)) or length == 0:
            errors.append(f"central_directory_entry_bounds_invalid:{i}")
            continue
        if offset < previous_offset:
            errors.append(f"central_directory_order_invalid:{i}")
        if offset < previous_end:
            errors.append(f"central_directory_overlap:{i}")
        if offset + length > end:
            errors.append(f"central_directory_record_truncated:{i}")
        if local >= start or local >= file_size:
            errors.append(f"central_directory_local_offset_invalid:{i}")
        previous_offset, previous_end = offset, offset + length
    zip64_offset = record.get("zip64_eocd_offset")
    zip64_size = record.get("zip64_eocd_size")
    locator_offset = record.get("zip64_locator_offset")
    if any(type(v) is not int or v < 0 for v in (zip64_offset, zip64_size, locator_offset)):
        errors.append("zip64_locator_scalars_invalid")
    elif zip64_offset != end or zip64_offset + zip64_size != locator_offset or locator_offset + 20 > file_size:
        errors.append("zip64_locator_record_boundary_invalid")
    return {"valid": not errors, "errors": errors, "entry_count": len(entries), "evidence_class": "SYNTHETIC_ZIP64_DIRECTORY_ORDER_VALIDATION"}


# E — synthetic identity custody and method-version gate.
def validate_material_custody(record: Mapping[str, Any], *, expected_method_version: str, as_of: date) -> dict[str, Any]:
    errors = []
    if record.get("evidence_class") != "SYNTHETIC_FIXTURE": errors.append("custody_evidence_class_not_synthetic")
    if not record.get("sample_id") or not record.get("control_id") or record.get("sample_id") == record.get("control_id"):
        errors.append("custody_sample_control_identity_invalid")
    if record.get("method_version") != expected_method_version: errors.append("custody_method_version_superseded")
    if record.get("unit") != record.get("uncertainty_unit"): errors.append("custody_uncertainty_unit_mismatch")
    try:
        if date.fromisoformat(record.get("calibration_expiry", "")) < as_of: errors.append("custody_calibration_expired")
    except (TypeError, ValueError): errors.append("custody_calibration_expiry_invalid")
    events = record.get("custody_chain")
    if not isinstance(events, list) or not events:
        errors.append("custody_chain_missing")
    else:
        if events[0].get("from_id") != record.get("origin_id") or events[-1].get("to_id") != record.get("sample_id"):
            errors.append("custody_chain_endpoints_mismatch")
        for i, event in enumerate(events):
            if not event.get("from_id") or not event.get("to_id") or not event.get("event_hash"):
                errors.append(f"custody_chain_event_incomplete:{i}")
            if i and events[i - 1].get("to_id") != event.get("from_id"):
                errors.append(f"custody_chain_link_disconnected:{i}")
    return {"valid": not errors, "errors": errors, "custody_links": len(events) if isinstance(events, list) else 0,
            "evidence_class": "SYNTHETIC_CUSTODY_CHAIN_GATE"}


# Shared PSD checker for F/G small covariance blocks.
def _matrix_psd(matrix: Any) -> bool:
    if not isinstance(matrix, list) or not matrix or any(not isinstance(row, list) or len(row) != len(matrix) for row in matrix):
        return False
    try:
        a = [[float(value) for value in row] for row in matrix]
    except (TypeError, ValueError):
        return False
    n = len(a)
    if any(not math.isfinite(v) for row in a for v in row): return False
    if any(abs(a[i][j] - a[j][i]) > 1e-10 for i in range(n) for j in range(n)): return False
    # Jacobi rotations avoid an external numerical dependency for these tiny gates.
    for _ in range(50 * n * n):
        p, q, largest = 0, 0, 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(a[i][j]) > largest: p, q, largest = i, j, abs(a[i][j])
        if largest < 1e-12: break
        angle = 0.5 * math.atan2(2 * a[p][q], a[q][q] - a[p][p])
        c, s = math.cos(angle), math.sin(angle)
        app, aqq, apq = a[p][p], a[q][q], a[p][q]
        a[p][p] = c*c*app - 2*s*c*apq + s*s*aqq
        a[q][q] = s*s*app + 2*s*c*apq + c*c*aqq
        a[p][q] = a[q][p] = 0.0
        for k in range(n):
            if k not in (p, q):
                akp, akq = a[k][p], a[k][q]
                a[k][p] = a[p][k] = c*akp - s*akq
                a[k][q] = a[q][k] = s*akp + c*akq
    return all(a[i][i] >= -1e-9 for i in range(n))


# F — interval and covariance propagation with fail-closed nulls.
def propagate_component_covariance(record: Mapping[str, Any]) -> dict[str, Any]:
    components, required = record.get("components"), record.get("required_component_ids")
    accepted = record.get("accepted_outputs")
    nulls = {"total_interval": None, "per_accepted_output_interval": None, "expanded_uncertainty": None}
    if not isinstance(components, list) or not isinstance(required, list) or not required:
        return {"complete": False, **nulls, "errors": ["cost_components_missing"]}
    if type(accepted) is not int or accepted <= 0:
        return {"complete": False, **nulls, "errors": ["accepted_output_count_invalid"]}
    if not record.get("currency") or record.get("currency") != record.get("unit"):
        return {"complete": False, **nulls, "errors": ["cost_currency_unit_mismatch"]}
    by_id = {row.get("component_id"): row for row in components if isinstance(row, dict)}
    if len(by_id) != len(components) or set(by_id) != set(required):
        return {"complete": False, **nulls, "errors": ["cost_component_set_incomplete"]}
    unit = record.get("unit")
    try:
        lows, highs, stds = [], [], []
        for component_id in required:
            row = by_id[component_id]
            if row.get("unit") != unit: raise ValueError("cost_component_unit_mismatch")
            lo, hi, std = Decimal(str(row["low"])), Decimal(str(row["high"])), Decimal(str(row["standard_uncertainty"]))
            if lo < 0 or hi < lo or std < 0: raise ValueError("cost_component_interval_invalid")
            lows.append(lo); highs.append(hi); stds.append(float(std))
    except (KeyError, InvalidOperation, ValueError, TypeError) as exc:
        return {"complete": False, **nulls, "errors": [str(exc) or "cost_component_value_invalid"]}
    total = [str(sum(lows)), str(sum(highs))]
    interval = [str(sum(lows) / accepted), str(sum(highs) / accepted)]
    matrix = record.get("correlation_matrix")
    uncertainty = None
    errors = []
    if not isinstance(matrix, list) or len(matrix) != len(required) or any(not isinstance(row, list) or len(row) != len(required) or any(v is None for v in row) for row in matrix):
        errors.append("covariance_matrix_incomplete")
    elif not _matrix_psd(matrix):
        errors.append("covariance_matrix_not_psd")
    else:
        variance = sum(stds[i] * float(matrix[i][j]) * stds[j] for i in range(len(stds)) for j in range(len(stds)))
        if variance < -1e-10: errors.append("propagated_variance_negative")
        else:
            k = record.get("coverage_factor", 2)
            if type(k) not in (int, float) or k <= 0: errors.append("coverage_factor_invalid")
            else: uncertainty = k * math.sqrt(max(0.0, variance))
    return {"complete": True, "currency": record.get("currency"), "total_interval": total,
            "per_accepted_output_interval": interval, "expanded_uncertainty": uncertainty,
            "uncertainty_errors": errors, "evidence_class": "SYNTHETIC_MULTI_COMPONENT_COVARIANCE_MODEL"}


# G — typed multi-measurand block with scope, method and coverage.
def validate_multimeasurand_budget(budget: Mapping[str, Any], as_of: date) -> dict[str, Any]:
    errors = []
    measurands, components = budget.get("measurands"), budget.get("components")
    if budget.get("scope") != budget.get("expected_scope"): errors.append("budget_scope_mismatch")
    if budget.get("method") != "SYNTHETIC_MULTI_MEASURAND_V1": errors.append("budget_method_unsupported")
    try:
        if date.fromisoformat(budget.get("expiry", "")) < as_of: errors.append("budget_expired")
    except (TypeError, ValueError): errors.append("budget_expiry_invalid")
    if not isinstance(measurands, list) or not measurands: measurands = []; errors.append("budget_measurands_missing")
    if not isinstance(components, list) or len(components) != len(measurands): errors.append("budget_component_count_mismatch")
    else:
        for i, (item, component) in enumerate(zip(measurands, components)):
            if item.get("id") != component.get("measurand_id") or item.get("unit") != component.get("unit"):
                errors.append(f"budget_component_scope_or_unit_mismatch:{i}")
            try:
                if Decimal(str(component.get("standard_uncertainty"))) < 0: errors.append(f"budget_uncertainty_negative:{i}")
            except (InvalidOperation, TypeError): errors.append(f"budget_uncertainty_invalid:{i}")
    matrix = budget.get("correlation_matrix")
    if not isinstance(matrix, list) or len(matrix) != len(measurands) or any(not isinstance(row, list) or len(row) != len(measurands) for row in matrix):
        errors.append("budget_covariance_dimension_mismatch")
    elif not _matrix_psd(matrix): errors.append("budget_covariance_not_psd")
    coverage = budget.get("coverage_factor")
    if type(coverage) not in (int, float) or coverage <= 0: errors.append("budget_coverage_invalid")
    return {"valid": not errors, "errors": errors, "measurand_count": len(measurands),
            "evidence_class": "SYNTHETIC_MULTI_MEASURAND_UNCERTAINTY_BUDGET"}


# H — four-gate assumed grid plus held-out assumption cases; no capital decision.
def rank_four_gate_priority(gates: Sequence[Mapping[str, Any]], levels: Sequence[float], held_out: Sequence[Mapping[str, float]]) -> dict[str, Any]:
    if len(gates) != 4 or len(levels) != 3: raise ValueError("four_gates_and_three_levels_required")
    ids = [row["gate_id"] for row in gates]
    if len(set(ids)) != 4 or any(row["effort"] <= 0 or row["impact"] <= 0 for row in gates): raise ValueError("gate_assumptions_invalid")
    base = {row["gate_id"]: row["impact"] / row["effort"] for row in gates}
    base_order = sorted(ids, key=lambda name: (-base[name], name))
    pairwise = {f"{a}|{b}": [] for a, b in itertools.combinations(sorted(ids), 2)}
    orders = []
    for multipliers in itertools.product(levels, repeat=8):
        scores = {row["gate_id"]: row["impact"] * multipliers[2*i+1] / (row["effort"] * multipliers[2*i]) for i, row in enumerate(gates)}
        order = sorted(ids, key=lambda name: (-scores[name], name)); orders.append(order)
        for key in pairwise:
            a, b = key.split("|")
            pairwise[key].append((order.index(a) < order.index(b)) == (base_order.index(a) < base_order.index(b)))
    heldout_rows = []
    for case in held_out:
        scores = {row["gate_id"]: row["impact"] * case.get(row["gate_id"], 1.0) / row["effort"] for row in gates}
        heldout_rows.append({"scenario_id": case.get("scenario_id"), "order": sorted(ids, key=lambda name: (-scores[name], name))})
    return {"scenario_count": len(orders), "distinct_order_count": len({tuple(row) for row in orders}),
            "base_order": base_order, "reversal_scenario_count": sum(row != base_order for row in orders),
            "pairwise_rank_stability": {key: sum(flags) / len(flags) for key, flags in pairwise.items()},
            "held_out_scenarios": heldout_rows, "capital_authorized": False, "capital_amount": None,
            "input_class": "ILLUSTRATIVE_ASSUMPTIONS_ONLY"}


# FND/EQN — exact dimensions plus source-bound interval declaration.
_EXPECTED_DIMENSIONS = {"USD/count": {"USD": 1, "count": -1}, "J/count": {"W": 1, "s": 1, "count": -1}}


def validate_sourced_interval(declaration: Mapping[str, Any], source_bytes: Mapping[str, bytes]) -> dict[str, Any]:
    errors = []
    unit = declaration.get("unit_code")
    expected = _EXPECTED_DIMENSIONS.get(unit)
    if expected is None or declaration.get("dimension_vector") != expected: errors.append("quantity_dimension_balance_invalid")
    payload = source_bytes.get(declaration.get("source_locator"))
    if not isinstance(payload, bytes) or declaration.get("source_sha256") != sha256_bytes(payload): errors.append("quantity_source_hash_mismatch")
    try:
        low, high = Decimal(str(declaration.get("low"))), Decimal(str(declaration.get("high")))
        if low < 0 or high < low: errors.append("quantity_interval_order_invalid")
    except (InvalidOperation, TypeError): errors.append("quantity_interval_value_invalid")
    return {"valid": not errors, "errors": errors, "quantity_id": declaration.get("quantity_id"),
            "unit_code": unit, "evidence_class": "SOURCE_HASH_BOUND_TYPED_INTERVAL_DECLARATION"}


# SCM — consent revocation invalidates subsequent fictional transitions.
def validate_consent_revocation(events: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    errors, active, revoked = [], set(), set()
    for i, event in enumerate(events):
        nonce, action = event.get("nonce"), event.get("action")
        if event.get("domain_sort") != "FICTION_CANON": errors.append(f"scm_cross_sort_transition:{i}")
        if not nonce: errors.append(f"scm_nonce_missing:{i}"); continue
        if action == "grant":
            if nonce in active or nonce in revoked: errors.append(f"scm_consent_nonce_replayed:{i}")
            else: active.add(nonce)
        elif action == "transition":
            if nonce not in active or nonce in revoked: errors.append(f"scm_transition_without_active_consent:{i}")
        elif action == "revoke":
            if nonce not in active: errors.append(f"scm_revoke_without_active_consent:{i}")
            active.discard(nonce); revoked.add(nonce)
        else: errors.append(f"scm_event_action_invalid:{i}")
    return {"valid": not errors, "errors": errors, "active_consent_count": len(active),
            "revoked_consent_count": len(revoked), "empirical_coupling": None,
            "evidence_class": "FICTION_ONLY_CONSENT_STATE_MACHINE"}


# AI-COST — second immutable synthetic source version with hash-linked migration.
def validate_ai_source_migration(previous: Mapping[str, Any], current: Mapping[str, Any], previous_bytes: Mapping[str, bytes], current_bytes: Mapping[str, bytes]) -> dict[str, Any]:
    errors = []
    if previous.get("schema_version") != 1 or current.get("schema_version") != 2: errors.append("ai_lineage_schema_migration_invalid")
    if current.get("lineage_from") != canonical_sha256(previous): errors.append("ai_lineage_parent_hash_mismatch")
    required = {"train", "validation", "test"}
    old_splits, new_splits = previous.get("splits", {}), current.get("splits", {})
    if set(old_splits) != required or set(new_splits) != required: errors.append("ai_lineage_split_set_invalid")
    old_ids, new_ids = set(), set()
    for split in sorted(required):
        old, new = old_splits.get(split, {}), new_splits.get(split, {})
        old_payload, new_payload = previous_bytes.get(split), current_bytes.get(split)
        if not isinstance(old_payload, bytes) or sha256_bytes(old_payload) != old.get("source_sha256"): errors.append(f"ai_v1_source_hash_invalid:{split}")
        if not isinstance(new_payload, bytes) or sha256_bytes(new_payload) != new.get("source_sha256"): errors.append(f"ai_v2_source_hash_invalid:{split}")
        if type(old.get("source_bytes_length")) is not int or old.get("source_bytes_length") != len(old_payload or b""): errors.append(f"ai_v1_source_length_invalid:{split}")
        if type(new.get("source_bytes_length")) is not int or new.get("source_bytes_length") != len(new_payload or b""): errors.append(f"ai_v2_source_length_invalid:{split}")
        old_ids.update(old.get("record_ids", [])); new_ids.update(new.get("record_ids", []))
        metrics = new.get("metrics", {})
        if not all(metrics.get(name, {}).get("complete") is True for name in current.get("required_metrics", [])): errors.append(f"ai_v2_heldout_metrics_incomplete:{split}")
    if len(new_ids) != sum(len(v.get("record_ids", [])) for v in new_splits.values()): errors.append("ai_v2_split_overlap")
    if old_ids != new_ids: errors.append("ai_lineage_record_identity_changed")
    return {"valid": not errors, "errors": errors, "previous_manifest_sha256": canonical_sha256(previous),
            "current_manifest_sha256": canonical_sha256(current), "scoring_performed": False,
            "evidence_class": "SYNTHETIC_IMMUTABLE_SOURCE_LINEAGE_MIGRATION"}


# QOS/QSVT — migrate a second frozen ER6 source and rebind its certificate.
def migrate_er6_certificate(source_v1: Mapping[str, Any], source_v2: Mapping[str, Any], certificate: Mapping[str, Any], bounds: Mapping[str, int]) -> dict[str, Any]:
    errors = []
    if source_v1.get("grammar") != "ER6_CYCLE010_FROZEN_SUBSET" or source_v2.get("grammar") != "ER6_CYCLE011_FROZEN_SUBSET": errors.append("er6_source_grammar_migration_invalid")
    if certificate.get("source_sha256") != canonical_sha256(source_v1): errors.append("er6_previous_certificate_source_mismatch")
    old_dest = source_v1.get("measurement_destinations", [])
    new_dest = source_v2.get("measurement_destinations", [])
    expected_added = {"qubit": f"q[{source_v1.get('qubit_count')}]", "bit": f"c[{source_v1.get('bit_count')}]"}
    if new_dest[:-1] != old_dest or len(new_dest) != len(old_dest) + 1 or new_dest[-1] != expected_added:
        errors.append("er6_migration_measurement_map_not_append_only")
    if source_v2.get("qubit_count") != source_v1.get("qubit_count", 0) + 1 or source_v2.get("bit_count") != source_v1.get("bit_count", 0) + 1:
        errors.append("er6_migration_register_delta_invalid")
    candidate = {"source_sha256": canonical_sha256(source_v2),
                 "registers": {"qubit_count": source_v2.get("qubit_count"), "bit_count": source_v2.get("bit_count")},
                 "measurement_destinations": new_dest,
                 "resources": source_v2.get("candidate_resources", {})}
    for register in ("qubit_count", "bit_count"):
        if candidate["registers"][register] > bounds.get(register, -1): errors.append(f"er6_migrated_register_bound_exceeded:{register}")
    for key in ("depth", "gate_count", "serialized_bytes"):
        value = candidate["resources"].get(key)
        if type(value) is not int or value < 0: errors.append(f"er6_migrated_resource_invalid:{key}")
        elif value > bounds.get(key, -1): errors.append(f"er6_migrated_resource_bound_exceeded:{key}")
    return {"valid": not errors, "errors": errors, "candidate": candidate,
            "source_v1_sha256": canonical_sha256(source_v1), "source_v2_sha256": canonical_sha256(source_v2),
            "evidence_class": "FROZEN_ER6_CERTIFICATE_MIGRATION"}
