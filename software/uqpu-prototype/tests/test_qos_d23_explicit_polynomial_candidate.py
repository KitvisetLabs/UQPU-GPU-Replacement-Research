import unittest

from uqpu.qos_d23_explicit_polynomial_candidate import (
    AMPLIFICATION_ERROR_BUDGET,
    DEGREE,
    ODD_CHEBYSHEV_COEFFICIENTS,
    TARGET_ENDPOINT,
    batch037_certificate,
    chebyshev_evaluate,
    grid_certificate,
)


class TestQosD23ExplicitPolynomialCandidate(unittest.TestCase):
    def test_explicit_degree_and_odd_parity(self):
        self.assertEqual(DEGREE, 81)
        self.assertEqual(len(ODD_CHEBYSHEV_COEFFICIENTS), 41)
        for x in (-1.0, -0.75, -0.25, -0.1, 0.0, 0.1, 0.25, 0.75, 1.0):
            self.assertAlmostEqual(chebyshev_evaluate(-x), -chebyshev_evaluate(x), places=12)

    def test_frozen_candidate_passes_reproducible_dense_grid(self):
        cert = grid_certificate(global_points=20_001, target_points=10_001)
        self.assertTrue(cert.sampled_global_bound_passes)
        self.assertLess(cert.sampled_global_max_abs, 0.9992)
        self.assertTrue(cert.sampled_target_error_passes)
        self.assertLess(cert.sampled_target_max_error, AMPLIFICATION_ERROR_BUDGET)
        self.assertLess(cert.sampled_odd_symmetry_residual, 1e-12)

    def test_endpoint_is_inside_approximation_contract(self):
        endpoint_error = abs(chebyshev_evaluate(TARGET_ENDPOINT) - (4.0 * (1.0 - 0.01 / 3.0)) * TARGET_ENDPOINT)
        self.assertLess(endpoint_error, AMPLIFICATION_ERROR_BUDGET)

    def test_evidence_boundaries_remain_closed(self):
        cert = batch037_certificate()
        self.assertEqual(
            cert["classification"],
            "D23_EXPLICIT_NUMERICAL_POLYNOMIAL_CANDIDATE_DEGREE_81_PHASES_OPEN",
        )
        self.assertTrue(cert["numerically_explicit_polynomial_candidate"])
        self.assertFalse(cert["formal_global_boundedness_proof_closed"])
        self.assertFalse(cert["qsp_phase_sequence_synthesized"])
        self.assertFalse(cert["qsp_phase_sequence_independently_verified"])
        self.assertFalse(cert["full_channel_repaired_D23_established"])
        self.assertFalse(cert["real_qpu"])
        self.assertFalse(cert["quantum_advantage_demonstrated"])
        self.assertFalse(cert["gpu_npu_ram_dram_hbm_replacement_demonstrated"])

    def test_out_of_domain_rejected(self):
        with self.assertRaises(ValueError):
            chebyshev_evaluate(1.0001)


if __name__ == "__main__":
    unittest.main()
