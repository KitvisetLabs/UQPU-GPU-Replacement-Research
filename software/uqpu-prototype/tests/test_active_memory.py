import math
import unittest

from uqpu.active_memory import (
    build_reference_report,
    entropy_bits,
    evaluate_memoryless_invariant_channel,
    evaluate_passive_iid_tape,
)


class ActiveMemoryReferenceTests(unittest.TestCase):
    def test_published_binary_active_channel_reference(self):
        report = build_reference_report()
        active = report["active_feedback"]
        self.assertTrue(report["validation"]["active_channel_matches_published_analytic_reference"])
        self.assertLessEqual(active["absolute_reference_error"], 1e-12)
        self.assertAlmostEqual(
            active["work_rate_kbt_ln2_per_round"],
            0.27155330316361204,
            places=12,
        )
        self.assertAlmostEqual(
            active["action_probabilities"][0],
            1.0 / math.sqrt(2.0),
            places=14,
        )

    def test_passive_control_matches_marginal_but_is_a_different_model(self):
        report = build_reference_report()
        active = report["active_feedback"]
        passive = report["passive_iid_tape_control"]
        self.assertTrue(passive["same_output_marginal_as_active_operating_point"])
        self.assertAlmostEqual(
            passive["work_rate_kbt_ln2_per_round"],
            0.39912396330714384,
            places=12,
        )
        self.assertGreater(
            passive["work_rate_kbt_ln2_per_round"],
            active["work_rate_kbt_ln2_per_round"],
        )
        self.assertIn("different environment assumptions", report["comparison"]["interpretation"])

    def test_entropy_handles_zero_probability(self):
        self.assertEqual(entropy_bits((1.0, 0.0)), 0.0)
        self.assertAlmostEqual(entropy_bits((0.5, 0.5)), 1.0, places=14)

    def test_rejects_invalid_distributions_and_rows(self):
        for invalid in ((0.2, 0.2), (-0.1, 1.1), (float("nan"), 0.0), (True, False)):
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    entropy_bits(invalid)
        with self.assertRaises(ValueError):
            evaluate_memoryless_invariant_channel(
                (0.5, 0.5),
                ((0.2, 0.2), (0.5, 0.5)),
            )
        with self.assertRaises(ValueError):
            evaluate_memoryless_invariant_channel(
                (0.5, 0.5),
                ((1.0, 0.0),),
            )

    def test_invalid_passive_source_is_rejected(self):
        with self.assertRaises(ValueError):
            evaluate_passive_iid_tape((0.5, 0.5), (0.2, 0.2))

    def test_reference_report_keeps_physical_metrics_null(self):
        report = build_reference_report()
        validation = report["validation"]
        self.assertIsNone(validation["physical_memory_bytes"])
        self.assertIsNone(validation["measured_energy_joules"])
        self.assertIsNone(validation["measured_cost_usd"])
        self.assertEqual(validation["provider_jobs"], 0)
        self.assertEqual(validation["qpu_shots"], 0)
        self.assertEqual(report["claims_promoted"], [])
        self.assertIn("new physical law", report["non_claims"])


if __name__ == "__main__":
    unittest.main()
