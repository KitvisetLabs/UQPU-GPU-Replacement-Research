import unittest

from uqpu.quality_adjusted_cloud_cost import (
    TaskShotPricing,
    TimePricing,
    best_task_shot_batch,
    task_shot_quality_adjusted_cost,
    time_priced_quality_adjusted_cost,
)


class QualityAdjustedCloudCostTests(unittest.TestCase):
    def test_task_shot_cost_counts_fixed_and_variable_fees(self):
        pricing = TaskShotPricing(task_fee=0.30, shot_fee=0.001)
        row = task_shot_quality_adjusted_cost(0.5, 2, pricing)
        self.assertAlmostEqual(row.success_probability_per_submission, 0.75)
        self.assertAlmostEqual(row.submission_cost, 0.302)
        self.assertAlmostEqual(row.expected_cost_per_accepted_solution, 0.302 / 0.75)

    def test_batch_optimizer_can_amortize_task_fee(self):
        pricing = TaskShotPricing(task_fee=0.30, shot_fee=0.000425)
        row = best_task_shot_batch(
            0.98095703125,
            pricing,
            maximum_shots=20,
            minimum_submission_success=0.999,
        )
        self.assertEqual(row.shots, 2)
        self.assertGreaterEqual(row.success_probability_per_submission, 0.999)

    def test_provider_minimum_shots_is_enforced(self):
        pricing = TaskShotPricing(task_fee=0.30, shot_fee=0.08, minimum_shots=2500)
        with self.assertRaises(ValueError):
            task_shot_quality_adjusted_cost(0.5, 2499, pricing)
        row = task_shot_quality_adjusted_cost(0.5, 2500, pricing)
        self.assertEqual(row.shots, 2500)

    def test_time_priced_cost_requires_measured_billable_time_input(self):
        pricing = TimePricing(price_per_second=2.0)
        self.assertAlmostEqual(time_priced_quality_adjusted_cost(0.5, 3.0, pricing), 12.0)

    def test_invalid_probability_rejected(self):
        with self.assertRaises(ValueError):
            best_task_shot_batch(0.0, TaskShotPricing(0.3, 0.001), maximum_shots=10)


if __name__ == "__main__":
    unittest.main()
