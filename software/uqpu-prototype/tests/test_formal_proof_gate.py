import unittest

from uqpu.formal_proof_gate import FormalProofRecord, sha256_hex


def _record(**overrides):
    statement = "forall x, x = x"
    axiom = sha256_hex("axioms-v1")
    proof = sha256_hex("proof-object-v1")
    data = dict(
        theorem_id="FND6-TEST-001",
        statement=statement,
        axiom_set_sha256=axiom,
        proof_object_sha256=proof,
        checker_id="checker-alpha",
        checker_version="1.0.0",
        checker_image_sha256=sha256_hex("checker-image-alpha"),
        checker_result="PASS",
        checker_exit_code=0,
        checker_log_sha256=sha256_hex("primary-log"),
        independent_checker_id="checker-beta",
        independent_checker_version="2.0.0",
        independent_checker_image_sha256=sha256_hex("checker-image-beta"),
        independent_result="PASS",
        independent_exit_code=0,
        independent_log_sha256=sha256_hex("independent-log"),
        independent_axiom_set_sha256=axiom,
        independent_proof_object_sha256=proof,
        independent_statement_sha256=sha256_hex(statement),
    )
    data.update(overrides)
    return FormalProofRecord(**data)


class FormalProofGateTests(unittest.TestCase):
    def test_unrun_candidate_is_unverified(self):
        candidate = FormalProofRecord(theorem_id="T-1", statement="x = x")
        self.assertEqual(candidate.audit_status, "UNVERIFIED")
        self.assertFalse(candidate.has_complete_primary_check_record)
        self.assertFalse(candidate.has_complete_independent_replay_record)

    def test_primary_pass_is_not_independent_replay(self):
        candidate = _record(
            independent_checker_id="",
            independent_checker_version="",
            independent_checker_image_sha256="",
            independent_result="NOT_RUN",
            independent_exit_code=None,
            independent_log_sha256="",
            independent_axiom_set_sha256="",
            independent_proof_object_sha256="",
            independent_statement_sha256="",
        )
        self.assertTrue(candidate.has_complete_primary_check_record)
        self.assertFalse(candidate.has_complete_independent_replay_record)
        self.assertEqual(candidate.audit_status, "PRIMARY_CHECK_METADATA_COMPLETE")

    def test_distinct_checker_replay_with_identical_inputs_is_recorded(self):
        candidate = _record()
        self.assertTrue(candidate.has_complete_independent_replay_record)
        self.assertEqual(
            candidate.audit_status, "INDEPENDENT_REPLAY_METADATA_COMPLETE"
        )

    def test_same_checker_identity_is_not_independent(self):
        candidate = _record(
            independent_checker_id="checker-alpha",
            independent_checker_image_sha256=sha256_hex("checker-image-alpha"),
        )
        self.assertTrue(candidate.has_complete_primary_check_record)
        self.assertFalse(candidate.has_complete_independent_replay_record)
        self.assertEqual(candidate.audit_status, "PRIMARY_CHECK_METADATA_COMPLETE")

    def test_changed_axioms_or_proof_object_blocks_replay(self):
        changed_axioms = _record(
            independent_axiom_set_sha256=sha256_hex("other-axioms")
        )
        changed_proof = _record(
            independent_proof_object_sha256=sha256_hex("other-proof")
        )
        self.assertFalse(changed_axioms.has_complete_independent_replay_record)
        self.assertFalse(changed_proof.has_complete_independent_replay_record)

    def test_statement_digest_must_match_exact_statement(self):
        candidate = _record(
            independent_statement_sha256=sha256_hex("different theorem")
        )
        self.assertFalse(candidate.has_complete_independent_replay_record)

    def test_pass_with_nonzero_exit_is_invalid(self):
        candidate = _record(checker_exit_code=2)
        self.assertEqual(candidate.audit_status, "INVALID_METADATA")
        self.assertFalse(candidate.has_complete_primary_check_record)

    def test_bad_digest_is_invalid(self):
        candidate = _record(proof_object_sha256="not-a-digest")
        self.assertEqual(candidate.audit_status, "INVALID_METADATA")

    def test_rejected_candidate_is_preserved_as_negative_result(self):
        candidate = _record(checker_result="REJECTED", checker_exit_code=0)
        self.assertEqual(candidate.audit_status, "FAILED_OR_COUNTEREXAMPLE")
        self.assertFalse(candidate.has_complete_primary_check_record)


if __name__ == "__main__":
    unittest.main()
