"""Cycle 008 Delta 01: typed quantities and fictional SCM invariants.

This module is a small, explicit checker for selected project equations and
fictional-world rules. It does not infer units from prose or turn canon values
into measurements.
"""

from __future__ import annotations

from fractions import Fraction
import math
from typing import Any


DIMENSION_BASIS = (
    "length", "mass", "time", "electric_current", "temperature",
    "amount_of_substance", "luminous_intensity", "currency",
    "information", "count",
)

REAL_EVIDENCE_TYPES = {
    "DEFINITION", "THEORY", "MODEL", "SIMULATION", "LOCAL_MEASUREMENT",
    "PROVIDER_MEASUREMENT", "PHYSICAL_EXPERIMENT", "COMMERCIAL_OBSERVATION",
}
FICTION_EVIDENCE_TYPES = {
    "FICTIONAL_ONTOLOGY", "FICTIONAL_MODEL", "FICTIONAL_PROTOCOL",
}
DOMAIN_SORTS = {"REAL_MODEL", "REAL_EMPIRICAL", "FICTION_CANON", "PROTOCOL_RECORD"}
LANES = (
    "A", "B", "C", "D", "E", "F", "G", "H",
    "FND/EQN", "SCM", "AI-COST", "QOS/QSVT",
)


def _fraction(value: Any) -> Fraction | None:
    if isinstance(value, bool) or isinstance(value, float):
        return None
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError):
            return None
    return None


def _vector(value: Any) -> dict[str, Fraction] | None:
    if not isinstance(value, dict) or set(value) != set(DIMENSION_BASIS):
        return None
    result = {}
    for axis in DIMENSION_BASIS:
        exponent = _fraction(value[axis])
        if exponent is None:
            return None
        result[axis] = exponent
    return result


def _vector_json(value: dict[str, Fraction]) -> dict[str, str]:
    return {
        axis: str(value[axis])
        for axis in DIMENSION_BASIS
    }


def _zero_vector() -> dict[str, Fraction]:
    return {axis: Fraction(0) for axis in DIMENSION_BASIS}


def validate_quantity_type(
    quantity: dict[str, Any],
    unit_registry: dict[str, dict[str, Any]],
) -> list[str]:
    """Check an explicit quantity declaration without guessing its meaning."""
    errors = []
    quantity_id = quantity.get("quantity_id") or "<missing>"
    domain_sort = quantity.get("domain_sort")
    evidence_type = quantity.get("evidence_type")

    if domain_sort not in DOMAIN_SORTS:
        errors.append(f"domain_sort_invalid:{quantity_id}")
    if not quantity.get("quantity_kind"):
        errors.append(f"quantity_kind_missing:{quantity_id}")

    if domain_sort == "FICTION_CANON":
        if evidence_type not in FICTION_EVIDENCE_TYPES:
            errors.append(f"fiction_evidence_type_invalid:{quantity_id}")
        if quantity.get("dimension_vector") is not None:
            errors.append(f"fiction_dimension_vector_requires_validated_bridge:{quantity_id}")
        unit_code = quantity.get("unit_code")
        if unit_code is not None and not str(unit_code).startswith("CANON:"):
            errors.append(f"fiction_unit_must_be_canon_scoped:{quantity_id}")
    elif domain_sort in {"REAL_MODEL", "REAL_EMPIRICAL"}:
        if evidence_type not in REAL_EVIDENCE_TYPES:
            errors.append(f"real_evidence_type_invalid:{quantity_id}")
        unit_code = quantity.get("unit_code")
        dimensions = _vector(quantity.get("dimension_vector"))
        if not unit_code:
            errors.append(f"real_quantity_unit_code_missing:{quantity_id}")
        if dimensions is None:
            errors.append(f"real_quantity_dimension_vector_invalid:{quantity_id}")
        unit = unit_registry.get(unit_code) if unit_code else None
        if not unit:
            errors.append(f"unit_code_unregistered:{quantity_id}")
        elif dimensions is not None and _vector(unit.get("dimension_vector")) != dimensions:
            errors.append(f"unit_dimension_mismatch:{quantity_id}")
    elif domain_sort == "PROTOCOL_RECORD":
        if evidence_type not in REAL_EVIDENCE_TYPES:
            errors.append(f"protocol_evidence_type_invalid:{quantity_id}")
        if quantity.get("dimension_vector") is not None:
            errors.append(f"protocol_record_must_not_claim_physical_dimension:{quantity_id}")

    return errors


def validate_domain_bridge(bridge: dict[str, Any] | None) -> dict[str, Any]:
    """Require independent physical validation for any fictional-to-real cast."""
    errors = []
    if not isinstance(bridge, dict):
        return {"allowed": False, "errors": ["bridge_missing"]}
    if bridge.get("source_sort") != "FICTION_CANON":
        errors.append("bridge_source_sort_must_be_fiction")
    if bridge.get("target_sort") not in {"REAL_MODEL", "REAL_EMPIRICAL"}:
        errors.append("bridge_target_sort_invalid")
    if bridge.get("evidence_type") != "PHYSICAL_EXPERIMENT":
        errors.append("bridge_physical_experiment_required")
    if bridge.get("independent_replication") is not True:
        errors.append("bridge_independent_replication_required")
    if bridge.get("provenance_id") in (None, ""):
        errors.append("bridge_provenance_missing")
    if bridge.get("status") != "VALIDATED":
        errors.append("bridge_not_validated")
    return {"allowed": not errors, "errors": errors}


def audit_dimension_equation(
    equation: dict[str, Any],
    quantities: dict[str, dict[str, Any]],
    unit_registry: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    """Check every additive RHS term against the typed LHS dimension."""
    errors = []
    lhs_id = equation.get("lhs")
    lhs = quantities.get(lhs_id)
    if lhs is None:
        return {
            "equation_id": equation.get("equation_id"),
            "balanced": False,
            "errors": ["lhs_quantity_missing"],
        }

    lhs_errors = validate_quantity_type(lhs, unit_registry)
    errors.extend(f"lhs:{error}" for error in lhs_errors)
    lhs_vector = _vector(lhs.get("dimension_vector"))
    if lhs_vector is None:
        errors.append("lhs_dimension_vector_invalid")
        lhs_vector = _zero_vector()

    if not isinstance(equation.get("rhs_terms"), list) or not equation["rhs_terms"]:
        errors.append("rhs_terms_missing")
        rhs_terms = []
    else:
        rhs_terms = equation["rhs_terms"]

    rhs_vectors = []
    for term_index, term in enumerate(rhs_terms):
        total = _zero_vector()
        factors = term.get("factors", []) if isinstance(term, dict) else []
        if not factors:
            errors.append(f"rhs_term_empty:{term_index}")
            continue
        for factor in factors:
            symbol = factor.get("quantity_id")
            quantity = quantities.get(symbol)
            if quantity is None:
                errors.append(f"rhs_quantity_missing:{term_index}:{symbol}")
                continue
            errors.extend(
                f"rhs:{error}"
                for error in validate_quantity_type(quantity, unit_registry)
            )
            if quantity.get("domain_sort") != lhs.get("domain_sort"):
                errors.append(f"domain_sort_mismatch:{term_index}:{symbol}")
            vector = _vector(quantity.get("dimension_vector"))
            power = _fraction(factor.get("power"))
            if vector is None:
                errors.append(f"rhs_dimension_vector_invalid:{term_index}:{symbol}")
                continue
            if power is None:
                errors.append(f"rhs_power_invalid:{term_index}:{symbol}")
                continue
            for axis in DIMENSION_BASIS:
                total[axis] += vector[axis] * power
        rhs_vectors.append(total)
        if total != lhs_vector:
            errors.append(f"dimension_mismatch_in_rhs_term:{term_index}")

    return {
        "equation_id": equation.get("equation_id"),
        "balanced": not errors,
        "lhs_dimension_vector": _vector_json(lhs_vector),
        "rhs_term_dimension_vectors": [_vector_json(row) for row in rhs_vectors],
        "errors": sorted(set(errors)),
        "scope": "DECLARED_SUBSET_ONLY",
    }


def validate_consent_request(
    grant: dict[str, Any],
    request: dict[str, Any],
    *,
    used_nonces: set[str] | None = None,
) -> dict[str, Any]:
    """Fail closed unless scoped, live, unrevoked consent and agency gates pass."""
    used_nonces = used_nonces or set()
    errors = []
    scoped_fields = ("subject_id", "action", "purpose", "resource_id")
    for field in scoped_fields:
        if not grant.get(field):
            errors.append(f"grant_scope_missing:{field}")
        elif grant.get(field) != request.get(field):
            errors.append(f"grant_scope_mismatch:{field}")

    issued = grant.get("issued_at_tick")
    expires = grant.get("expires_at_tick")
    now = request.get("now_tick")
    if any(type(value) is not int for value in (issued, expires, now)):
        errors.append("consent_time_fields_must_be_integer_ticks")
    elif not issued <= now < expires:
        errors.append("consent_outside_validity_window")
    if grant.get("consent_state") != "GRANTED":
        errors.append("consent_not_granted")
    if grant.get("revoked") is not False:
        errors.append("consent_revoked_or_unknown")
    nonce = grant.get("nonce")
    if not nonce:
        errors.append("consent_nonce_missing")
    elif nonce in used_nonces:
        errors.append("consent_nonce_replayed")
    if request.get("agency_active") is not True:
        errors.append("subject_agency_not_active")
    if request.get("safety_pass") is not True:
        errors.append("safety_gate_not_passed")
    if not request.get("audit_record_id"):
        errors.append("audit_record_missing")

    return {
        "authorized": not errors,
        "errors": sorted(set(errors)),
        "domain_sort": "FICTION_CANON",
        "evidence_class": "SYNTHETIC_CONSENT_GATE_FIXTURE",
    }


def validate_fictional_conservation(
    ledger: dict[str, Any],
    *,
    tolerance: Any,
) -> dict[str, Any]:
    """Check an authored canon ledger in one declared fictional unit."""
    errors = []
    entries = ledger.get("entries", [])
    if ledger.get("domain_sort") != "FICTION_CANON":
        errors.append("conservation_ledger_must_be_fiction_only")
    if not entries:
        errors.append("conservation_entries_missing")
    unit_codes = {row.get("unit_code") for row in entries}
    if len(unit_codes) != 1 or None in unit_codes:
        errors.append("conservation_unit_mismatch")
    elif not next(iter(unit_codes)).startswith("CANON:"):
        errors.append("conservation_unit_must_be_canon_scoped")
    quantity_ids = {row.get("quantity_id") for row in entries}
    if len(quantity_ids) != 1 or None in quantity_ids:
        errors.append("conservation_quantity_mismatch")
    canon_versions = {row.get("canon_version") for row in entries}
    if len(canon_versions) != 1 or None in canon_versions:
        errors.append("conservation_canon_version_mismatch")

    values = [_fraction(row.get("delta")) for row in entries]
    if any(value is None for value in values):
        errors.append("conservation_delta_must_be_exact_rational")
    uncertainty = _fraction(tolerance)
    if uncertainty is None or uncertainty < 0:
        errors.append("conservation_tolerance_invalid")
    residual = sum((value for value in values if value is not None), Fraction(0))
    balanced = (
        not errors
        and uncertainty is not None
        and abs(residual) <= uncertainty
    )
    if not errors and not balanced:
        errors.append("conservation_residual_exceeds_tolerance")
    return {
        "balanced": balanced,
        "residual": str(residual),
        "tolerance": str(uncertainty) if uncertainty is not None else None,
        "unit_code": next(iter(unit_codes)) if len(unit_codes) == 1 else None,
        "errors": sorted(set(errors)),
        "claim_ceiling": "FICTIONAL_INTERNAL_CONSISTENCY_ONLY",
    }


def audit_five_volume_contracts(volumes: list[dict[str, Any]]) -> dict[str, Any]:
    """Require five versioned canon volumes and their local agency/firewall rules."""
    required = {
        1: "CANON_TAXONOMY_VERSIONED",
        2: "CONSENT_SCOPED_CONTROL",
        3: "CHALLENGE_RESPONSE_AUTHENTICATION",
        4: "ANTI_REPLAY_AND_NONCOERCION",
        5: "DOUBLE_ENTRY_AND_CONSENTED_SETTLEMENT",
    }
    errors = []
    found = {}
    for row in volumes:
        number = row.get("volume")
        if number in found:
            errors.append(f"duplicate_volume:{number}")
        found[number] = row
    if set(found) != set(required):
        errors.append("exactly_five_volumes_required")
    for number, invariant in required.items():
        row = found.get(number, {})
        if row.get("domain_sort") != "FICTION_CANON":
            errors.append(f"volume_domain_sort_invalid:{number}")
        if row.get("fiction_only") is not True:
            errors.append(f"volume_fiction_boundary_missing:{number}")
        if row.get("real_evidence_cast") != "FORBIDDEN_WITHOUT_VALIDATED_BRIDGE":
            errors.append(f"volume_no_cast_rule_missing:{number}")
        if invariant not in row.get("required_invariants", []):
            errors.append(f"volume_required_invariant_missing:{number}:{invariant}")
    return {
        "valid": not errors,
        "volume_count": len(found),
        "errors": sorted(set(errors)),
        "claim_ceiling": "FICTIONAL_CANON_CONSISTENCY_ONLY",
    }


def audit_scm_equation_extensions(equations: list[dict[str, Any]]) -> dict[str, Any]:
    """Require typed fiction-only declarations for the four Cycle 008 additions."""
    expected_ids = {f"SCM-MATH-{number:03d}" for number in range(20, 24)}
    errors = []
    found = {}
    for equation in equations:
        equation_id = equation.get("equation_id")
        if not equation_id:
            errors.append("scm_extension_equation_id_missing")
            continue
        if equation_id in found:
            errors.append(f"scm_extension_equation_duplicate:{equation_id}")
        found[equation_id] = equation
    if set(found) != expected_ids:
        errors.append("scm_extension_must_cover_020_through_023")
    for equation_id, equation in found.items():
        if equation.get("domain_sort") != "FICTION_CANON":
            errors.append(f"scm_extension_domain_sort_invalid:{equation_id}")
        if equation.get("evidence_type") not in FICTION_EVIDENCE_TYPES:
            errors.append(f"scm_extension_evidence_type_invalid:{equation_id}")
        if equation.get("real_world_status") in (None, "", "VALIDATED"):
            errors.append(f"scm_extension_claim_boundary_missing:{equation_id}")
        if not equation.get("falsifier"):
            errors.append(f"scm_extension_falsifier_missing:{equation_id}")
        variables = equation.get("variables", [])
        if not variables:
            errors.append(f"scm_extension_variables_missing:{equation_id}")
        for variable in variables:
            if variable.get("domain_sort") != "FICTION_CANON":
                errors.append(f"scm_extension_variable_sort_invalid:{equation_id}")
            if not variable.get("quantity_kind"):
                errors.append(f"scm_extension_variable_kind_missing:{equation_id}")
    return {
        "valid": not errors,
        "equation_ids": sorted(found),
        "errors": sorted(set(errors)),
        "claim_ceiling": "FICTIONAL_FORMALISM_ONLY",
    }


def audit_lane_links(lane_links: dict[str, Any]) -> dict[str, Any]:
    """Check that the typed interface names every lane and only known equations."""
    errors = []
    if set(lane_links) != set(LANES):
        errors.append("lane_link_set_must_cover_all_twelve")
    known = {f"UMRL-{number:03d}" for number in range(1, 32)}
    known.update(f"SCM-MATH-{number:03d}" for number in range(20, 24))
    for lane in LANES:
        identifiers = lane_links.get(lane)
        if not isinstance(identifiers, list) or not identifiers:
            errors.append(f"lane_link_missing:{lane}")
            continue
        for identifier in identifiers:
            normalized = identifier.split(":", 1)[0]
            if normalized not in known:
                errors.append(f"lane_link_equation_unknown:{lane}:{identifier}")
    return {
        "valid": not errors,
        "lane_count": len(lane_links),
        "errors": sorted(set(errors)),
    }


def audit_umrl_extension(extension: dict[str, Any]) -> dict[str, Any]:
    """Validate the structural fields of the versioned UMRL-031 addition."""
    errors = []
    if extension.get("equation_id") != "UMRL-031":
        errors.append("umrl_extension_id_invalid")
    if extension.get("version") != "0.2":
        errors.append("umrl_extension_version_invalid")
    for field in ("name", "expression", "domain_sort", "evidence_type", "falsifier"):
        if not extension.get(field):
            errors.append(f"umrl_extension_field_missing:{field}")
    if extension.get("domain_sort") != "PROJECT_WIDE_TYPE_RULE":
        errors.append("umrl_extension_domain_sort_invalid")
    if extension.get("evidence_type") != "FORMAL_DEFINITION":
        errors.append("umrl_extension_evidence_type_invalid")
    return {"valid": not errors, "errors": errors}


def build_cycle008_math_audit(registry: dict[str, Any]) -> dict[str, Any]:
    """Generate a deterministic validation summary for the Cycle 008 supplement."""
    unit_registry = registry.get("unit_registry", {})
    quantities_list = registry.get("quantities", [])
    quantities = {row.get("quantity_id"): row for row in quantities_list}
    errors = []
    if len(quantities) != len(quantities_list) or None in quantities:
        errors.append("quantity_ids_missing_or_duplicate")
    quantity_errors = {
        key: validate_quantity_type(row, unit_registry)
        for key, row in quantities.items()
    }
    equations = [
        audit_dimension_equation(row, quantities, unit_registry)
        for row in registry.get("dimension_equations", [])
    ]
    if any(quantity_errors.values()):
        errors.append("quantity_type_validation_failed")
    if any(not row["balanced"] for row in equations):
        errors.append("dimension_equation_validation_failed")

    volume_audit = audit_five_volume_contracts(registry.get("five_volume_contracts", []))
    if not volume_audit["valid"]:
        errors.append("five_volume_contract_validation_failed")
    lane_audit = audit_lane_links(registry.get("lane_links", {}))
    if not lane_audit["valid"]:
        errors.append("lane_link_validation_failed")
    umrl_extension = audit_umrl_extension(registry.get("umrl_extension", {}))
    if not umrl_extension["valid"]:
        errors.append("umrl_extension_validation_failed")
    scm_equation_audit = audit_scm_equation_extensions(
        registry.get("scm_equations", [])
    )
    if not scm_equation_audit["valid"]:
        errors.append("scm_equation_extension_validation_failed")

    consent = registry.get("consent_fixtures", {})
    consent_positive = validate_consent_request(
        consent.get("valid", {}).get("grant", {}),
        consent.get("valid", {}).get("request", {}),
    )
    consent_negative = [
        validate_consent_request(
            row.get("grant", {}),
            row.get("request", {}),
            used_nonces=set(row.get("used_nonces", [])),
        )
        for row in consent.get("negative", [])
    ]
    if not consent_positive["authorized"] or any(row["authorized"] for row in consent_negative):
        errors.append("consent_fixture_gate_failed")

    conservation = registry.get("conservation_fixtures", {})
    conservation_positive = validate_fictional_conservation(
        conservation.get("valid", {}), tolerance=conservation.get("valid_tolerance")
    )
    conservation_negative = [
        validate_fictional_conservation(
            row.get("ledger", {}),
            tolerance=row.get("tolerance"),
        )
        for row in conservation.get("negative", [])
    ]
    if not conservation_positive["balanced"] or any(
        row["balanced"] for row in conservation_negative
    ):
        errors.append("fictional_conservation_fixture_gate_failed")

    cast_negative = validate_domain_bridge(registry.get("bridge_fixture_unvalidated"))
    if cast_negative["allowed"]:
        errors.append("no_cast_fixture_gate_failed")

    return {
        "schema": "uqpu-cycle008-delta01-typed-math-scm-audit-v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": sorted(set(errors)),
        "quantity_count": len(quantities),
        "quantity_type_errors": quantity_errors,
        "dimension_equation_count": len(equations),
        "dimension_equations": equations,
        "umrl_extension": umrl_extension,
        "scm_equation_extensions": scm_equation_audit,
        "five_volume_contract": volume_audit,
        "lane_links": lane_audit,
        "consent_gate": {
            "valid_case_authorized": consent_positive["authorized"],
            "negative_cases_rejected": sum(not row["authorized"] for row in consent_negative),
            "negative_case_count": len(consent_negative),
        },
        "fictional_conservation": {
            "valid_case_balanced": conservation_positive["balanced"],
            "negative_cases_rejected": sum(not row["balanced"] for row in conservation_negative),
            "negative_case_count": len(conservation_negative),
        },
        "fiction_to_real_cast": {
            "unvalidated_cast_rejected": not cast_negative["allowed"],
            "no_synthetic_valid_bridge_fixture": "bridge_fixture_valid" not in registry,
        },
        "evidence_class": "FORMAL_SCHEMA_AND_SYNTHETIC_FIXTURES_NO_PHYSICAL_OR_SPIRITUAL_MEASUREMENT",
        "nonclaims": [
            "The dimension check covers only the explicitly declared subset.",
            "Canon state and conservation checks test fictional consistency, not physical laws.",
            "No positive fictional-to-real bridge fixture is fabricated.",
            "No empirical spiritual communication, mind control, or portal capability is demonstrated.",
        ],
    }


def compare_deterministic_solver_restarts(
    *, node_count: int, seed: int, edge_probability: float = 0.3
) -> dict[str, Any]:
    """Compare exact completion with two seeded local restart counts."""
    from .cycle005_delta01 import benchmark_scale_case

    if type(node_count) is not int or node_count < 2 or node_count > 16:
        raise ValueError("node_count must be in the bounded range 2..16")
    state_count = 1 << node_count
    exact_rows = []
    solver_variants = []
    for restarts in (32, 128):
        row = benchmark_scale_case(
            node_count,
            seed,
            edge_probability=edge_probability,
            max_states=state_count,
            deadline_seconds=30.0,
            heuristic_restarts=restarts,
        )
        exact_rows.append(row["exact"])
        heuristic = row["heuristic"]
        solver_variants.append({
            "method": heuristic["method"],
            "restarts": restarts,
            "objective": heuristic["objective"],
            "gap_to_exact": heuristic["objective_gap_to_exact"],
            "elapsed_seconds": heuristic["elapsed_seconds"],
        })
    if not all(row["complete"] and row["states_evaluated"] == state_count for row in exact_rows):
        raise ValueError("exact control did not exhaust the bounded state space")
    if len({row["best_objective"] for row in exact_rows}) != 1:
        raise ValueError("exact reference drift between restart comparisons")
    return {
        "schema": "uqpu-cycle008-solver-restart-comparison-v1",
        "evidence_class": "LOCAL_SEEDED_CLASSICAL_SOFTWARE_COMPARISON",
        "fixture": {
            "generator": "seeded_erdos_renyi_maxcut",
            "node_count": node_count,
            "seed": seed,
            "edge_probability": edge_probability,
        },
        "exact_control": {
            "complete": True,
            "states_evaluated": state_count,
            "total_state_space": state_count,
            "best_objective": exact_rows[0]["best_objective"],
        },
        "solver_variants": solver_variants,
        "nonclaims": [
            "This is one generated finite fixture, not a competitive benchmark suite.",
            "Restart sensitivity is not an asymptotic scaling law.",
            "No GPU, QPU, energy, provider, or hardware comparison is made.",
        ],
    }


def _canonical_sha256(value: Any) -> str:
    import hashlib
    import json

    payload = json.dumps(
        value, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def validate_synthetic_request_receipt(
    request: dict[str, Any], receipt: dict[str, Any]
) -> dict[str, Any]:
    """Verify hash-linked schema evidence while requiring a non-execution receipt."""
    import hashlib
    import json

    errors = []
    token = request.get("clientToken")
    if not isinstance(token, str) or not token:
        errors.append("client_token_missing")
    request_hash = _canonical_sha256(request)
    if receipt.get("request_sha256") != request_hash:
        errors.append("request_hash_mismatch")
    if receipt.get("clientToken") != token:
        errors.append("receipt_token_mismatch")
    if receipt.get("submitted") is not False:
        errors.append("submission_must_remain_disabled")
    if receipt.get("execution_id") is not None or receipt.get("actual_bill") is not None:
        errors.append("synthetic_receipt_must_not_claim_execution_or_bill")
    body = {key: value for key, value in receipt.items() if key != "receipt_sha256"}
    expected_receipt_hash = hashlib.sha256(json.dumps(
        body, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8")).hexdigest()
    if receipt.get("receipt_sha256") != expected_receipt_hash:
        errors.append("receipt_hash_mismatch")
    return {
        "valid": not errors,
        "errors": sorted(set(errors)),
        "evidence_class": "SYNTHETIC_HASH_LINKED_REQUEST_RECEIPT_GATE",
        "submission_authorized": False,
    }


def build_synthetic_request_receipt(request: dict[str, Any]) -> dict[str, Any]:
    import hashlib
    import json

    receipt = {
        "clientToken": request.get("clientToken"),
        "request_sha256": _canonical_sha256(request),
        "submitted": False,
        "execution_id": None,
        "actual_bill": None,
        "receipt_kind": "SYNTHETIC_SCHEMA_FIXTURE",
    }
    receipt["receipt_sha256"] = hashlib.sha256(json.dumps(
        receipt, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8")).hexdigest()
    return receipt


def plan_archive_download(size_bytes: Any, *, max_bytes: int) -> dict[str, Any]:
    """Return a resource decision only; this helper never downloads a file."""
    errors = []
    if type(size_bytes) is not int or size_bytes < 0:
        errors.append("archive_size_must_be_nonnegative_integer")
    if type(max_bytes) is not int or max_bytes < 1:
        errors.append("max_bytes_must_be_positive_integer")
    allowed = not errors and size_bytes <= max_bytes
    return {
        "allowed_by_size_cap": allowed,
        "download_performed": False,
        "size_bytes": size_bytes if type(size_bytes) is int else None,
        "max_bytes": max_bytes if type(max_bytes) is int else None,
        "errors": errors,
        "evidence_class": "RESOURCE_GUARDED_ARCHIVE_PLAN_NO_DOWNLOAD",
    }


def validate_material_measurement_record(record: dict[str, Any]) -> dict[str, Any]:
    """Validate a synthetic, function-specific measurement record's units."""
    errors = []
    required = (
        "record_id", "lot_id", "function_id", "quantity_id", "unit_code",
        "control_id", "calibration_id", "evidence_status",
    )
    for field in required:
        if not record.get(field):
            errors.append(f"material_field_missing:{field}")
    value = _fraction(record.get("value"))
    uncertainty = _fraction(record.get("expanded_uncertainty"))
    if value is None:
        errors.append("material_value_must_be_exact_rational")
    if uncertainty is None or uncertainty < 0:
        errors.append("material_uncertainty_must_be_nonnegative_exact_rational")
    if record.get("unit_code") != record.get("uncertainty_unit_code"):
        errors.append("material_uncertainty_unit_mismatch")
    if record.get("synthetic") is not True:
        errors.append("cycle008_material_record_must_be_synthetic")
    if record.get("physical_sampled") is not False:
        errors.append("physical_sample_must_remain_absent")
    return {
        "valid": not errors,
        "errors": sorted(set(errors)),
        "evidence_class": "SYNTHETIC_FUNCTION_SPECIFIC_MATERIAL_RECORD",
        "physical_measurement_claim": False,
    }


def validate_cost_interval(ledger: dict[str, Any]) -> dict[str, Any]:
    """Compute a bounded synthetic cost interval only with common units and outputs."""
    errors = []
    currency = ledger.get("currency")
    components = ledger.get("components")
    required = ledger.get("required_components", [])
    if not currency:
        errors.append("currency_missing")
    if not isinstance(components, dict):
        components = {}
        errors.append("components_missing")
    if not required or any(name not in components for name in required):
        errors.append("required_component_missing")
    provenance = ledger.get("accepted_output_provenance", {})
    if not provenance.get("contract_id"):
        errors.append("accepted_output_contract_id_missing")
    digest = provenance.get("sha256")
    if not isinstance(digest, str) or len(digest) != 64 or any(
        character not in "0123456789abcdef" for character in digest.lower()
    ):
        errors.append("accepted_output_provenance_hash_invalid")
    if provenance.get("evidence_status") not in {"SYNTHETIC", "MEASURED"}:
        errors.append("accepted_output_provenance_status_invalid")
    lower_total = Fraction(0)
    upper_total = Fraction(0)
    for name in required:
        component = components.get(name, {})
        if component.get("currency") != currency:
            errors.append(f"currency_mismatch:{name}")
        if component.get("unit_code") != currency:
            errors.append(f"amount_unit_mismatch:{name}")
        lower = _fraction(component.get("lower"))
        upper = _fraction(component.get("upper"))
        if lower is None or upper is None or lower < 0 or upper < lower:
            errors.append(f"interval_invalid:{name}")
            continue
        lower_total += lower
        upper_total += upper
    outputs = ledger.get("accepted_outputs")
    if type(outputs) is not int or outputs <= 0:
        errors.append("accepted_outputs_must_be_positive_integer")
    complete = not errors
    return {
        "complete": complete,
        "errors": sorted(set(errors)),
        "total_interval": (
            {"lower": str(lower_total), "upper": str(upper_total), "currency": currency}
            if complete else None
        ),
        "per_accepted_output_interval": (
            {
                "lower": str(lower_total / outputs),
                "upper": str(upper_total / outputs),
                "currency_per_output": currency,
            }
            if complete else None
        ),
        "accepted_output_provenance": provenance if complete else None,
        "funding_authorized": False,
        "evidence_class": "SYNTHETIC_COST_INTERVAL_SCHEMA",
    }


def validate_calibration_uncertainty_gate(
    certificate: dict[str, Any],
    *,
    as_of_tick: int,
    required_scope: str,
    measurement_unit: str,
) -> dict[str, Any]:
    """Check certificate scope, validity interval, uncertainty unit, and roles."""
    errors = []
    if certificate.get("method_scope") != required_scope:
        errors.append("calibration_scope_mismatch")
    start = certificate.get("valid_from_tick")
    end = certificate.get("valid_through_tick")
    if type(start) is not int or type(end) is not int or type(as_of_tick) is not int:
        errors.append("calibration_time_fields_invalid")
    elif not start <= as_of_tick <= end:
        errors.append("calibration_expired_or_not_yet_valid")
    budget = certificate.get("uncertainty_budget", {})
    components = budget.get("components", []) if isinstance(budget, dict) else []
    if not isinstance(budget, dict) or budget.get("combination_rule") != "ROOT_SUM_OF_SQUARES_UNCORRELATED":
        errors.append("calibration_combination_rule_missing_or_unsupported")
    if not components:
        errors.append("calibration_uncertainty_components_missing")
    component_ids = [row.get("component_id") for row in components]
    if any(not value for value in component_ids) or len(component_ids) != len(set(component_ids)):
        errors.append("calibration_uncertainty_component_ids_invalid")
    component_values = []
    for row in components:
        value = _fraction(row.get("standard_uncertainty"))
        if value is None or value < 0:
            errors.append("calibration_standard_uncertainty_invalid")
        else:
            component_values.append(value)
        if row.get("unit_code") != measurement_unit:
            errors.append("calibration_uncertainty_unit_mismatch")
    combined = _fraction(budget.get("combined_standard_uncertainty"))
    coverage_factor = _fraction(budget.get("coverage_factor"))
    expanded = _fraction(budget.get("expanded_uncertainty"))
    if combined is None or combined < 0:
        errors.append("calibration_combined_uncertainty_invalid")
    if coverage_factor is None or coverage_factor <= 0:
        errors.append("calibration_coverage_factor_invalid")
    if expanded is None or expanded < 0:
        errors.append("calibration_expanded_uncertainty_invalid")
    if len(component_values) == len(components) and combined is not None:
        sum_squares = sum((value * value for value in component_values), Fraction(0))
        numerator_root = math.isqrt(sum_squares.numerator)
        denominator_root = math.isqrt(sum_squares.denominator)
        exact_root = (
            Fraction(numerator_root, denominator_root)
            if numerator_root * numerator_root == sum_squares.numerator
            and denominator_root * denominator_root == sum_squares.denominator
            else None
        )
        if exact_root is None:
            errors.append("calibration_combined_uncertainty_not_exact_rational")
        elif combined != exact_root:
            errors.append("calibration_combined_uncertainty_mismatch")
    if combined is not None and coverage_factor is not None and expanded is not None:
        if expanded != combined * coverage_factor:
            errors.append("calibration_expanded_uncertainty_mismatch")
    if not certificate.get("certificate_id") or not certificate.get("instrument_id"):
        errors.append("calibration_identity_missing")
    if not certificate.get("issuer") or not certificate.get("reviewer"):
        errors.append("calibration_roles_missing")
    elif certificate["issuer"] == certificate["reviewer"]:
        errors.append("calibration_issuer_reviewer_collision")
    return {
        "ready": not errors,
        "errors": sorted(set(errors)),
        "uncertainty_budget_unit": measurement_unit,
        "evidence_class": "SYNTHETIC_CALIBRATION_UNCERTAINTY_GATE",
        "physical_calibration_claim": False,
    }


def rank_evidence_gates(gates: list[dict[str, Any]]) -> dict[str, Any]:
    """Rank illustrative information-per-cost ratios without authorizing capital."""
    errors = []
    currencies = {row.get("currency") for row in gates}
    if len(currencies) != 1 or None in currencies:
        errors.append("gate_cost_currency_mismatch")
    ranked = []
    for gate in gates:
        information = _fraction(gate.get("information_gain_bits"))
        cost = _fraction(gate.get("illustrative_cost"))
        if information is None or information < 0:
            errors.append(f"information_gain_invalid:{gate.get('gate_id')}")
        if cost is None or cost <= 0:
            errors.append(f"illustrative_cost_invalid:{gate.get('gate_id')}")
        if not gate.get("assumptions"):
            errors.append(f"ranking_assumptions_missing:{gate.get('gate_id')}")
        if information is not None and cost is not None and cost > 0:
            ranked.append({
                "gate_id": gate.get("gate_id"),
                "information_per_cost": str(information / cost),
                "assumptions": gate.get("assumptions"),
            })
    ranked.sort(key=lambda row: Fraction(row["information_per_cost"]), reverse=True)
    return {
        "valid": not errors,
        "errors": sorted(set(errors)),
        "ranking": ranked if not errors else [],
        "capital_authorized": False,
        "evidence_class": "ILLUSTRATIVE_SENSITIVITY_RANKING_NO_CAPITAL",
    }


def validate_ai_candidate_evidence(candidate: dict[str, Any]) -> dict[str, Any]:
    """Validate a synthetic candidate manifest without admitting it as evidence."""
    errors = []
    train_ids = candidate.get("train_ids")
    held_out_ids = candidate.get("held_out_ids")
    if not isinstance(train_ids, list) or not isinstance(held_out_ids, list):
        errors.append("train_and_held_out_ids_required")
    else:
        for split_name, identifiers in (("train", train_ids), ("held_out", held_out_ids)):
            if not identifiers or any(not isinstance(value, str) or not value for value in identifiers):
                errors.append(f"{split_name}_ids_must_be_nonempty_strings")
            elif len(set(identifiers)) != len(identifiers):
                errors.append(f"{split_name}_ids_must_be_unique")
        if all(isinstance(value, str) and value for value in train_ids + held_out_ids):
            if set(train_ids) & set(held_out_ids):
                errors.append("train_held_out_leakage")
    for field in ("model_sha256", "dataset_sha256", "evaluation_sha256"):
        value = candidate.get(field)
        if not isinstance(value, str) or len(value) != 64 or any(
            character not in "0123456789abcdef" for character in value.lower()
        ):
            errors.append(f"candidate_provenance_missing:{field}")
    quality = candidate.get("quality")
    if (
        not isinstance(quality, dict)
        or not quality.get("metric")
        or _fraction(quality.get("value")) is None
    ):
        errors.append("candidate_quality_incomplete")
    for field in ("runtime_seconds", "energy_joules", "total_cost"):
        value = _fraction(candidate.get(field))
        if value is None or value < 0:
            errors.append(f"candidate_measurement_missing_or_invalid:{field}")
    if not candidate.get("cost_currency"):
        errors.append("candidate_cost_currency_missing")
    outputs = candidate.get("accepted_outputs")
    if type(outputs) is not int or outputs < 1:
        errors.append("candidate_accepted_outputs_invalid")
    return {
        "schema_valid": not errors,
        "errors": sorted(set(errors)),
        "evidence_admissible": False,
        "candidate_result_claimed": False,
        "evidence_class": "SYNTHETIC_CANDIDATE_EVALUATION_REJECTION_GATE",
    }


def validate_qos_semantic_certificate(
    actual_measurement_map: dict[int, int],
    expected_measurement_map: dict[int, int],
    resource_certificate: dict[str, Any],
) -> dict[str, Any]:
    """Check the frozen ER6 output map and bounded symbolic resource fields."""
    errors = []
    if actual_measurement_map != expected_measurement_map:
        errors.append("measurement_map_mismatch")
    for field in ("contract_id", "source_sha256", "qubit_count", "gate_count", "depth"):
        if field not in resource_certificate or resource_certificate[field] in (None, ""):
            errors.append(f"resource_certificate_field_missing:{field}")
    for field in ("qubit_count", "gate_count", "depth"):
        value = resource_certificate.get(field)
        if type(value) is not int or value < 0:
            errors.append(f"resource_certificate_count_invalid:{field}")
    return {
        "valid": not errors,
        "errors": sorted(set(errors)),
        "provider_transpile_receipt": None,
        "hardware_receipt": None,
        "evidence_class": "FROZEN_ER6_SEMANTIC_CERTIFICATE_SCHEMA",
    }
