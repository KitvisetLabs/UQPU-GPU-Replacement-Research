import unittest

from uqpu.formal_proof_evidence import (
    FormalProofEvidence,
    build_formal_proof_evidence,
    sha256_hex,
)


class FormalProofEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.proof = b"theorem demo : True := by trivial\n"
        self.log = b"Lean 4.19.0; exit_code=0\n"
        self.environment = b"lakefile.lean + lean-toolchain pinned\n"
        self.revision = "a" * 40

    def _checked(self, **overrides):
        values = dict(
            claim_id="EQN-PROOF-TEST-001",
            claim_kind="MATHEMATICAL_THEOREM",
            statement="theorem demo : True",
            assumptions=("Lean kernel and declared imports",),
            status="KERNEL_CHECKED",
            source_revision=self.revision,
            proof_artifact=self.proof,
            checker_name="Lean",
            checker_version="4.19.0",
            checker_command="lake env lean Demo.lean",
            environment_bytes=self.environment,
            run_log=self.log,
            checker_exit_code=0,
        )
        values.update(overrides)
        return build_formal_proof_evidence(**values)

    def test_exact_artifact_bytes_are_bound_to_record(self):
        record = self._checked()
        result = record.verify_artifact_bytes(self.proof, self.log)
        self.assertTrue(result.record_integrity_verified)
        self.assertFalse(result.empirical_physics_established)
        self.assertFalse(result.independent_reproduction_recorded)

    def test_tampered_proof_bytes_fail_closed(self):
        record = self._checked()
        with self.assertRaisesRegex(ValueError, "proof artifact bytes"):
            record.verify_artifact_bytes(self.proof + b"--tampered", self.log)

    def test_tampered_run_log_fails_closed(self):
        record = self._checked()
        with self.assertRaisesRegex(ValueError, "run log bytes"):
            record.verify_artifact_bytes(self.proof, self.log + b"changed")

    def test_statement_hash_mismatch_is_rejected(self):
        record = self._checked()
        altered = FormalProofEvidence(**{**record.__dict__, "statement": "theorem demo : False"})
        with self.assertRaisesRegex(ValueError, "statement_sha256"):
            altered.validate_metadata()

    def test_kernel_checked_without_checker_identity_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "checker_name"):
            self._checked(checker_name="")

    def test_formal_statement_is_not_kernel_checked(self):
        record = build_formal_proof_evidence(
            claim_id="EQN-PROOF-TEST-002",
            claim_kind="PHYSICAL_EQUATION_HYPOTHESIS",
            statement="candidate equation is dimensionally consistent",
            assumptions=("continuum model",),
            status="FORMAL_STATEMENT",
        )
        self.assertEqual(record.status, "FORMAL_STATEMENT")
        with self.assertRaisesRegex(ValueError, "checked or failed attempt"):
            record.verify_artifact_bytes(b"", b"")

    def test_independent_reproduction_requires_positive_count(self):
        with self.assertRaisesRegex(ValueError, "at least one independent reproduction"):
            self._checked(status="INDEPENDENTLY_REPRODUCED", independent_reproduction_count=0)

    def test_failed_proof_is_retained_as_negative_evidence(self):
        failure_log = b"Lean 4.19.0; exit_code=1\n"
        record = self._checked(
            status="FAILED",
            checker_exit_code=1,
            run_log=failure_log,
            notes=("Kernel rejected the candidate proof term.",),
        )
        result = record.verify_artifact_bytes(self.proof, failure_log)
        self.assertEqual(result.status, "FAILED")
        self.assertFalse(result.empirical_physics_established)

    def test_environment_digest_is_derived_from_exact_bytes(self):
        record = self._checked()
        self.assertEqual(record.environment_sha256, sha256_hex(self.environment))


if __name__ == "__main__":
    unittest.main()
