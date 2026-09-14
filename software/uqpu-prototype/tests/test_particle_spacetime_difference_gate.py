"""Tests for INV-036 / FND-008 particle-spacetime difference gate.

Research Attribution:
- Research Owner / Principal Investigator / Research Direction: Kanutsanan Pongpanna
- AI Research Agent: OpenAI GPT-5.6 Sol
- AI-assisted contribution: executable promotion-gate and evidence-boundary tests.
"""

import math
import unittest

from uqpu.particle_spacetime_difference_gate import (
    REQUIRED_DOMAINS,
    DifferenceTechnologyRoute,
    batch045_certificate,
    canonical_registry,
    coverage_complete,
    energy_difference,
    registry_domains,
)


class ParticleSpacetimeDifferenceGateTests(unittest.TestCase):
    def test_energy_difference_is_physical_delta_not_universal_identity(self):
        self.assertEqual(energy_difference(7.5, 2.0), 5.5)
        self.assertEqual(energy_difference(2.0, 7.5), -5.5)
        with self.assertRaises(ValueError):
            energy_difference(math.inf, 0.0)

    def test_registry_covers_all_mandatory_domains_exactly(self):
        routes = canonical_registry()
        self.assertEqual(registry_domains(routes), set(REQUIRED_DOMAINS))
        self.assertTrue(coverage_complete(routes))
        self.assertEqual(len(routes), len(REQUIRED_DOMAINS))

    def test_all_routes_have_complete_promotion_contracts(self):
        for route in canonical_registry():
            route.validate()
            self.assertTrue(route.difference_coordinate)
            self.assertTrue(route.preparation)
            self.assertTrue(route.control)
            self.assertTrue(route.retention)
            self.assertTrue(route.readout)
            self.assertTrue(route.useful_function)
            self.assertTrue(route.baseline)
            self.assertTrue(route.resources)
            self.assertTrue(route.falsifier)
            self.assertFalse(route.project_demonstrated_technology)

    def test_dark_sector_and_extra_dimension_boundaries_are_explicit(self):
        routes = {route.domain: route for route in canonical_registry()}
        self.assertIn("microscopic identity is not established", routes["dark_matter_detection"].carrier_status)
        self.assertIn("no localized controllable dark-energy medium", routes["dark_energy_cosmology"].carrier_status)
        self.assertIn("no project-validated extra-dimensional", routes["extra_dimensions_quantum_gravity"].carrier_status)
        self.assertFalse(routes["dark_matter_detection"].project_demonstrated_technology)
        self.assertFalse(routes["dark_energy_cosmology"].project_demonstrated_technology)
        self.assertFalse(routes["extra_dimensions_quantum_gravity"].project_demonstrated_technology)

    def test_quark_route_preserves_confinement_boundary(self):
        route = next(route for route in canonical_registry() if route.domain == "quark_spin_qcd")
        self.assertIn("confined", route.carrier_status)
        self.assertIn("hadronic", route.preparation)
        self.assertFalse(route.project_demonstrated_technology)

    def test_biomass_diamond_route_is_hypothesis_not_demonstration(self):
        route = next(route for route in canonical_registry() if route.domain == "diamond_defect_spin")
        self.assertEqual(route.evidence_level, "MATERIAL_PATH_HYPOTHESIS")
        self.assertIn("Pangola/bio-oil-residue feedstock route is unproven", route.carrier_status)
        self.assertIn("HPHT/CVD", route.preparation)
        self.assertIn("ODMR", route.readout)
        self.assertFalse(route.project_demonstrated_technology)

    def test_project_demonstrated_claim_is_rejected_in_batch045(self):
        base = canonical_registry()[0]
        invalid = DifferenceTechnologyRoute(
            name=base.name,
            domain=base.domain,
            difference_coordinate=base.difference_coordinate,
            evidence_level=base.evidence_level,
            carrier_status=base.carrier_status,
            preparation=base.preparation,
            control=base.control,
            retention=base.retention,
            readout=base.readout,
            useful_function=base.useful_function,
            baseline=base.baseline,
            resources=base.resources,
            falsifier=base.falsifier,
            project_demonstrated_technology=True,
        )
        with self.assertRaises(ValueError):
            invalid.validate()

    def test_certificate_preserves_nonclaims(self):
        certificate = batch045_certificate()
        self.assertEqual(
            certificate["classification"],
            "PARTICLE_SPACETIME_DIFFERENCE_TECHNOLOGY_RESEARCH_EXPANSION",
        )
        self.assertTrue(certificate["coverage_complete"])
        self.assertIn("treat energy differences as ΔE", certificate["difference_principle"])
        self.assertTrue(all(value is False for value in certificate["non_claims"].values()))


if __name__ == "__main__":
    unittest.main()
