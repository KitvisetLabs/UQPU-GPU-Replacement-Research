"""Machine-checkable evidence gate for fundamental-theory technology routes."""

from __future__ import annotations

REQUIRED_FIELDS = (
    "mathematical_formulation",
    "causal_physical_mechanism",
    "target_bottleneck",
    "known_constraints",
    "scaling_law",
    "falsifier",
    "observable",
    "baseline",
    "full_resource_accounting",
    "evidence_label",
)

THEORY_FAMILIES = {
    "standard_model_qcd",
    "qed_electroweak_higgs",
    "neutrino_flavour",
    "lattice_gauge_and_eft",
    "strongly_coupled_qcd_matter",
    "bsm_open_registry",
    "string_m_theory_holography",
    "quantum_gravity_open_registry",
}


def missing_contract_fields(candidate: dict[str, object]) -> list[str]:
    """Return mandatory fields that are absent or blank."""
    return [
        field
        for field in REQUIRED_FIELDS
        if field not in candidate or candidate[field] in (None, "", [], {})
    ]


def candidate_is_promotable(candidate: dict[str, object]) -> bool:
    """A candidate is promotable only when the full hypothesis contract exists."""
    family = candidate.get("theory_family")
    return family in THEORY_FAMILIES and not missing_contract_fields(candidate)


def coverage_summary() -> dict[str, object]:
    return {
        "classification": "FUNDAMENTAL_THEORY_TECHNOLOGY_SEARCH_GATE_ESTABLISHED",
        "theory_family_count": len(THEORY_FAMILIES),
        "theory_families": sorted(THEORY_FAMILIES),
        "required_fields": list(REQUIRED_FIELDS),
        "non_claims": {
            "direct_quark_computer": False,
            "string_theory_device": False,
            "bsm_discovery": False,
            "new_physical_law": False,
            "quantum_advantage": False,
            "one_hundred_million_x_saving": False,
        },
    }
