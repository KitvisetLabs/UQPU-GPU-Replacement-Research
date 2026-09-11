import unittest

from uqpu.qos_d23_qsvt_margin_audit import (
    batch033_certificate,
    endpoint_bounded_polynomial_degree_lower_bound,
    uniform_sva_margin_certificate,
)


class TestQOSD23QSVTMarginAudit(unittest.TestCase):
    def test_endpoint_has_no_positive_uniform_sva_margin(self):
        cert = uniform_sva_margin_certificate(matrix_norm=1.0, sparsity=4)
        self.assertEqual(cert["maximum_positive_margin_delta"], 0.0)
        self.assertFalse(cert["positive_margin_exists"])
        self.assertTrue(cert["endpoint_saturation_case"])
        self.assertFalse(cert["d23_theorem_refuted"])

    def test_interior_case_has_positive_margin(self):
        cert = uniform_sva_margin_certificate(matrix_norm=0.9, sparsity=4)
        self.assertAlmostEqual(cert["maximum_positive_margin_delta"], 0.1)
        self.assertTrue(cert["positive_margin_exists"])
        self.assertFalse(cert["endpoint_saturation_case"])

    def test_endpoint_degree_lower_bound_outgrows_nominal_s_log_diagnostic(self):
        e4 = endpoint_bounded_polynomial_degree_lower_bound(sparsity=4, epsilon=1e-4)
        e6 = endpoint_bounded_polynomial_degree_lower_bound(sparsity=4, epsilon=1e-6)
        self.assertGreater(e4["degree_lower_bound"], 60.0)
        self.assertGreater(e6["degree_lower_bound"], 600.0)
        self.assertGreater(e6["lower_bound_over_nominal_s_log"], e4["lower_bound_over_nominal_s_log"])
        self.assertEqual(e6["asymptotic_lower_bound_scaling"], "Omega(s/sqrt(epsilon))")
        self.assertFalse(e6["d23_theorem_refuted"])

    def test_batch_certificate_preserves_claim_boundaries(self):
        cert = batch033_certificate(sparsity=4)
        self.assertEqual(cert["classification"], "SOURCE_V1_D23_QSVT_ENDPOINT_CONTRACT_NOT_ESTABLISHED")
        self.assertFalse(cert["real_qpu"])
        self.assertFalse(cert["quantum_advantage_demonstrated"])
        self.assertFalse(cert["uqpu_advantage_demonstrated"])

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            uniform_sva_margin_certificate(matrix_norm=1.1, sparsity=4)
        with self.assertRaises(ValueError):
            endpoint_bounded_polynomial_degree_lower_bound(sparsity=1, epsilon=1e-4)
        with self.assertRaises(ValueError):
            endpoint_bounded_polynomial_degree_lower_bound(sparsity=4, epsilon=0.2)


if __name__ == "__main__":
    unittest.main()
