from __future__ import annotations

import math
import unittest

from uqpu.qos_d23_positive_margin_repair import batch034_certificate, positive_margin_repair


class TestQosD23PositiveMarginRepair(unittest.TestCase):
    def test_endpoint_repair_creates_positive_margin(self):
        result = positive_margin_repair(sparsity=4, total_error=0.01)
        self.assertAlmostEqual(result["normalization_bias_budget"], 0.005)
        self.assertAlmostEqual(result["target_scale"], 0.995)
        self.assertAlmostEqual(result["amplification_gamma"], 3.98)
        self.assertAlmostEqual(result["maximum_positive_margin_delta"], 0.005)
        self.assertTrue(result["endpoint_positive_margin_contract_closed_for_exact_input"])

    def test_exact_input_additive_budget_is_respected(self):
        for epsilon in (0.05, 0.01, 0.001, 0.0001):
            result = positive_margin_repair(sparsity=4, total_error=epsilon)
            self.assertLessEqual(result["additive_error_upper_bound_exact_input"], epsilon)

    def test_proxy_exposes_accuracy_overhead(self):
        coarse = positive_margin_repair(sparsity=4, total_error=0.05)
        fine = positive_margin_repair(sparsity=4, total_error=0.001)
        self.assertGreater(
            fine["proxy_ratio_to_source_nominal"], coarse["proxy_ratio_to_source_nominal"]
        )
        self.assertTrue(math.isfinite(fine["theorem30_scaling_proxy_without_hidden_constant"]))

    def test_claim_boundaries_remain_closed(self):
        cert = batch034_certificate(sparsity=4)
        self.assertEqual(
            cert["classification"], "D23_ENDPOINT_POSITIVE_MARGIN_REPAIR_EXACT_INPUT_ONLY"
        )
        self.assertFalse(cert["d23_theorem_refuted"])
        self.assertFalse(cert["qos_globally_invalidated"])
        self.assertFalse(cert["real_qpu"])
        self.assertFalse(cert["quantum_advantage_demonstrated"])
        self.assertFalse(cert["gpu_npu_dram_hbm_replacement_demonstrated"])
        for example in cert["examples"].values():
            self.assertFalse(example["approximate_input_robustness_closed"])
            self.assertFalse(example["full_channel_error_closed"])
            self.assertFalse(example["earlier_dependencies_closed"])

    def test_invalid_inputs_rejected(self):
        with self.assertRaises(ValueError):
            positive_margin_repair(sparsity=1, total_error=0.01)
        with self.assertRaises(ValueError):
            positive_margin_repair(sparsity=4, total_error=0.0)
        with self.assertRaises(ValueError):
            positive_margin_repair(sparsity=4, total_error=0.01, bias_fraction=1.0)


if __name__ == "__main__":
    unittest.main()
