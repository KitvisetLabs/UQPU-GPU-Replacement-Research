from uqpu.fundamental_theory_gate import (
    ELEMENTARY_PARTICLE_FAMILIES,
    THEORY_FRAMEWORKS,
    candidate_is_promotable,
    coverage_summary,
    missing_contract_fields,
)


def _complete_candidate():
    return {
        "particle_family": "quarks",
        "particle_or_state": "up/down quark sector represented through a specified observable state",
        "theory_framework": "qcd",
        "mathematical_formulation": "explicit Hamiltonian or field-theory model",
        "causal_physical_mechanism": "specified interaction maps state to an observable device function",
        "preparation": "specified state-preparation procedure",
        "controllability": "specified controllable parameter or operation",
        "retention_or_coherence": "specified lifetime/coherence requirement",
        "readout": "specified observable/readout procedure",
        "target_bottleneck": "specified compute, memory, sensing, energy or cost bottleneck",
        "known_constraints": "confinement, conservation laws, thermodynamics and experimental bounds",
        "scaling_law": "explicit resources versus problem/device size",
        "falsifier": "measurable or computational result that would reject the hypothesis",
        "observable": "specified measurable quantity",
        "baseline": "competitive established technology baseline",
        "full_resource_accounting": "preparation, control, readout, energy, apparatus and cost",
        "evidence_label": "CONCEPT",
    }


def test_registry_separates_particles_from_theories():
    assert "quarks" in ELEMENTARY_PARTICLE_FAMILIES
    assert "neutrinos" in ELEMENTARY_PARTICLE_FAMILIES
    assert "string_m_theory_holography" in THEORY_FRAMEWORKS
    assert "string_m_theory_holography" not in ELEMENTARY_PARTICLE_FAMILIES


def test_complete_candidate_passes_contract():
    candidate = _complete_candidate()
    assert missing_contract_fields(candidate) == []
    assert candidate_is_promotable(candidate)


def test_missing_readout_blocks_promotion():
    candidate = _complete_candidate()
    candidate["readout"] = ""
    assert "readout" in missing_contract_fields(candidate)
    assert not candidate_is_promotable(candidate)


def test_unknown_particle_family_blocks_promotion():
    candidate = _complete_candidate()
    candidate["particle_family"] = "unregistered_claim"
    assert not candidate_is_promotable(candidate)


def test_summary_has_non_claim_boundaries():
    summary = coverage_summary()
    assert summary["classification"] == "ELEMENTARY_PARTICLE_TECHNOLOGY_SEARCH_GATE_ESTABLISHED"
    assert summary["non_claims"]["new_physical_law"] is False
    assert summary["non_claims"]["quantum_advantage"] is False
    assert summary["non_claims"]["one_hundred_million_x_saving"] is False
