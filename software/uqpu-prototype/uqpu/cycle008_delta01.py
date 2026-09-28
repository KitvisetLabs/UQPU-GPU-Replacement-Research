"""Cycle 008 Delta 01: typed quantities and fictional SCM invariants.

This module is a small, explicit checker for selected project equations and
fictional-world rules. It does not infer units from prose or turn canon values
into measurements.
"""

from __future__ import annotations

from fractions import Fraction
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
        for variable in equation.get("variables", []):
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
        "scm_equation_extensions": scm_equation_audit,
        "five_volume_contract": volume_audit,
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
