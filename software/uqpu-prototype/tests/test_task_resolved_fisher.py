import unittest

from uqpu.task_resolved_fisher import FeatureInformation, TaskResolvedFisherRecord


class TaskResolvedFisherTests(unittest.TestCase):
    def _record(self, **overrides):
        data = dict(
            workload_id="forecast-five-step",
            model_id="open-spin-model-v1",
            task_score_basis_id="orthonormal-score-basis-v1",
            split_sha256="a" * 64,
            provenance="arXiv:2609.29570; local contract fixture only",
            evidence_level="MODEL_ONLY",
            matrix_semantics="ANALYTIC",
            qfi_matrix=((3.0, 0.0), (0.0, 2.0)),
            complete_record_fi_matrix=((2.0, 0.0), (0.0, 1.5)),
            retained_features=(
                FeatureInformation(1, ((1.0, 0.0), (0.0, 0.5)), 16),
                FeatureInformation(2, ((1.5, 0.0), (0.0, 1.0)), 24),
            ),
            shots_per_history=100,
            history_count=20,
            measurement_setting_count=2,
            raw_record_bytes_per_history=64,
            evaluated_task_count=100,
            accepted_task_count=90,
            quality_metric="NRMSE",
            quality_value=0.08,
            quality_threshold=0.10,
            quality_direction="LOWER_IS_BETTER",
            cost_scope="END_TO_END_RUN",
            total_run_cost_usd=2.0,
            energy_scope="END_TO_END_RUN",
            total_run_energy_joules=100.0,
            wall_clock_seconds=5.0,
            host_compute_seconds=1.0,
        )
        data.update(overrides)
        return TaskResolvedFisherRecord(**data)

    def test_comparable_analytic_hierarchy_and_ratios(self):
        record = self._record()
        record.validate()
        self.assertTrue(record.quality_pass)
        self.assertAlmostEqual(record.information_retention_ratio(2), 2.5 / 3.5)
        self.assertAlmostEqual(record.record_byte_reduction_ratio(2), 64.0 / 24.0)
        self.assertAlmostEqual(record.end_to_end_cost_per_accepted_task_usd, 2.0 / 90.0)
        self.assertAlmostEqual(record.end_to_end_energy_per_accepted_task_joules, 100.0 / 90.0)

    def test_unknown_energy_and_cost_remain_unknown_not_zero(self):
        record = self._record(
            total_run_cost_usd=None,
            total_run_energy_joules=None,
            cost_scope="UNKNOWN",
            energy_scope="UNKNOWN",
        )
        self.assertIsNone(record.end_to_end_cost_per_accepted_task_usd)
        self.assertIsNone(record.end_to_end_energy_per_accepted_task_joules)

    def test_device_only_cost_cannot_be_reported_as_end_to_end(self):
        record = self._record(cost_scope="DEVICE_ONLY")
        self.assertIsNone(record.end_to_end_cost_per_accepted_task_usd)

    def test_analytic_information_hierarchy_failure_is_rejected(self):
        record = self._record(
            qfi_matrix=((1.0, 0.0), (0.0, 1.0)),
            complete_record_fi_matrix=((2.0, 0.0), (0.0, 1.0)),
        )
        with self.assertRaisesRegex(ValueError, "analytic information hierarchy failed"):
            record.validate()

    def test_estimated_hierarchy_violation_is_flagged_not_silently_accepted(self):
        record = self._record(
            matrix_semantics="ESTIMATED",
            qfi_matrix=((1.0, 0.0), (0.0, 1.0)),
            complete_record_fi_matrix=((2.0, 0.0), (0.0, 1.0)),
        )
        warnings = record.diagnostics
        self.assertTrue(any("ESTIMATED-MATRIX WARNING" in item for item in warnings))

    def test_non_psd_matrix_is_rejected(self):
        record = self._record(qfi_matrix=((1.0, 2.0), (2.0, 1.0)))
        with self.assertRaisesRegex(ValueError, "positive semidefinite"):
            record.validate()

    def test_duplicate_or_unsorted_feature_orders_are_rejected(self):
        record = self._record(
            retained_features=(
                FeatureInformation(2, ((1.5, 0.0), (0.0, 1.0)), 24),
                FeatureInformation(2, ((1.5, 0.0), (0.0, 1.0)), 24),
            )
        )
        with self.assertRaisesRegex(ValueError, "strictly increasing"):
            record.validate()

    def test_real_qpu_requires_provider_target_provenance(self):
        record = self._record(evidence_level="REAL_QPU")
        with self.assertRaisesRegex(ValueError, "exact provider and target"):
            record.validate()

    def test_zero_accepted_tasks_has_no_per_accepted_task_cost(self):
        record = self._record(accepted_task_count=0)
        self.assertIsNone(record.end_to_end_cost_per_accepted_task_usd)
        self.assertIsNone(record.end_to_end_energy_per_accepted_task_joules)


if __name__ == "__main__":
    unittest.main()
