import hashlib
import unittest
from dataclasses import replace

from uqpu.equation_discovery_comparison import DiscoveryBudget, DiscoveryRun
from uqpu.split_disjointness import (
    validate_comparison_manifest,
    validate_split_manifest,
)


def _digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _manifest():
    return {
        "schema": "uqpu-split-manifest-v1",
        "dataset_sha256": _digest("dataset-v1"),
        "holdout_unit": "LAW_FAMILY",
        "splits": {
            "train": [
                {"record_id": "train-1", "group_id": "law-a", "record_sha256": _digest("record-a")},
                {"record_id": "train-2", "group_id": "law-b", "record_sha256": _digest("record-b")},
            ],
            "validation": [
                {"record_id": "validation-1", "group_id": "law-c", "record_sha256": _digest("record-c")},
            ],
            "test": [
                {"record_id": "test-1", "group_id": "law-d", "record_sha256": _digest("record-d")},
                {"record_id": "test-2", "group_id": "law-e", "record_sha256": _digest("record-e")},
            ],
        },
    }


def _comparison_runs(manifest, certificate):
    budget = DiscoveryBudget(
        max_wall_clock_seconds=60.0,
        max_cpu_core_seconds=120.0,
        max_peak_memory_bytes=1_000_000,
        max_accelerator_seconds=0.0,
        max_candidate_evaluations=100,
        max_generated_tokens=1_000,
    )
    records = []
    for method in ("one-shot", "progressive"):
        for seed in range(30):
            records.append(DiscoveryRun(
                method_id=method,
                method_revision_sha256=_digest(method + "-revision"),
                seed=seed,
                dataset_sha256=manifest["dataset_sha256"],
                train_split_sha256=certificate["split_sha256"]["train"],
                validation_split_sha256=certificate["split_sha256"]["validation"],
                test_split_sha256=certificate["split_sha256"]["test"],
                preprocessing_sha256=_digest("preprocessing-v1"),
                grammar_sha256=_digest("grammar-v1"),
                unit_schema_sha256=_digest("units-v1"),
                acceptance_rule_sha256=_digest("acceptance-v1"),
                split_policy_sha256=_digest("group-disjoint-law-family-v1"),
                heldout_group_manifest_sha256=certificate["heldout_group_manifest_sha256"],
                holdout_unit="LAW_FAMILY",
                heldout_group_count=certificate["test_group_count"],
                budget=budget,
                wall_clock_seconds=2.0,
                cpu_core_seconds=3.0,
                peak_memory_bytes=100_000,
                accelerator_seconds=0.0,
                candidate_evaluations=10,
                generated_tokens=10,
                accepted=True,
                heldout_error=0.1,
            ))
    return records


class SplitDisjointnessTests(unittest.TestCase):
    def test_valid_manifest_returns_reproducible_certificate(self):
        manifest = _manifest()
        certificate = validate_split_manifest(manifest, expected_group_count=2)
        reordered = _manifest()
        reordered["splits"]["train"].reverse()
        reordered["splits"]["test"].reverse()
        self.assertEqual(certificate["status"], "PASS")
        self.assertTrue(certificate["record_level_disjoint"])
        self.assertTrue(certificate["group_level_disjoint"])
        self.assertEqual(certificate["record_counts"], {"train": 2, "validation": 1, "test": 2})
        self.assertEqual(certificate["canonical_manifest_sha256"],
                         validate_split_manifest(reordered)["canonical_manifest_sha256"])

    def test_cross_split_record_id_overlap_is_rejected(self):
        manifest = _manifest()
        manifest["splits"]["test"][0]["record_id"] = "train-1"
        with self.assertRaisesRegex(ValueError, "record_id"):
            validate_split_manifest(manifest)

    def test_duplicate_content_hash_is_rejected(self):
        manifest = _manifest()
        manifest["splits"]["test"][0]["record_sha256"] = manifest["splits"]["train"][0]["record_sha256"]
        with self.assertRaisesRegex(ValueError, "record_sha256"):
            validate_split_manifest(manifest)

    def test_group_leakage_across_splits_is_rejected(self):
        manifest = _manifest()
        manifest["splits"]["test"][0]["group_id"] = "law-a"
        with self.assertRaisesRegex(ValueError, "leaks across splits"):
            validate_split_manifest(manifest)

    def test_empty_split_is_rejected(self):
        manifest = _manifest()
        manifest["splits"]["validation"] = []
        with self.assertRaisesRegex(ValueError, "nonempty list"):
            validate_split_manifest(manifest)

    def test_bad_hash_and_wrong_group_count_are_rejected(self):
        manifest = _manifest()
        manifest["dataset_sha256"] = "not-a-hash"
        with self.assertRaisesRegex(ValueError, "dataset_sha256"):
            validate_split_manifest(manifest)
        with self.assertRaisesRegex(ValueError, "group count"):
            validate_split_manifest(_manifest(), expected_group_count=3)

    def test_comparison_is_bound_to_actual_manifest_content(self):
        manifest = _manifest()
        certificate = validate_split_manifest(manifest)
        result = validate_comparison_manifest(_comparison_runs(manifest, certificate), manifest)
        self.assertTrue(result["manifest_content_verified"])
        self.assertEqual(result["method_ids"], ["one-shot", "progressive"])
        self.assertEqual(result["evidence_class"], "MANIFEST_LEVEL_PARTITION_CERTIFICATE_ONLY")

    def test_comparison_rejects_split_hash_that_does_not_match_manifest(self):
        manifest = _manifest()
        certificate = validate_split_manifest(manifest)
        runs = _comparison_runs(manifest, certificate)
        runs[0] = replace(runs[0], test_split_sha256=_digest("tampered-test-split"))
        with self.assertRaisesRegex(ValueError, "test_split_sha256"):
            validate_comparison_manifest(runs, manifest)


if __name__ == "__main__":
    unittest.main()
