"""Cycle 010 bounded falsification gates for the synchronized 12-lane portfolio.

All positive material, cost, uncertainty, AI and SCM fixtures are synthetic.
The MaxCut and filesystem outputs are finite local software results only.
"""

from __future__ import annotations

from datetime import date
from decimal import Decimal, InvalidOperation
from fractions import Fraction
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import random
import re
import subprocess
import sys
import tempfile
import time
from typing import Any, Iterable, Mapping, Sequence

LANES = ("A", "B", "C", "D", "E", "F", "G", "H", "FND/EQN", "SCM", "AI-COST", "QOS/QSVT")
ZIP64_SENTINEL = (1 << 32) - 1
UINT64_MAX = (1 << 64) - 1


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def canonical_sha256(value: Any) -> str:
    return sha256_bytes(canonical_bytes(value))


# A — Preregistered exact-capped MaxCut comparison with stable restart prefixes.
def generate_maxcut_instance(seed: int, node_count: int, density: float) -> dict[str, Any]:
    if type(seed) is not int or type(node_count) is not int or not 2 <= node_count <= 12:
        raise ValueError("seed or bounded node count invalid")
    if not 0.0 < density < 1.0:
        raise ValueError("density must be strictly between zero and one")
    rng = random.Random(seed)
    edges = [[i, j, 1] for i in range(node_count) for j in range(i + 1, node_count) if rng.random() < density]
    if not edges:
        edges = [[0, node_count - 1, 1]]
    return {"seed": seed, "node_count": node_count, "density": density, "edges": edges}


def cut_objective(bits: Sequence[int], edges: Sequence[Sequence[int]]) -> int:
    return sum(int(weight) for left, right, weight in edges if bits[left] != bits[right])


def exact_maxcut(instance: Mapping[str, Any], state_cap: int) -> dict[str, Any]:
    n = instance["node_count"]
    states = 1 << n
    if type(state_cap) is not int or state_cap < states:
        return {"complete": False, "states_evaluated": 0, "best_objective": None, "error": "state_cap_exceeded"}
    best = max(cut_objective(tuple((mask >> i) & 1 for i in range(n)), instance["edges"]) for mask in range(states))
    return {"complete": True, "states_evaluated": states, "state_cap": state_cap, "best_objective": best}


def _greedy_maxcut(bits: Sequence[int], edges: Sequence[Sequence[int]]) -> tuple[tuple[int, ...], int]:
    state = list(bits)
    score = cut_objective(state, edges)
    changed = True
    while changed:
        changed = False
        for i in range(len(state)):
            candidate = state.copy()
            candidate[i] ^= 1
            candidate_score = cut_objective(candidate, edges)
            if candidate_score > score:
                state, score, changed = candidate, candidate_score, True
    return tuple(state), score


def run_maxcut_restart_sweep(instances: Sequence[Mapping[str, Any]], budgets: Sequence[int], state_cap: int) -> dict[str, Any]:
    if not instances or tuple(budgets) != (1, 4, 16, 64):
        raise ValueError("three or more instances and frozen budgets 1/4/16/64 are required")
    if len(instances) < 3:
        raise ValueError("at least three preregistered instances are required")
    output = []
    for spec in instances:
        instance = generate_maxcut_instance(spec["seed"], spec["node_count"], spec["density"])
        instance_hash = canonical_sha256(instance)
        exact = exact_maxcut(instance, state_cap)
        if not exact["complete"]:
            raise ValueError("exact control is incomplete")
        rng = random.Random(spec["seed"] ^ 0xA510)
        starts: list[tuple[int, ...]] = []
        scores: list[int] = []
        elapsed: list[int] = []
        for _ in range(max(budgets)):
            start = tuple(rng.randrange(2) for _ in range(instance["node_count"]))
            starts.append(start)
            started = time.perf_counter_ns()
            _, score = _greedy_maxcut(start, instance["edges"])
            elapsed.append(max(0, time.perf_counter_ns() - started))
            scores.append(score)
        rows = []
        for budget in budgets:
            rows.append({
                "restarts": budget,
                "restart_objectives": scores[:budget],
                "best_objective": max(scores[:budget]),
                "exact_objective": exact["best_objective"],
                "gap_to_exact": exact["best_objective"] - max(scores[:budget]),
                "exact_states_evaluated": exact["states_evaluated"],
                "exact_complete": exact["complete"],
                "restart_prefix_sha256": canonical_sha256(starts[:budget]),
                "restart_start_sha256": [canonical_sha256(start) for start in starts[:budget]],
                "host_elapsed_ns": sum(elapsed[:budget]),
            })
        output.append({"instance": instance, "instance_sha256": instance_hash, "results": rows})
    return {"instances": output, "budgets": list(budgets), "state_cap": state_cap, "evidence_class": "LOCAL_SEEDED_CLASSICAL_SOFTWARE_COMPARISON"}


# B — Duplicate-key rejection and explicit envelope migration before hashing.
def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate_json_key:{key}")
        result[key] = value
    return result


def parse_json_reject_duplicates(payload: str) -> Any:
    return json.loads(payload, object_pairs_hook=_unique_object, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(f"non_finite_json_number:{value}")))


def migrate_request_envelope(envelope: Mapping[str, Any]) -> dict[str, Any]:
    version = envelope.get("schema_version")
    if version == 1:
        request = envelope.get("request")
        if not isinstance(request, dict) or not envelope.get("idempotency_token") or not envelope.get("source_commit"):
            raise ValueError("v1_required_field_missing")
        return {
            "schema_version": 2,
            "idempotency_token": envelope["idempotency_token"],
            "source_commit": envelope["source_commit"],
            "request": request,
            "payload_sha256": canonical_sha256(request),
        }
    if version == 2:
        request = envelope.get("request")
        if not isinstance(request, dict) or not envelope.get("idempotency_token") or not envelope.get("source_commit"):
            raise ValueError("v2_required_field_missing")
        if envelope.get("payload_sha256") != canonical_sha256(request):
            raise ValueError("v2_payload_hash_mismatch")
        return dict(envelope)
    raise ValueError("unsupported_envelope_schema_version")


def validate_request_replay(original: Mapping[str, Any], replay: Mapping[str, Any]) -> dict[str, Any]:
    try:
        first, second = migrate_request_envelope(original), migrate_request_envelope(replay)
    except (ValueError, TypeError) as exc:
        return {"valid": False, "errors": [str(exc)]}
    errors = []
    if first["idempotency_token"] != second["idempotency_token"]:
        errors.append("idempotency_token_changed")
    if first["source_commit"] != second["source_commit"]:
        errors.append("source_commit_changed")
    if first["payload_sha256"] != second["payload_sha256"]:
        errors.append("request_payload_changed")
    return {"valid": not errors, "errors": errors, "request_sha256": first["payload_sha256"]}


# C — Named local atomic-write protocol. Cache remains explicitly uncontrolled.
def _fsync_directory(directory: Path) -> bool:
    flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
    try:
        fd = os.open(str(directory), flags)
        try:
            os.fsync(fd)
        finally:
            os.close(fd)
        return True
    except (OSError, AttributeError):
        return False


def atomic_write_local(path: Path, payload: bytes) -> dict[str, Any]:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_name = None
    try:
        with tempfile.NamedTemporaryFile(mode="wb", dir=path.parent, prefix=".uqpu-cycle010-", delete=False) as stream:
            temp_name = stream.name
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp_name, path)
        directory_fsync = _fsync_directory(path.parent)
        return {"file_fsync": True, "directory_fsync": directory_fsync, "sha256": sha256_bytes(path.read_bytes())}
    finally:
        if temp_name and os.path.exists(temp_name):
            os.unlink(temp_name)


_FRESH_WRITER = r'''import hashlib, json, os, pathlib, sys, tempfile
path = pathlib.Path(sys.argv[1])
payload = bytes.fromhex(sys.argv[2])
with tempfile.NamedTemporaryFile(mode="wb", dir=path.parent, prefix=".uqpu-cycle010-child-", delete=False) as f:
    name=f.name; f.write(payload); f.flush(); os.fsync(f.fileno())
os.replace(name, path)
try:
    fd=os.open(str(path.parent), os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)); os.fsync(fd); os.close(fd); directory=True
except (OSError, AttributeError):
    directory=False
print(json.dumps({"sha256":hashlib.sha256(path.read_bytes()).hexdigest(),"file_fsync":True,"directory_fsync":directory}))
'''


def simulate_interrupted_atomic_write(old_payload: bytes, new_payload: bytes, boundary: str) -> dict[str, Any]:
    if boundary not in {"before_write", "after_staging_fsync", "after_replace"}:
        raise ValueError("unsupported_interruption_boundary")
    with tempfile.TemporaryDirectory(prefix="uqpu-cycle010-fault-") as directory:
        target = Path(directory) / "accepted.bin"
        target.write_bytes(old_payload)
        temp_path = Path(directory) / "staged.bin"
        if boundary == "before_write":
            pass
        else:
            with temp_path.open("wb") as handle:
                handle.write(new_payload)
                handle.flush()
                os.fsync(handle.fileno())
            if boundary == "after_replace":
                os.replace(temp_path, target)
        final = target.read_bytes()
        return {"boundary": boundary, "old_or_new_payload_preserved": final in (old_payload, new_payload), "final_sha256": sha256_bytes(final), "cache_state": "UNCONTROLLED"}


def run_local_atomic_write_protocol() -> dict[str, Any]:
    old, new = b"cycle010-old-payload", b"cycle010-new-payload"
    rows = []
    with tempfile.TemporaryDirectory(prefix="uqpu-cycle010-io-") as directory:
        path = Path(directory) / "artifact.bin"
        atomic_write_local(path, old)
        repeated = []
        for index in range(3):
            payload = new + str(index).encode("ascii")
            started = time.perf_counter_ns()
            result = atomic_write_local(path, payload)
            repeated.append({"write_index": index, "expected_sha256": sha256_bytes(payload), "readback_sha256": result["sha256"], "file_fsync": result["file_fsync"], "directory_fsync": result["directory_fsync"], "host_elapsed_ns": max(0, time.perf_counter_ns() - started)})
        rows.append({"process_scope": "same_process_repeated", "rows": repeated, "cache_state": "UNCONTROLLED"})
        fresh = []
        for index in range(2):
            payload = new + b"-fresh-" + str(index).encode("ascii")
            completed = subprocess.run([sys.executable, "-c", _FRESH_WRITER, str(path), payload.hex()], capture_output=True, text=True, timeout=10, check=False)
            if completed.returncode != 0:
                raise RuntimeError("fresh-process atomic write failed: " + completed.stderr[-500:])
            result = json.loads(completed.stdout)
            fresh.append({"process_scope": "fresh_child_process", "write_index": index, "expected_sha256": sha256_bytes(payload), "readback_sha256": result["sha256"], "file_fsync": result["file_fsync"], "directory_fsync": result["directory_fsync"], "cache_state": "UNCONTROLLED"})
        rows.append({"process_scope": "fresh_child_process", "rows": fresh, "cache_state": "UNCONTROLLED"})
    interruptions = {stage: simulate_interrupted_atomic_write(old, new, stage) for stage in ("before_write", "after_staging_fsync", "after_replace")}
    return {"rows": rows, "interruptions": interruptions, "all_hashes_match": all(row["expected_sha256"] == row["readback_sha256"] for scope in rows for row in scope["rows"]), "all_interrupted_payloads_preserved": all(row["old_or_new_payload_preserved"] for row in interruptions.values()), "cache_state": "UNCONTROLLED", "evidence_class": "LOCAL_SOFTWARE_FILESYSTEM_SCREEN_ONLY"}


# D — Offline HTTP range responses and bounded ZIP64 directory metadata.
def validate_http_range_response(status: int, content_range: str, expected_total: int, body_length: int, start: int | None = None, end: int | None = None) -> dict[str, Any]:
    if type(status) is not int or type(expected_total) is not int or type(body_length) is not int or body_length < 0:
        return {"valid": False, "errors": ["range_scalar_invalid"]}
    if status == 416:
        match = re.fullmatch(r"bytes \*/(\d+)", content_range.strip()) if isinstance(content_range, str) else None
        valid = bool(match and int(match.group(1)) == expected_total and body_length == 0)
        return {"valid": valid, "errors": [] if valid else ["unsatisfied_range_response_inconsistent"], "response_kind": "UNSATISFIED_RANGE"}
    match = re.fullmatch(r"bytes (\d+)-(\d+)/(\d+)", content_range.strip()) if isinstance(content_range, str) else None
    if status != 206 or not match:
        return {"valid": False, "errors": ["partial_content_status_or_header_invalid"], "response_kind": "RANGE_RESPONSE"}
    got_start, got_end, got_total = map(int, match.groups())
    errors = []
    if start is not None and got_start != start: errors.append("range_start_mismatch")
    if end is not None and got_end != end: errors.append("range_end_mismatch")
    if got_total != expected_total: errors.append("range_total_mismatch")
    if got_end < got_start or body_length != got_end - got_start + 1: errors.append("range_body_length_mismatch")
    return {"valid": not errors, "errors": errors, "response_kind": "PARTIAL_CONTENT"}


def validate_zip64_metadata(record: Mapping[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    names = ("file_size", "central_directory_start", "central_directory_size", "zip64_eocd_offset", "zip64_eocd_size", "zip64_locator_offset")
    values: dict[str, int] = {}
    for name in names:
        value = record.get(name)
        if type(value) is not int or value < 0 or value > UINT64_MAX:
            errors.append(f"zip64_scalar_invalid:{name}")
        else:
            values[name] = value
    if len(values) == len(names):
        if values["central_directory_start"] + values["central_directory_size"] != values["zip64_eocd_offset"]:
            errors.append("central_directory_end_mismatch")
        if values["zip64_eocd_offset"] + values["zip64_eocd_size"] != values["zip64_locator_offset"]:
            errors.append("zip64_locator_offset_mismatch")
        if values["zip64_locator_offset"] + 20 > values["file_size"]:
            errors.append("zip64_locator_out_of_bounds")
    entries = record.get("entries")
    if not isinstance(entries, list) or not entries:
        errors.append("zip64_entries_missing")
    else:
        for index, entry in enumerate(entries):
            if not isinstance(entry, dict):
                errors.append(f"zip64_entry_invalid:{index}")
                continue
            extra = entry.get("zip64_extra")
            if not isinstance(extra, dict): extra = {}
            for field in ("compressed_size", "uncompressed_size", "local_header_offset"):
                raw = entry.get(field)
                effective = extra.get(field) if raw == ZIP64_SENTINEL else raw
                if raw == ZIP64_SENTINEL and field not in extra:
                    errors.append(f"zip64_extra_missing:{index}:{field}")
                    continue
                if type(effective) is not int or not 0 <= effective <= UINT64_MAX:
                    errors.append(f"zip64_value_invalid:{index}:{field}")
                elif field == "local_header_offset" and values.get("central_directory_start") is not None and effective >= values["central_directory_start"]:
                    errors.append(f"zip64_local_header_out_of_bounds:{index}")
    return {"valid": not errors, "errors": errors, "evidence_class": "SYNTHETIC_ZIP64_METADATA_VALIDATION"}


# E — Synthetic material sample/control/calibration provenance mutations.
def validate_material_provenance(record: Mapping[str, Any], as_of: date) -> dict[str, Any]:
    errors = []
    required = ("sample_id", "control_id", "measurand", "unit", "method_id", "calibration_issuer", "calibration_scope", "calibration_expiry", "uncertainty", "uncertainty_unit", "evidence_class")
    for name in required:
        if record.get(name) in (None, ""):
            errors.append(f"material_field_missing:{name}")
    if record.get("sample_id") and record.get("sample_id") == record.get("control_id"):
        errors.append("sample_control_identity_collision")
    if record.get("measurand") not in set(record.get("calibration_scope", [])):
        errors.append("calibration_scope_mismatch")
    try:
        if date.fromisoformat(record.get("calibration_expiry", "")) < as_of:
            errors.append("calibration_expired")
    except (TypeError, ValueError):
        errors.append("calibration_expiry_invalid")
    if record.get("unit") and record.get("uncertainty_unit") != record.get("unit"):
        errors.append("uncertainty_unit_mismatch")
    if record.get("evidence_class") != "SYNTHETIC_FIXTURE":
        errors.append("material_evidence_class_not_synthetic")
    try:
        if Decimal(str(record.get("uncertainty"))) <= 0:
            errors.append("uncertainty_not_positive")
    except (InvalidOperation, TypeError):
        errors.append("uncertainty_invalid")
    return {"valid": not errors, "errors": errors, "evidence_class": "SYNTHETIC_MATERIAL_PROVENANCE_GATE"}


# F/G — Synthetic interval totals plus explicit 2x2 correlation/uncertainty validation.
def validate_correlation_matrix(matrix: Sequence[Sequence[Any]]) -> dict[str, Any]:
    if not isinstance(matrix, (list, tuple)) or len(matrix) != 2 or any(not isinstance(row, (list, tuple)) or len(row) != 2 for row in matrix):
        return {"valid": False, "errors": ["correlation_matrix_shape_invalid"]}
    try:
        a, b, c, d = (Decimal(str(matrix[0][0])), Decimal(str(matrix[0][1])), Decimal(str(matrix[1][0])), Decimal(str(matrix[1][1])))
    except (InvalidOperation, TypeError):
        return {"valid": False, "errors": ["correlation_matrix_value_invalid"]}
    errors = []
    if a != 1 or d != 1: errors.append("correlation_diagonal_must_equal_one")
    if b != c: errors.append("correlation_matrix_not_symmetric")
    if abs(b) > 1: errors.append("correlation_matrix_not_psd")
    return {"valid": not errors, "errors": errors, "rho": str(b), "evidence_class": "SYNTHETIC_CORRELATION_MATRIX"}


def propagate_cost_interval(record: Mapping[str, Any]) -> dict[str, Any]:
    required = set(record.get("required_components", []))
    components = record.get("components", {})
    errors = []
    if not record.get("currency"):
        errors.append("cost_currency_missing")
    if record.get("uncertainty_unit") != record.get("currency"):
        errors.append("cost_uncertainty_unit_mismatch")
    if not isinstance(components, dict) or not required.issubset(components):
        errors.append("cost_component_incomplete")
    n = record.get("accepted_outputs")
    if type(n) is not int or n <= 0:
        errors.append("accepted_output_denominator_invalid")
    if errors:
        return {"complete": False, "total_interval": None, "per_accepted_output_interval": None, "uncertainty": None, "errors": errors}
    try:
        lower = sum(Decimal(str(components[k]["low"])) for k in required)
        upper = sum(Decimal(str(components[k]["high"])) for k in required)
        uncertainties = [Decimal(str(v)) for v in record["standard_uncertainties"]]
        coverage = Decimal(str(record["coverage_factor"]))
    except (KeyError, TypeError, InvalidOperation, ValueError):
        return {"complete": False, "total_interval": None, "per_accepted_output_interval": None, "uncertainty": None, "errors": ["cost_or_uncertainty_value_invalid"]}
    interval = [str(lower), str(upper)]
    correlation = validate_correlation_matrix(record.get("correlation_matrix", []))
    expanded = None
    uncertainty_errors = []
    if not correlation["valid"]:
        uncertainty_errors.extend(correlation["errors"])
    elif len(uncertainties) != 2 or any(value < 0 for value in uncertainties) or coverage <= 0:
        uncertainty_errors.append("uncertainty_inputs_invalid")
    else:
        rho = Decimal(correlation["rho"])
        variance = uncertainties[0] ** 2 + uncertainties[1] ** 2 + Decimal(2) * rho * uncertainties[0] * uncertainties[1]
        if variance < 0:
            uncertainty_errors.append("propagated_variance_negative")
        else:
            expanded = str(Decimal(str(math.sqrt(float(variance)))) * coverage)
    return {
        "complete": True,
        "currency": record.get("currency"),
        "uncertainty_unit": record.get("uncertainty_unit"),
        "total_interval": interval,
        "per_accepted_output_interval": [str(lower / n), str(upper / n)],
        "uncertainty": expanded,
        "uncertainty_errors": uncertainty_errors,
        "covariance_valid": correlation["valid"],
        "evidence_class": "SYNTHETIC_COST_AND_COVARIANCE_MODEL",
        "contract_sha256": canonical_sha256(record.get("accepted_output_contract", {})),
    }


def validate_uncertainty_budget(budget: Mapping[str, Any], as_of: date) -> dict[str, Any]:
    errors = []
    components = budget.get("components", [])
    component_ids = [row.get("component_id") for row in components if isinstance(row, dict)] if isinstance(components, list) else []
    expected = list(budget.get("required_component_ids", []))
    if set(component_ids) != set(expected) or len(component_ids) != len(expected): errors.append("uncertainty_components_incomplete")
    if budget.get("method") != "CORRELATED_STANDARD_UNCERTAINTY_V1": errors.append("uncertainty_method_unsupported")
    if budget.get("scope") != budget.get("expected_scope"): errors.append("uncertainty_scope_mismatch")
    if budget.get("unit") != budget.get("expected_unit"): errors.append("uncertainty_unit_mismatch")
    try:
        if date.fromisoformat(budget.get("certificate_expiry", "")) < as_of: errors.append("uncertainty_certificate_expired")
    except (TypeError, ValueError): errors.append("uncertainty_expiry_invalid")
    matrix = validate_correlation_matrix(budget.get("correlation_matrix", []))
    if not matrix["valid"]: errors.extend(matrix["errors"])
    if type(budget.get("coverage_factor")) not in (int, float) or budget.get("coverage_factor", 0) <= 0:
        errors.append("uncertainty_coverage_factor_invalid")
    return {"valid": not errors, "errors": errors, "correlation": matrix, "evidence_class": "SYNTHETIC_UNCERTAINTY_BUDGET"}


# H — Preregistered assumed-input gate-order sensitivity grid; no capital authority.
def rank_assumed_gate_grid(gates: Sequence[Mapping[str, Any]], multipliers: Sequence[float]) -> dict[str, Any]:
    if len(gates) != 3 or tuple(multipliers) != (0.5, 1.0, 2.0):
        raise ValueError("frozen three-gate, three-level grid required")
    scenarios = itertools.product(multipliers, repeat=6)
    rankings = []
    score_bounds: dict[str, list[float]] = {row["gate_id"]: [] for row in gates}
    base = {row["gate_id"]: row["impact"] / row["effort"] for row in gates}
    base_order = [name for name, _ in sorted(base.items(), key=lambda item: (-item[1], item[0]))]
    pairwise = {(a, b): [] for a, b in itertools.combinations(sorted(base), 2)}
    for values in scenarios:
        scores = {}
        for index, gate in enumerate(gates):
            effort_multiplier, impact_multiplier = values[2 * index], values[2 * index + 1]
            score = (gate["impact"] * impact_multiplier) / (gate["effort"] * effort_multiplier)
            scores[gate["gate_id"]] = score
            score_bounds[gate["gate_id"]].append(score)
        order = [name for name, _ in sorted(scores.items(), key=lambda item: (-item[1], item[0]))]
        rankings.append(order)
        for pair in pairwise:
            pairwise[pair].append((order.index(pair[0]) < order.index(pair[1])) == (base_order.index(pair[0]) < base_order.index(pair[1])))
    pair_stability = {f"{a}|{b}": sum(values) / len(values) for (a, b), values in pairwise.items()}
    distinct_orders = {tuple(order) for order in rankings}
    return {
        "scenario_count": len(rankings),
        "base_order": base_order,
        "distinct_order_count": len(distinct_orders),
        "reversal_scenario_count": sum(order != base_order for order in rankings),
        "pairwise_rank_stability": pair_stability,
        "score_bounds": {key: {"min": min(values), "max": max(values)} for key, values in score_bounds.items()},
        "capital_authorized": False,
        "capital_amount": None,
        "input_class": "ILLUSTRATIVE_ASSUMPTIONS_ONLY",
    }


# FND/EQN — Exact derived unit vectors linked to the project's accepted-output equations.
def derive_dimension_vector(registry: Mapping[str, Any], numerator_units: Sequence[str], denominator_units: Sequence[str]) -> dict[str, str]:
    names = registry.get("dimension_basis", [])
    vector = {name: Fraction(0) for name in names}
    for unit, sign in itertools.chain(((x, 1) for x in numerator_units), ((x, -1) for x in denominator_units)):
        definition = registry.get("unit_registry", {}).get(unit)
        raw = definition.get("dimension_vector") if isinstance(definition, dict) else None
        if not isinstance(raw, dict):
            raise ValueError(f"unit_not_registered:{unit}")
        for name in names:
            vector[name] += sign * Fraction(raw.get(name, "0"))
    return {name: str(value) for name, value in vector.items()}


def validate_sourced_quantity(declaration: Mapping[str, Any], registry: Mapping[str, Any]) -> dict[str, Any]:
    errors = []
    unit_code = declaration.get("unit_code")
    unit = registry.get("unit_registry", {}).get(unit_code) if unit_code else None
    if not isinstance(unit, dict) or not isinstance(unit.get("dimension_vector"), dict):
        errors.append("unit_unregistered_or_unclassified")
    elif declaration.get("dimension_vector") != unit["dimension_vector"]:
        errors.append("dimension_vector_mismatch")
    if declaration.get("domain_sort") != "REAL_MODEL": errors.append("quantity_domain_sort_invalid")
    if not declaration.get("source_locator") or not declaration.get("source_sha256"):
        errors.append("quantity_source_provenance_missing")
    return {"valid": not errors, "errors": errors, "quantity_id": declaration.get("quantity_id"), "evidence_class": "BOUNDED_SOURCE_LINKED_TYPED_DECLARATION"}


# SCM — Versioned fictional graph with complete five-volume equation coverage.
def validate_fictional_state_graph(graph: Mapping[str, Any], *, used_nonces: set[str]) -> dict[str, Any]:
    errors = []
    if graph.get("schema_version") != 1: errors.append("scm_schema_version_unsupported")
    states = graph.get("states", [])
    equations = set(graph.get("equations", []))
    state_ids = {row.get("state_id") for row in states if isinstance(row, dict)}
    version = graph.get("canon_version")
    edges = graph.get("edges", [])
    if not state_ids or len(state_ids) != len(states): errors.append("scm_state_ids_invalid")
    for i, edge in enumerate(edges if isinstance(edges, list) else []):
        if edge.get("from_state") not in state_ids or edge.get("to_state") not in state_ids: errors.append(f"scm_edge_state_unknown:{i}")
        if edge.get("equation_id") not in equations: errors.append(f"scm_edge_equation_unknown:{i}")
        if edge.get("canon_version") != version: errors.append(f"scm_edge_version_mismatch:{i}")
        if edge.get("domain_sort") != "FICTION_CANON": errors.append(f"scm_cross_sort_conversion:{i}")
        if edge.get("consent_required") is not True: errors.append(f"scm_consent_required_missing:{i}")
        nonce = edge.get("consent_nonce")
        if not nonce or nonce in used_nonces: errors.append(f"scm_nonce_missing_or_replayed:{i}")
    links = graph.get("volume_equation_links")
    if not isinstance(links, dict) or set(links) != {"V1", "V2", "V3", "V4", "V5"}:
        errors.append("scm_five_volume_coverage_incomplete")
    elif any(not set(values).issubset(equations) or not values for values in links.values()):
        errors.append("scm_volume_equation_reference_invalid")
    if graph.get("empirical_coupling") is not None: errors.append("scm_empirical_coupling_nonnull")
    return {"valid": not errors, "errors": errors, "volume_count": len(links) if isinstance(links, dict) else 0, "empirical_coupling": None, "evidence_class": "FICTION_ONLY_VERSIONED_GRAPH"}


# AI-COST — Immutable synthetic bytes, disjoint splits and per-split metrics.
def validate_ai_source_manifest(manifest: Mapping[str, Any], source_bytes: Mapping[str, bytes]) -> dict[str, Any]:
    errors = []
    if manifest.get("schema_version") != 1: errors.append("ai_manifest_schema_unsupported")
    splits = manifest.get("splits", {})
    required_splits = {"train", "validation", "test"}
    if not isinstance(splits, dict) or set(splits) != required_splits:
        errors.append("ai_three_way_splits_invalid")
        splits = {}
    ids = {name: set(splits.get(name, {}).get("record_ids", [])) for name in required_splits}
    for first, second in itertools.combinations(sorted(required_splits), 2):
        if ids[first] & ids[second]: errors.append(f"ai_split_overlap:{first}:{second}")
    for name in required_splits:
        split = splits.get(name, {})
        payload = source_bytes.get(name)
        if not isinstance(payload, bytes) or split.get("source_sha256") != sha256_bytes(payload):
            errors.append(f"ai_source_bytes_hash_mismatch:{name}")
        if type(split.get("source_bytes_length")) is not int or payload is None or split.get("source_bytes_length") != len(payload):
            errors.append(f"ai_source_bytes_length_mismatch:{name}")
        if not isinstance(split.get("metrics"), dict) or not set(manifest.get("required_metrics", [])).issubset(split["metrics"]):
            errors.append(f"ai_split_metrics_incomplete:{name}")
    return {"valid": not errors, "errors": errors, "scoring_performed": False, "evidence_class": "SYNTHETIC_IMMUTABLE_SOURCE_MANIFEST"}


def build_ai_source_manifest(source_records: Mapping[str, Any], record_ids: Mapping[str, Sequence[str]], required_metrics: Sequence[str]) -> tuple[dict[str, Any], dict[str, bytes]]:
    source_bytes = {name: canonical_bytes(source_records[name]) for name in ("train", "validation", "test")}
    manifest = {
        "schema_version": 1,
        "required_metrics": list(required_metrics),
        "splits": {
            name: {
                "record_ids": list(record_ids[name]),
                "source_sha256": sha256_bytes(source_bytes[name]),
                "source_bytes_length": len(source_bytes[name]),
                "metrics": {metric: {"complete": True, "value": 0.0} for metric in required_metrics},
            }
            for name in ("train", "validation", "test")
        },
        "evidence_class": "SYNTHETIC_IMMUTABLE_SOURCE_MANIFEST",
    }
    return manifest, source_bytes


# QOS/QSVT — Frozen ER6 semantic/resource certificate with explicit source identity.
def validate_er6_register_certificate(source: Mapping[str, Any], candidate: Mapping[str, Any], bounds: Mapping[str, int]) -> dict[str, Any]:
    errors = []
    source_hash = canonical_sha256(source)
    if candidate.get("source_sha256") != source_hash: errors.append("er6_source_identity_mismatch")
    qsize, bsize = source.get("qubit_count"), source.get("bit_count")
    registers = candidate.get("registers", {})
    if registers.get("qubit_count") != qsize or registers.get("bit_count") != bsize: errors.append("er6_register_semantics_mismatch")
    if type(qsize) is not int or qsize > bounds.get("qubit_count", -1) or type(bsize) is not int or bsize > bounds.get("bit_count", -1):
        errors.append("er6_register_bound_exceeded")
    if candidate.get("measurement_destinations") != source.get("measurement_destinations"):
        errors.append("er6_measurement_destination_changed")
    resources = candidate.get("resources", {})
    for name in ("depth", "gate_count", "serialized_bytes"):
        value = resources.get(name)
        if type(value) is not int or value < 0: errors.append(f"er6_resource_invalid:{name}")
        elif value > bounds.get(name, -1): errors.append(f"er6_resource_bound_exceeded:{name}")
    return {"valid": not errors, "errors": errors, "source_sha256": source_hash, "evidence_class": "FROZEN_ER6_SEMANTIC_RESOURCE_CERTIFICATE"}
