import unittest

from uqpu.fundamental_particle_technology_matrix import (
    PARTICLES,
    STANDARD_MODEL_NAMES,
    classification_counts,
    ranked_candidates,
    run_gate,
)


class FundamentalParticleTechnologyMatrixTests(unittest.TestCase):
    def test_standard_model_coverage_is_complete_at_species_level(self):
        names = {particle.name for particle in PARTICLES}
        self.assertEqual(len(STANDARD_MODEL_NAMES), 17)
        self.assertTrue(STANDARD_MODEL_NAMES.issubset(names))

    def test_direct_baselines_are_electron_and_photon_only(self):
        result = run_gate()
        self.assertEqual(
            set(result["direct_particle_technology_bridges"]),
            {"electron", "photon"},
        )

    def test_quarks_are_not_promoted_to_direct_device_claims(self):
        by_name = {particle.name: particle for particle in PARTICLES}
        for name in (
            "up quark", "down quark", "strange quark", "charm quark",
            "bottom quark", "top quark",
        ):
            self.assertNotEqual(by_name[name].bridge_class, "DIRECT_PARTICLE_TECH_BRIDGE")
            self.assertEqual(by_name[name].direct_control, 0)

    def test_neutrinos_are_simulation_bridges_not_direct_devices(self):
        by_name = {particle.name: particle for particle in PARTICLES}
        for name in ("electron neutrino", "muon neutrino", "tau neutrino"):
            self.assertEqual(by_name[name].bridge_class, "SIMULATED_PARTICLE_DYNAMICS_BRIDGE")
            self.assertEqual(by_name[name].direct_control, 0)

    def test_hypothetical_candidates_cannot_be_direct_technology(self):
        for particle in PARTICLES:
            if particle.empirical_status == 0:
                self.assertEqual(particle.bridge_class, "SPECULATIVE_PARTICLE_CANDIDATE_ONLY")

    def test_classification_counts_are_frozen(self):
        self.assertEqual(
            classification_counts(),
            {
                "DIRECT_PARTICLE_TECH_BRIDGE": 2,
                "INDIRECT_PARTICLE_DERIVED_BRIDGE": 4,
                "NO_CURRENT_CONTROLLABLE_BRIDGE": 5,
                "SIMULATED_PARTICLE_DYNAMICS_BRIDGE": 6,
                "SPECULATIVE_PARTICLE_CANDIDATE_ONLY": 5,
            },
        )

    def test_screening_score_prioritizes_testable_bridges(self):
        ranked = ranked_candidates()
        self.assertEqual(ranked[0]["name"], "electron")
        self.assertEqual(ranked[0]["priority_score"], 58)
        self.assertEqual(ranked[1]["name"], "photon")
        self.assertEqual(ranked[1]["priority_score"], 57)
        scores = {row["name"]: row["priority_score"] for row in ranked}
        self.assertEqual(scores["up quark"], 25)
        self.assertEqual(scores["down quark"], 25)
        self.assertEqual(scores["gluon"], 25)
        self.assertEqual(scores["electron neutrino"], 30)
        self.assertLess(scores["axion / ALP"], scores["up quark"])

    def test_non_claims_stay_false(self):
        non_claims = run_gate()["non_claims"]
        self.assertTrue(all(value is False for value in non_claims.values()))


if __name__ == "__main__":
    unittest.main()
