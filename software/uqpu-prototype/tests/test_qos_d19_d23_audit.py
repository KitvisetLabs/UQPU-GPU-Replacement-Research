import unittest

from uqpu.qos_d19_d23_audit import (
    MEMORY_TRANSLATION_REQUIRED_FIELDS,
    average_random_z_rotation_error,
    d19_shared_realization_certificate,
    d23_dependency_certificate,
    qos_machine_size_memory_translation_gate,
    shared_realization_joint_error,
)


class TestQOSD19D23Audit(unittest.TestCase):
    def test_shared_realization_can_break_joint_target_even_when_marginal_sum_meets_it(self):
        cert = d19_shared_realization_certificate(bit_count=8, target_epsilon=1.0e-3)
        self.assertAlmostEqual(cert["sum_of_marginal_average_errors"], 1.0e-3, places=12)
        self.assertTrue(cert["marginal_sum_within_target"])
        self.assertGreater(cert["shared_realization_joint_error"], 1.0e-3)
        self.assertGreater(cert["joint_over_target_ratio"], 7.9)
        self.assertFalse(cert["joint_within_target"])
        self.assertFalse(cert["epsilon_over_b_marginal_control_alone_repairs_shared_realization"])
        self.assertFalse(cert["specific_d19_matrix_stream_counterexample_claimed"])
        self.assertFalse(cert["d19_theorem_refuted"])

    def test_joint_error_matches_closed_form(self):
        theta = 0.02
        self.assertAlmostEqual(average_random_z_rotation_error(theta), 1.0 - __import__("math").cos(theta))
        self.assertAlmostEqual(
            shared_realization_joint_error(bit_count=8, theta=theta),
            1.0 - __import__("math").cos(8 * theta),
        )

    def test_one_slot_has_no_shared_reuse_amplification(self):
        cert = d19_shared_realization_certificate(bit_count=1, target_epsilon=1.0e-3)
        self.assertAlmostEqual(cert["shared_realization_joint_error"], 1.0e-3, places=12)
        self.assertAlmostEqual(cert["joint_over_target_ratio"], 1.0, places=12)

    def test_d23_is_dependency_blocked_not_declared_refuted(self):
        cert = d23_dependency_certificate()
        self.assertTrue(cert["source_d23_uses_d19_and_d21"])
        self.assertFalse(cert["d23_dependency_chain_closed"])
        self.assertFalse(cert["d23_theorem_refuted"])
        self.assertFalse(cert["d23_sample_complexity_ready_for_uqpu_advantage_claim"])

    def test_machine_size_is_not_memory_replacement_without_full_role_ledger(self):
        empty = qos_machine_size_memory_translation_gate()
        self.assertFalse(empty["translation_complete"])
        self.assertFalse(empty["dram_hbm_replacement_claim_ready"])
        self.assertEqual(len(empty["missing_fields"]), len(MEMORY_TRANSLATION_REQUIRED_FIELDS))

        complete = qos_machine_size_memory_translation_gate(MEMORY_TRANSLATION_REQUIRED_FIELDS)
        self.assertTrue(complete["translation_complete"])
        self.assertTrue(complete["dram_hbm_replacement_claim_ready"])
        self.assertFalse(complete["machine_size_reduction_equals_cost_reduction"])

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            d19_shared_realization_certificate(bit_count=0)
        with self.assertRaises(ValueError):
            d19_shared_realization_certificate(target_epsilon=1.0)
        with self.assertRaises(ValueError):
            shared_realization_joint_error(bit_count=0, theta=0.1)


if __name__ == "__main__":
    unittest.main()
