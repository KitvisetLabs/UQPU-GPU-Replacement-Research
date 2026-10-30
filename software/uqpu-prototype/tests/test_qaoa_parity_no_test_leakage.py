"""Fail-closed preregistration test for the v2 parity-QAOA holdout protocol."""
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[3]
MANIFEST_PATH = ROOT / "benchmarks/manifests/qaoa-parity-heldout-v2-2026-10-30.json"
REFERENCE_PATH = ROOT / "benchmarks/references/qaoa-parity-exact-references-v2-2026-10-30.json"


class QAOAParityNoTestLeakageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        cls.references = json.loads(REFERENCE_PATH.read_text(encoding="utf-8"))

    def test_test_split_is_never_used_for_parameter_or_method_selection(self):
        self.assertEqual(self.manifest["schema"], "uqpu-qaoa-parity-heldout-manifest-v2")
        protocol = self.manifest["evaluation_protocol"]
        self.assertEqual(protocol["parameter_training_split"], "train")
        self.assertEqual(protocol["hyperparameter_selection_split"], "validation")
        self.assertEqual(protocol["final_evaluation_split"], "test")
        self.assertIs(protocol["test_objective_used_for_parameter_optimization"], False)
        self.assertIs(protocol["per_instance_test_adaptation"], False)
        self.assertEqual(protocol["test_reference_use"], "scoring_only")
        self.assertIn("disjoint adaptation and evaluation shots", protocol["adaptation_track"])

    def test_split_membership_is_bound_to_declared_protocol(self):
        splits = self.manifest["splits"]
        protocol = self.manifest["evaluation_protocol"]
        self.assertEqual(protocol["training_instance_ids"], splits["train"]["instances"])
        self.assertEqual(protocol["validation_instance_ids"], splits["validation"]["instances"])
        self.assertEqual(protocol["test_instance_ids"], splits["test"]["instances"])
        train = set(splits["train"]["instances"])
        validation = set(splits["validation"]["instances"])
        test = set(splits["test"]["instances"])
        self.assertFalse(train & validation)
        self.assertFalse(train & test)
        self.assertFalse(validation & test)
        self.assertEqual(
            self.manifest["proposed_equal_budget"]["optimizer_evaluation_scope"],
            "TRAIN_SPLIT_ONLY",
        )
        self.assertIs(self.manifest["proposed_equal_budget"]["per_instance_test_adaptation"], False)

    def test_exact_references_are_hash_bound_and_scoring_only(self):
        digest = hashlib.sha256(MANIFEST_PATH.read_bytes()).hexdigest()
        self.assertEqual(self.references["manifest_sha256"], digest)
        self.assertEqual(self.references["workload_contract_id"], self.manifest["workload_contract_id"])
        self.assertEqual(self.references["protocol_status"], "EXACT_REFERENCES_FOR_SCORING_ONLY_NOT_SELECTION")
        self.assertEqual(
            {item["instance_id"] for item in self.references["certificates"]},
            set(self.manifest["splits"]["train"]["instances"]
                + self.manifest["splits"]["validation"]["instances"]
                + self.manifest["splits"]["test"]["instances"]),
        )


if __name__ == "__main__":
    unittest.main()
