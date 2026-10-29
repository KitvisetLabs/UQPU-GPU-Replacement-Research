import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SPEC_PATH = (
    ROOT
    / "research_lanes"
    / "A_quantum_programming_runtime"
    / "SPARSE_STATEPREP_TOFFOLI_BENCHMARK_V1.json"
)


class SparseStateprepToffoliContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))

    def test_contract_is_source_pinned_and_not_project_evidence(self):
        self.assertEqual(
            self.spec["schema"], "uqpu-sparse-stateprep-toffoli-benchmark-v1"
        )
        self.assertEqual(
            self.spec["evidence_class"], "PREREGISTERED_BENCHMARK_CONTRACT"
        )
        self.assertEqual(
            self.spec["source"]["doi"], "10.22331/q-2026-09-10-2208"
        )
        self.assertFalse(
            self.spec["external_claims_not_project_results"][
                "independent_reproduction"
            ]
        )
        self.assertFalse(self.spec["nonclaims"]["UQPU_hardware_advantage_established"])
        self.assertFalse(self.spec["nonclaims"]["cost_advantage_established"])

    def test_toffoli_and_t_count_are_separate_required_metrics(self):
        axes = set(self.spec["comparison_axes"])
        self.assertIn("Toffoli_count", axes)
        self.assertIn("decomposed_T_count", axes)
        self.assertIn("logical_depth", axes)
        self.assertIn("ancilla_count", axes)

    def test_memory_and_output_contracts_cannot_be_omitted(self):
        axes = set(self.spec["comparison_axes"])
        self.assertIn("classical_description_bytes", axes)
        self.assertIn("transfer_and_state_io", axes)
        self.assertIn("measurement_and_output_reconstruction", axes)
        self.assertFalse(
            self.spec["nonclaims"][
                "Hilbert_space_dimension_equals_readable_classical_bytes"
            ]
        )

    def test_acceptance_gate_requires_heldout_and_independent_reproduction(self):
        gates = self.spec["acceptance_gates"]
        self.assertTrue(gates["independent_small_instance_reproduction"])
        self.assertTrue(gates["disjoint_held_out_n_s_epsilon_cases"])
        self.assertTrue(gates["counterexample_and_promise_violation_tests"])
        self.assertTrue(
            gates["theorem_assumptions_aligned_before_cross_paper_comparison"]
        )

    def test_paid_execution_remains_explicitly_unauthorized(self):
        self.assertTrue(
            self.spec["acceptance_gates"][
                "paid_qpu_requires_credentials_bounded_budget_and_explicit_consent"
            ]
        )
        self.assertFalse(self.spec["nonclaims"]["paid_QPU_execution_authorized"])


if __name__ == "__main__":
    unittest.main()
