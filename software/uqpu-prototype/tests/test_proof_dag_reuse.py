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


    def test_boolean_false_is_not_a_checked_exit_code(self):
        with self.assertRaisesRegex(ValueError, "integer checker_exit_code=0"):
            validate_proof_dag([checked_node(checker_exit_code=False)])

    def test_boolean_true_is_not_a_failed_exit_code(self):
        failed = dict(
            node_id="bad-bool", claim_family="family-failed-bool", split="validation",
            status="FAILED", statement_sha256=h("a"), parents=[], residual_premises=[],
            proof_record_sha256=h("b"), checker_run_sha256=h("c"),
            source_revision="d" * 40, checker_name="Lean", checker_version="4.19.0",
            checker_exit_code=True, failure_reason="Boolean is not a process exit code",
        )
        with self.assertRaisesRegex(ValueError, "integer nonzero checker_exit_code"):
            validate_proof_dag([failed])

    def test_boolean_reproduction_count_is_not_an_integer_count(self):
        with self.assertRaisesRegex(ValueError, "integer independent_reproduction_count"):
            validate_proof_dag([checked_node(
                status="INDEPENDENTLY_REPRODUCED", independent_reproduction_count=True
            )])

    def test_reproduced_requires_positive_count(self):
        node = checked_node(status="INDEPENDENTLY_REPRODUCED", independent_reproduction_count=0)
        with self.assertRaisesRegex(ValueError, "independent_reproduction_count"):
            validate_proof_dag([node])

    def test_train_node_cannot_depend_on_held_out_parent(self):
        parent = dict(node_id="held-out", claim_family="held-family", split="test",
                      status="CANDIDATE", statement_sha256=h("a"), parents=[],
                      residual_premises=[])
        child = dict(node_id="train-child", claim_family="train-family", split="train",
                     status="CANDIDATE", statement_sha256=h("b"), parents=["held-out"],
                     residual_premises=[])
        with self.assertRaisesRegex(ValueError, "held-out dependency leakage"):
            validate_proof_dag([parent, child])

    def test_held_out_node_cannot_depend_on_other_held_out_family(self):
        parent = dict(node_id="validation-fragment", claim_family="family-a", split="validation",
                      status="CANDIDATE", statement_sha256=h("a"), parents=[],
                      residual_premises=[])
        child = dict(node_id="test-target", claim_family="family-b", split="test",
                     status="CANDIDATE", statement_sha256=h("b"), parents=["validation-fragment"],
                     residual_premises=[])
        with self.assertRaisesRegex(ValueError, "held-out dependency leakage"):
            validate_proof_dag([parent, child])

    def test_same_family_same_split_internal_edge_is_allowed(self):
        parent = dict(node_id="test-lemma", claim_family="family-test", split="test",
                      status="CANDIDATE", statement_sha256=h("a"), parents=[],
                      residual_premises=[])
        child = dict(node_id="test-target", claim_family="family-test", split="test",
                     status="CANDIDATE", statement_sha256=h("b"), parents=["test-lemma"],
                     residual_premises=[])
        result = validate_proof_dag([parent, child])
        self.assertTrue(result["metadata_gate_passed"])

    def test_validation_node_can_depend_on_training_parent(self):
        parent = dict(node_id="train-lemma", claim_family="family-train", split="train",
                      status="CANDIDATE", statement_sha256=h("a"), parents=[],
                      residual_premises=[])
        child = dict(node_id="validation-target", claim_family="family-validation",
                     split="validation", status="CANDIDATE", statement_sha256=h("b"),
                     parents=["train-lemma"], residual_premises=[])
        result = validate_proof_dag([parent, child])
        self.assertTrue(result["metadata_gate_passed"])


if __name__ == "__main__":
    unittest.main()
