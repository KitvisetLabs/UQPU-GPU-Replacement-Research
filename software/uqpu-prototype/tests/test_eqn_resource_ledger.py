import unittest

from uqpu.eqn_resource_ledger import METHOD_ARMS, resource_parity_summary, validate_resource_ledger


def _row(method_arm: str, candidates: int = 400) -> dict[str, object]:
    return {
        "method_arm": method_arm,
        "candidate_evaluations": candidates,
        "optimizer_evaluations": 400,
        "llm_calls": 0 if method_arm == "BANK" else 10,
        "prompt_tokens": 0 if method_arm == "BANK" else 1000,
        "completion_tokens": 0 if method_arm == "BANK" else 500,
        "wall_seconds": 12.0,
        "peak_memory_bytes": 1_000_000,
        "hardware_description": "frozen-test-host",
        "monetary_cost_usd": 0.0,
    }


class TestEQNResourceLedger(unittest.TestCase):
    def test_complete_record_is_valid(self):
        self.assertTrue(validate_resource_ledger(_row("BANK"))["complete"])

    def test_missing_llm_token_accounting_blocks_comparison(self):
        row = _row("LLM_DIRECT")
        del row["prompt_tokens"]
        result = validate_resource_ledger(row)
        self.assertFalse(result["complete"])
        self.assertIn("prompt_tokens", result["missing_fields"])

    def test_equal_candidate_budget_does_not_claim_equal_compute_cost(self):
        rows = [_row("BANK"), _row("LLM_DIRECT"), _row("LLM_GUIDED_SEARCH_SPACE")]
        summary = resource_parity_summary(rows)
        self.assertTrue(summary["candidate_budget_equal"])
        self.assertTrue(summary["all_resource_ledgers_complete"])
        self.assertTrue(summary["full_resource_comparison_ready"])
        self.assertFalse(summary["candidate_budget_parity_equals_compute_cost_parity"])

    def test_unequal_candidate_budget_is_not_ready(self):
        rows = [_row("BANK", 400), _row("LLM_DIRECT", 399)]
        summary = resource_parity_summary(rows)
        self.assertFalse(summary["candidate_budget_equal"])
        self.assertFalse(summary["full_resource_comparison_ready"])

    def test_duplicate_method_arm_is_rejected_by_parity_summary(self):
        rows = [_row("BANK"), _row("BANK")]
        summary = resource_parity_summary(rows)
        self.assertFalse(summary["unique_method_arms"])
        self.assertFalse(summary["full_resource_comparison_ready"])

    def test_frozen_method_arms_include_search_space_guidance(self):
        self.assertIn("LLM_GUIDED_SEARCH_SPACE", METHOD_ARMS)

    def test_invalid_method_arm_is_rejected(self):
        row = _row("UNKNOWN")
        self.assertFalse(validate_resource_ledger(row)["complete"])


if __name__ == "__main__":
    unittest.main()
