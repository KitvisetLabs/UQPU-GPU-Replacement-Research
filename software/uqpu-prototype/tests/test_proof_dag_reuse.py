import unittest

from uqpu.proof_dag_reuse import validate_proof_dag


def h(ch):
    return ch * 64


def checked_node(**overrides):
    node = dict(
        node_id="lemma-1", claim_family="family-train", split="train",
        status="KERNEL_CHECKED", statement_sha256=h("a"), parents=[],
        residual_premises=[], proof_record_sha256=h("b"),
        checker_run_sha256=h("c"), source_revision="d" * 40,
        checker_name="Lean", checker_version="4.19.0", checker_exit_code=0,
    )
    node.update(overrides)
    return node


class ProofDagReuseTests(unittest.TestCase):
    def test_checked_train_schema_reused_with_explicit_residual(self):
        source = checked_node()
        target = dict(
            node_id="target-1", claim_family="family-test", split="test",
            status="CANDIDATE", statement_sha256=h("e"), parents=["lemma-1"],
            residual_premises=["remaining hypothesis P"], reused_schema_from="lemma-1",
        )
        result = validate_proof_dag([source, target])
        self.assertTrue(result["metadata_gate_passed"])
        self.assertEqual(result["reused_schema_count"], 1)
        self.assertEqual(result["evidence_class"], "METADATA_ONLY_NOT_PROOF")

    def test_invalid_statement_digest_rejected(self):
        node = dict(node_id="x", claim_family="f", split="train", status="CANDIDATE",
                    statement_sha256="not-a-digest", parents=[], residual_premises=[])
        with self.assertRaisesRegex(ValueError, "statement_sha256"):
            validate_proof_dag([node])

    def test_checked_node_requires_bound_checker_metadata(self):
        with self.assertRaisesRegex(ValueError, "checker_version is required"):
            validate_proof_dag([checked_node(checker_version="")])

    def test_missing_required_residual_field_rejected(self):
        node = dict(node_id="x", claim_family="f", split="train", status="CANDIDATE",
                    statement_sha256=h("a"), parents=[])
        with self.assertRaisesRegex(ValueError, "residual_premises is required"):
            validate_proof_dag([node])

    def test_missing_parent_rejected(self):
        node = dict(node_id="x", claim_family="f", split="train", status="CANDIDATE",
                    statement_sha256=h("a"), parents=["missing"], residual_premises=[])
        with self.assertRaisesRegex(ValueError, "missing parent"):
            validate_proof_dag([node])

    def test_cycle_rejected(self):
        a = dict(node_id="a", claim_family="fa", split="train", status="CANDIDATE",
                 statement_sha256=h("a"), parents=["b"], residual_premises=[])
        b = dict(node_id="b", claim_family="fb", split="train", status="CANDIDATE",
                 statement_sha256=h("b"), parents=["a"], residual_premises=[])
        with self.assertRaisesRegex(ValueError, "cycle"):
            validate_proof_dag([a, b])

    def test_claim_family_leakage_rejected(self):
        a = dict(node_id="a", claim_family="same", split="train", status="CANDIDATE",
                 statement_sha256=h("a"), parents=[], residual_premises=[])
        b = dict(node_id="b", claim_family="same", split="test", status="CANDIDATE",
                 statement_sha256=h("b"), parents=[], residual_premises=[])
        with self.assertRaisesRegex(ValueError, "leakage"):
            validate_proof_dag([a, b])

    def test_unverified_schema_source_rejected(self):
        source = checked_node(status="CANDIDATE", proof_record_sha256="", checker_run_sha256="")
        target = dict(node_id="t", claim_family="ft", split="test", status="CANDIDATE",
                      statement_sha256=h("e"), parents=["lemma-1"], residual_premises=["P"],
                      reused_schema_from="lemma-1")
        with self.assertRaisesRegex(ValueError, "not verified"):
            validate_proof_dag([source, target])

    def test_empty_residual_requires_explicit_closure(self):
        source = checked_node()
        target = dict(node_id="t", claim_family="ft", split="test", status="CANDIDATE",
                      statement_sha256=h("e"), parents=["lemma-1"], residual_premises=[],
                      reused_schema_from="lemma-1")
        with self.assertRaisesRegex(ValueError, "residual premises"):
            validate_proof_dag([source, target])

    def test_failed_attempt_is_retained_and_counted(self):
        failed = dict(
            node_id="bad", claim_family="family-failed", split="validation", status="FAILED",
            statement_sha256=h("a"), parents=[], residual_premises=[],
            proof_record_sha256=h("b"), checker_run_sha256=h("c"),
            source_revision="d" * 40, checker_name="Lean", checker_version="4.19.0",
            checker_exit_code=1, failure_reason="Kernel rejected candidate",
        )
        result = validate_proof_dag([failed])
        self.assertEqual(result["failed_attempt_count"], 1)

    def test_reproduced_requires_positive_count(self):
        node = checked_node(status="INDEPENDENTLY_REPRODUCED", independent_reproduction_count=0)
        with self.assertRaisesRegex(ValueError, "independent_reproduction_count"):
            validate_proof_dag([node])


if __name__ == "__main__":
    unittest.main()
