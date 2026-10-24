import unittest

from uqpu.search_comparison import (
    SearchBudget,
    SearchRun,
    cost_per_accepted_useful_model,
    energy_comparison_available,
    validate_matched_search_runs,
)


class SearchComparisonTests(unittest.TestCase):
    def budget(self, **changes):
        values = dict(
            max_wall_seconds=900.0,
            max_evaluator_calls=3000,
            max_generated_tokens=100000,
            max_energy_joules=None,
            max_direct_cost_usd=None,
        )
        values.update(changes)
        return SearchBudget(**values)

    def make_run(self, method_id, **changes):
        values = dict(
            method_id=method_id,
            benchmark_id="EQN-SYNTH-001",
            dataset_digest="dataset-v1",
            train_digest="train-a",
            validation_digest="validation-b",
            heldout_digest="heldout-c",
            budget=self.budget(),
            actual_wall_seconds=400.0,
            actual_evaluator_calls=1200,
            actual_generated_tokens=40000,
            energy_joules=None,
            direct_cost_usd=None,
            candidate_count=100,
            accepted_useful_model_count=0,
            best_heldout_error=None,
            constraint_violating_candidate_count=2,
            accepted_model_constraint_violations=0,
            false_discovery_count=4,
            independent_replay_count=0,
        )
        values.update(changes)
        return SearchRun(**values)

    def test_matched_comparison_accepts_same_contract(self):
        validate_matched_search_runs([self.make_run("static"), self.make_run("adaptive")])

    def test_budget_mismatch_is_rejected(self):
        a = self.make_run("static")
        b = self.make_run("adaptive", budget=self.budget(max_evaluator_calls=3001))
        with self.assertRaisesRegex(ValueError, "identical declared resource caps"):
            validate_matched_search_runs([a, b])

    def test_split_overlap_is_rejected(self):
        b = self.make_run("adaptive", heldout_digest="validation-b")
        with self.assertRaisesRegex(ValueError, "digests must be distinct"):
            validate_matched_search_runs([self.make_run("static"), b])

    def test_actual_use_above_cap_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "exceed"):
            self.make_run("adaptive", actual_evaluator_calls=3001).validate()

    def test_energy_is_not_inferred_when_unmeasured(self):
        runs = [self.make_run("static"), self.make_run("adaptive")]
        self.assertFalse(energy_comparison_available(runs))

    def test_accepted_model_requires_heldout_constraints_and_replay(self):
        with self.assertRaisesRegex(ValueError, "independent replay"):
            self.make_run(
                "adaptive",
                candidate_count=1,
                accepted_useful_model_count=1,
                best_heldout_error=0.01,
                constraint_violating_candidate_count=0,
                accepted_model_constraint_violations=0,
                false_discovery_count=0,
                independent_replay_count=0,
            ).validate()

    def test_accepted_model_requires_zero_constraint_violations(self):
        with self.assertRaisesRegex(ValueError, "zero recorded"):
            self.make_run(
                "adaptive",
                candidate_count=1,
                accepted_useful_model_count=1,
                best_heldout_error=0.01,
                constraint_violating_candidate_count=0,
                accepted_model_constraint_violations=1,
                false_discovery_count=0,
                independent_replay_count=1,
            ).validate()

    def test_cost_per_accepted_model_is_none_when_cost_unknown_or_no_acceptance(self):
        self.assertIsNone(cost_per_accepted_useful_model(self.make_run("static")))
        accepted = self.make_run(
            "adaptive",
            candidate_count=2,
            accepted_useful_model_count=1,
            best_heldout_error=0.01,
            constraint_violating_candidate_count=1,
            accepted_model_constraint_violations=0,
            false_discovery_count=0,
            independent_replay_count=1,
            direct_cost_usd=5.0,
        )
        self.assertEqual(cost_per_accepted_useful_model(accepted), 5.0)

    def test_duplicate_methods_rejected(self):
        with self.assertRaisesRegex(ValueError, "unique"):
            validate_matched_search_runs([self.make_run("same"), self.make_run("same")])

    def test_nonfinite_metrics_rejected(self):
        with self.assertRaises(ValueError):
            self.make_run("static", actual_wall_seconds=float("nan")).validate()

    def test_false_discovery_count_is_first_class_and_bounded(self):
        with self.assertRaisesRegex(ValueError, "false discoveries cannot exceed candidates"):
            self.make_run("static", candidate_count=2, false_discovery_count=3).validate()

    def test_declared_energy_cap_requires_measured_energy(self):
        with self.assertRaisesRegex(ValueError, "energy cap declared"):
            self.make_run("static", budget=self.budget(max_energy_joules=100.0)).validate()

    def test_each_accepted_model_requires_its_own_replay(self):
        with self.assertRaisesRegex(ValueError, "each accepted model"):
            self.make_run(
                "adaptive",
                candidate_count=3,
                accepted_useful_model_count=2,
                best_heldout_error=0.01,
                constraint_violating_candidate_count=0,
                accepted_model_constraint_violations=0,
                false_discovery_count=0,
                independent_replay_count=1,
            ).validate()


if __name__ == "__main__":
    unittest.main()
