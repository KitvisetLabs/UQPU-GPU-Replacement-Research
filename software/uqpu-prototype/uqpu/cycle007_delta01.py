"""Cycle 007 Delta 01: audit machine-readable units in project equations."""

from __future__ import annotations

from fractions import Fraction
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
