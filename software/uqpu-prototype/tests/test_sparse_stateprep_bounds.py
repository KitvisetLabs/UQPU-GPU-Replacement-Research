import math
import unittest

from uqpu.sparse_stateprep_bounds import (
    build_sparse_stateprep_bound_contract,
    validate_sparse_stateprep_bound_contract,
)


class SparseStatePrepBoundTests(unittest.TestCase):
    def test_contract_records_symbolic_bounds_not_numeric_gate_counts(self):
        contract = build_sparse_stateprep_bound_contract(8, 12, 0.01)
        self.assertEqual(validate_sparse_stateprep_bound_contract(contract), [])
        self.assertIn("n^(3/4)*sqrt(s)", contract["theorem_reference"]["upper_bound_expression"])
        self.assertIsNone(contract["unknown_resources"]["numeric_t_count"])
        self.assertIsNone(contract["unknown_resources"]["physical_memory_bytes"])
        self.assertEqual(contract["evidence_class"], "MODEL_ONLY")

    def test_lower_bound_is_exposed_only_inside_its_stated_range(self):
        inside = build_sparse_stateprep_bound_contract(4, 4, 1 / 6)
        self.assertTrue(inside["theorem_reference"]["lower_bound_range_checked"])
        self.assertEqual(
            inside["theorem_reference"]["lower_bound_expression"],
            "Omega(min(s, sqrt(n*s)))",
        )
        outside = build_sparse_stateprep_bound_contract(4, 5, 1 / 6)
        self.assertFalse(outside["theorem_reference"]["lower_bound_range_checked"])
        self.assertIsNone(outside["theorem_reference"]["lower_bound_expression"])

    def test_single_support_does_not_receive_lower_bound_claim(self):
        contract = build_sparse_stateprep_bound_contract(10, 1, 0.1)
        self.assertIsNone(contract["theorem_reference"]["lower_bound_expression"])

    def test_rejects_invalid_dimensions_and_support(self):
        for args in (
            (0, 1, 0.1),
            (4, 0, 0.1),
            (4, 17, 0.1),
            (True, 1, 0.1),
            (4, True, 0.1),
        ):
            with self.subTest(args=args):
                with self.assertRaises(ValueError):
                    build_sparse_stateprep_bound_contract(*args)

    def test_rejects_epsilon_outside_the_lower_bound_domain(self):
        for epsilon in (0.0, -0.1, 1 / 6 + 1e-8, math.nan, math.inf, True):
            with self.subTest(epsilon=epsilon):
                with self.assertRaises(ValueError):
                    build_sparse_stateprep_bound_contract(4, 2, epsilon)

    def test_cross_paper_comparability_is_not_assumed(self):
        contract = build_sparse_stateprep_bound_contract(8, 12, 0.01)
        self.assertEqual(
            contract["cross_paper_alignment"]["sparse_qrom_2607_28260_v2"],
            "NOT_ESTABLISHED",
        )

    def test_validator_rejects_mutated_theorem_or_evidence_labels(self):
        contract = build_sparse_stateprep_bound_contract(8, 12, 0.01)
        contract["theorem_reference"]["lower_bound_expression"] = "0"
        self.assertEqual(
            validate_sparse_stateprep_bound_contract(contract),
            ["contract_mismatch"],
        )

    def test_large_symbolic_dimension_avoids_materializing_exponential_arrays(self):
        contract = build_sparse_stateprep_bound_contract(100000, 3, 0.01)
        self.assertEqual(contract["input_contract"]["n_qubits"], 100000)
        self.assertIsNone(contract["unknown_resources"]["numeric_t_count"])


if __name__ == "__main__":
    unittest.main()
