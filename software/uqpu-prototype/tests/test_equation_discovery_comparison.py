import hashlib
import unittest
from dataclasses import replace

from uqpu.equation_discovery_comparison import (
    DiscoveryBudget,
    DiscoveryRun,
    compare_methods,
    validate_matched_comparison,
)


def _digest(label):
    return hashlib.sha256(label.encode("utf-8")).hexdigest()


class EquationDiscoveryComparisonTests(unittest.TestCase):
    def _runs(self, seed_count=30):
        budget = DiscoveryBudget(
            max_wall_clock_seconds=60.0,
            max_cpu_core_seconds=120.0,
            max_peak_memory_bytes=1_000_000_000,
            max_accelerator_seconds=0.0,
            max_candidate_evaluations=1_000,
            max_generated_tokens=50_000,
            max_total_cost_usd=1.0,
        )
        records = []
        for method in ("one-shot", "progressive"):
            for seed in range(seed_count):
                accepted = (seed % 2 == 0) if method == "one-shot" else (seed % 3 != 0)
                records.append(
                    DiscoveryRun(
                        method_id=method,
                        method_revision_sha256=_digest(method + "-revision"),
                        method_config_sha256=_digest(method + "-config-v1"),
                        runtime_environment_sha256=_digest(method + "-environment-v1"),
                        seed=seed,
                        dataset_sha256=_digest("dataset-v1"),
                        dataset_provenance_sha256=_digest("dataset-source-license-v1"),
                        train_split_sha256=_digest("train-law-families-v1"),
                        validation_split_sha256=_digest("validation-law-families-v1"),
                        test_split_sha256=_digest("heldout-scale-law-families-v1"),
                        preprocessing_sha256=_digest("preprocess-v1"),
                        grammar_sha256=_digest("grammar-v1"),
                        unit_schema_sha256=_digest("units-v1"),
                        acceptance_rule_sha256=_digest("acceptance-v1"),
                        split_policy_sha256=_digest("group-disjoint-law-family-v1"),
                        heldout_group_manifest_sha256=_digest("heldout-law-family-manifest-v1"),
                        holdout_unit="LAW_FAMILY",
                        heldout_group_count=6,
                        budget=budget,
                        wall_clock_seconds=5.0 + seed / 10.0,
                        cpu_core_seconds=10.0,
                        peak_memory_bytes=500_000_000,
                        accelerator_seconds=0.0,
                        candidate_evaluations=200 + seed,
                        generated_tokens=10_000,
                        accepted=accepted,
                        heldout_error=0.1 + seed / 1000.0,
                        constraint_violations=0 if accepted else 1,
                        counterexamples=0,
                        false_discoveries=0,
                        total_cost_usd=0.02,
                        cost_basis_id="same-host-cost-model-v1",
                    )
                )
        return records

    def test_matched_30_seed_comparison_returns_descriptive_summary(self):
        summary = compare_methods(self._runs())
        self.assertEqual(summary["preregistered_seed_count"], 30)
        self.assertEqual(set(summary["method_ids"]), {"one-shot", "progressive"})
        self.assertEqual(summary["methods"]["one-shot"]["accepted_candidates"], 15)
        self.assertEqual(summary["methods"]["progressive"]["accepted_candidates"], 20)
        self.assertAlmostEqual(
            summary["methods"]["progressive"]["cost_per_accepted_candidate_usd"],
            0.60 / 20,
        )
        self.assertIn("does not establish a physical law", summary["interpretation"])

    def test_uncertainty_and_paired_acceptance_counts_are_reported(self):
        summary = compare_methods(self._runs())
        self.assertEqual(summary["schema"], "uqpu-equation-discovery-matched-comparison-v4")
        self.assertEqual(summary["shared_dataset"]["dataset_provenance_sha256"], _digest("dataset-source-license-v1"))
        self.assertEqual(summary["methods"]["one-shot"]["provenance"]["method_config_sha256"], _digest("one-shot-config-v1"))
        self.assertEqual(summary["shared_holdout"]["unit"], "LAW_FAMILY")
        self.assertEqual(summary["shared_holdout"]["group_count"], 6)
        self.assertFalse(summary["shared_holdout"]["manifest_content_verified_by_this_module"])
        for method in summary["method_ids"]:
            values = summary["methods"][method]
            low, high = values["acceptance_rate_95pct_wilson_ci"]
            self.assertLessEqual(low, values["acceptance_rate"])
            self.assertGreaterEqual(high, values["acceptance_rate"])
            self.assertLess(low, high)

        pair = summary["pairwise_acceptance"]["one-shot__vs__progressive"]
        self.assertEqual(pair["shared_seed_count"], 30)
        self.assertEqual(pair["both_accepted"], 10)
        self.assertEqual(pair["left_only_accepted"], 5)
        self.assertEqual(pair["right_only_accepted"], 10)
        self.assertEqual(pair["neither_accepted"], 5)
        self.assertAlmostEqual(pair["acceptance_rate_difference_left_minus_right"], -1 / 6)
        self.assertIn("no p-values or winner", summary["interpretation"])

    def test_different_dataset_or_split_is_rejected(self):
        records = self._runs()
        records[-1] = replace(records[-1], test_split_sha256=_digest("different-test-split"))
        with self.assertRaises(ValueError):
            validate_matched_comparison(records)

    def test_unequal_budgets_are_rejected(self):
        records = self._runs()
        records[-1] = replace(
            records[-1],
            budget=replace(records[-1].budget, max_generated_tokens=49_999),
        )
        with self.assertRaises(ValueError):
            validate_matched_comparison(records)

    def test_seed_sets_must_match_and_have_at_least_30_seeds(self):
        records = [r for r in self._runs() if not (r.method_id == "progressive" and r.seed == 29)]
        with self.assertRaises(ValueError):
            validate_matched_comparison(records)
        with self.assertRaises(ValueError):
            validate_matched_comparison(self._runs(seed_count=29))

    def test_duplicate_method_seed_is_rejected(self):
        records = self._runs()
        records.append(records[0])
        with self.assertRaises(ValueError):
            validate_matched_comparison(records)

    def test_resource_overrun_is_rejected(self):
        records = self._runs()
        records[0] = replace(records[0], wall_clock_seconds=61.0)
        with self.assertRaises(ValueError):
            validate_matched_comparison(records)

    def test_accepted_candidate_cannot_have_counterexamples_or_violations(self):
        records = self._runs()
        records[0] = replace(records[0], counterexamples=1)
        with self.assertRaises(ValueError):
            validate_matched_comparison(records)

    def test_mixed_cost_bases_are_rejected(self):
        records = self._runs()
        records[-1] = replace(records[-1], cost_basis_id="different-price-boundary")
        with self.assertRaises(ValueError):
            validate_matched_comparison(records)

    def test_random_point_only_holdout_is_rejected(self):
        records = self._runs()
        records[0] = replace(records[0], holdout_unit="RANDOM_POINT")
        with self.assertRaisesRegex(ValueError, "group-disjoint"):
            validate_matched_comparison(records)

    def test_holdout_manifest_and_policy_must_match(self):
        for field in ("heldout_group_manifest_sha256", "split_policy_sha256"):
            records = self._runs()
            records[-1] = replace(records[-1], **{field: _digest("different-" + field)})
            with self.assertRaises(ValueError):
                validate_matched_comparison(records)

    def test_holdout_unit_and_group_count_must_match(self):
        records = self._runs()
        records[-1] = replace(records[-1], holdout_unit="SCALE")
        with self.assertRaisesRegex(ValueError, "grouped holdout"):
            validate_matched_comparison(records)
        records = self._runs()
        records[-1] = replace(records[-1], heldout_group_count=5)
        with self.assertRaisesRegex(ValueError, "grouped holdout"):
            validate_matched_comparison(records)

    def test_heldout_group_count_must_be_positive(self):
        records = self._runs()
        records[0] = replace(records[0], heldout_group_count=0)
        with self.assertRaisesRegex(ValueError, "heldout_group_count"):
            validate_matched_comparison(records)

    def test_invalid_hash_is_rejected(self):
        for field in ("dataset_sha256", "dataset_provenance_sha256", "method_config_sha256", "runtime_environment_sha256"):
            records = self._runs()
            records[0] = replace(records[0], **{field: "not-a-hash"})
            with self.assertRaises(ValueError):
                validate_matched_comparison(records)

    def test_method_revision_config_and_environment_are_fixed_across_seeds(self):
        for field in ("method_revision_sha256", "method_config_sha256", "runtime_environment_sha256"):
            records = self._runs()
            records[1] = replace(records[1], **{field: _digest("drifted-" + field)})
            with self.assertRaisesRegex(ValueError, field + " must remain constant"):
                validate_matched_comparison(records)

    def test_dataset_source_provenance_must_match(self):
        records = self._runs()
        records[-1] = replace(records[-1], dataset_provenance_sha256=_digest("different-license-or-source"))
        with self.assertRaisesRegex(ValueError, "dataset_provenance_sha256"):
            validate_matched_comparison(records)


if __name__ == "__main__":
    unittest.main()
