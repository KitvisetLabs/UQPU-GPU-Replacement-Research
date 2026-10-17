import copy
import unittest

from uqpu.er6_qsvt_prefix_growth_falsifier import (
    DETERMINISTIC_METRICS,
    NEXT_QUERY_COUNT,
    build_preregistration,
    evaluate_eight_query_result,
    validate_preregistration,
)


class PrefixGrowthFalsifierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = build_preregistration()

    def test_contract_is_valid_and_frozen_to_measured_series(self):
        self.assertEqual(validate_preregistration(self.contract), [])
        self.assertEqual(self.contract["measured_query_counts"], [1, 2, 3, 5])
        self.assertEqual(self.contract["next_query_count"], 8)
        self.assertEqual(len(self.contract["source_certificates"]), 3)
        self.assertEqual(self.contract["evidence_class"], "MODEL_ONLY")

    def test_deterministic_limits_are_explicit_and_below_safety_qasm_cap(self):
        limits = self.contract["acceptance"]["deterministic_metric_model_limits"]
        self.assertEqual(set(limits), set(DETERMINISTIC_METRICS))
        self.assertLess(limits["serialized_openqasm2_bytes"], 500_000)
        self.assertGreater(limits["cx"], self.contract["measured_series"]["5"]["cx"])

    def _nominal_result(self):
        limits = self.contract["acceptance"]["deterministic_metric_model_limits"]
        result = {metric: limit for metric, limit in limits.items()}
        result.update({
            "queries": NEXT_QUERY_COUNT,
            "host_runtime_ns": 800_000_000_000,
            "host_peak_traced_bytes": 700_000_000,
            "max_raw_residual": 1e-12,
            "provider_jobs": 0,
            "shots": 0,
        })
        return result

    def test_nominal_result_passes_model_and_experiment_gates(self):
        outcome = evaluate_eight_query_result(self.contract, self._nominal_result())
        self.assertTrue(outcome["model_growth_accepted"])
        self.assertTrue(outcome["experiment_accepted"])

    def test_model_rejection_is_separate_from_absolute_stop(self):
        result = self._nominal_result()
        result["cx"] += 1
        outcome = evaluate_eight_query_result(self.contract, result)
        self.assertFalse(outcome["model_growth_accepted"])
        self.assertIn("cx", outcome["deterministic_metric_failures"])
        self.assertTrue(outcome["experiment_accepted"])

    def test_absolute_runtime_and_authorization_fail_closed(self):
        result = self._nominal_result()
        result["host_runtime_ns"] = 900_000_000_001
        result["provider_jobs"] = 1
        outcome = evaluate_eight_query_result(self.contract, result)
        self.assertFalse(outcome["experiment_accepted"])
        self.assertIn("host_runtime_ns", outcome["absolute_safety_failures"])
        self.assertTrue(outcome["authorization_failed"])

    def test_digest_and_query_mutations_are_rejected(self):
        changed = copy.deepcopy(self.contract)
        changed["next_query_count"] = 9
        self.assertIn("next_query_count_mismatch", validate_preregistration(changed))
        self.assertIn("contract_digest_mismatch", validate_preregistration(changed))


if __name__ == "__main__":
    unittest.main()

