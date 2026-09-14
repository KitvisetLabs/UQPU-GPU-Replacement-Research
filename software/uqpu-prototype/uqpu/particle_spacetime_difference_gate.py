"""Evidence gate for INV-036 / FND-008 difference-to-technology research.

Research Attribution:
- Research Owner / Principal Investigator / Research Direction: Kanutsanan Pongpanna
- Facebook: https://www.facebook.com/LoveMoneyTH
- YouTube: https://www.youtube.com/@LoveMoneyTHOfficial
- AI Research Agent: OpenAI GPT-5.6 Sol
- AI-assisted contribution: executable evidence-gate design, domain registry,
  validation logic, falsifier structure and evidence-boundary encoding.

This module does not assert new physics or a demonstrated particle/spacetime device.
It encodes the minimum information required before a research idea can be treated as
an engineering candidate.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Iterable


REQUIRED_DOMAINS = (
    "quark_spin_qcd",
    "antimatter_antiparticle",
    "dark_matter_detection",
    "dark_energy_cosmology",
    "spacetime_gravity",
    "extra_dimensions_quantum_gravity",
    "diamond_defect_spin",
    "other_particle_quantum_states",
)

EVIDENCE_LEVELS = {
    "ESTABLISHED_PHYSICS_TECHNOLOGY_BRIDGE",
    "ESTABLISHED_PHENOMENON_DETECTOR_TECH",
    "SOURCE_GROUNDED_RESEARCH_ROUTE",
    "MATERIAL_PATH_HYPOTHESIS",
    "SPECULATIVE_PHYSICS_SEARCH",
}


@dataclass(frozen=True)
class DifferenceTechnologyRoute:
    name: str
    domain: str
    difference_coordinate: str
    evidence_level: str
    carrier_status: str
    preparation: str
    control: str
    retention: str
    readout: str
    useful_function: str
    baseline: str
    resources: str
    falsifier: str
    project_demonstrated_technology: bool = False

    def validate(self) -> None:
        if self.domain not in REQUIRED_DOMAINS:
            raise ValueError(f"unknown domain: {self.domain}")
        if self.evidence_level not in EVIDENCE_LEVELS:
            raise ValueError(f"unknown evidence level: {self.evidence_level}")
        required_text = (
            self.name,
            self.difference_coordinate,
            self.carrier_status,
            self.preparation,
            self.control,
            self.retention,
            self.readout,
            self.useful_function,
            self.baseline,
            self.resources,
            self.falsifier,
        )
        if any(not value.strip() for value in required_text):
            raise ValueError("all promotion-contract fields must be non-empty")
        if self.project_demonstrated_technology:
            raise ValueError(
                "Batch 045 contains research routes only; project-demonstrated "
                "particle/spacetime technology requires a later evidence gate"
            )


def energy_difference(final_energy: float, initial_energy: float) -> float:
    """Return ordinary physical energy difference ΔE = E_final - E_initial."""

    if not all(map(_is_finite, (final_energy, initial_energy))):
        raise ValueError("energies must be finite")
    return final_energy - initial_energy


def _is_finite(value: float) -> bool:
    return value == value and value not in (float("inf"), float("-inf"))


def canonical_registry() -> tuple[DifferenceTechnologyRoute, ...]:
    routes = (
        DifferenceTechnologyRoute(
            name="QCD spin-structure technology search",
            domain="quark_spin_qcd",
            difference_coordinate="spin/polarization and QCD quantum-number-dependent observables",
            evidence_level="SOURCE_GROUNDED_RESEARCH_ROUTE",
            carrier_status="quarks/gluons are confined in ordinary low-energy matter; use hadronic/nuclear or simulation observables unless a direct mechanism is proven",
            preparation="polarized hadronic/nuclear states or controlled gauge-theory simulation state",
            control="beam polarization, fields, pulse/control sequence or encoded gauge dynamics",
            retention="defined by prepared hadronic/simulator state and experimental coherence/stability window",
            readout="spin asymmetry, scattering observable, hadronic/nuclear observable or encoded gauge observable",
            useful_function="candidate sensing, encoding, error-protection or algorithmic primitive",
            baseline="best conventional spin/gauge/sensing/encoding method for the same accepted function",
            resources="preparation energy, accelerator/simulator/control/readout hardware, time, samples and cost",
            falsifier="no reproducible controllable/readable primitive or no functional/resource gain after full accounting",
        ),
        DifferenceTechnologyRoute(
            name="Antimatter / antiparticle precision-technology search",
            domain="antimatter_antiparticle",
            difference_coordinate="particle/antiparticle charge, magnetic moment, spectroscopy, gravity-response or annihilation observables",
            evidence_level="ESTABLISHED_PHYSICS_TECHNOLOGY_BRIDGE",
            carrier_status="positrons/antiprotons/antihydrogen are experimentally produced and measured but expensive/demanding to create and confine",
            preparation="source/accelerator production, deceleration, cooling and trapping as appropriate",
            control="electromagnetic traps, lasers, microwaves or interferometric control",
            retention="trap lifetime and vacuum/field stability",
            readout="spectroscopy, annihilation detection, charge-to-mass, magnetic moment or gravitational observable",
            useful_function="precision metrology, detector technology, imaging/material analysis or future information primitive",
            baseline="matter-only metrology/detection/imaging route for the same function",
            resources="production, deceleration, cooling, trapping, vacuum, control, losses, readout, time and cost",
            falsifier="no accepted-function advantage after counting production/trapping/readout burden",
        ),
        DifferenceTechnologyRoute(
            name="Dark-matter detector technology search",
            domain="dark_matter_detection",
            difference_coordinate="model-specific weak perturbation to energy, phase, frequency, phonon, photon or spin observable",
            evidence_level="ESTABLISHED_PHENOMENON_DETECTOR_TECH",
            carrier_status="dark matter is inferred astrophysically/cosmologically; microscopic identity is not established",
            preparation="prepare the detector/sensor, not a presumed dark-matter material",
            control="sensor bias, resonator/clock/spin control, shielding and calibration",
            retention="sensor coherence/stability and background-control interval",
            readout="model-specific excess, spectral line, phase/frequency shift, phonon/photon event or other discriminating observable",
            useful_function="weak-signal sensing technology and fundamental-physics search",
            baseline="best current detector/sensor for the same coupling/energy regime",
            resources="cryogenics, shielding, sensor area/volume, exposure, calibration, readout and analysis cost",
            falsifier="null result excludes the target parameter region or sensor fails to beat the comparison sensitivity/resource contract",
        ),
        DifferenceTechnologyRoute(
            name="Dark-energy / cosmic-acceleration measurement technology search",
            domain="dark_energy_cosmology",
            difference_coordinate="redshift/distance/expansion-history observables and model-parameter differences",
            evidence_level="SOURCE_GROUNDED_RESEARCH_ROUTE",
            carrier_status="cosmic acceleration is observed; no localized controllable dark-energy medium is established",
            preparation="prepare/calibrate telescope, spectrograph, clock or other precision-measurement system",
            control="instrument calibration, survey strategy, frequency/wavelength standards and analysis pipeline",
            retention="instrument and calibration stability over measurement campaign",
            readout="redshift, distance, BAO, supernova, clock or other cosmological observable",
            useful_function="precision instrumentation, timing, mapping, inference and model discrimination",
            baseline="best current cosmology/instrumentation method for the same parameter",
            resources="instrument aperture, detector, observing time, calibration, computation, data movement and cost",
            falsifier="no discriminating observable or no transferable instrumentation/algorithmic advantage",
        ),
        DifferenceTechnologyRoute(
            name="Spacetime / gravity difference technology search",
            domain="spacetime_gravity",
            difference_coordinate="frequency/time/phase or acceleration difference associated with gravitational potential or motion",
            evidence_level="ESTABLISHED_PHYSICS_TECHNOLOGY_BRIDGE",
            carrier_status="relativistic time/frequency and gravitational effects are established and measurable",
            preparation="prepare clocks, atoms, interferometers or gravimeters",
            control="laser/microwave pulses, timing links, trajectories and environmental isolation",
            retention="clock/interferometer coherence and reference stability",
            readout="frequency ratio, phase, acceleration, geopotential or timing residual",
            useful_function="timekeeping, navigation, geodesy, gravimetry, subsurface sensing or tests of new interactions",
            baseline="best conventional timing/gravity/geodesy sensor for the same accepted task",
            resources="laser/control systems, reference links, environmental isolation, integration time and cost",
            falsifier="no sensitivity/resource advantage for the selected field-deployable task",
        ),
        DifferenceTechnologyRoute(
            name="Extra-dimension / quantum-gravity observable search",
            domain="extra_dimensions_quantum_gravity",
            difference_coordinate="theory-specific deviation from established gravity/field/dispersion/clock/interferometer prediction",
            evidence_level="SPECULATIVE_PHYSICS_SEARCH",
            carrier_status="no project-validated extra-dimensional or quantum-gravity device channel is established",
            preparation="prepare the conventional test system predicted to couple to the proposed effect",
            control="theory-specific geometry, field, frequency, distance or interferometric variable",
            retention="stability required to resolve the predicted deviation",
            readout="pre-registered discriminating residual against established theory",
            useful_function="initially model discrimination; technology claim only after a reproducible controllable effect exists",
            baseline="general relativity / Standard Model / best established prediction in the tested regime",
            resources="precision apparatus, isolation, exposure/integration time, analysis and cost",
            falsifier="predicted deviation absent at required sensitivity or alternative established explanation fits the data",
        ),
        DifferenceTechnologyRoute(
            name="Pangola/biomass carbon to diamond spin-defect route",
            domain="diamond_defect_spin",
            difference_coordinate="diamond defect electronic-spin / optical-state energy and population differences",
            evidence_level="MATERIAL_PATH_HYPOTHESIS",
            carrier_status="diamond color-center spin technology is established externally; Pangola/bio-oil-residue feedstock route is unproven",
            preparation="recover/purify biomass carbon, prepare HPHT/CVD precursor, synthesize diamond and engineer a selected defect",
            control="optical and microwave spin initialization/manipulation plus field/temperature/strain control",
            retention="diamond crystal/defect stability and measured T1/T2/T2* as relevant",
            readout="ODMR, photoluminescence or other accepted color-center state readout",
            useful_function="quantum sensing, metrology or information-device experiment",
            baseline="conventional synthetic-diamond feedstock and incumbent sensor/device for the same function",
            resources="biomass collection, carbon recovery/purification, HPHT/CVD, defect creation, laser/microwave control, characterization, yield, energy and cost",
            falsifier="feedstock cannot reproducibly yield acceptable diamond/defect performance or loses lifecycle cost/resource comparison",
        ),
        DifferenceTechnologyRoute(
            name="Other particle / quantum-state difference search",
            domain="other_particle_quantum_states",
            difference_coordinate="explicit charge/spin/flavour/mass/phase/frequency/state difference for the selected carrier",
            evidence_level="SOURCE_GROUNDED_RESEARCH_ROUTE",
            carrier_status="route-specific; must identify established versus proposed carrier status",
            preparation="route-specific preparation protocol",
            control="route-specific controllable parameter",
            retention="route-specific lifetime/coherence/stability",
            readout="route-specific observable with uncertainty model",
            useful_function="computation, sensing, communication, materials, energy, control or metrology candidate",
            baseline="best established technology for the same accepted function",
            resources="full preparation/control/readout/environment/time/energy/material/cost ledger",
            falsifier="missing reproducible preparation-control-readout chain or no accepted-function advantage",
        ),
    )
    for route in routes:
        route.validate()
    return routes


def registry_domains(routes: Iterable[DifferenceTechnologyRoute] | None = None) -> set[str]:
    selected = canonical_registry() if routes is None else tuple(routes)
    return {route.domain for route in selected}


def coverage_complete(routes: Iterable[DifferenceTechnologyRoute] | None = None) -> bool:
    return registry_domains(routes) == set(REQUIRED_DOMAINS)


def batch045_certificate() -> dict[str, object]:
    routes = canonical_registry()
    return {
        "program": "INV-036/FND-008/BATCH-045",
        "classification": "PARTICLE_SPACETIME_DIFFERENCE_TECHNOLOGY_RESEARCH_EXPANSION",
        "evidence_level": "SOURCE_GROUNDED_RESEARCH_PROGRAM_WITH_TESTABLE_MATERIAL_HYPOTHESIS",
        "difference_principle": (
            "Search for reproducible measurable differences that can be prepared, "
            "controlled, retained and read out; treat energy differences as ΔE, not "
            "all abstract differences as literal energy."
        ),
        "required_domains": list(REQUIRED_DOMAINS),
        "coverage_complete": coverage_complete(routes),
        "routes": [asdict(route) for route in routes],
        "non_claims": {
            "new_physical_law": False,
            "direct_quark_computer": False,
            "dark_matter_device_material": False,
            "dark_energy_power_source": False,
            "extra_dimensional_device": False,
            "antimatter_net_energy_source": False,
            "pangola_device_grade_diamond_demonstrated": False,
            "quantum_advantage": False,
            "gpu_npu_ram_hbm_replacement": False,
            "hundred_x_saving": False,
            "hundred_million_x_saving": False,
        },
    }
