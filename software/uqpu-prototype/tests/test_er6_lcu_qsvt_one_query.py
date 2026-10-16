import copy
import importlib.util
import json
from pathlib import Path
import unittest

from uqpu.er6_lcu_qsvt_one_query import (
    BASIS_GATES,
    build_one_query_contract,
    reproduce_with_qiskit,
    validate_one_query_contract,
)


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "benchmarks/experiments/cycle002-delta01-er6-frozen-contract.json"
ARTIFACT = ROOT / "benchmarks/results/cycle008-delta07-er6-lcu-qsvt-one-query-contract.json"
SDK_ARTIFACT = ROOT / "benchmarks/results/cycle008-delta07-er6-lcu-qsvt-one-query-qiskit.json"
qiskit_available = importlib.util.find_spec("qiskit") is not None


class ER6QSVTOneQueryContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = json.loads(SOURCE.read_text(encoding="utf-8"))

    def test_committed_contract_is_deterministic_and_valid(self):
        expected = build_one_query_contract(self.source)
        actual = json.loads(ARTIFACT.read_text(encoding="utf-8"))
        self.assertEqual(actual, expected)
        self.assertEqual(validate_one_query_contract(actual), [])

    def test_bounded_fragment_and_authorization(self):
        contract = build_one_query_contract(self.source)
        self.assertEqual(contract["phase_source"]["selected_indices"], [0, 1])
        self.assertEqual(contract["composition"]["block_queries"], 1)
        self.assertEqual(contract["composition"]["projector_phases"], 2)
        self.assertFalse(contract["authorization"]["provider_submission"])
        self.assertFalse(contract["authorization"]["paid_execution"])

    def test_mutation_fails_closed(self):
        contract = build_one_query_contract(self.source)
        mutated = copy.deepcopy(contract)
        mutated["authorization"]["provider_submission"] = True
        self.assertIn("authorization_must_fail_closed", validate_one_query_contract(mutated))
        self.assertIn("contract_digest_mismatch", validate_one_query_contract(mutated))

    def test_persisted_sdk_certificate_is_provenance_bound_and_fail_closed(self):
        result = json.loads(SDK_ARTIFACT.read_text(encoding="utf-8"))
        self.assertTrue(result["passed"])
        self.assertEqual(result["contract_sha256"], build_one_query_contract(self.source)["contract_sha256"])
        self.assertEqual(result["provenance"]["commit"], "9d7e5d761fc8ddf18a0fec4a9564ce836e617e96")
        self.assertLessEqual(
            result["operator_agreement"]["decomposed_vs_logical_full_operator_max_abs_residual"],
            result["operator_agreement"]["tolerance"],
        )
        self.assertEqual(result["resources"]["provider_jobs"], 0)
        self.assertIsNone(result["resources"]["provider_cost"])
        self.assertIsNone(result["resources"]["energy_j"])


@unittest.skipUnless(qiskit_available, "optional pinned Qiskit dependency")
class ER6QSVTOneQueryPinnedQiskitTests(unittest.TestCase):
    def test_projected_fragment_and_decomposition(self):
        result = reproduce_with_qiskit()
        self.assertTrue(result["passed"], result)
        agreement = result["operator_agreement"]
        self.assertLessEqual(agreement["projected_fragment_max_abs_residual"], 2e-12)
        self.assertLessEqual(agreement["decomposed_projected_fragment_max_abs_residual"], 2e-12)
        self.assertLessEqual(agreement["decomposed_vs_logical_full_operator_max_abs_residual"], 2e-12)
        self.assertTrue(set(result["resources"]["decomposed_operation_counts"]).issubset(BASIS_GATES))
        self.assertEqual(result["resources"]["provider_jobs"], 0)
        self.assertIsNone(result["resources"]["provider_cost"])


if __name__ == "__main__":
    unittest.main()
