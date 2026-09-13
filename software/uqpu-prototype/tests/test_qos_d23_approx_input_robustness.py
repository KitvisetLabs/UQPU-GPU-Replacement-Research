"""Tests for Batch 035 QOS D.23 projected-block robustness audit.

Research Attribution
--------------------
Research Owner / Principal Investigator / Research Direction: Kanutsanan Pongpanna
Facebook: https://www.facebook.com/LoveMoneyTH
YouTube: https://www.youtube.com/@LoveMoneyTHOfficial
AI Research Agent: OpenAI GPT-5.6 Sol
AI-assisted contribution: theorem/interface audit, test design, implementation,
and reproducibility verification preparation.
"""

from __future__ import annotations

import math
import unittest

from uqpu.qos_d23_approx_input_robustness import (
    batch035_certificate,
    lemma23_margin_cap,
    max_projected_input_error_for_linear_budget,
    projected_transform_robustness,
)


class TestQosD23ApproxInputRobustness(unittest.TestCase):
    def test_closed_form_margin_cap_hits_lemma23_boundary(self):
        for sparsity in (2, 4, 8, 16):
            eta = lemma23_margin_cap(sparsity=sparsity)
            lhs = eta + (1.0 / sparsity + eta / 2.0) ** 2
            self.assertAlmostEqual(lhs, 1.0, places=12)
            self.assertGreater(eta, 0.0)

    def test_d23_normalized_block_has_large_interior_region(self):
        cap = lemma23_margin_cap(sparsity=4)
        self.assertAlmostEqual(cap, 0.6622776601683795, places=12)
        result = projected_transform_robustness(
            sparsity=4, degree=100, projected_input_error=1e-4
        )
        self.assertTrue(result["lemma23_condition_satisfied"])
        self.assertIsNotNone(result["lemma23_linear_error_bound"])

    def test_linear_lemma23_is_less_restrictive_than_generic_sqrt_ledger(self):
        budget = 0.01 / 3.0
        for degree in (10, 100, 1000):
            eta_linear = max_projected_input_error_for_linear_budget(
                sparsity=4, degree=degree, robustness_budget=budget
            )
            eta_generic = (budget / (4.0 * degree)) ** 2
            self.assertGreater(eta_linear, eta_generic)
            result = projected_transform_robustness(
                sparsity=4, degree=degree, projected_input_error=eta_linear
            )
            self.assertTrue(result["lemma23_condition_satisfied"])
            self.assertLessEqual(result["lemma23_linear_error_bound"], budget * (1.0 + 1e-12))

    def test_linear_bound_scales_locally_as_degree_times_input_error(self):
        eta = 1e-6
        low = projected_transform_robustness(
            sparsity=4, degree=100, projected_input_error=eta
        )
        high = projected_transform_robustness(
            sparsity=4, degree=200, projected_input_error=eta
        )
        self.assertAlmostEqual(
            high["lemma23_linear_error_bound"],
            2.0 * low["lemma23_linear_error_bound"],
            places=12,
        )
        self.assertGreater(low["lemma22_generic_sqrt_error_bound"], 0.0)

    def test_certificate_preserves_non_claims(self):
        cert = batch035_certificate(sparsity=4, total_error=0.01)
        self.assertEqual(
            cert["classification"],
            "D23_PROJECTED_BLOCK_LINEAR_ROBUSTNESS_MARGIN_CONTRACT_IDENTIFIED",
        )
        self.assertTrue(
            cert[
                "source_d215_linear_O_d_eta_form_supportable_under_explicit_interior_contract"
            ]
        )
        self.assertFalse(cert["d23_theorem_proved"])
        self.assertFalse(cert["d23_theorem_refuted"])
        self.assertFalse(cert["full_unitary_error_bound_established"])
        self.assertFalse(cert["full_channel_error_bound_established"])
        self.assertFalse(cert["real_qpu"])
        self.assertFalse(cert["quantum_advantage_demonstrated"])
        self.assertFalse(cert["gpu_npu_ram_dram_hbm_replacement_demonstrated"])

    def test_invalid_inputs_rejected(self):
        with self.assertRaises(ValueError):
            lemma23_margin_cap(sparsity=1)
        with self.assertRaises(ValueError):
            projected_transform_robustness(
                sparsity=4, degree=0, projected_input_error=1e-4
            )
        with self.assertRaises(ValueError):
            projected_transform_robustness(
                sparsity=4, degree=10, projected_input_error=-1e-4
            )
        with self.assertRaises(ValueError):
            max_projected_input_error_for_linear_budget(
                sparsity=4, degree=10, robustness_budget=0.0
            )
        self.assertTrue(math.isfinite(lemma23_margin_cap(sparsity=4)))


if __name__ == "__main__":
    unittest.main()
