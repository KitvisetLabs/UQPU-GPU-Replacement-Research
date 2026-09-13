"""Machine-checkable evidence gate for elementary-particle technology research."""

from __future__ import annotations

ELEMENTARY_PARTICLE_FAMILIES = {
    "quarks",
    "charged_leptons",
    "neutrinos",
    "photon",
    "gluon",
    "w_boson",
    "z_boson",
    "higgs_boson",
    "antiparticle_states",
    "proposed_bsm_particles",
}

THEORY_FRAMEWORKS = {
    "standard_model_qft",
    "qcd",
    "qed",
    "electroweak_theory",
    "lattice_gauge_theory",
    "effective_field_theory",
    "string_m_theory_holography",
    "other_quantum_gravity",
    "bsm_open_registry",
}

REQUIRED_FIELDS = (
    "particle_or_state",
    "theory_framework",
    "mathematical_formulation",
    "causal_physical_mechanism",
    "preparation",
    "controllability",
    "retention_or_coherence",
    "readout",
    "target_bottleneck",
    "known_constraints",
    "scaling_law",
    "falsifier",
    "observable",
    "baseline",
    "full_resource_accounting",
    "evidence_label",
)


def missing_contract_fields(candidate: dict[str, object]) -> list[str]:
    """Return mandatory elementary-particle hypothesis fields that are blank."""
    return [
        field
        for field in REQUIRED_FIELDS
        if field not in candidate or candidate[field] in (None, "", [], {})
    ]


def candidate_is_promotable(candidate: dict[str, object]) -> bool:
    """Require registered particle and theory categories plus the full contract."""
    return (
        candidate.get("particle_family") in ELEMENTARY_PARTICLE_FAMILIES
        and candidate.get("theory_framework") in THEORY_FRAMEWORKS
        and not missing_contract_fields(candidate)
    )


def coverage_summary() -> dict[str, object]:
    return {
        "classification": "ELEMENTARY_PARTICLE_TECHNOLOGY_SEARCH_GATE_ESTABLISHED",
        "particle_family_count": len(ELEMENTARY_PARTICLE_FAMILIES),
        "particle_families": sorted(ELEMENTARY_PARTICLE_FAMILIES),
        "theory_framework_count": len(THEORY_FRAMEWORKS),
        "theory_frameworks": sorted(THEORY_FRAMEWORKS),
        "required_fields": list(REQUIRED_FIELDS),
        "non_claims": {
            "direct_quark_device_demonstrated": False,
            "elementary_particle_device_demonstrated": False,
            "string_scale_device_demonstrated": False,
            "bsm_particle_discovery": False,
            "new_physical_law": False,
            "quantum_advantage": False,
            "one_hundred_million_x_saving": False,
        },
    }
