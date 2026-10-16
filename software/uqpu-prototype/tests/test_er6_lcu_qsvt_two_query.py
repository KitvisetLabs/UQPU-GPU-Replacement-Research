import copy
import importlib.util
import json
from pathlib import Path
import unittest

from uqpu.er6_lcu_qsvt_two_query import (
    BASIS_GATES,
    build_two_query_contract,
    reproduce_with_qiskit,
    validate_two_query_contract,
)


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "benchmarks/experiments/cycle002-delta01-er6-frozen-contract.json"
ARTIFACT = ROOT / "benchmarks/results/cycle008-delta08-er6-lcu-qsvt-two-query-contract.json"
SDK_ARTIFACT = ROOT / "benchmarks/results/cycle008-delta08-er6-lcu-qsvt-two-query-qiskit.json"
qiskit_available = importlib.util.find_spec("qiskit") is not None


class ER6QSVTTwoQueryContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = json.loads(SOURCE.read_text(encoding="utf-8"))

    def test_committed_contract_is_deterministic_and_valid(self):
        expected = build_two_query_contract(self.source)
        actual = json.loads(ARTIFACT.read_text(encoding="utf-8"))
        self.assertEqual(actual, expected)
        self.assertEqual(validate_two_query_contract(actual), [])

    def test_recurrence_and_authorization(self):
        contract = build_two_query_contract(self.source)
        self.assertEqual(contract["phase_source"]["selected_indices"], [0, 1, 2])
        self.assertEqual(contract["composition"]["block_queries"], 2)
        self.assertEqual(contract["composition"]["projector_phases"], 3)
        self.assertFalse(contract["authorization"]["provider_submission"])

    def test_mutation_fails_closed(self):
        contract = build_two_query_contract(self.source)
        mutated = copy.deepcopy(contract)
        mutated["composition"]["block_queries"] = 81
        self.assertIn("recurrence_count_mismatch", validate_two_query_contract(mutated))
        self.assertIn("contract_digest_mismatch", validate_two_query_contract(mutated))

    def test_persisted_sdk_certificate_is_provenance_bound_and_fail_closed(self):
        result = json.loads(SDK_ARTIFACT.read_text(encoding="utf-8"))
        self.assertTrue(result["passed"])
        self.assertEqual(result["contract_sha256"], build_two_query_contract(self.source)["contract_sha256"])
        self.assertEqual(result["provenance"]["commit"], "2bf019cf21efd43ec7ae9f8196ec03e5734e7945")
        for key, value in result["operator_agreement"].items():
            if key.endswith("residual"):
                self.assertLessEqual(value, result["operator_agreement"]["tolerance"])
        self.assertEqual(result["resources"]["provider_jobs"], 0)
        self.assertEqual(result["resources"]["shots"], 0)
        self.assertIsNone(result["resources"]["provider_cost"])
        self.assertIsNone(result["resources"]["energy_j"])


@unittest.skipUnless(qiskit_available, "optional pinned Qiskit dependency")
class ER6QSVTTwoQueryPinnedQiskitTests(unittest.TestCase):
    def test_independent_recurrence_and_decomposition(self):
        result = reproduce_with_qiskit()
        self.assertTrue(result["passed"], result)
        for key, value in result["operator_agreement"].items():
            if key.endswith("residual"):
                self.assertLessEqual(value, result["operator_agreement"]["tolerance"])
        self.assertTrue(set(result["resources"]["decomposed_operation_counts"]).issubset(BASIS_GATES))
        self.assertEqual(result["resources"]["provider_jobs"], 0)
        self.assertEqual(result["spectral_sector_agreement"]["workload_sectors_checked"], 64)
        for key, value in result["spectral_sector_agreement"].items():
            if key.endswith("residual"):
                self.assertLessEqual(value, result["spectral_sector_agreement"]["tolerance"])


if __name__ == "__main__":
    unittest.main()
