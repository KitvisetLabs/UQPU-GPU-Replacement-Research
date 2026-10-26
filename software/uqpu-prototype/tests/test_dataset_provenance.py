import copy
import hashlib
import unittest

from uqpu.dataset_provenance import (
    build_dataset_provenance,
    validate_benchmark_bundle,
    validate_dataset_provenance,
)
from uqpu.split_disjointness import build_split_manifest


def _digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _raw_records():
    return [
        {"record_id": "r1", "group_id": "law-a", "split": "train", "payload": {"x": 1.0, "y": 2.0}},
        {"record_id": "r2", "group_id": "law-b", "split": "validation", "payload": {"x": 2.0, "y": 4.0}},
        {"record_id": "r3", "group_id": "law-c", "split": "test", "payload": {"x": 3.0, "y": 6.0}},
    ]


def _split_manifest(records=None):
    return build_split_manifest(records or _raw_records(), holdout_unit="LAW_FAMILY")


def _provenance(split_manifest, **overrides):
    args = {
        "source_url": "https://example.org/benchmark/archive",
        "source_revision": "0123456789abcdef0123456789abcdef01234567",
        "license_id": "CC-BY-4.0",
        "acquired_date": "2026-10-26",
        "raw_files": [{"path": "data/raw.csv", "sha256": _digest("raw bytes")}],
        "split_manifest": split_manifest,
        "preprocessing_sha256": _digest("preprocessing-v1"),
        "schema_sha256": _digest("schema-v1"),
        "inclusion_policy_sha256": _digest("include-v1"),
        "exclusion_policy_sha256": _digest("exclude-v1"),
        "group_policy_sha256": _digest("group-by-law-v1"),
    }
    args.update(overrides)
    return build_dataset_provenance(**args)


class DatasetProvenanceTests(unittest.TestCase):
    def test_bundle_passes_with_raw_records_and_matching_provenance(self):
        records = _raw_records()
        split_manifest = _split_manifest(records)
        provenance = _provenance(split_manifest)
        certificate = validate_benchmark_bundle(
            split_manifest=split_manifest,
            raw_records=records,
            provenance_manifest=provenance,
        )
        self.assertEqual(certificate["status"], "PASS")
        self.assertTrue(certificate["raw_record_binding_verified"])
        self.assertTrue(certificate["split_disjointness_verified"])
        self.assertFalse(certificate["source_authenticated"])
        self.assertFalse(certificate["scientific_validity_established"])
        self.assertEqual(certificate["row_count"], 3)

    def test_raw_file_order_is_canonical(self):
        split_manifest = _split_manifest()
        files = [
            {"path": "b.csv", "sha256": _digest("b")},
            {"path": "a.csv", "sha256": _digest("a")},
        ]
        first = _provenance(split_manifest, raw_files=files)
        second = _provenance(split_manifest, raw_files=list(reversed(files)))
        self.assertEqual(first, second)

    def test_tampered_manifest_fields_fail_digest_check(self):
        split_manifest = _split_manifest()
        manifest = _provenance(split_manifest)
        changed = copy.deepcopy(manifest)
        changed["license_id"] = "CC0-1.0"
        with self.assertRaisesRegex(ValueError, "provenance_sha256"):
            validate_dataset_provenance(changed, split_manifest)

    def test_provenance_cannot_be_reused_for_another_dataset(self):
        first = _split_manifest()
        manifest = _provenance(first)
        other_records = _raw_records()
        other_records[0]["payload"]["y"] = 999.0
        other = _split_manifest(other_records)
        with self.assertRaisesRegex(ValueError, "dataset digest"):
            validate_dataset_provenance(manifest, other)

    def test_mutable_branch_alias_is_rejected(self):
        split_manifest = _split_manifest()
        with self.assertRaisesRegex(ValueError, "mutable branch alias"):
            _provenance(split_manifest, source_revision="main")

    def test_missing_license_is_rejected(self):
        split_manifest = _split_manifest()
        with self.assertRaisesRegex(ValueError, "license_id"):
            _provenance(split_manifest, license_id=" ")

    def test_non_https_source_is_rejected(self):
        split_manifest = _split_manifest()
        with self.assertRaisesRegex(ValueError, "HTTPS"):
            _provenance(split_manifest, source_url="http://example.org/data")

    def test_duplicate_or_unsafe_raw_file_paths_are_rejected(self):
        split_manifest = _split_manifest()
        duplicated = [
            {"path": "data.csv", "sha256": _digest("a")},
            {"path": "data.csv", "sha256": _digest("b")},
        ]
        with self.assertRaisesRegex(ValueError, "duplicated"):
            _provenance(split_manifest, raw_files=duplicated)
        unsafe = [{"path": "../data.csv", "sha256": _digest("a")}]
        with self.assertRaisesRegex(ValueError, "relative POSIX"):
            _provenance(split_manifest, raw_files=unsafe)

    def test_invalid_raw_file_digest_is_rejected(self):
        split_manifest = _split_manifest()
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            _provenance(split_manifest, raw_files=[{"path": "data.csv", "sha256": "bad"}])

    def test_changed_raw_records_fail_bundle_preflight(self):
        records = _raw_records()
        split_manifest = _split_manifest(records)
        provenance = _provenance(split_manifest)
        changed = copy.deepcopy(records)
        changed[0]["payload"]["y"] = 7.0
        with self.assertRaisesRegex(ValueError, "does not match canonical raw records"):
            validate_benchmark_bundle(
                split_manifest=split_manifest,
                raw_records=changed,
                provenance_manifest=provenance,
            )


if __name__ == "__main__":
    unittest.main()
