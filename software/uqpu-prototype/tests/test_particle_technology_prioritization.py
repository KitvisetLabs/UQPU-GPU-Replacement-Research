import unittest

from uqpu.particle_technology_prioritization import batch048_certificate, canonical_candidates, ranked_candidates


class ParticleTechnologyPrioritizationTests(unittest.TestCase):
    def test_all_candidates_validate_and_rank_deterministically(self):
        candidates = canonical_candidates()
        self.assertEqual(len(candidates), 8)
        for candidate in candidates:
            candidate.validate()
        ranked = ranked_candidates()
        self.assertEqual(ranked[0].name, "Silicon-carbide spin-defect semiconductor platform")
        self.assertEqual(ranked[0].positive_score, 16)
        self.assertEqual(ranked[0].actionability_score, 15)
        self.assertEqual(ranked[0].priority, "P1_BUILD_AND_BENCHMARK")

    def test_near_term_direct_build_shortlist_is_evidence_gated(self):
        by_name = {candidate.name: candidate for candidate in canonical_candidates()}
        for name in (
            "Silicon-carbide spin-defect semiconductor platform",
            "Diamond NV / color-center spin platform",
            "Atomic-clock spacetime/gravity sensing platform",
        ):
            self.assertTrue(by_name[name].direct_device_ready_for_build_gate)
            self.assertEqual(by_name[name].priority, "P1_BUILD_AND_BENCHMARK")

    def test_detector_and_speculative_routes_cannot_be_promoted_by_score_alone(self):
        by_domain = {candidate.domain: candidate for candidate in canonical_candidates()}
        self.assertFalse(by_domain["dark_matter_detection"].direct_device_ready_for_build_gate)
        self.assertEqual(by_domain["dark_matter_detection"].priority, "P2_INSTRUMENT_SPILLOVER")
        self.assertFalse(by_domain["dark_energy_cosmology"].direct_device_ready_for_build_gate)
        self.assertEqual(by_domain["dark_energy_cosmology"].priority, "P2_INSTRUMENT_SPILLOVER")
        self.assertFalse(by_domain["extra_dimensions_quantum_gravity"].direct_device_ready_for_build_gate)
        self.assertEqual(by_domain["extra_dimensions_quantum_gravity"].priority, "P4_THEORY_OR_PRECISION_SEARCH")

    def test_qcd_route_is_indirect_not_direct_quark_control(self):
        qcd = next(c for c in canonical_candidates() if c.domain == "quark_spin_qcd")
        self.assertEqual(qcd.route_kind, "INDIRECT_PLATFORM")
        self.assertFalse(qcd.direct_carrier_controlled)
        self.assertFalse(qcd.direct_device_ready_for_build_gate)

    def test_certificate_preserves_non_claims(self):
        cert = batch048_certificate()
        self.assertEqual(cert["classification"], "PARTICLE_SPACETIME_TECHNOLOGY_ORDINAL_PRIORITIZATION_GATE")
        self.assertIn("Ordinal", cert["score_warning"])
        self.assertEqual(
            cert["top_build_candidates"],
            [
                "Silicon-carbide spin-defect semiconductor platform",
                "Diamond NV / color-center spin platform",
                "Atomic-clock spacetime/gravity sensing platform",
            ],
        )
        for claimed in cert["non_claims"].values():
            self.assertFalse(claimed)


if __name__ == "__main__":
    unittest.main()
