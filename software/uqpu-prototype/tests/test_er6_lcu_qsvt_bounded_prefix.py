import copy
import importlib.util
import json
from pathlib import Path
import unittest

from uqpu.er6_lcu_qsvt_bounded_prefix import (
    QUERY_COUNTS,
    TOLERANCE,
    build_bounded_prefix_contract,
    explicit_prefix_matrix,
    independent_prefix_state,
    reproduce_with_qiskit,
    validate_bounded_prefix_contract,
)


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "benchmarks/experiments/cycle002-delta01-er6-frozen-contract.json"
ARTIFACT = ROOT / "benchmarks/results/cycle008-delta10-er6-lcu-qsvt-bounded-prefix-contract.json"
SDK_ARTIFACT = ROOT / "benchmarks/results/cycle008-delta10-er6-lcu-qsvt-bounded-prefix-qiskit.json"
qiskit_available = importlib.util.find_spec("qiskit") is not None


class ER6QSVTBoundedPrefixContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = json.loads(SOURCE.read_text(encoding="utf-8"))

    def test_committed_contract_is_deterministic_and_valid(self):
        expected = build_bounded_prefix_contract(self.source)
        actual = json.loads(ARTIFACT.read_text(encoding="utf-8"))
        self.assertEqual(actual, expected)
        self.assertEqual(validate_bounded_prefix_contract(actual), [])

    def test_three_and_five_query_ladder_covers_every_sector(self):
        contract = build_bounded_prefix_contract(self.source)
        self.assertEqual([item["queries"] for item in contract["prefixes"]], list(QUERY_COUNTS))
        self.assertEqual(contract["workload_sectors"], 64)
        self.assertEqual(len(contract["workload_eigenvalues"]), 64)
        for item in contract["prefixes"]:
            self.assertEqual(len(item["rows"]), 7)
            self.assertEqual(item["unique_eigenvalues_checked"], 7)
            self.assertEqual(item["projector_phases"], item["queries"] + 1)
        self.assertLessEqual(contract["acceptance"]["matrix_vs_state_max_abs_residual"], TOLERANCE)
        self.assertFalse(contract["authorization"]["provider_submission"])

    def test_matrix_and_independent_state_agree_at_domain_edges(self):
        for queries in QUERY_COUNTS:
            for eigenvalue in (-1.0, 0.0, 1.0):
                matrix = explicit_prefix_matrix(eigenvalue, queries)
                state = independent_prefix_state(eigenvalue, queries)
                self.assertLessEqual(abs(matrix[0][0] - state[0]), TOLERANCE)
                self.assertLessEqual(abs(matrix[1][0] - state[1]), TOLERANCE)

    def test_query_or_sector_mutation_fails_closed(self):
        contract = build_bounded_prefix_contract(self.source)
        mutated = copy.deepcopy(contract)
        mutated["prefixes"][0]["queries"] = 81
        mutated["prefixes"][1]["rows"].pop()
        errors = validate_bounded_prefix_contract(mutated)
        self.assertIn("query_ladder_mismatch", errors)
        self.assertIn("unique_spectrum_mismatch_5", errors)
        self.assertIn("contract_digest_mismatch", errors)

    def test_persisted_sdk_certificate_is_provenance_bound_and_fail_closed(self):
        contract = json.loads(ARTIFACT.read_text(encoding="utf-8"))
        result = json.loads(SDK_ARTIFACT.read_text(encoding="utf-8"))
        self.assertTrue(result["passed"])
        self.assertEqual(result["contract_sha256"], contract["contract_sha256"])
        self.assertEqual(result["provenance"]["commit"], "39fa6f99d6cc512555e5613deb182ed79d054f34")
        self.assertEqual([item["queries"] for item in result["prefix_results"]], list(QUERY_COUNTS))
        for item in result["prefix_results"]:
            self.assertTrue(item["passed"])
            self.assertTrue(item["resource_gate_passed"])
            self.assertEqual(item["resources"]["provider_jobs"], 0)
            self.assertEqual(item["resources"]["shots"], 0)
            self.assertIsNone(item["resources"]["provider_cost"])
            self.assertIsNone(item["resources"]["energy_j"])
            for key, value in item["agreement"].items():
                if key.endswith("residual"):
                    self.assertLessEqual(value, item["agreement"]["tolerance"])


@unittest.skipUnless(qiskit_available, "optional pinned Qiskit dependency")
class ER6QSVTBoundedPrefixPinnedQiskitTests(unittest.TestCase):
    def test_bounded_prefix_ladder_passes_all_gates(self):
        result = reproduce_with_qiskit()
        self.assertTrue(result["passed"], result)
        self.assertEqual([item["queries"] for item in result["prefix_results"]], list(QUERY_COUNTS))
        for item in result["prefix_results"]:
            self.assertTrue(item["resource_gate_passed"])
            self.assertEqual(item["resources"]["provider_jobs"], 0)
            for key, value in item["agreement"].items():
                if key.endswith("residual"):
                    self.assertLessEqual(value, item["agreement"]["tolerance"])


if __name__ == "__main__":
    unittest.main()
