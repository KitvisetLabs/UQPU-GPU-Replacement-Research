import unittest

from uqpu.spin_defect_benchmark_gate import (
    EvidencePoint,
    audit_current_pairs,
    batch049_certificate,
    comparison_blockers,
    current_public_evidence,
    winner_claim_allowed,
)


class SpinDefectBenchmarkGateTests(unittest.TestCase):
    def test_public_evidence_validates(self):
        points = current_public_evidence()
        self.assertEqual(len(points), 5)
        for point in points:
            point.validate()

    def test_current_public_cross_host_pairs_do_not_support_performance_winner(self):
        rows = audit_current_pairs()
        self.assertGreater(len(rows), 0)
        self.assertTrue(all(not row["performance_winner_allowed"] for row in rows))
        self.assertFalse(batch049_certificate()["any_current_performance_winner_allowed"])

    def test_single_defect_vs_ensemble_is_rejected(self):
        points = {point.name: point for point in current_public_evidence()}
        blockers = comparison_blockers(
            points["SiC shallow single-divacancy magnetometry estimate"],
            points["Portable diamond NV ensemble magnetometer"],
        )
        self.assertIn("SENSOR_CLASS_MISMATCH", blockers)
        self.assertIn("PROTOCOL_MISMATCH", blockers)
        self.assertFalse(winner_claim_allowed(
            points["SiC shallow single-divacancy magnetometry estimate"],
            points["Portable diamond NV ensemble magnetometer"],
        ))

    def test_model_derived_numbers_cannot_be_promoted_as_direct_measured_winner(self):
        points = {point.name: point for point in current_public_evidence()}
        blockers = comparison_blockers(
            points["SiC shallow single-divacancy magnetometry estimate"],
            points["Diamond shallow single-NV AC sensitivity estimate"],
        )
        self.assertIn("DIRECT_MEASURED_SENSITIVITY_REQUIRED", blockers)
        self.assertIn("PROTOCOL_MISMATCH", blockers)
        self.assertIn("MATCHED_FREQUENCY_BAND_REQUIRED", blockers)
        self.assertIn("MATCHED_DEFECT_DEPTH_REQUIRED", blockers)

    def test_end_to_end_cost_claim_requires_complete_cost_boundary(self):
        points = {point.name: point for point in current_public_evidence()}
        blockers = comparison_blockers(
            points["SiC shallow single-divacancy magnetometry estimate"],
            points["Diamond shallow single-NV AC sensitivity estimate"],
            "END_TO_END_COST_WINNER",
        )
        self.assertIn("COMPLETE_COST_BOUNDARY_REQUIRED", blockers)

    def test_a_truly_matched_direct_pair_can_pass_performance_gate(self):
        base = dict(
            accepted_function="ROOM_TEMPERATURE_MAGNETIC_FIELD_SENSING",
            sensor_class="SINGLE_DEFECT",
            temperature_regime="ROOM_TEMPERATURE",
            protocol="MATCHED_AC_PROTOCOL",
            sensitivity_status="MEASURED_DIRECT",
            frequency_min_hz=1000.0,
            frequency_max_hz=2000.0,
            defect_depth_nm=5.0,
            readout="DECLARED",
            control="DECLARED",
            cost_boundary_complete=False,
            note="synthetic unit-test fixture",
        )
        a = EvidencePoint(name="A", host="SiC", sensitivity_nt_sqrt_hz=10.0, source_url="https://example.com/a", **base)
        b = EvidencePoint(name="B", host="diamond", sensitivity_nt_sqrt_hz=12.0, source_url="https://example.com/b", **base)
        self.assertTrue(winner_claim_allowed(a, b, "PERFORMANCE_WINNER"))
        self.assertFalse(winner_claim_allowed(a, b, "END_TO_END_COST_WINNER"))

    def test_certificate_preserves_nonclaims_and_next_experiment(self):
        cert = batch049_certificate()
        self.assertEqual(cert["principle"], "SAME_ACCEPTED_FUNCTION_OR_NO_WINNER")
        self.assertIn("same protocol", cert["next_experiment"].lower())
        self.assertTrue(all(value is False for value in cert["non_claims"].values()))


if __name__ == "__main__":
    unittest.main()
