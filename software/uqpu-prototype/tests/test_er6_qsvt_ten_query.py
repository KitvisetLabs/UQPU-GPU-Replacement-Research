import importlib.util
import json
import unittest

from uqpu.er6_qsvt_ten_query import (
    PREREGISTRATION,
    QUERY_COUNT,
    evaluate_result,
    explicit_ten_query_matrix,
    independent_ten_query_state,
    reproduce_with_qiskit,
)
from uqpu.er6_qsvt_next_boundary_preregistration import validate_preregistration


qiskit_available = importlib.util.find_spec("qiskit") is not None


class TenQueryContractTests(unittest.TestCase):
    def setUp(self):
        self.contract = json.loads(PREREGISTRATION.read_text(encoding="utf-8"))

    def test_preregistration_is_valid_and_selects_ten(self):
        self.assertEqual(validate_preregistration(self.contract), [])
        self.assertEqual(self.contract["selection"]["selected_query_count"], QUERY_COUNT)

    def test_independent_recurrences_agree_on_frozen_spectrum(self):
        for numerator in (0, 2, 3, 4, 5, 6, 7):
            eigenvalue = numerator / 9
            matrix = explicit_ten_query_matrix(eigenvalue)
            state = independent_ten_query_state(eigenvalue)
            self.assertLessEqual(abs(matrix[0][0] - state[0]), 2e-12)
            self.assertLessEqual(abs(matrix[1][0] - state[1]), 2e-12)

    def test_out_of_domain_eigenvalue_fails_closed(self):
        with self.assertRaises(ValueError):
            explicit_ten_query_matrix(1.01)
        with self.assertRaises(ValueError):
            independent_ten_query_state(-1.01)

    def _nominal_result(self):
        limits = self.contract["acceptance"]["deterministic_metric_model_limits"]
        absolute = self.contract["acceptance"]["absolute_safety_ceilings"]
        return {
            **limits,
            "host_runtime_ns": absolute["host_runtime_ns"] - 1,
            "host_peak_traced_bytes": absolute["host_peak_traced_bytes"] - 1,
            "max_raw_residual": 1e-13,
            "provider_jobs": 0,
            "shots": 0,
        }

    def test_model_and_absolute_failures_are_distinct(self):
        result = self._nominal_result()
        result["cx"] += 1
        evaluation = evaluate_result(self.contract, result)
        self.assertEqual(evaluation["deterministic_model_failures"], ["cx"])
        self.assertEqual(evaluation["absolute_safety_failures"], [])
        self.assertFalse(evaluation["experiment_accepted"])

        result = self._nominal_result()
        result["host_runtime_ns"] += 2
        evaluation = evaluate_result(self.contract, result)
        self.assertEqual(evaluation["absolute_safety_failures"], ["host_runtime_ns"])
        self.assertFalse(evaluation["experiment_accepted"])

    def test_residual_and_provider_mutations_fail_closed(self):
        result = self._nominal_result()
        self.assertTrue(evaluate_result(self.contract, result)["experiment_accepted"])
        result["max_raw_residual"] = 2.01e-12
        self.assertFalse(evaluate_result(self.contract, result)["experiment_accepted"])
        result = self._nominal_result()
        result["provider_jobs"] = 1
        self.assertFalse(evaluate_result(self.contract, result)["experiment_accepted"])


@unittest.skipUnless(qiskit_available, "optional pinned Qiskit dependency")
class TenQueryPinnedQiskitTests(unittest.TestCase):
    def test_ten_query_experiment_obeys_frozen_gates(self):
        result = reproduce_with_qiskit()
        self.assertTrue(result["passed"])
        self.assertEqual(result["resources"]["provider_jobs"], 0)
        self.assertEqual(result["resources"]["shots"], 0)
        self.assertIsNone(result["resources"]["provider_cost"])
        self.assertIsNone(result["resources"]["energy_j"])


if __name__ == "__main__":
    unittest.main()
