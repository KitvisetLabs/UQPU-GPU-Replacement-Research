import unittest

from uqpu.reversible_circuit_contract import (
    ReversibleCircuitCandidate,
    compare_resource_frontier,
)


class ReversibleCircuitContractTests(unittest.TestCase):
    def _candidate(self, candidate_id="candidate-a", **overrides):
        data = dict(
            candidate_id=candidate_id,
            function_id="toy-reversible-function-v1",
            function_spec_sha256="a" * 64,
            candidate_sha256=("b" if candidate_id == "candidate-a" else "c") * 64,
            generator_id="llm-generator-v1",
            evaluator_id="independent-evaluator-v1",
            evaluator_sha256="d" * 64,
            input_width_bits=2,
            output_width_bits=2,
            peak_qubits=4,
            toffoli_count=10,
            t_depth=5,
            logical_depth=8,
            failure_probability_upper_bound=0.0,
            allowed_failure_probability=0.0,
            verification_status="EXHAUSTIVE_PASS",
            exhaustive_basis_states_checked=16,
            verification_artifact_sha256="e" * 64,
            phase_check_status="EXACT_RELATIVE_PHASE_PASS",
            ancilla_cleanup_status="EXHAUSTIVE_ZERO_PASS",
        )
        data.update(overrides)
        return ReversibleCircuitCandidate(**data)

    def test_fully_checked_candidate_is_eligible_for_resource_comparison(self):
        candidate = self._candidate()
        candidate.validate()
        self.assertTrue(candidate.eligible_for_resource_comparison)
        self.assertEqual(candidate.toffoli_qubit_proxy, 40)

    def test_exhaustive_pass_requires_full_declared_basis_domain(self):
        candidate = self._candidate(exhaustive_basis_states_checked=15)
        with self.assertRaises(ValueError):
            candidate.validate()

    def test_unverified_phase_or_dirty_ancilla_blocks_comparison(self):
        self.assertFalse(self._candidate(phase_check_status="UNVERIFIED").eligible_for_resource_comparison)
        self.assertFalse(self._candidate(ancilla_cleanup_status="UNVERIFIED").eligible_for_resource_comparison)

    def test_failure_bound_must_fit_same_declared_budget(self):
        candidate = self._candidate(failure_probability_upper_bound=0.01, allowed_failure_probability=0.001)
        self.assertFalse(candidate.eligible_for_resource_comparison)

    def test_generator_and_evaluator_must_be_distinct_roles(self):
        candidate = self._candidate(evaluator_id="llm-generator-v1")
        with self.assertRaises(ValueError):
            candidate.validate()

    def test_formal_status_requires_proof_artifact_hash(self):
        candidate = self._candidate(
            verification_status="FORMAL_PROOF_CHECKED",
            proof_artifact_sha256=None,
        )
        with self.assertRaises(ValueError):
            candidate.validate()

    def test_pareto_dominance_requires_same_contract(self):
        a = self._candidate(candidate_id="candidate-a", toffoli_count=8, peak_qubits=4, t_depth=4, logical_depth=7)
        b = self._candidate(candidate_id="candidate-b", toffoli_count=10, peak_qubits=5, t_depth=5, logical_depth=8)
        self.assertEqual(compare_resource_frontier(a, b), "A_DOMINATES_B")

    def test_tradeoff_is_not_collapsed_to_toffoli_times_qubits(self):
        a = self._candidate(candidate_id="candidate-a", toffoli_count=8, peak_qubits=7, t_depth=4, logical_depth=7)
        b = self._candidate(candidate_id="candidate-b", toffoli_count=10, peak_qubits=5, t_depth=5, logical_depth=8)
        self.assertEqual(compare_resource_frontier(a, b), "TRADEOFF")

    def test_different_semantics_or_failure_budget_are_incomparable(self):
        a = self._candidate(candidate_id="candidate-a")
        b = self._candidate(candidate_id="candidate-b", function_spec_sha256="f" * 64)
        self.assertEqual(compare_resource_frontier(a, b), "INCOMPARABLE")
        c = self._candidate(candidate_id="candidate-c", allowed_failure_probability=0.01)
        self.assertEqual(compare_resource_frontier(a, c), "INCOMPARABLE")

    def test_unverified_candidate_cannot_enter_resource_frontier(self):
        a = self._candidate(candidate_id="candidate-a")
        b = self._candidate(candidate_id="candidate-b", verification_status="UNVERIFIED")
        self.assertEqual(compare_resource_frontier(a, b), "BLOCKED_UNVERIFIED")


if __name__ == "__main__":
    unittest.main()
