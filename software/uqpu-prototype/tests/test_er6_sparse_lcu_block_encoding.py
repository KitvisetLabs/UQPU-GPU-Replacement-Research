import json
from pathlib import Path
import unittest

from uqpu.er6_sparse_lcu_block_encoding import build_lcu_contract, validate_lcu_contract


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "benchmarks/experiments/cycle002-delta01-er6-frozen-contract.json"
ARTIFACT = ROOT / "benchmarks/results/cycle008-delta05-er6-sparse-lcu-block-encoding.json"


class ER6SparseLCUBlockEncodingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = json.loads(SOURCE.read_text(encoding="utf-8"))

    def test_all_basis_states_match_maxcut_operator(self):
        contract = build_lcu_contract(self.source)
        self.assertEqual(contract["verification"]["basis_states_exhaustively_checked"], 64)
        self.assertLessEqual(contract["verification"]["max_projected_diagonal_residual"], 1e-15)
        self.assertEqual(contract["verification"]["accepted_normalized_cut_values"], [7 / 9] * 4)

    def test_resource_fields_fail_closed(self):
        contract = build_lcu_contract(self.source)
        self.assertEqual(validate_lcu_contract(contract), [])
        self.assertIsNone(contract["resource_contract"]["prep_gate_count"])
        self.assertIsNone(contract["resource_contract"]["provider_cost"])
        self.assertFalse(contract["scaling_and_access_boundary"]["general_sparse_qrom_bound_applied"])

    def test_mutations_are_rejected(self):
        contract = build_lcu_contract(self.source)
        contract["resource_contract"]["provider_cost"] = 1.0
        self.assertIn("unmeasured_resource_must_remain_null", validate_lcu_contract(contract))
        self.assertIn("contract_digest_mismatch", validate_lcu_contract(contract))

    def test_committed_artifact_matches_builder(self):
        expected = build_lcu_contract(self.source)
        actual = json.loads(ARTIFACT.read_text(encoding="utf-8"))
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
