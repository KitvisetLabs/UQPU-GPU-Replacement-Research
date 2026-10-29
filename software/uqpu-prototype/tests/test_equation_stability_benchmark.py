import unittest

from uqpu.equation_stability_benchmark import run_cancellation_stability_fixture


class EquationStabilityBenchmarkTests(unittest.TestCase):
    def test_stable_equivalent_form_tracks_high_precision_reference(self):
        result = run_cancellation_stability_fixture()
        stable = result["stable_rationalized"]
        self.assertLess(stable["max_abs_error"], 1e-15)
        self.assertEqual(stable["normalized_perturbation_amplification"], 0.0)

    def test_cancellation_prone_form_is_flagged(self):
        result = run_cancellation_stability_fixture()
        unstable = result["cancellation_prone"]
        self.assertGreater(unstable["max_abs_error"], 0.4)
        self.assertGreater(
            unstable["normalized_perturbation_amplification"], 0.1
        )

    def test_fixture_is_deterministic_and_evidence_labeled(self):
        first = run_cancellation_stability_fixture()
        second = run_cancellation_stability_fixture()
        self.assertEqual(first, second)
        self.assertEqual(
            first["evidence_class"], "MODEL_ONLY_SYNTHETIC_FLOATING_POINT"
        )
        self.assertEqual(first["fixture_id"], "EQN-STABILITY-CANCEL-001")

    def test_algebraic_equivalence_is_not_promoted_to_physical_truth(self):
        result = run_cancellation_stability_fixture()
        self.assertIn("does not reproduce EIC", result["claim_boundary"])
        self.assertIn("does not", result["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
