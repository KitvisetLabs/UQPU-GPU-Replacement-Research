import unittest

from uqpu.qos_d23_exact_bernstein_certificate import (
    batch051_certificate,
    coefficient_fingerprint,
    global_boundedness_certificate,
)


class TestQosD23ExactBernsteinCertificate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = batch051_certificate()

    def test_certificate_is_bound_to_frozen_runtime_coefficients(self):
        self.assertEqual(
            coefficient_fingerprint(),
            "4364297169fe219da396c1d663680f474508a03afed93e321dc8e9d8f0bad13a",
        )
        self.assertEqual(self.certificate["degree"], 81)

    def test_exact_global_all_real_bound_closes_for_frozen_polynomial(self):
        result = self.certificate["global_all_real_bound"]
        self.assertTrue(result["certified"])
        self.assertEqual(result["leaf_intervals"], 196)
        self.assertEqual(result["maximum_depth"], 13)
        self.assertGreater(result["tightest_bernstein_margin_lower_bound"], 0.0)
        self.assertTrue(
            self.certificate["formal_global_boundedness_for_frozen_runtime_polynomial_closed"]
        )

    def test_exact_target_error_bound_closes_for_frozen_polynomial(self):
        result = self.certificate["target_error_bound"]
        self.assertTrue(result["certified"])
        self.assertEqual(result["leaf_intervals"], 6)
        self.assertEqual(result["maximum_depth"], 3)
        self.assertGreater(result["tightest_bernstein_margin_lower_bound"], 0.0)
        self.assertTrue(
            self.certificate["formal_target_error_bound_for_frozen_runtime_polynomial_closed"]
        )

    def test_depth_cap_failure_is_preserved_as_failure(self):
        shallow = global_boundedness_certificate(max_depth=0)
        self.assertFalse(shallow.certified)

    def test_phase_and_hardware_claims_remain_open(self):
        self.assertEqual(self.certificate["gate"], "QOS-AUDIT-010A")
        self.assertFalse(self.certificate["qsp_phase_sequence_synthesized"])
        self.assertFalse(self.certificate["qsp_response_independently_reconstructed"])
        self.assertFalse(self.certificate["full_channel_repaired_D23_established"])
        self.assertFalse(self.certificate["real_qpu"])
        self.assertFalse(self.certificate["quantum_advantage_demonstrated"])
        self.assertFalse(
            self.certificate["gpu_npu_ram_dram_hbm_replacement_demonstrated"]
        )
        self.assertFalse(self.certificate["hundred_x_advantage_demonstrated"])
        self.assertFalse(self.certificate["hundred_million_x_advantage_demonstrated"])
        self.assertFalse(self.certificate["new_physical_law"])


if __name__ == "__main__":
    unittest.main()
