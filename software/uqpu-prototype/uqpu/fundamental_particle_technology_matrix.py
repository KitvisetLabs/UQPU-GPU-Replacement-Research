"""FUND-PARTICLE-001: elementary-particle-to-technology screening matrix.

The matrix deliberately distinguishes established particles, direct technology
bridges, indirect particle-derived bridges, quantum simulations of particle
dynamics, and hypothetical particle candidates. Scores are a deterministic
research-prioritization heuristic, not physical-performance measurements.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass

RESEARCH_ATTRIBUTION = {
    "research_owner_principal_investigator_research_direction": "Kanutsanan Pongpanna",
    "facebook": "https://www.facebook.com/LoveMoneyTH",
    "youtube": "https://www.youtube.com/@LoveMoneyTHOfficial",
    "ai_research_agent": "OpenAI GPT-5.6 Sol",
    "ai_assisted_contribution": (
        "elementary-particle taxonomy, public-literature triage, technology-bridge "
        "screening model, executable matrix/tests/results and documentation"
    ),
}

BRIDGE_CLASSES = {
    "DIRECT_PARTICLE_TECH_BRIDGE",
    "INDIRECT_PARTICLE_DERIVED_BRIDGE",
    "SIMULATED_PARTICLE_DYNAMICS_BRIDGE",
    "SPECULATIVE_PARTICLE_CANDIDATE_ONLY",
    "NO_CURRENT_CONTROLLABLE_BRIDGE",
}


@dataclass(frozen=True)
class ParticleCandidate:
    name: str
    family: str
    empirical_status: int          # 0 hypothetical -> 4 established/high-confidence
    direct_control: int            # 0 none -> 4 mature direct control
    state_preparation: int         # 0 none -> 4 mature
    readout: int                   # 0 none -> 4 mature
    retention_coherence: int       # 0 extremely unsuitable -> 4 strong controllable storage/coherence
    operating_accessibility: int   # 0 extreme collider-only -> 4 ordinary device conditions
    indirect_bridge: int           # 0 none -> 4 demonstrated strong indirect/simulator bridge
    hardware_analogue: int         # 0 none -> 4 mature hardware implementation
    computation_relevance: int     # 0 none known -> 4 already central to information technology
    scaling_fabrication: int       # 0 no path -> 4 mature scalable path
    unproven_assumptions: int      # 0 minimal -> 4 many/speculative
    bridge_class: str
    primary_route: str
    hard_blocker: str

    def validate(self) -> None:
        if self.bridge_class not in BRIDGE_CLASSES:
            raise ValueError(f"unknown bridge class {self.bridge_class}")
        for key, value in asdict(self).items():
            if key in {
                "empirical_status", "direct_control", "state_preparation", "readout",
                "retention_coherence", "operating_accessibility", "indirect_bridge",
                "hardware_analogue", "computation_relevance", "scaling_fabrication",
                "unproven_assumptions",
            } and not 0 <= value <= 4:
                raise ValueError(f"{self.name}: {key} outside [0,4]")
        if self.empirical_status == 0 and self.bridge_class == "DIRECT_PARTICLE_TECH_BRIDGE":
            raise ValueError("hypothetical particles cannot be classified as direct technology")

    def priority_score(self) -> int:
        """Screening score for next experiments; not a physical figure of merit."""
        positive = (
            2 * self.empirical_status
            + 2 * self.direct_control
            + self.state_preparation
            + self.readout
            + self.retention_coherence
            + self.operating_accessibility
            + 2 * self.indirect_bridge
            + 2 * self.hardware_analogue
            + 2 * self.computation_relevance
            + self.scaling_fabrication
        )
        return positive - 3 * self.unproven_assumptions


def _p(name, family, empirical, control, prep, readout, retention, access, indirect,
       hardware, relevance, scaling, assumptions, bridge, route, blocker):
    candidate = ParticleCandidate(
        name, family, empirical, control, prep, readout, retention, access, indirect,
        hardware, relevance, scaling, assumptions, bridge, route, blocker
    )
    candidate.validate()
    return candidate


# This is a technology-screening matrix rather than a claim that every listed
# particle can serve as an information carrier.  Values encode evidence maturity
# at the research-program level and are intentionally coarse ordinal scores.
PARTICLES = (
    # Established direct baselines.
    _p("electron", "charged lepton", 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 0,
       "DIRECT_PARTICLE_TECH_BRIDGE",
       "charge/spin in semiconductor, vacuum, trap and quantum-dot technologies",
       "none at the particle-existence level; device noise/material limits remain"),
    _p("photon", "gauge boson", 4, 4, 4, 4, 3, 4, 3, 4, 4, 4, 0,
       "DIRECT_PARTICLE_TECH_BRIDGE",
       "photonic state preparation, transmission, interference and detection",
       "storage/nonlinearity and deterministic interaction costs for some architectures"),

    # Quarks: direct isolated-particle devices are blocked by confinement; use
    # hadronic/isospin and lattice-gauge encodings as the nearer technology bridge.
    _p("up quark", "quark", 4, 0, 0, 1, 0, 0, 4, 3, 2, 1, 1,
       "INDIRECT_PARTICLE_DERIVED_BRIDGE",
       "proton/neutron isospin, hadronic structure and gauge-theory simulators",
       "QCD confinement prevents ordinary isolated-quark device states"),
    _p("down quark", "quark", 4, 0, 0, 1, 0, 0, 4, 3, 2, 1, 1,
       "INDIRECT_PARTICLE_DERIVED_BRIDGE",
       "proton/neutron isospin, hadronic structure and gauge-theory simulators",
       "QCD confinement prevents ordinary isolated-quark device states"),
    _p("strange quark", "quark", 4, 0, 0, 1, 0, 0, 3, 2, 1, 0, 1,
       "INDIRECT_PARTICLE_DERIVED_BRIDGE",
       "strange-hadron observables and encoded gauge/hadron simulations",
       "confinement plus unstable strange-hadron device carriers"),
    _p("charm quark", "quark", 4, 0, 0, 1, 0, 0, 2, 2, 1, 0, 1,
       "SIMULATED_PARTICLE_DYNAMICS_BRIDGE",
       "heavy-flavor simulation and collider-derived observables",
       "confinement, short-lived hadrons and high preparation energy"),
    _p("bottom quark", "quark", 4, 0, 0, 1, 0, 0, 2, 2, 1, 0, 1,
       "SIMULATED_PARTICLE_DYNAMICS_BRIDGE",
       "heavy-flavor simulation and collider-derived observables",
       "confinement, short-lived hadrons and high preparation energy"),
    _p("top quark", "quark", 4, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1,
       "NO_CURRENT_CONTROLLABLE_BRIDGE",
       "collider measurement and future encoded simulation",
       "decays before hadronization; extreme production energy and no retention path"),
    _p("gluon", "gauge boson", 4, 0, 0, 1, 0, 0, 4, 3, 2, 1, 1,
       "SIMULATED_PARTICLE_DYNAMICS_BRIDGE",
       "non-Abelian lattice-gauge/qudit simulation of color-field dynamics",
       "color confinement prevents isolated low-energy gluon device carriers"),

    # Charged leptons heavier than the electron.
    _p("muon", "charged lepton", 4, 2, 2, 4, 0, 1, 2, 2, 1, 0, 0,
       "INDIRECT_PARTICLE_DERIVED_BRIDGE",
       "beam/trap/spin-probe and muonic-system sensing concepts",
       "finite lifetime and costly source/infrastructure prevent ordinary scalable memory"),
    _p("tau", "charged lepton", 4, 0, 0, 3, 0, 0, 1, 1, 0, 0, 0,
       "NO_CURRENT_CONTROLLABLE_BRIDGE",
       "collider measurement and possible simulation abstractions",
       "extremely short lifetime and high-energy production"),

    # Neutrino flavors: particle dynamics are actively mapped to qubits/qutrits,
    # but that is simulator evidence rather than direct neutrino-device control.
    _p("electron neutrino", "neutrino", 4, 0, 0, 2, 4, 0, 4, 3, 2, 1, 1,
       "SIMULATED_PARTICLE_DYNAMICS_BRIDGE",
       "qubit/qutrit encoding of three-flavor oscillation dynamics",
       "weak interaction makes state preparation, switching and readout impractical for devices"),
    _p("muon neutrino", "neutrino", 4, 0, 0, 2, 4, 0, 4, 3, 2, 1, 1,
       "SIMULATED_PARTICLE_DYNAMICS_BRIDGE",
       "qubit/qutrit encoding of three-flavor oscillation dynamics",
       "weak interaction makes state preparation, switching and readout impractical for devices"),
    _p("tau neutrino", "neutrino", 4, 0, 0, 1, 4, 0, 4, 3, 2, 1, 1,
       "SIMULATED_PARTICLE_DYNAMICS_BRIDGE",
       "qubit/qutrit encoding of three-flavor oscillation dynamics",
       "weak interaction and especially difficult direct detection/control"),

    # Massive weak/Higgs bosons.
    _p("W boson", "electroweak gauge boson", 4, 0, 0, 3, 0, 0, 1, 1, 0, 0, 0,
       "NO_CURRENT_CONTROLLABLE_BRIDGE",
       "collider observables and encoded field-theory simulation",
       "very short lifetime and high production energy"),
    _p("Z boson", "electroweak gauge boson", 4, 0, 0, 3, 0, 0, 1, 1, 0, 0, 0,
       "NO_CURRENT_CONTROLLABLE_BRIDGE",
       "collider observables and encoded field-theory simulation",
       "very short lifetime and high production energy"),
    _p("Higgs boson", "scalar boson", 4, 0, 0, 3, 0, 0, 1, 1, 0, 0, 0,
       "NO_CURRENT_CONTROLLABLE_BRIDGE",
       "collider observables and encoded symmetry-breaking simulation",
       "very short lifetime, rare/high-energy production and no retention path"),

    # Explicit particle candidates. Sensor/simulator technology can be real even
    # when the particle's existence is not established.
    _p("axion / ALP", "BSM candidate", 0, 0, 0, 0, 0, 0, 3, 3, 2, 2, 4,
       "SPECULATIVE_PARTICLE_CANDIDATE_ONLY",
       "distributed spin-sensor networks and analogue/simulation studies",
       "particle existence and couplings remain unconfirmed"),
    _p("sterile neutrino", "BSM candidate", 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 4,
       "SPECULATIVE_PARTICLE_CANDIDATE_ONLY",
       "oscillation/search models and simulated mixing dynamics",
       "particle existence/mixing parameters remain unconfirmed"),
    _p("dark photon", "BSM candidate", 0, 0, 0, 0, 0, 0, 2, 2, 2, 1, 4,
       "SPECULATIVE_PARTICLE_CANDIDATE_ONLY",
       "resonant/sensor searches and model-guided analogue systems",
       "particle existence and kinetic-mixing parameters remain unconfirmed"),
    _p("neutralino", "supersymmetric candidate", 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 4,
       "SPECULATIVE_PARTICLE_CANDIDATE_ONLY",
       "supersymmetric model/search and simulation only",
       "supersymmetry/neutralino existence is unconfirmed"),
    _p("graviton", "quantum-gravity candidate", 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 4,
       "SPECULATIVE_PARTICLE_CANDIDATE_ONLY",
       "quantum-gravity/string-inspired model and simulator/code analogues",
       "no experimentally established quantum graviton particle control"),
)


STANDARD_MODEL_NAMES = {
    "up quark", "down quark", "strange quark", "charm quark", "bottom quark", "top quark",
    "electron", "muon", "tau",
    "electron neutrino", "muon neutrino", "tau neutrino",
    "photon", "gluon", "W boson", "Z boson", "Higgs boson",
}


def matrix_rows() -> list[dict]:
    rows = []
    for particle in PARTICLES:
        row = asdict(particle)
        row["priority_score"] = particle.priority_score()
        rows.append(row)
    return rows


def ranked_candidates() -> list[dict]:
    return sorted(matrix_rows(), key=lambda row: (-row["priority_score"], row["name"]))


def classification_counts() -> dict[str, int]:
    counts = {name: 0 for name in sorted(BRIDGE_CLASSES)}
    for particle in PARTICLES:
        counts[particle.bridge_class] += 1
    return counts


def run_gate() -> dict:
    ranked = ranked_candidates()
    direct = [row["name"] for row in ranked if row["bridge_class"] == "DIRECT_PARTICLE_TECH_BRIDGE"]
    indirect = [row["name"] for row in ranked if row["bridge_class"] == "INDIRECT_PARTICLE_DERIVED_BRIDGE"]
    simulated = [row["name"] for row in ranked if row["bridge_class"] == "SIMULATED_PARTICLE_DYNAMICS_BRIDGE"]
    speculative = [row["name"] for row in ranked if row["bridge_class"] == "SPECULATIVE_PARTICLE_CANDIDATE_ONLY"]
    blocked = [row["name"] for row in ranked if row["bridge_class"] == "NO_CURRENT_CONTROLLABLE_BRIDGE"]
    return {
        "batch": 41,
        "gate": "FUND-PARTICLE-001",
        "classification": "ELEMENTARY_PARTICLE_TECHNOLOGY_BRIDGE_MATRIX_ESTABLISHED",
        "evidence_level": "LITERATURE_GROUNDED_SCREENING_MATRIX_NOT_DEVICE_DEMONSTRATION",
        "standard_model_particle_coverage_count": len(STANDARD_MODEL_NAMES),
        "candidate_count_total": len(PARTICLES),
        "classification_counts": classification_counts(),
        "direct_particle_technology_bridges": direct,
        "indirect_particle_derived_bridges": indirect,
        "simulated_particle_dynamics_bridges": simulated,
        "no_current_controllable_bridges": blocked,
        "speculative_particle_candidates": speculative,
        "ranked_matrix": ranked,
        "next_gates": [
            "FUND-PARTICLE-002: up/down quark -> isospin/hadron/gauge-simulator primitive audit",
            "FUND-PARTICLE-003: neutrino flavor -> qutrit information-encoding/resource audit",
            "FUND-PARTICLE-004: compare particle-derived primitives against electron/photon baselines at fixed functionality",
        ],
        "non_claims": {
            "direct_isolated_quark_device": False,
            "direct_neutrino_computing_device": False,
            "bsm_particle_discovery": False,
            "string_particle_hardware": False,
            "quantum_advantage": False,
            "gpu_npu_ram_dram_hbm_replacement": False,
            "one_hundred_million_x_saving": False,
            "data_center_to_tens_of_thousands_thb_equivalence": False,
            "new_physical_law": False,
        },
        "research_attribution": RESEARCH_ATTRIBUTION,
    }
