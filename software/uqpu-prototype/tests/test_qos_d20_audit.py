import math
import unittest

from uqpu.qos_d20_audit import (
    D20BoundaryWitness,
    corrected_visible_arithmetic_bound,
    d20_arithmetic_gap_certificate,
    d20_zero_sample_boundary_certificate,
    minimally_integerized_visible_sample_count,
    printed_d185_sample_count,
    source_bias_substitution_ratio,
)


class QOSD20AuditTests(unittest.TestCase):
    def test_d185_boundary_prints_zero_samples_at_r_zero(self):
        value = printed_d185_sample_count(
            dimension=4,
            row_sparsity=1,
            repetition_number=0.0,
            epsilon=0.5,
        )
        self.assertEqual(value, 0.0)

    def test_zero_sample_certificate_separates_targets(self):
        cert = d20_zero_sample_boundary_certificate(D20BoundaryWitness())
        self.assertTrue(cert["printed_formula_permits_zero_samples"])
        self.assertAlmostEqual(cert["target_output_unnormalized_trace_distance"], math.sqrt(3.0), places=12)
        self.assertAlmostEqual(cert["common_zero_sample_channel_diamond_lower_bound"], math.sqrt(3.0) / 2.0, places=12)
        self.assertTrue(cert["stated_epsilon_cannot_hold_for_both_targets"])
        self.assertFalse(cert["qos_globally_invalidated"])

    def test_sqrt_r_is_larger_than_r_for_nontrivial_r(self):
        self.assertAlmostEqual(source_bias_substitution_ratio(0.5), math.sqrt(2.0), places=12)

    def test_corrected_visible_bound_exceeds_source_epsilon_at_source_budget(self):
        cert = d20_arithmetic_gap_certificate()
        self.assertEqual(cert["source_integer_samples_from_displayed_linear_R_bound"], 225)
        self.assertEqual(cert["corrected_visible_integer_samples"], 277)
        self.assertLessEqual(cert["source_displayed_bound_at_source_samples"], 0.05)
        self.assertGreater(cert["corrected_visible_bound_at_source_samples"], 0.05)
        self.assertLessEqual(cert["corrected_visible_bound_at_corrected_samples"], 0.05)
        self.assertFalse(cert["repaired_d20_theorem_claimed"])

    def test_positive_floor_for_r_zero(self):
        self.assertEqual(
            minimally_integerized_visible_sample_count(
                support_size=1,
                repetition_number=0.0,
                epsilon=0.5,
            ),
            1,
        )

    def test_uniform_support_model_rejects_too_small_r(self):
        with self.assertRaises(ValueError):
            d20_arithmetic_gap_certificate(support_size=2, repetition_number=0.25)

    def test_corrected_bound_requires_positive_samples(self):
        with self.assertRaises(ValueError):
            corrected_visible_arithmetic_bound(
                support_size=2,
                repetition_number=0.5,
                samples=0,
            )


if __name__ == "__main__":
    unittest.main()
