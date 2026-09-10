import unittest

from uqpu.qos_d21_audit import (
    corrected_visible_d20_local_coefficient,
    d20_downstream_inflation_certificate,
    d20_visible_coefficient_inflation,
    d21_counter_oracle_use_count,
    d21_error_budget_certificate,
    source_d20_local_coefficient,
    triangle_safe_per_call_epsilon,
)


class TestQOSD21Audit(unittest.TestCase):
    def test_counter_oracle_count_matches_source_structure(self):
        counts = d21_counter_oracle_use_count(dimension=2**20, row_sparsity=1024)
        self.assertEqual(counts, {"n": 20, "m": 10, "uses": 30})

    def test_source_displayed_allocation_exceeds_simple_triangle_budget(self):
        cert = d21_error_budget_certificate(dimension=2**20, row_sparsity=1024, epsilon=0.01)
        self.assertAlmostEqual(cert["source_displayed_epsilon2"], 0.0005)
        self.assertAlmostEqual(cert["triangle_bound_using_source_epsilon2"], 0.015)
        self.assertAlmostEqual(cert["triangle_bound_over_target_ratio"], 1.5)
        self.assertFalse(cert["displayed_allocation_alone_certifies_target"])
        self.assertFalse(cert["d21_theorem_refuted"])

    def test_triangle_safe_allocation_closes_displayed_constant_budget(self):
        per_call = triangle_safe_per_call_epsilon(epsilon=0.01, uses=30)
        self.assertAlmostEqual(30 * per_call, 0.01)

    def test_worst_case_call_count_ratio_can_reach_two(self):
        cert = d21_error_budget_certificate(dimension=2**20, row_sparsity=2**20, epsilon=0.01)
        self.assertEqual(cert["counter_oracle_uses"], 40)
        self.assertAlmostEqual(cert["triangle_bound_over_target_ratio"], 2.0)

    def test_d20_visible_correction_is_constant_factor_on_nondegenerate_uniform_regime(self):
        ratio = d20_visible_coefficient_inflation(0.5)
        self.assertAlmostEqual(ratio, 1.2320006656581772)
        self.assertAlmostEqual(d20_visible_coefficient_inflation(1.0), 1.0)
        self.assertGreater(corrected_visible_d20_local_coefficient(0.5), source_d20_local_coefficient(0.5))

        cert = d20_downstream_inflation_certificate()
        self.assertAlmostEqual(cert["maximum_percent_inflation"], 23.20006656581772)
        self.assertFalse(cert["asymptotic_order_changed_by_this_specific_correction"])
        self.assertFalse(cert["complete_d20_repair_claimed"])

    def test_invalid_sparsity_is_rejected(self):
        with self.assertRaises(ValueError):
            d21_counter_oracle_use_count(dimension=16, row_sparsity=17)


if __name__ == "__main__":
    unittest.main()
