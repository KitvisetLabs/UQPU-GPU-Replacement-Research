import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
MANIFEST_PATH = (
    ROOT
    / "research_lanes"
    / "A_quantum_programming_runtime"
    / "SPARSE_STATEPREP_TOFFOLI_ASSET_PROVENANCE_V1.json"
)


def _reject_duplicate_json_keys(pairs):
    """Reject ambiguous JSON objects instead of silently keeping the last key."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key!r}")
        result[key] = value
    return result


class SparseStateprepAssetProvenanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads(
            MANIFEST_PATH.read_text(encoding="utf-8"),
            object_pairs_hook=_reject_duplicate_json_keys,
        )

    def test_duplicate_json_key_guard_rejects_ambiguous_objects(self):
        with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
            json.loads(
                '{"evidence_class": "SOURCE_METADATA_ONLY", '
                '"evidence_class": "REPRODUCED"}',
                object_pairs_hook=_reject_duplicate_json_keys,
            )

    def test_source_record_and_asset_are_pinned(self):
        self.assertEqual(
            self.manifest["schema"],
            "uqpu-sparse-stateprep-toffoli-asset-provenance-v1",
        )
        source = self.manifest["source"]
        self.assertEqual(source["paper_doi"], "10.22331/q-2026-09-10-2208")
        self.assertEqual(source["software_record_doi"], "10.5281/zenodo.18234600")
        asset = self.manifest["asset"]
        self.assertEqual(
            asset["filename"],
            "Code_for_Sparse_quantum_state_preparation_with_improved_Toffoli_cost.zip",
        )
        self.assertEqual(len(asset["publisher_reported_md5"]), 32)
        self.assertIsNone(asset["local_sha256"])

    def test_manifest_does_not_claim_download_or_reproduction(self):
        state = self.manifest["provenance_state"]
        for key in (
            "asset_downloaded_in_this_cycle",
            "publisher_md5_recomputed_locally",
            "local_sha256_computed",
            "archive_paths_audited",
            "dependency_lockfile_audited",
            "upstream_python_tests_run",
            "upstream_rust_tests_run",
            "independent_small_instance_reproduction",
        ):
            with self.subTest(key=key):
                self.assertFalse(state[key])
        self.assertEqual(state["evidence_class"], "SOURCE_METADATA_ONLY")
        self.assertEqual(state["project_reproduction"], "NOT_PERFORMED")
        self.assertIn("failed", self.manifest["retrieval_note"].lower())

    def test_license_and_dependency_security_gate_are_preserved(self):
        security = self.manifest["licensing_and_security"]
        self.assertEqual(security["source_code_license"], "Apache-2.0")
        self.assertEqual(security["figures_license"], "CC-BY-4.0")
        self.assertIn("nbconvert", security["upstream_dependency_warning"])
        self.assertIn("7.16.6", security["upstream_dependency_warning"])
        self.assertTrue(security["isolated_environment_required"])
        self.assertFalse(security["install_unpinned_dependencies_before_review"])

    def test_next_gate_requires_integrity_tests_and_independent_reference(self):
        steps = self.manifest["required_next_gate"]
        joined = " ".join(steps).lower()
        for marker in (
            "sha-256",
            "lockfiles",
            "python and rust tests",
            "independent classical state-vector reference",
            "decomposed t-count",
            "accepted-task cost",
        ):
            with self.subTest(marker=marker):
                self.assertIn(marker, joined)

    def test_no_resource_or_mission_claim_is_promoted(self):
        nonclaims = self.manifest["nonclaims"]
        self.assertFalse(nonclaims["external_Toffoli_claim_independently_verified"])
        self.assertFalse(nonclaims["numeric_T_count_established"])
        self.assertFalse(nonclaims["hardware_advantage_established"])
        self.assertFalse(nonclaims["energy_or_cost_advantage_established"])
        self.assertFalse(nonclaims["Hilbert_space_dimension_equals_readable_classical_bytes"])
        self.assertFalse(nonclaims["paid_QPU_execution_authorized"])


if __name__ == "__main__":
    unittest.main()
