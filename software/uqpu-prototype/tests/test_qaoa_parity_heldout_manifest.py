import hashlib
import itertools
import json
import math
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MANIFEST_PATH = ROOT / "benchmarks/manifests/qaoa-parity-heldout-2026-10-30.json"
REFERENCE_PATH = ROOT / "benchmarks/references/qaoa-parity-exact-references-2026-10-30.json"


class QAOAParityHeldoutManifestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest_bytes = MANIFEST_PATH.read_bytes()
        cls.manifest = json.loads(cls.manifest_bytes)
        cls.references = json.loads(REFERENCE_PATH.read_text(encoding="utf-8"))

    def test_manifest_hash_is_bound_to_exact_reference_file(self):
        digest = hashlib.sha256(self.manifest_bytes).hexdigest()
        self.assertEqual(self.references["manifest_sha256"], digest)

    def test_split_membership_and_graph_families_are_disjoint(self):
        instances = self.manifest["instances"]
        ids = [item["id"] for item in instances]
        self.assertEqual(len(ids), len(set(ids)))
        family_sets = []
        for split, spec in self.manifest["splits"].items():
            selected = set(spec["instances"])
            self.assertTrue(selected)
            self.assertEqual(selected, {item["id"] for item in instances if item["split"] == split})
            family_sets.append(set(spec["families"]))
        for index, left in enumerate(family_sets):
            for right in family_sets[index + 1:]:
                self.assertTrue(left.isdisjoint(right))

    def test_graphs_preserve_canonical_signed_objective_inputs(self):
        for item in self.manifest["instances"]:
            self.assertEqual(len(item["edges"]), len(item["weights"]))
            self.assertEqual(item["edges"], sorted(item["edges"]))
            self.assertEqual(len(item["edges"]), len({tuple(edge) for edge in item["edges"]}))
            for u, v in item["edges"]:
                self.assertTrue(0 <= u < v < item["vertex_count"])
            self.assertTrue(all(math.isfinite(weight) for weight in item["weights"]))
        weights = [weight for item in self.manifest["instances"] for weight in item["weights"]]
        self.assertTrue(any(weight < 0 for weight in weights))
        self.assertTrue(any(weight > 0 for weight in weights))
        self.assertTrue(self.manifest["objective"]["signed_weights_preserved"])

    def test_exact_reference_certificates_recompute(self):
        self.assertEqual(self.references["workload_contract_id"], self.manifest["workload_contract_id"])
        by_id = {item["id"]: item for item in self.manifest["instances"]}
        certs = self.references["certificates"]
        self.assertEqual({cert["instance_id"] for cert in certs}, set(by_id))
        for cert in certs:
            item = by_id[cert["instance_id"]]
            scored = []
            for bits in itertools.product((0, 1), repeat=item["vertex_count"]):
                score = sum(
                    weight * (bits[u] ^ bits[v])
                    for (u, v), weight in zip(item["edges"], item["weights"])
                )
                scored.append((score, "".join(str(bit) for bit in bits)))
            optimum = max(score for score, _ in scored)
            argmax = sorted(
                bitstring for score, bitstring in scored
                if math.isclose(score, optimum, rel_tol=0.0, abs_tol=1e-12)
            )
            self.assertTrue(math.isclose(cert["optimum_score"], optimum, rel_tol=0.0, abs_tol=1e-12))
            self.assertEqual(cert["optimal_assignments"], argmax)
            self.assertEqual(cert["states_evaluated"], 1 << item["vertex_count"])
            self.assertEqual(cert["evidence_class"], "MODEL_ONLY_EXACT_SMALL_INSTANCE_REFERENCE")

    def test_acceptance_and_equal_budget_contract_are_explicit(self):
        acceptance = self.manifest["acceptance_contract"]
        self.assertEqual(acceptance["id"], "SIGNED-MAXCUT-PARITY-QAOA-ACCEPTANCE-001")
        self.assertIn("cycle", acceptance["parity_feasibility"])
        self.assertIn("0.05", acceptance["quality_pass"])
        budget = self.manifest["proposed_equal_budget"]
        self.assertEqual(budget["shots_per_instance_per_method_per_repetition"], 8192)
        self.assertEqual(budget["optimizer_evaluations_per_instance_per_method_per_repetition"], 32)
        self.assertEqual(budget["independent_repetitions"], 10)

    def test_test_split_is_evaluation_only_and_no_paid_job_is_authorized(self):
        self.assertTrue(self.manifest["objective"]["no_test_optimum_for_selection"])
        self.assertIn("must not inform selection", self.manifest["proposed_equal_budget"]["parameter_selection"])
        self.assertFalse(self.manifest["proposed_equal_budget"]["paid_qpu_execution_authorized"])
        self.assertEqual(self.manifest["status"], "PREREGISTERED_NOT_EXECUTED")


if __name__ == "__main__":
    unittest.main()
