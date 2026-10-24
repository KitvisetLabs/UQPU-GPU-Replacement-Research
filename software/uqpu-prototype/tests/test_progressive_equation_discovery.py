import unittest

from uqpu.progressive_equation_discovery import (
    DataSplits,
    DiscoveryStage,
    ProgressiveDiscoveryPlan,
    ResourceBudget,
)


CONSTRAINTS = (
    "dimensional_consistency: checked",
    "symmetry: checked",
    "conservation: not_applicable: static toy relation has no exchange process",
    "causality: not_applicable: static scalar mapping has no propagation model",
)


def stage(stage_id, parents=(), evaluations=5, **overrides):
    values = dict(
        stage_id=stage_id,
        knowledge_unit=f"interpretable unit {stage_id}",
        parent_stage_ids=parents,
        variables_and_units=("x [s]", "y [m]"),
        constraint_audit=CONSTRAINTS,
        limiting_cases=("coefficient -> 0 recovers incumbent",),
        falsifier="held-out prediction fails the preregistered tolerance",
        discriminating_observable="blind held-out y(x)",
        candidate_evaluations=evaluations,
        heldout_used_for_selection=False,
    )
    values.update(overrides)
    return DiscoveryStage(**values)


def plan(**overrides):
    budget = ResourceBudget(10, 60, 12, 100)
    values = dict(
        experiment_id="EQN-COSR-001",
        incumbent_model="known baseline relation",
        one_shot_method="one-shot symbolic regression",
        progressive_method="progressive chain search",
        grammar_sha256="a" * 64,
        evaluator_version="evaluator-v1",
        evaluation_metric="normalized held-out error",
        optimization_direction="minimize",
        data_splits=DataSplits("b" * 64, "c" * 64, "d" * 64),
        one_shot_budget=budget,
        progressive_budget=budget,
        stages=(stage("S1", evaluations=4), stage("S2", parents=("S1",), evaluations=6)),
    )
    values.update(overrides)
    return ProgressiveDiscoveryPlan(**values)


class ProgressiveEquationDiscoveryTests(unittest.TestCase):
    def test_valid_plan_passes_and_stays_model_only(self):
        candidate = plan()
        candidate.validate()
        self.assertFalse(candidate.physical_law_promotion_allowed)

    def test_train_validation_and_heldout_hashes_must_be_distinct(self):
        candidate = plan(data_splits=DataSplits("b" * 64, "b" * 64, "d" * 64))
        with self.assertRaisesRegex(ValueError, "distinct"):
            candidate.validate()

    def test_malformed_split_digest_fails_closed(self):
        candidate = plan(data_splits=DataSplits("NOT_A_HASH", "c" * 64, "d" * 64))
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            candidate.validate()

    def test_comparison_arms_must_have_equal_resource_caps(self):
        candidate = plan(progressive_budget=ResourceBudget(10, 61, 12, 100))
        with self.assertRaisesRegex(ValueError, "identical resource budgets"):
            candidate.validate()

    def test_stage_evaluations_must_consume_exactly_the_progressive_budget(self):
        candidate = plan(stages=(stage("S1", evaluations=4), stage("S2", parents=("S1",), evaluations=5)))
        with self.assertRaisesRegex(ValueError, "sum of stage"):
            candidate.validate()

    def test_later_stage_must_depend_on_an_earlier_unit(self):
        candidate = plan(stages=(stage("S1", evaluations=4), stage("S2", evaluations=6)))
        with self.assertRaisesRegex(ValueError, "earlier knowledge unit"):
            candidate.validate()

    def test_forward_dependency_is_rejected(self):
        candidate = plan(stages=(stage("S1", parents=("S2",), evaluations=4), stage("S2", parents=("S1",), evaluations=6)))
        with self.assertRaisesRegex(ValueError, "first stage"):
            candidate.validate()

    def test_heldout_data_cannot_guide_selection(self):
        candidate = plan(stages=(stage("S1", evaluations=4), stage("S2", parents=("S1",), evaluations=6, heldout_used_for_selection=True)))
        with self.assertRaisesRegex(ValueError, "held-out data"):
            candidate.validate()

    def test_every_stage_must_audit_dimensions_symmetry_conservation_and_causality(self):
        candidate = plan(stages=(stage("S1", evaluations=4, constraint_audit=("dimensional_consistency: checked",)), stage("S2", parents=("S1",), evaluations=6)))
        with self.assertRaisesRegex(ValueError, "constraint audit incomplete"):
            candidate.validate()

    def test_not_applicable_constraint_requires_reason(self):
        bad = ("dimensional_consistency: checked", "symmetry: checked", "conservation: not_applicable", "causality: not_applicable: no dynamics")
        candidate = plan(stages=(stage("S1", evaluations=4, constraint_audit=bad), stage("S2", parents=("S1",), evaluations=6)))
        with self.assertRaisesRegex(ValueError, "requires a reason"):
            candidate.validate()

    def test_plan_must_be_frozen_before_heldout_unblinding(self):
        candidate = plan(heldout_unblinded_before_freeze=True)
        with self.assertRaisesRegex(ValueError, "unblinded"):
            candidate.validate()

    def test_protocol_cannot_promote_itself_to_experimental_evidence(self):
        candidate = plan(evidence_class="PUBLISHED_EXPERIMENT")
        with self.assertRaisesRegex(ValueError, "MODEL_ONLY"):
            candidate.validate()

    def test_no_provider_or_qpu_execution_is_allowed_by_offline_plan(self):
        candidate = plan(provider_calls=1)
        with self.assertRaisesRegex(ValueError, "zero provider calls"):
            candidate.validate()

    def test_budget_booleans_are_not_accepted_as_integers(self):
        candidate = plan(one_shot_budget=ResourceBudget(True, 60, 12, 100), progressive_budget=ResourceBudget(True, 60, 12, 100))
        with self.assertRaisesRegex(ValueError, "positive integer"):
            candidate.validate()

    def test_comparison_arms_must_be_distinct_methods(self):
        candidate = plan(progressive_method="one-shot symbolic regression")
        with self.assertRaisesRegex(ValueError, "distinct search methods"):
            candidate.validate()

    def test_nonstring_grammar_digest_fails_closed(self):
        candidate = plan(grammar_sha256=None)
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            candidate.validate()

    def test_boolean_provider_counter_is_not_accepted_as_zero(self):
        candidate = plan(provider_calls=False)
        with self.assertRaisesRegex(ValueError, "zero provider calls"):
            candidate.validate()

    def test_constraint_audit_must_be_a_tuple(self):
        candidate = plan(stages=(stage("S1", evaluations=4, constraint_audit=list(CONSTRAINTS)), stage("S2", parents=("S1",), evaluations=6)))
        with self.assertRaisesRegex(ValueError, "must be a tuple"):
            candidate.validate()


    def test_non_boolean_heldout_unblinding_flag_fails_closed(self):
        candidate = plan(heldout_unblinded_before_freeze=None)
        with self.assertRaisesRegex(ValueError, "must be boolean false"):
            candidate.validate()

    def test_data_splits_wrong_type_fails_with_contract_error(self):
        candidate = plan(data_splits=None)
        with self.assertRaisesRegex(ValueError, "data_splits must be a DataSplits"):
            candidate.validate()

    def test_resource_budget_wrong_type_fails_with_contract_error(self):
        candidate = plan(one_shot_budget=None)
        with self.assertRaisesRegex(ValueError, "one_shot_budget must be a ResourceBudget"):
            candidate.validate()

    def test_non_stage_entry_fails_with_contract_error(self):
        candidate = plan(stages=(stage("S1", evaluations=4), "not-a-stage"))
        with self.assertRaisesRegex(ValueError, "each stages entry must be a DiscoveryStage"):
            candidate.validate()

    def test_checked_constraint_cannot_include_unparsed_extra_reason(self):
        bad = (
            "dimensional_consistency: checked: hidden override",
            "symmetry: checked",
            "conservation: not_applicable: static toy relation has no exchange process",
            "causality: not_applicable: static scalar mapping has no propagation model",
        )
        candidate = plan(stages=(stage("S1", evaluations=4, constraint_audit=bad), stage("S2", parents=("S1",), evaluations=6)))
        with self.assertRaisesRegex(ValueError, "must not include an extra reason"):
            candidate.validate()


if __name__ == "__main__":
    unittest.main()
