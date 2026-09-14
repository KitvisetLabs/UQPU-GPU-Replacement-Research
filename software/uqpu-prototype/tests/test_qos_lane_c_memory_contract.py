from __future__ import annotations

import unittest

from uqpu.qos_lane_c_memory_contract import (
    Metric,
    ROLE_FIELDS,
    UPSTREAM_REQUIRED_GATES,
    batch050_qos_lane_c_certificate,
    memory_role_contract,
)


def profile(value: float | None, evidence: str) -> dict[str, Metric]:
    return {field: Metric(value=value, evidence=evidence) for field in ROLE_FIELDS}


def gates(value: bool) -> dict[str, bool]:
    return {field: value for field in UPSTREAM_REQUIRED_GATES}


class TestQosLaneCMemoryContract(unittest.TestCase):
    def test_current_qos_state_is_not_replacement_ready(self):
        cert = batch050_qos_lane_c_certificate()
        self.assertEqual(cert["gate"], "LANE-C-QOS-MEMORY-001")
        contract = cert["contract"]
        self.assertFalse(contract["upstream_contract_closed"])
        self.assertFalse(contract["dram_hbm_replacement_claim_ready"])
        self.assertFalse(contract["economic_winner_claim_ready"])

    def test_unknown_physical_roles_block_claim(self):
        result = memory_role_contract(
            baseline=profile(None, "UNKNOWN"),
            candidate=profile(None, "UNKNOWN"),
            same_accepted_function=True,
            upstream_gates=gates(True),
        )
        self.assertFalse(result["all_roles_quantified"])
        self.assertFalse(result["dram_hbm_replacement_claim_ready"])
        self.assertTrue(all(value is None for value in result["ratios_baseline_over_candidate"].values()))

    def test_model_only_ratios_do_not_promote_winner(self):
        result = memory_role_contract(
            baseline=profile(100.0, "SOURCE_REPORTED"),
            candidate=profile(10.0, "MODEL_ONLY"),
            same_accepted_function=True,
            upstream_gates=gates(True),
        )
        self.assertTrue(result["all_roles_quantified"])
        self.assertFalse(result["all_roles_non_model_or_estimate"])
        self.assertFalse(result["dram_hbm_replacement_claim_ready"])
        self.assertTrue(all(value == 10.0 for value in result["ratios_baseline_over_candidate"].values()))

    def test_matched_non_model_contract_can_be_ready(self):
        result = memory_role_contract(
            baseline=profile(100.0, "MEASURED"),
            candidate=profile(20.0, "MEASURED"),
            same_accepted_function=True,
            upstream_gates=gates(True),
        )
        self.assertTrue(result["dram_hbm_replacement_claim_ready"])
        self.assertTrue(result["economic_winner_claim_ready"])
        self.assertTrue(all(value == 5.0 for value in result["ratios_baseline_over_candidate"].values()))

    def test_accepted_function_mismatch_blocks_claim(self):
        result = memory_role_contract(
            baseline=profile(100.0, "MEASURED"),
            candidate=profile(20.0, "MEASURED"),
            same_accepted_function=False,
            upstream_gates=gates(True),
        )
        self.assertFalse(result["dram_hbm_replacement_claim_ready"])

    def test_missing_upstream_gate_blocks_claim(self):
        upstream = gates(True)
        upstream["full_channel_contract_closed"] = False
        result = memory_role_contract(
            baseline=profile(100.0, "MEASURED"),
            candidate=profile(20.0, "MEASURED"),
            same_accepted_function=True,
            upstream_gates=upstream,
        )
        self.assertFalse(result["upstream_contract_closed"])
        self.assertFalse(result["dram_hbm_replacement_claim_ready"])

    def test_profile_and_gate_schema_are_strict(self):
        bad_profile = profile(1.0, "MEASURED")
        bad_profile.pop("latency_seconds")
        with self.assertRaises(ValueError):
            memory_role_contract(
                baseline=bad_profile,
                candidate=profile(1.0, "MEASURED"),
                same_accepted_function=True,
                upstream_gates=gates(True),
            )

        bad_gates = gates(True)
        bad_gates.pop("qsp_phase_sequence_synthesized")
        with self.assertRaises(ValueError):
            memory_role_contract(
                baseline=profile(1.0, "MEASURED"),
                candidate=profile(1.0, "MEASURED"),
                same_accepted_function=True,
                upstream_gates=bad_gates,
            )


if __name__ == "__main__":
    unittest.main()
