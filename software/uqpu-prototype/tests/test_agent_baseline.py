import unittest

from uqpu.agent_baseline import KernelRunContract, KernelRunMeasurement, compare_goal_only_and_specialized

SHAPES = ("shape-a", "shape-b")


def contract(**overrides):
    fields = dict(
        model_id="agent-model", model_version="2026-10-27-build-1", reasoning_effort="high",
        target_id="nvidia-b200-target-01", driver_version="580.105.08", runtime_version="cuda-13.0",
        operator_id="attention-forward", scope_id="whole-operator-v1", workload_shapes=SHAPES,
        budget_seconds=3600.0, precision="fp16-accum-fp32",
        correctness_protocol_id="reference-tolerance-v1", timing_protocol_id="cold-l2-cupti-v1",
        reference_code_access=False, kernel_specific_knowledge=False,
        kernel_specific_evaluator=False, predefined_search_workflow=False,
    )
    fields.update(overrides)
    return KernelRunContract(**fields)


def measurement(samples_a=(1.0, 1.01, 0.99), samples_b=(2.0, 2.01, 1.99), **overrides):
    fields = dict(
        latency_samples_by_shape=(("shape-a", samples_a), ("shape-b", samples_b)),
        correctness_passed=True, independent_verifier_passed=True, sanitizer_passed=True,
    )
    fields.update(overrides)
    return KernelRunMeasurement(**fields)


class AgentBaselineTests(unittest.TestCase):
    def test_scope_matched_pair_returns_per_shape_and_geomean_speedups(self):
        specialist = contract(kernel_specific_knowledge=True, kernel_specific_evaluator=True,
                              predefined_search_workflow=True)
        result = compare_goal_only_and_specialized(
            contract(), specialist,
            measurement((1.0, 1.2, 1.1), (2.0, 2.2, 2.1)),
            measurement((0.8, 0.9, 0.85), (1.0, 1.1, 1.05)),
        )
        self.assertTrue(result.accepted)
        self.assertAlmostEqual(dict(result.goal_only_medians_by_shape)["shape-a"], 1.1)
        self.assertAlmostEqual(dict(result.specialized_medians_by_shape)["shape-b"], 1.05)
        self.assertAlmostEqual(dict(result.specialized_speedups_by_shape)["shape-a"], 1.1 / 0.85)
        self.assertAlmostEqual(result.specialized_geomean_speedup_over_goal_only,
                               ((1.1 / 0.85) * (2.1 / 1.05)) ** 0.5)

    def test_rejects_model_version_mismatch(self):
        result = compare_goal_only_and_specialized(contract(), contract(model_version="other"), measurement(), measurement())
        self.assertIn("mismatch:model_version", result.rejection_reasons)
        self.assertIsNone(result.specialized_geomean_speedup_over_goal_only)

    def test_rejects_scope_or_shape_mismatch(self):
        result = compare_goal_only_and_specialized(contract(), contract(scope_id="single", workload_shapes=("shape-a",)), measurement(), measurement())
        self.assertIn("mismatch:scope_id", result.rejection_reasons)
        self.assertIn("mismatch:workload_shapes", result.rejection_reasons)

    def test_rejects_budget_target_and_evaluator_mismatch(self):
        result = compare_goal_only_and_specialized(contract(), contract(budget_seconds=7200, target_id="other", correctness_protocol_id="other"), measurement(), measurement())
        self.assertIn("mismatch:budget_seconds", result.rejection_reasons)
        self.assertIn("mismatch:target_id", result.rejection_reasons)
        self.assertIn("mismatch:correctness_protocol_id", result.rejection_reasons)

    def test_rejects_missing_per_shape_measurements(self):
        bad = measurement(latency_samples_by_shape=(("shape-a", (1.0, 1.1, 1.2)),))
        result = compare_goal_only_and_specialized(contract(), contract(), bad, measurement())
        self.assertIn("goal_only_shape_coverage_mismatch", result.rejection_reasons)

    def test_rejects_reference_code_leakage_into_goal_only_arm(self):
        result = compare_goal_only_and_specialized(contract(reference_code_access=True), contract(reference_code_access=True), measurement(), measurement())
        self.assertIn("goal_only_reference_code_access_not_allowed", result.rejection_reasons)

    def test_rejects_specialized_mechanisms_in_goal_only_arm(self):
        goal = contract(kernel_specific_knowledge=True, kernel_specific_evaluator=True, predefined_search_workflow=True)
        result = compare_goal_only_and_specialized(goal, goal, measurement(), measurement())
        self.assertIn("goal_only_kernel_specific_knowledge_not_allowed", result.rejection_reasons)
        self.assertIn("goal_only_kernel_specific_evaluator_not_allowed", result.rejection_reasons)
        self.assertIn("goal_only_predefined_search_workflow_not_allowed", result.rejection_reasons)

    def test_rejects_correctness_verification_or_sanitizer_failure(self):
        result = compare_goal_only_and_specialized(
            contract(), contract(), measurement(correctness_passed=False),
            measurement(independent_verifier_passed=False, sanitizer_passed=False))
        self.assertIn("goal_only_correctness_failed", result.rejection_reasons)
        self.assertIn("specialized_independent_verifier_failed", result.rejection_reasons)
        self.assertIn("specialized_sanitizer_failed", result.rejection_reasons)
        self.assertIsNone(result.specialized_geomean_speedup_over_goal_only)

    def test_contract_rejects_invalid_budget_shape_and_boolean(self):
        with self.assertRaisesRegex(ValueError, "strictly positive"):
            contract(budget_seconds=0)
        with self.assertRaisesRegex(ValueError, "must not be empty"):
            contract(workload_shapes=())
        with self.assertRaisesRegex(ValueError, "must be boolean"):
            contract(reference_code_access=1)

    def test_measurement_rejects_invalid_or_too_few_samples(self):
        with self.assertRaisesRegex(ValueError, "at least three"):
            measurement(latency_samples_by_shape=(("shape-a", (1.0, 2.0)), ("shape-b", (2.0, 3.0, 4.0))))
        with self.assertRaisesRegex(ValueError, "strictly positive"):
            measurement(samples_a=(1.0, 0.0, 2.0))
        with self.assertRaisesRegex(ValueError, "must be boolean"):
            measurement(correctness_passed=1)


if __name__ == "__main__":
    unittest.main()
