from __future__ import annotations

import unittest

from uqpu.qos_d23_composed_repair_ledger import (
    asymptotic_repair_consequence,
    batch036_certificate,
    composed_projected_ledger,
    theorem30_repair_interface,
)


class TestQosD23ComposedRepairLedger(unittest.TestCase):
    def test_theorem30_proof_parameter_map_hits_A_over_s_endpoint(self):
        interface = theorem30_repair_interface(sparsity=4, total_error=0.01)
        self.assertAlmostEqual(interface["certified_linear_domain_endpoint"], 0.25)
        self.assertAlmostEqual(interface["rectangle_inner_endpoint"], 0.25)
        self.assertAlmostEqual(interface["endpoint_identity_residual"], 0.0)
        self.assertEqual(interface["theorem30_polynomial_parity"], "odd")
        self.assertTrue(interface["corollary18_real_polynomial_route"])

    def test_source_local_even_only_interface_is_not_silently_used(self):
        interface = theorem30_repair_interface(sparsity=4, total_error=0.01)
        self.assertTrue(interface["source_local_lemma_D8_even_only"])
        self.assertFalse(interface["source_local_D8_directly_covers_linear_odd_polynomial"])
        self.assertFalse(interface["numeric_degree_from_primary_source_closed"])

    def test_composed_projected_budget_closes_conditionally_on_actual_degree(self):
        for degree in (101, 1001, 10001):
            ledger = composed_projected_ledger(
                sparsity=4, total_error=0.01, actual_degree=degree
            )
            self.assertTrue(ledger["projected_total_budget_respected"])
            self.assertLessEqual(ledger["projected_total_error_upper_bound"], 0.01)
            self.assertAlmostEqual(ledger["diamond_subadditivity_check"], 0.01)
            self.assertFalse(ledger["projected_block_error_is_full_channel_error"])
            self.assertFalse(ledger["full_channel_repaired_D23_established"])

    def test_tighter_degree_requires_tighter_projected_input(self):
        d101 = composed_projected_ledger(
            sparsity=4, total_error=0.01, actual_degree=101
        )
        d1001 = composed_projected_ledger(
            sparsity=4, total_error=0.01, actual_degree=1001
        )
        self.assertLess(
            d1001["max_projected_input_error_eta"], d101["max_projected_input_error_eta"]
        )
        self.assertLess(
            d1001["sufficient_per_query_diamond_error_budget"],
            d101["sufficient_per_query_diamond_error_budget"],
        )

    def test_repaired_scaling_proxy_penalty_grows_with_precision(self):
        coarse = asymptotic_repair_consequence(sparsity=4, total_error=0.05)
        fine = asymptotic_repair_consequence(sparsity=4, total_error=0.001)
        self.assertGreater(
            fine["diagnostic_degree_proxy_ratio"], coarse["diagnostic_degree_proxy_ratio"]
        )
        self.assertGreater(
            fine["diagnostic_D217_common_factor_ratio"],
            coarse["diagnostic_D217_common_factor_ratio"],
        )
        self.assertFalse(fine["diagnostic_ratios_are_measured_resources"])
        self.assertFalse(fine["numeric_degree_closed"])

    def test_claim_boundaries_remain_closed(self):
        cert = batch036_certificate(sparsity=4)
        self.assertEqual(
            cert["classification"],
            "D23_REPAIRED_PROJECTED_LEDGER_COMPOSED_NUMERIC_DEGREE_OPEN",
        )
        self.assertTrue(cert["theorem30_polynomial_interface_bridge_closed"])
        self.assertFalse(cert["numeric_degree_constant_closed"])
        self.assertFalse(cert["d23_theorem_proved"])
        self.assertFalse(cert["d23_theorem_refuted"])
        self.assertFalse(cert["full_channel_repaired_D23_established"])
        self.assertFalse(cert["real_qpu"])
        self.assertFalse(cert["quantum_advantage_demonstrated"])
        self.assertFalse(cert["gpu_npu_ram_dram_hbm_replacement_demonstrated"])

    def test_invalid_inputs_rejected(self):
        with self.assertRaises(ValueError):
            theorem30_repair_interface(sparsity=1, total_error=0.01)
        with self.assertRaises(ValueError):
            theorem30_repair_interface(
                sparsity=4,
                total_error=0.01,
                bias_fraction=0.7,
                amplification_fraction=0.3,
            )
        with self.assertRaises(ValueError):
            composed_projected_ledger(
                sparsity=4, total_error=0.01, actual_degree=100
            )


if __name__ == "__main__":
    unittest.main()
