"""Cycle 007 Delta 01: audit machine-readable units in project equations."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import os
import platform
import re
import statistics
import subprocess
import sys
import tempfile
from time import perf_counter_ns
from typing import Any


LANES = (
    "A", "B", "C", "D", "E", "F", "G", "H",
    "FND/EQN", "SCM", "AI-COST", "QOS/QSVT",
)

PROJECT_DIMENSION_BASIS = (
    "length", "mass", "time", "electric_current", "temperature",
    "amount_of_substance", "luminous_intensity", "currency",
    "information", "count",
)


def _is_exact_rational(value: Any) -> bool:
    if isinstance(value, bool) or isinstance(value, float):
        return False
    if isinstance(value, int):
        return True
    if isinstance(value, str):
        try:
            Fraction(value)
        except (ValueError, ZeroDivisionError):
            return False
        return True
    return False


def _valid_dimension_vector(value: Any) -> bool:
    return (
        isinstance(value, dict)
        and set(value) == set(PROJECT_DIMENSION_BASIS)
        and all(_is_exact_rational(value[axis]) for axis in PROJECT_DIMENSION_BASIS)
    )


_CONTENT_RANGE_RE = re.compile(r"bytes (\d+)-(\d+)/(\d+)")


def validate_content_range(
    *, status: int, content_range: str | None,
    start: int, end: int, total: int, body_length: int,
) -> list[str]:
    """Require an exact bounded HTTP 206 range response.

    This gate prevents a server that ignores ``Range`` and returns HTTP 200
    from being treated as a successful small metadata fetch. It checks the
    response coordinates and byte count; it does not authenticate the server
    or verify a publisher checksum over an entire archive.
    """
    errors = []
    if not all(isinstance(value, int) and not isinstance(value, bool)
               for value in (status, start, end, total, body_length)):
        return ["range_coordinates_must_be_integers"]
    if total < 1 or start < 0 or end < start or end >= total:
        errors.append("requested_range_out_of_bounds")
    if status != 206:
        errors.append("http_status_must_be_206")
    match = _CONTENT_RANGE_RE.fullmatch(content_range or "")
    if not match:
        errors.append("content_range_header_invalid")
    elif tuple(map(int, match.groups())) != (start, end, total):
        errors.append("content_range_coordinates_mismatch")
    if body_length != end - start + 1:
        errors.append("range_body_length_mismatch")
    return errors


def _fresh_process_durability_probe(payload: Any) -> dict:
    """Perform one bounded local atomic-publication probe in a child process."""
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    expected_sha256 = hashlib.sha256(encoded).hexdigest()
    with tempfile.TemporaryDirectory(prefix="uqpu-cycle007-durability-") as temporary:
        directory = os.path.abspath(temporary)
        staging = os.path.join(directory, "staging.json")
        final = os.path.join(directory, "published.json")
        started = perf_counter_ns()
        with open(staging, "wb") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(staging, final)
        publication_ns = perf_counter_ns() - started

        directory_fsync_supported = hasattr(os, "O_DIRECTORY")
        directory_fsync_completed = False
        directory_fsync_error = None
        if directory_fsync_supported:
            try:
                descriptor = os.open(directory, os.O_RDONLY | os.O_DIRECTORY)
                try:
                    os.fsync(descriptor)
                    directory_fsync_completed = True
                finally:
                    os.close(descriptor)
            except OSError as error:
                directory_fsync_error = error.errno

        started = perf_counter_ns()
        recovered = open(final, "rb").read()
        read_ns = perf_counter_ns() - started
    recovered_sha256 = hashlib.sha256(recovered).hexdigest()
    if recovered_sha256 != expected_sha256:
        raise ValueError("fresh-process publication readback hash mismatch")
    return {
        "process_id": os.getpid(),
        "payload_bytes": len(encoded),
        "payload_sha256": expected_sha256,
        "publication_ns": publication_ns,
        "readback_ns": read_ns,
        "directory_fsync_supported": directory_fsync_supported,
        "directory_fsync_completed": directory_fsync_completed,
        "directory_fsync_error_errno": directory_fsync_error,
        "readback_sha256_matches": True,
    }


def measure_fresh_process_durability(payload: Any, *, repetitions: int = 5) -> dict:
    """Repeat a local durability probe in separate child processes.

    Cache-control commands are deliberately not attempted. The result reports
    that limitation instead of labeling reads cold or warm.
    """
    if type(repetitions) is not int or repetitions < 3 or repetitions > 20:
        raise ValueError("repetitions must be an integer from 3 through 20")
    payload_json = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    child_code = (
        "import json,sys; "
        "from uqpu.cycle007_delta01 import _fresh_process_durability_probe; "
        "print(json.dumps(_fresh_process_durability_probe(json.loads(sys.argv[1])), sort_keys=True))"
    )
    rows = []
    for index in range(repetitions):
        completed = subprocess.run(
            [sys.executable, "-c", child_code, payload_json],
            check=False,
            capture_output=True,
            text=True,
            timeout=30,
        )
        if completed.returncode != 0:
            raise RuntimeError(
                f"durability child {index} failed: {completed.stderr[-1000:]}"
            )
        row = json.loads(completed.stdout)
        if not row["readback_sha256_matches"]:
            raise ValueError(f"durability child {index} readback mismatch")
        rows.append(row)
    return {
        "schema": "uqpu-cycle007-fresh-process-local-durability-v1",
        "repetitions": repetitions,
        "fresh_process_per_repetition": True,
        "rows": rows,
        "timing_summary_ns": {
            "publication_median": statistics.median(row["publication_ns"] for row in rows),
            "readback_median": statistics.median(row["readback_ns"] for row in rows),
        },
        "platform_capabilities": {
            "system": platform.system(),
            "os_name": os.name,
            "directory_fsync_supported_in_all_children": all(
                row["directory_fsync_supported"] for row in rows
            ),
            "directory_fsync_completed_in_all_children": all(
                row["directory_fsync_completed"] for row in rows
            ),
            "cache_control_attempted": False,
            "cache_state": "UNCONTROLLED",
        },
        "evidence_class": "FRESH_PROCESS_LOCAL_FILESYSTEM_SCREEN_NOT_CACHE_OR_POWER_LOSS_EVIDENCE",
        "non_claims": [
            "No cold-cache or warm-cache label is inferred.",
            "No device-flush attestation or power-loss survival is tested.",
            "No remote-storage, cloud, energy, or hardware result is measured.",
        ],
    }


def validate_cycle007_material_registry(registry: dict, *, as_of: Any) -> dict:
    """Add issuer/reviewer independence and method-scope checks to the v2 gate."""
    from uqpu.cycle006_delta01 import validate_material_registry_v2

    result = validate_material_registry_v2(registry, as_of=as_of)
    errors_by_id = {key: list(value) for key, value in result["errors_by_prerequisite"].items()}
    expected_method_scope = registry.get("method_scope_id")
    for slot in registry.get("slots", []):
        prerequisite_id = slot.get("prerequisite_id") or "<missing>"
        errors = errors_by_id.setdefault(prerequisite_id, [])
        evidence = slot.get("evidence", {})
        if not expected_method_scope:
            errors.append("method_scope_id_missing")
        elif evidence.get("method_scope_id") != expected_method_scope:
            errors.append("method_scope_mismatch")
        issuer = evidence.get("issuer_or_operator")
        reviewer = evidence.get("reviewer")
        if issuer and reviewer and issuer == reviewer:
            errors.append("issuer_reviewer_collision")
    passing = sorted(key for key, errors in errors_by_id.items() if not errors)
    result.update({
        "errors_by_prerequisite": errors_by_id,
        "passing_prerequisite_ids": passing,
        "passing_count": len(passing),
        "ready": len(passing) == result["required_count"],
        "evidence_class": "SYNTHETIC_METHOD_SCOPE_AND_ROLE_SEPARATION_GATE_NO_MATERIAL_EVIDENCE",
    })
    return result


def validate_cycle007_custody_fixture(fixture: dict) -> list[str]:
    """Extend the existing custody validator with event-ID uniqueness."""
    from uqpu.cycle006_delta01 import validate_custody_fixture

    errors = validate_custody_fixture(fixture)
    event_ids = [event.get("event_id") for event in fixture.get("events", [])]
    if any(not event_id for event_id in event_ids):
        errors.append("event_id_missing")
    if len(event_ids) != len(set(event_ids)):
        errors.append("duplicate_event_id")
    return sorted(set(errors))


def validate_cycle007_complete_cost(ledger: dict) -> dict:
    """Require cost-unit and provider-receipt agreement before exposing totals."""
    from uqpu.cycle006_delta01 import COST_COMPONENTS, validate_complete_cost_v2

    result = validate_complete_cost_v2(ledger)
    errors = list(result["errors"])
    currency = ledger.get("currency")
    amount_unit = ledger.get("amount_unit")
    if not amount_unit:
        errors.append("amount_unit_missing")
    elif amount_unit != currency:
        errors.append("amount_unit_currency_mismatch")
    for name in COST_COMPONENTS:
        component = ledger.get("components", {}).get(name)
        if isinstance(component, dict) and component.get("unit_code") != amount_unit:
            errors.append(f"unit_code_mismatch:{name}")
    accepted = ledger.get("accepted_outputs", {})
    if accepted.get("unit_code") != "count":
        errors.append("accepted_output_unit_must_be_count")
    receipt_id = ledger.get("provider_receipt", {}).get("receipt_id")
    bill = ledger.get("components", {}).get("provider_actual_bill", {})
    if not receipt_id or bill.get("receipt_id") != receipt_id:
        errors.append("provider_receipt_mismatch")
    errors = sorted(set(errors))
    complete = not errors
    count = accepted.get("count")
    total = result["total_cost"] if complete else None
    result.update({
        "errors": errors,
        "complete": complete,
        "total_cost": total,
        "cost_per_accepted_output": total / count if complete else None,
        "currency": currency if complete else None,
        "refusal_active": not complete,
    })
    return result


def validate_ai_dataset_replay(frozen: dict, replayed: dict) -> dict:
    """Reject any frozen-data, seed, generator, or provenance replay mismatch."""
    errors = []
    for field in ("baseline_file_sha256", "generator_module_sha256", "generator", "seed_policy"):
        if frozen.get(field) != replayed.get(field):
            errors.append(f"replay_provenance_mismatch:{field}")
    for split in ("train", "held_out"):
        if frozen.get(split) != replayed.get(split):
            errors.append(f"replay_hash_mismatch:{split}")
    return {
        "replay_valid": not errors,
        "errors": errors,
        "candidate_result_admissible": False,
        "evidence_class": "DETERMINISTIC_TOY_DATA_REPLAY_GATE_NO_CANDIDATE_QUALITY_OR_COST",
    }


def qasm_measurement_map(ast: list[dict]) -> dict[int, int]:
    """Return classical-bit to qubit assignments, rejecting duplicate outputs."""
    mapping = {}
    for statement in ast:
        if statement.get("kind") != "measure":
            continue
        classical_bit, qubit = map(int, statement["arguments"])
        if classical_bit in mapping:
            raise ValueError(f"duplicate classical measurement target: {classical_bit}")
        mapping[classical_bit] = qubit
    return dict(sorted(mapping.items()))


def audit_dimension_contracts(unified_registry: dict, scm_registry: dict) -> dict:
    """Inventory type labels and machine-readable dimension-vector coverage.

    The audit deliberately does not infer dimensions from free-text labels such
    as ``"joule per kg"`` or ``"same as y_wk"``. Those require an explicit
    quantity-kind and unit registry before equation balance can be checked.
    """
    errors: list[str] = []
    lane_rows = {
        lane: {
            "umrl_equations": 0,
            "umrl_variables": 0,
            "scm_equations": 0,
            "scm_variables": 0,
            "unit_or_type_present": 0,
            "quantity_kinds": 0,
            "unit_codes": 0,
            "machine_dimension_vectors": 0,
        }
        for lane in LANES
    }
    declarations: list[dict] = []
    unit_or_type_present = 0
    dimension_vectors_present = 0
    invalid_dimension_vectors = 0

    for equation in unified_registry.get("equations", []):
        equation_id = equation.get("equation_id", "<missing>")
        owners = set(equation.get("owner_lanes", []))
        if not owners or not owners <= set(LANES):
            errors.append(f"umrl_owner_lanes_invalid:{equation_id}")
            owners &= set(LANES)
        for lane in owners:
            lane_rows[lane]["umrl_equations"] += 1
        for variable in equation.get("variables", []):
            row = {
                "equation_id": equation_id,
                "symbol": variable.get("symbol"),
                "unit_or_type": variable.get("unit_or_type"),
                "quantity_kind_present": bool(variable.get("quantity_kind")),
                "unit_code_present": bool(variable.get("unit_code")),
                "dimension_vector_present": "dimension_vector" in variable,
                "owners": sorted(owners),
                "registry_kind": "UMRL",
            }
            if not variable.get("symbol") or not variable.get("unit_or_type"):
                errors.append(f"umrl_variable_type_label_missing:{equation_id}")
            else:
                unit_or_type_present += 1
            if "dimension_vector" in variable:
                dimension_vectors_present += 1
                row["dimension_vector_valid"] = _valid_dimension_vector(
                    variable["dimension_vector"]
                )
                if not row["dimension_vector_valid"]:
                    invalid_dimension_vectors += 1
                    errors.append(f"umrl_dimension_vector_invalid:{equation_id}:{row['symbol']}")
            declarations.append(row)
            for lane in owners:
                lane_rows[lane]["umrl_variables"] += 1
                if variable.get("unit_or_type"):
                    lane_rows[lane]["unit_or_type_present"] += 1
                if variable.get("quantity_kind"):
                    lane_rows[lane]["quantity_kinds"] += 1
                if variable.get("unit_code"):
                    lane_rows[lane]["unit_codes"] += 1
                if "dimension_vector" in variable and row.get("dimension_vector_valid"):
                    lane_rows[lane]["machine_dimension_vectors"] += 1

    for equation in scm_registry.get("equations", []):
        equation_id = equation.get("equation_id", "<missing>")
        lane_rows["SCM"]["scm_equations"] += 1
        for variable in equation.get("variables", []):
            row = {
                "equation_id": equation_id,
                "symbol": variable.get("symbol"),
                "unit_or_type": variable.get("unit_or_type"),
                "quantity_kind_present": bool(variable.get("quantity_kind")),
                "unit_code_present": bool(variable.get("unit_code")),
                "dimension_vector_present": "dimension_vector" in variable,
                "owners": ["SCM"],
                "registry_kind": "SCM",
            }
            if not variable.get("symbol") or not variable.get("unit_or_type"):
                errors.append(f"scm_variable_type_label_missing:{equation_id}")
            else:
                unit_or_type_present += 1
                lane_rows["SCM"]["unit_or_type_present"] += 1
            if variable.get("quantity_kind"):
                lane_rows["SCM"]["quantity_kinds"] += 1
            if variable.get("unit_code"):
                lane_rows["SCM"]["unit_codes"] += 1
            if "dimension_vector" in variable:
                dimension_vectors_present += 1
                row["dimension_vector_valid"] = _valid_dimension_vector(
                    variable["dimension_vector"]
                )
                if not row["dimension_vector_valid"]:
                    invalid_dimension_vectors += 1
                    errors.append(f"scm_dimension_vector_invalid:{equation_id}:{row['symbol']}")
                elif row["dimension_vector_valid"]:
                    lane_rows["SCM"]["machine_dimension_vectors"] += 1
            declarations.append(row)
            lane_rows["SCM"]["scm_variables"] += 1

    if {lane for lane, row in lane_rows.items() if row["umrl_equations"]} != set(LANES):
        errors.append("umrl_lane_equation_coverage_incomplete")
    if not lane_rows["SCM"]["scm_equations"]:
        errors.append("scm_equations_missing")

    variable_count = len(declarations)
    return {
        "schema": "uqpu-cycle007-delta01-dimension-contract-audit-v1",
        "cycle": "007",
        "delta": "01",
        "errors": errors,
        "valid_registry_structure": not errors,
        "equation_count": {
            "umrl": len(unified_registry.get("equations", [])),
            "scm": len(scm_registry.get("equations", [])),
        },
        "goal_count": len(unified_registry.get("goal_contracts", [])),
        "lane_count": len(LANES),
        "variable_declaration_count": variable_count,
        "unit_or_type_present_count": unit_or_type_present,
        "unit_or_type_coverage": (
            unit_or_type_present / variable_count if variable_count else 0.0
        ),
        "machine_dimension_vector_count": dimension_vectors_present,
        "quantity_kind_count": sum(
            bool(row.get("quantity_kind_present")) for row in declarations
        ),
        "unit_code_count": sum(bool(row.get("unit_code_present")) for row in declarations),
        "valid_machine_dimension_vector_count": sum(
            bool(row.get("dimension_vector_valid")) for row in declarations
        ),
        "invalid_machine_dimension_vector_count": invalid_dimension_vectors,
        "machine_dimension_vector_coverage": (
            dimension_vectors_present / variable_count if variable_count else 0.0
        ),
        "project_dimension_basis": list(PROJECT_DIMENSION_BASIS),
        "lane_audit": lane_rows,
        "dimensionally_auditable": False,
        "dimensional_consistency_claim": False,
        "evidence_class": "STRUCTURAL_SCHEMA_AUDIT_NOT_DIMENSIONAL_PROOF",
        "finding": (
            "Free-text unit_or_type labels cover the declarations but do not "
            "supply machine-readable quantity kinds or dimension vectors. "
            "Do not infer dimensional balance until quantity kinds distinguish "
            "physical quantities from states, categories, records, information "
            "and fictional model variables."
        ),
        "next_gate": (
            "Define quantity_kind and a canonical unit registry; then annotate "
            "only dimensional quantities with exact rational exponent vectors "
            "and add equation-level balance rules."
        ),
        "variable_declarations": declarations,
    }
