import unittest

from uqpu.equation_discovery import EquationHypothesis, required_discovery_fields


SHA = "sha256:" + "a" * 64


class EquationDiscoveryTests(unittest.TestCase):
    def _candidate(self, **overrides):
        data = dict(
            equation_id="EQN-test-001",
            baseline_model="y = a*x",
            proposed_equation="y = a*x + b*x**2",
            variables_and_units=("x [s]", "y [m]", "a [m/s]", "b [m/s^2]"),
            domain_and_assumptions=("x >= 0", "closed test domain"),
            known_constraints_checked=("dimensional consistency", "finite x->0 limit"),
            scaling_or_limiting_cases=("b->0 recovers baseline",),
            falsifier="held-out error is not lower than baseline or predicted curvature is absent",
            discriminating_observables=("held-out y(x)",),
            evidence_level="CONCEPT",
            data_or_proof_provenance=("synthetic unit-test dataset",),
            independent_validation_plan=("blind held-out dataset",),
            heldout_baseline_error=0.2,
            heldout_candidate_error=0.1,
            heldout_split_hash=SHA,
            counterexample_search_status="SEARCHED_NONE_FOUND",
            counterexample_search_provenance=("bounded adversarial boundary sweep v1",),
            discriminating_experiment_protocol="measure curvature on a frozen held-out x grid",
            independent_replication_status="REPLICATED",
            independent_replication_provenance=("independent implementation hash sha256:" + "b" * 64,),
        )
        data.update(overrides)
        return EquationHypothesis(**data)

    def test_complete_candidate_is_testable(self):
        candidate = self._candidate()
        candidate.validate()
        self.assertTrue(candidate.testable)

    def test_ai_generated_concept_cannot_be_promoted_to_physical_candidate(self):
        candidate = self._candidate(independent_validation_count=10)
        self.assertFalse(candidate.ready_for_physical_candidate_claim)

    def test_missing_falsifier_is_rejected(self):
        candidate = self._candidate(falsifier="")
        with self.assertRaises(ValueError):
            candidate.validate()

    def test_unknown_evidence_label_is_rejected(self):
        candidate = self._candidate(evidence_level="AI_DISCOVERED_LAW")
        with self.assertRaises(ValueError):
            candidate.validate()

    def test_physical_candidate_gate_requires_full_evidence_chain(self):
        candidate = self._candidate(
            evidence_level="PUBLISHED_EXPERIMENT",
            independent_validation_count=1,
        )
        self.assertTrue(candidate.ready_for_physical_candidate_claim)

        no_replication = self._candidate(
            evidence_level="PUBLISHED_EXPERIMENT",
            independent_validation_count=1,
            independent_replication_status="NOT_ATTEMPTED",
            independent_replication_provenance=(),
        )
        self.assertFalse(no_replication.ready_for_physical_candidate_claim)

        no_counterexample_search = self._candidate(
            evidence_level="PUBLISHED_EXPERIMENT",
            independent_validation_count=1,
            counterexample_search_status="NOT_ATTEMPTED",
            counterexample_search_provenance=(),
        )
        self.assertFalse(no_counterexample_search.ready_for_physical_candidate_claim)

        no_gain = self._candidate(
            evidence_level="PUBLISHED_EXPERIMENT",
            independent_validation_count=1,
            heldout_candidate_error=0.3,
        )
        self.assertFalse(no_gain.ready_for_physical_candidate_claim)

    def test_formal_proof_requires_pinned_statement_and_assumptions(self):
        candidate = self._candidate(formal_verification_status="PROVED")
        with self.assertRaises(ValueError):
            candidate.validate()

    def test_formal_proof_does_not_promote_a_concept_to_physics(self):
        candidate = self._candidate(
            formal_verification_status="PROVED",
            formal_system="Lean 4 / Mathlib pinned environment",
            formal_statement_hash=SHA,
            formal_assumptions=("real-valued variables; stated domain",),
            formal_proof_provenance=("proof source hash sha256:" + "c" * 64,),
            independent_validation_count=10,
        )
        candidate.validate()
        self.assertFalse(candidate.ready_for_physical_candidate_claim)

    def test_disproved_formal_obligation_blocks_candidate_claim(self):
        candidate = self._candidate(
            evidence_level="PUBLISHED_EXPERIMENT",
            independent_validation_count=1,
            formal_verification_status="DISPROVED",
            formal_system="Lean 4 / Mathlib pinned environment",
            formal_statement_hash=SHA,
            formal_assumptions=("real-valued variables; stated domain",),
            formal_proof_provenance=("counterexample proof hash sha256:" + "d" * 64,),
        )
        candidate.validate()
        self.assertFalse(candidate.ready_for_physical_candidate_claim)

    def test_required_contract_includes_proof_counterexample_and_replication_fields(self):
        fields = required_discovery_fields()
        for name in (
            "baseline_model",
            "proposed_equation",
            "known_constraints_checked",
            "falsifier",
            "discriminating_observables",
            "independent_validation_plan",
            "heldout_split_hash",
            "formal_verification_status",
            "counterexample_search_status",
            "discriminating_experiment_protocol",
            "independent_replication_status",
        ):
            self.assertIn(name, fields)


if __name__ == "__main__":
    unittest.main()
