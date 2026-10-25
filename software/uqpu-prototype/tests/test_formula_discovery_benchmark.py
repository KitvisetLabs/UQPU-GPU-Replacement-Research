import hashlib
import unittest
from dataclasses import replace

from uqpu.formula_discovery_benchmark import (
    FormulaDiscoveryRun,
    audit_formula_discovery_comparison,
)


def digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def run(method, seed, **overrides):
    data = dict(
        method=method,
        seed=seed,
        dataset_sha256=digest("dataset-v1"),
        train_split_sha256=digest("train-rows"),
        heldout_split_sha256=digest("heldout-rows"),
        extrapolation_split_sha256=digest("extrapolation-rows"),
        split_disjointness_certificate_sha256=digest("split-certificate-v1"),
        candidate_sha256=digest(f"{method}-{seed}"),
        train_error=0.05,
        heldout_error=0.10 if method == "symbolic_search" else 0.08,
        extrapolation_error=0.20 if method == "symbolic_search" else 0.12,
        budget_seconds=10.0,
        wall_clock_seconds=9.0,
        host_cpu_seconds=8.0,
        peak_memory_bytes=1024,
        candidate_complexity=8,
        candidate_count=100,
        dimensional_consistency_passed=True,
        symmetry_passed=True,
        conservation_passed=True,
        causality_passed=True,
        energy_joules=None,
        token_count=200 if method == "transformer_generator" else None,
        model_sha256=digest("transformer-model-v1") if method == "transformer_generator" else None,
        training_gpu_hours=12.0 if method == "transformer_generator" else None,
        training_energy_joules=2400.0 if method == "transformer_generator" else None,
        model_parameters=1000 if method == "transformer_generator" else None,
        counterexample_count=1,
        failed_search_count=2,
        false_discovery=False,
        provenance="synthetic fixture with frozen split manifest",
    )
    data.update(overrides)
    return FormulaDiscoveryRun(**data)


def matched_runs():
    return [
        run(method, seed)
        for method in ("symbolic_search", "transformer_generator")
        for seed in (1, 2, 3)
    ]


class FormulaDiscoveryBenchmarkTests(unittest.TestCase):
    def test_matched_comparison_is_model_only_and_never_promotes_law(self):
        audit = audit_formula_discovery_comparison(matched_runs())
        self.assertEqual(audit.run_count, 6)
        self.assertEqual(audit.evidence_class, "MODEL_ONLY")
        self.assertFalse(audit.physical_law_claim_allowed)
        self.assertEqual(dict(audit.runs_per_method), {
            "symbolic_search": 3,
            "transformer_generator": 3,
        })
        self.assertEqual(audit.token_instrumented_runs, 3)
        self.assertEqual(audit.training_models_instrumented, 1)
        self.assertEqual(dict(audit.training_gpu_hours_by_method)["transformer_generator"], 12.0)
        self.assertIsNone(dict(audit.training_gpu_hours_by_method)["symbolic_search"])
        self.assertEqual(dict(audit.training_energy_joules_by_method)["transformer_generator"], 2400.0)

    def test_rejects_non_disjoint_split_hashes(self):
        rows = matched_runs()
        rows[0] = replace(rows[0], heldout_split_sha256=rows[0].train_split_sha256)
        with self.assertRaisesRegex(ValueError, "split hashes must be distinct"):
            audit_formula_discovery_comparison(rows)

    def test_rejects_different_split_manifest_across_methods(self):
        rows = matched_runs()
        rows[-1] = replace(rows[-1], split_disjointness_certificate_sha256=digest("different"))
        with self.assertRaisesRegex(ValueError, "same split_disjointness_certificate_sha256"):
            audit_formula_discovery_comparison(rows)

    def test_rejects_unmatched_budgets(self):
        rows = matched_runs()
        rows[-1] = replace(rows[-1], budget_seconds=20.0)
        with self.assertRaisesRegex(ValueError, "budgets are not matched"):
            audit_formula_discovery_comparison(rows)

    def test_rejects_nonfinite_error_metrics(self):
        for bad in (float("nan"), float("inf"), -1.0):
            rows = matched_runs()
            rows[0] = replace(rows[0], extrapolation_error=bad)
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                audit_formula_discovery_comparison(rows)

    def test_rejects_duplicate_seed_within_method(self):
        rows = matched_runs()
        rows[1] = replace(rows[1], seed=rows[0].seed)
        with self.assertRaisesRegex(ValueError, "duplicate seeds"):
            audit_formula_discovery_comparison(rows)

    def test_records_false_discoveries_and_constraint_failures(self):
        rows = matched_runs()
        rows[0] = replace(
            rows[0],
            false_discovery=True,
            dimensional_consistency_passed=False,
            failed_search_count=4,
        )
        audit = audit_formula_discovery_comparison(rows)
        self.assertEqual(audit.false_discovery_runs, 1)
        self.assertEqual(audit.failed_search_count, 14)
        self.assertEqual(audit.counterexample_count, 6)
        self.assertEqual(dict(audit.constraint_failure_counts)["dimensional_consistency"], 1)
        self.assertFalse(audit.physical_law_claim_allowed)

    def test_rejects_run_that_exceeds_budget(self):
        rows = matched_runs()
        rows[0] = replace(rows[0], wall_clock_seconds=10.1)
        with self.assertRaisesRegex(ValueError, "exceeds the declared run budget"):
            audit_formula_discovery_comparison(rows)

    def test_rejects_unknown_method(self):
        rows = matched_runs()
        rows[0] = replace(rows[0], method="magic_law_generator")
        with self.assertRaisesRegex(ValueError, "unsupported discovery method"):
            audit_formula_discovery_comparison(rows)

    def test_rejects_inconsistent_training_cost_for_same_model_hash(self):
        rows = matched_runs()
        rows[-1] = replace(rows[-1], training_gpu_hours=13.0)
        with self.assertRaisesRegex(ValueError, "training resource metadata differs"):
            audit_formula_discovery_comparison(rows)

    def test_training_resources_require_a_model_hash(self):
        rows = matched_runs()
        rows[0] = replace(rows[0], training_gpu_hours=1.0)
        with self.assertRaisesRegex(ValueError, "model_sha256 is required"):
            audit_formula_discovery_comparison(rows)

    def test_rejects_too_few_seeds(self):
        rows = matched_runs()[:5]
        with self.assertRaisesRegex(ValueError, "fewer than 3 seeds"):
            audit_formula_discovery_comparison(rows)


if __name__ == "__main__":
    unittest.main()
