import importlib.util
import json
import unittest

from uqpu.er6_qsvt_eight_query import (
    PREREGISTRATION,
    explicit_eight_query_matrix,
    independent_eight_query_state,
    reproduce_with_qiskit,
)
from uqpu.er6_qsvt_prefix_growth_falsifier import validate_preregistration


qiskit_available = importlib.util.find_spec("qiskit") is not None


class EightQueryContractTests(unittest.TestCase):
    def test_preregistration_is_valid_before_execution(self):
        contract = json.loads(PREREGISTRATION.read_text(encoding="utf-8"))
        self.assertEqual(validate_preregistration(contract), [])
        self.assertEqual(contract["next_query_count"], 8)

    def test_independent_recurrences_agree_on_frozen_spectrum(self):
        for numerator in (0, 2, 3, 4, 5, 6, 7):
            eigenvalue = numerator / 9
            matrix = explicit_eight_query_matrix(eigenvalue)
            state = independent_eight_query_state(eigenvalue)
            self.assertLessEqual(abs(matrix[0][0] - state[0]), 2e-12)
            self.assertLessEqual(abs(matrix[1][0] - state[1]), 2e-12)

    def test_out_of_domain_eigenvalue_fails_closed(self):
        with self.assertRaises(ValueError):
            explicit_eight_query_matrix(1.01)


@unittest.skipUnless(qiskit_available, "optional pinned Qiskit dependency")
class EightQueryPinnedQiskitTests(unittest.TestCase):
    def test_eight_query_experiment_obeys_absolute_gates(self):
        result = reproduce_with_qiskit()
        self.assertTrue(result["passed"])
        self.assertEqual(result["resources"]["provider_jobs"], 0)
        self.assertEqual(result["resources"]["shots"], 0)
        self.assertIsNone(result["resources"]["provider_cost"])
        self.assertIsNone(result["resources"]["energy_j"])


if __name__ == "__main__":
    unittest.main()

