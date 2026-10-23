import hashlib
import unittest
from dataclasses import replace

from uqpu.experiment_design import (
    ExperimentPlan,
    PredictionSummary,
    ResourceBudget,
    validate_matched_plans,
)


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


class ExperimentDesignContractTests(unittest.TestCase):
    def setUp(self):
        self.cap = ResourceBudget(10, 100, 120.0, 100.0, 20.0, 10000, 3, 20.0, 20.0, None)
        self.used = ResourceBudget(2, 50, 40.0, 35.0, 5.0, 4000, 1, 3.0, 5.0, None)

    def plan(self, planner="human", **overrides):
        values = dict(
            plan_id=f"plan-{planner}", planner_id=planner,
            experiment_action="sample x at preregistered points",
            incumbent_model="y=a*x", incumbent_assumptions=("linear in x",),
            alternative_model="y=a*x+b*x^2", changed_assumption="allow quadratic curvature",
            observable_name="y", observable_unit="m",
            incumbent_prediction=PredictionSummary("normal", (1.0, 0.1), 0.1, "m"),
            alternative_prediction=PredictionSummary("normal", (1.0, 0.2), 0.1, "m"),
            uncertainty_model="known Gaussian measurement noise",
            acceptance_predicate="held-out log score improves by preregistered margin",
            falsifier="held-out score fails threshold or curvature absent",
            heldout_prediction="quadratic model predicts larger curvature at x=2",
            capability_constraints=("offline deterministic simulator",),
            hard_constraints=("no instrument access", "no provider jobs"),
            violated_hard_constraints=(),
            training_sha256=digest("train"), validation_sha256=digest("validation"),
            heldout_sha256=digest("heldout"), simulator_version="synthetic-sim-1",
            model_version="model-set-1",
            independent_validation_method="clean-process replay with frozen hashes",
            budget_cap=self.cap, budget_used=self.used,
        )
        values.update(overrides)
        return ExperimentPlan(**values)

    def test_valid_offline_plan_passes_contract(self):
        self.plan().validate()

    def test_three_planners_pass_only_with_same_caps(self):
        plans = (
            self.plan("human"),
            self.plan("information_gain"),
            self.plan("ai_proposed"),
        )
        self.assertEqual(validate_matched_plans(plans), tuple(p.plan_id for p in plans))
        changed_cap = replace(self.cap, simulator_calls=99)
        with self.assertRaisesRegex(ValueError, "identical declared budget cap"):
            validate_matched_plans((
                plans[0], plans[1],
                self.plan("ai_proposed", budget_cap=changed_cap),
            ))

    def test_rejects_duplicate_splits_and_bad_hashes(self):
        with self.assertRaisesRegex(ValueError, "distinct"):
            self.plan(heldout_sha256=digest("train")).validate()
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            self.plan(training_sha256="not-a-hash").validate()

    def test_rejects_prediction_unit_mismatch(self):
        bad = PredictionSummary("normal", (1.0,), 0.1, "seconds")
        with self.assertRaisesRegex(ValueError, "match observable_unit"):
            self.plan(alternative_prediction=bad).validate()

    def test_rejects_invalid_budgets_and_overruns(self):
        bad_used = replace(self.used, wall_time_seconds=float("inf"))
        with self.assertRaisesRegex(ValueError, "finite"):
            self.plan(budget_used=bad_used).validate()
        over_cap = replace(self.used, simulator_calls=101)
        with self.assertRaisesRegex(ValueError, "exceeds"):
            self.plan(budget_used=over_cap).validate()
        bad_integer = replace(self.used, retries=True)
        with self.assertRaisesRegex(ValueError, "nonnegative integer"):
            self.plan(budget_used=bad_integer).validate()

    def test_rejects_hard_constraint_violations_and_live_modes(self):
        with self.assertRaisesRegex(ValueError, "hard feasibility"):
            self.plan(violated_hard_constraints=("paid provider job",)).validate()
        with self.assertRaisesRegex(ValueError, "OFFLINE_SIMULATION"):
            self.plan(execution_mode="REAL_QPU").validate()
        live = replace(self.used, provider_jobs=1)
        with self.assertRaisesRegex(ValueError, "zero provider"):
            self.plan(budget_used=live).validate()

    def test_energy_unknown_is_not_zero_or_comparable_to_a_measured_cap(self):
        measured_cap = replace(self.cap, energy_joules=1000.0)
        with self.assertRaisesRegex(ValueError, "measured for both"):
            self.plan(budget_cap=measured_cap).validate()

    def test_requires_three_distinct_planners(self):
        with self.assertRaisesRegex(ValueError, "requires human"):
            validate_matched_plans((self.plan("human"), self.plan("information_gain")))
        with self.assertRaisesRegex(ValueError, "include human"):
            validate_matched_plans((
                self.plan("human"), self.plan("information_gain"), self.plan("random")
            ))
        with self.assertRaisesRegex(ValueError, "unique"):
            validate_matched_plans((
                self.plan("human"), self.plan("information_gain"),
                self.plan("ai_proposed"),
                self.plan("ai_proposed", plan_id="other"),
            ))


if __name__ == "__main__":
    unittest.main()
