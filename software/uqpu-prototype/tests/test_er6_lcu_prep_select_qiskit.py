import copy
import importlib.util
import json
from pathlib import Path
import unittest

from uqpu.er6_lcu_prep_select_qiskit import (
    BASIS_GATES,
    build_provider_neutral_contract,
    reproduce_with_qiskit,
    validate_provider_neutral_contract,
)


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "benchmarks/experiments/cycle002-delta01-er6-frozen-contract.json"
ARTIFACT = ROOT / "benchmarks/results/cycle008-delta06-er6-lcu-prep-select-contract.json"
qiskit_available = importlib.util.find_spec("qiskit") is not None


class ER6ProviderNeutralPrepSelectTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = json.loads(SOURCE.read_text(encoding="utf-8"))

    def test_committed_contract_is_deterministic_and_valid(self):
        expected = build_provider_neutral_contract(self.source)
        actual = json.loads(ARTIFACT.read_text(encoding="utf-8"))
        self.assertEqual(actual, expected)
        self.assertEqual(validate_provider_neutral_contract(actual), [])

    def test_prep_select_semantics_and_authorization(self):
        contract = build_provider_neutral_contract(self.source)
        self.assertEqual(len(contract["prep"]["amplitudes"]), 16)
        self.assertEqual(contract["prep"]["amplitude_norm_residual"], 0.0)
        self.assertEqual(len(contract["select"]["branches"]), 10)
        self.assertEqual(contract["select"]["padded_identity_indices"], list(range(10, 16)))
        self.assertFalse(contract["authorization"]["provider_submission"])
        self.assertFalse(contract["authorization"]["paid_execution"])

    def test_mutation_fails_closed(self):
        contract = build_provider_neutral_contract(self.source)
        mutated = copy.deepcopy(contract)
        mutated["authorization"]["provider_submission"] = True
        self.assertIn("authorization_must_fail_closed", validate_provider_neutral_contract(mutated))
        self.assertIn("contract_digest_mismatch", validate_provider_neutral_contract(mutated))


@unittest.skipUnless(qiskit_available, "optional pinned Qiskit dependency")
class ER6PinnedQiskitPrepSelectTests(unittest.TestCase):
    def test_projected_operator_and_decomposition(self):
        result = reproduce_with_qiskit()
        self.assertTrue(result["passed"], result)
        self.assertLessEqual(result["operator_agreement"]["projected_block_max_abs_residual"], 2e-12)
        self.assertLessEqual(result["operator_agreement"]["decomposed_projected_block_max_abs_residual"], 2e-12)
        self.assertTrue(set(result["resources"]["decomposed_operation_counts"]).issubset(BASIS_GATES))
        self.assertEqual(result["resources"]["provider_jobs"], 0)
        self.assertIsNone(result["resources"]["provider_cost"])


if __name__ == "__main__":
    unittest.main()
