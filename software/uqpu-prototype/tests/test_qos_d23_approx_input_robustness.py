from __future__ import annotations

import unittest

from uqpu.qos_d23_approx_input_robustness import (
    approximate_input_robustness_ledger,
    batch050_certificate,
)


class TestQosD23ApproxInputRobustness(unittest.TestCase):
    def test_sparse_normalization_satisfies_half_norm_premise(self):
        for sparsity in (2, 4, 8):
            result = approximate_input_robustness_ledger(
                sparsity=sparsity,
                total_error=0.01,
                polynomial_degree=256,
            )
            self.assertTrue(result["robust_qsvt_half_norm_premise"])
            self.assertLessEqual(result["ideal_normalized_block_norm_bound"], 0.5)

    def test_theorem8_linear_allowance_exceeds_general_sqrt_route(self):
        result = approximate_input_robustness_ledger(
            sparsity=4,
            total_error=0.01,
            polynomial_degree=1024,
        )
        self.assertAlmostEqual(
            result["robust_qsvt_theorem8_input_eta_max"],
            0.005 / (2.0 * 1024.0),
        )
        self.assertGreater(
            result["robust_qsvt_theorem8_input_eta_max"],
            result["gilyen_lemma22_input_eta_max"],
        )
        self.assertGreater(result["linear_vs_sqrt_eta_allowance_ratio"], 1.0)

    def test_total_error_budget_is_respected(self):
        for degree in (64, 256, 1024, 4096):
            result = approximate_input_robustness_ledger(
                sparsity=4,
                total_error=0.01,
                polynomial_degree=degree,
            )
            self.assertTrue(result["total_budget_respected"])
            self.assertLessEqual(
                result["additive_error_upper_bound_at_theorem8_limit"], 0.01
            )

    def test_required_input_accuracy_tightens_with_degree(self):
        low = approximate_input_robustness_ledger(
            sparsity=4, total_error=0.01, polynomial_degree=64
        )
        high = approximate_input_robustness_ledger(
            sparsity=4, total_error=0.01, polynomial_degree=4096
        )
        self.assertGreater(
            low["robust_qsvt_theorem8_input_eta_max"],
            high["robust_qsvt_theorem8_input_eta_max"],
        )

    def test_claim_boundaries_remain_closed(self):
        cert = batch050_certificate()
        self.assertEqual(cert["gate"], "QOS-AUDIT-007")
        self.assertEqual(
            cert["classification"],
            "D23_APPROX_INPUT_ROBUSTNESS_DEGREE_CONDITIONED_SUFFICIENT_CONTRACT",
        )
        for result in cert["examples"].values():
            self.assertFalse(result["exact_polynomial_degree_certified"])
            self.assertFalse(result["full_unitary_error_closed"])
            self.assertFalse(result["full_channel_or_diamond_error_closed"])
            self.assertFalse(result["earlier_D16_D19_D20_D21_dependencies_closed"])
            self.assertFalse(result["physical_resource_or_economic_advantage_closed"])

    def test_invalid_inputs_rejected(self):
        with self.assertRaises(ValueError):
            approximate_input_robustness_ledger(
                sparsity=1, total_error=0.01, polynomial_degree=64
            )
        with self.assertRaises(ValueError):
            approximate_input_robustness_ledger(
                sparsity=4, total_error=0.01, polynomial_degree=1
            )
        with self.assertRaises(ValueError):
            approximate_input_robustness_ledger(
                sparsity=4,
                total_error=0.01,
                polynomial_degree=64,
                bias_fraction=0.6,
                amplification_fraction=0.4,
            )


if __name__ == "__main__":
    unittest.main()
