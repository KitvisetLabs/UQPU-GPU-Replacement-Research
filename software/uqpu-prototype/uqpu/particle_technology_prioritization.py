"""FND-008C evidence-gated prioritization for particle/spacetime technology routes.

Research Attribution:
- Research Owner / Principal Investigator / Research Direction: Kanutsanan Pongpanna
- Facebook: https://www.facebook.com/LoveMoneyTH
- YouTube: https://www.youtube.com/@LoveMoneyTHOfficial
- AI Research Agent: OpenAI GPT-5.6 Sol
- AI-assisted contribution: literature triage, scoring-contract design,
  executable prioritization, falsifier/evidence-boundary encoding and tests.

Scores are ordinal research-priority bookkeeping only. They are not physical
measurements, success probabilities, TRL certifications, or advantage claims.
"""

from __future__ import annotations
from dataclasses import asdict, dataclass

ROUTE_KINDS = {"DIRECT_PLATFORM", "INDIRECT_PLATFORM", "DETECTOR_OR_INSTRUMENT", "SPECULATIVE_SEARCH"}


@dataclass(frozen=True)
class Candidate:
    name: str
    domain: str
    route_kind: str
    evidence_maturity: int
    preparation_maturity: int
    control_maturity: int
    retention_maturity: int
    readout_maturity: int
    integration_maturity: int
    low_cost_material_fit: int
    spillover_value: int
    infrastructure_burden: int
    direct_carrier_controlled: bool
    source_url: str
    blocker: str
    next_experiment: str

    def validate(self) -> None:
        if self.route_kind not in ROUTE_KINDS:
            raise ValueError(f"unknown route_kind: {self.route_kind}")
        if not 0 <= self.evidence_maturity <= 3:
            raise ValueError("evidence_maturity must be 0..3")
        for value in (self.preparation_maturity, self.control_maturity, self.retention_maturity,
                      self.readout_maturity, self.integration_maturity, self.low_cost_material_fit,
                      self.spillover_value):
            if not 0 <= value <= 2:
                raise ValueError("maturity/value fields must be 0..2")
        if not 0 <= self.infrastructure_burden <= 3:
            raise ValueError("infrastructure_burden must be 0..3")
        if any(not value.strip() for value in (self.name, self.domain, self.source_url, self.blocker, self.next_experiment)):
            raise ValueError("candidate text fields must be non-empty")
        if self.route_kind != "DIRECT_PLATFORM" and self.direct_carrier_controlled:
            raise ValueError("only DIRECT_PLATFORM may claim direct carrier control")

    @property
    def positive_score(self) -> int:
        return sum((self.evidence_maturity, self.preparation_maturity, self.control_maturity,
                    self.retention_maturity, self.readout_maturity, self.integration_maturity,
                    self.low_cost_material_fit, self.spillover_value))

    @property
    def actionability_score(self) -> int:
        return self.positive_score - self.infrastructure_burden

    @property
    def direct_device_ready_for_build_gate(self) -> bool:
        return (self.route_kind == "DIRECT_PLATFORM" and self.direct_carrier_controlled
                and self.evidence_maturity >= 2 and self.preparation_maturity >= 1
                and self.control_maturity >= 1 and self.readout_maturity >= 1)

    @property
    def priority(self) -> str:
        if self.route_kind == "SPECULATIVE_SEARCH":
            return "P4_THEORY_OR_PRECISION_SEARCH"
        if self.route_kind in {"DETECTOR_OR_INSTRUMENT", "INDIRECT_PLATFORM"}:
            return "P2_INSTRUMENT_SPILLOVER" if self.spillover_value >= 2 else "P3_DETECTOR_OR_INDIRECT_RESEARCH"
        if self.direct_device_ready_for_build_gate and self.actionability_score >= 13:
            return "P1_BUILD_AND_BENCHMARK"
        if self.direct_device_ready_for_build_gate and self.actionability_score >= 8:
            return "P2_REPRODUCE_AND_BENCHMARK"
        return "P3_RESEARCH_BLOCKERS"


def canonical_candidates() -> tuple[Candidate, ...]:
    C = Candidate
    candidates = (
        C("Silicon-carbide spin-defect semiconductor platform", "other_particle_quantum_states", "DIRECT_PLATFORM",
          3,2,2,1,2,2,2,2,1,True,
          "https://www.nature.com/articles/s41467-025-58629-1",
          "UQPU-specific defect reproducibility, coherence/readout yield and cost per accepted task are unmeasured.",
          "Freeze a SiC defect target and compare room-temperature electrical/optical readout, coherence, yield, control power and lifecycle cost against diamond NV and a classical sensor baseline."),
        C("Diamond NV / color-center spin platform", "diamond_defect_spin", "DIRECT_PLATFORM",
          3,2,2,2,2,1,1,2,1,True,
          "https://www.nature.com/articles/s41563-026-02648-w",
          "The Pangola/biomass-to-device-grade-diamond chain is unproven and growth/defect-engineering cost must be counted end to end.",
          "Define low-cost carbon-feedstock acceptance criteria then benchmark ODMR/coherence/sensitivity and lifecycle cost against conventional diamond and SiC."),
        C("Atomic-clock spacetime/gravity sensing platform", "spacetime_gravity", "DIRECT_PLATFORM",
          3,2,2,2,2,1,1,2,2,True,
          "https://www.nature.com/articles/s41467-026-73441-1",
          "Portable low-cost packaging, reference distribution, isolation and accepted-task cost must close against incumbents.",
          "Freeze a field task such as geopotential or synchronization and measure stability, integration time, power, package and total cost."),
        C("Dark-matter quantum-sensor spillover platform", "dark_matter_detection", "DETECTOR_OR_INSTRUMENT",
          3,2,2,1,2,1,1,2,2,False,
          "https://www.nature.com/articles/s42005-026-02563-1",
          "Dark matter's microscopic identity is unknown; detector technology is not a controllable dark-matter medium.",
          "Select one transferable phonon/resonator/superconducting/clock/spin sensor primitive and benchmark its non-dark-matter value under equal resource accounting."),
        C("Dark-energy precision-instrumentation route", "dark_energy_cosmology", "DETECTOR_OR_INSTRUMENT",
          3,2,2,2,2,0,0,2,3,False,
          "https://www.desi.lbl.gov/2026/07/30/new-desi-dr2-lyman-alpha-results-shed-light-on-dark-energy/",
          "Cosmological inference does not establish a local controllable dark-energy carrier or extractable energy source.",
          "Extract transferable spectrograph/calibration/inference primitives and benchmark them as instrumentation, not dark-energy devices."),
        C("Antimatter precision trapping / readout route", "antimatter_antiparticle", "DIRECT_PLATFORM",
          3,1,2,1,2,0,0,2,3,True,
          "https://home.cern/alpha-measures-tiny-energy-gap-in-antimatter-with-improved-precision/",
          "Production, deceleration, trapping, vacuum, loss rate and infrastructure dominate practicality.",
          "Build a production-to-readout resource ledger and identify detector/trap technology that retains value without economical bulk antimatter."),
        C("QCD spin / gauge-structure indirect technology route", "quark_spin_qcd", "INDIRECT_PLATFORM",
          3,1,1,1,2,0,0,1,3,False,
          "https://www.bnl.gov/eic/goals.php",
          "Quark/gluon confinement blocks ordinary isolated-quark logic; present routes are hadronic, nuclear or gauge-simulation based.",
          "Move from U(1) lattice-QED toward an SU(3)/QCD-adjacent symmetry-protection benchmark with violation metric and resource ledger."),
        C("Extra-dimension / quantum-gravity precision search", "extra_dimensions_quantum_gravity", "SPECULATIVE_SEARCH",
          0,1,1,1,1,0,0,1,3,False,
          "https://www.nature.com/articles/s41467-026-73441-1",
          "No project-validated extra-dimensional or quantum-gravity technology channel exists; mathematics alone is insufficient.",
          "Pre-register one deviation observable on an established precision platform and keep the route falsifiable even if null."),
    )
    for candidate in candidates:
        candidate.validate()
    return candidates


def ranked_candidates() -> tuple[Candidate, ...]:
    return tuple(sorted(canonical_candidates(), key=lambda c: (-c.actionability_score, -c.positive_score, c.name)))


def batch048_certificate() -> dict[str, object]:
    ranked = ranked_candidates()
    return {
        "program": "FND-008C/BATCH-048",
        "classification": "PARTICLE_SPACETIME_TECHNOLOGY_ORDINAL_PRIORITIZATION_GATE",
        "evidence_level": "SOURCE_GROUNDED_ORDINAL_RESEARCH_PRIORITY_MODEL",
        "score_warning": "Ordinal research-priority bookkeeping only; not a physical metric, success probability, TRL certification or advantage claim.",
        "top_build_candidates": [c.name for c in ranked if c.priority == "P1_BUILD_AND_BENCHMARK"],
        "ranking": [{**asdict(c), "positive_score": c.positive_score,
                     "actionability_score": c.actionability_score, "priority": c.priority,
                     "direct_device_ready_for_build_gate": c.direct_device_ready_for_build_gate}
                    for c in ranked],
        "non_claims": {
            "score_is_physical_metric": False,
            "quantum_advantage": False,
            "direct_dark_matter_device": False,
            "dark_energy_power_source": False,
            "extra_dimensional_device": False,
            "economical_antimatter": False,
            "direct_quark_computer": False,
            "pangola_device_grade_diamond_demonstrated": False,
            "hundred_x_saving": False,
            "hundred_million_x_saving": False,
        },
    }
