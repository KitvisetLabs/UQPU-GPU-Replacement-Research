import hashlib
import json
import unittest

from uqpu.stateprep_lower_bound_methodology import (
    build_stateprep_lower_bound_methodology,
    validate_stateprep_lower_bound_methodology,
)


class StateprepLowerBoundMethodologyTests(unittest.TestCase):
    def _build(self, **overrides):
        values = dict(
            claim_id="RG-STATEPREP-SPARSE-001-LOWER-BOUND-CANDIDATE",
            claim_statement="A stated circuit family requires superpolynomial resources.",
            proof_method="Property-based lower-bound argument",
            naturalness_status="NATURAL",
            holds_for_sufficient_fraction_of_haar_random_states=True,
            efficiently_testable_given_all_amplitudes=True,
            target_is_superpolynomial_lower_bound=True,
            against_fixed_magic_hierarchy_level=True,
            approximation_regime_matches_source=True,
            target_uses_polynomial_size_circuits=True,
            cryptographic_assumption_matches_source=True,
            cryptographic_assumption_statement=(
                "Classically subexponentially secure PRF with polynomial-size depth-d threshold-circuit implementation."
            ),
            standard_cryptographic_assumption_adopted=True,
            assessment_basis="Illustrative fixture only; not a classification of either source paper.",
        )
        values.update(overrides)
        return build_stateprep_lower_bound_methodology(**values)

    def test_in_scope_flags_method_barrier_without_rejecting_claim(self):
        record = self._build()
        self.assertEqual(record["scope_classification"], "METHOD_BARRIER_APPLIES_TO_PROOF_STRATEGY_ONLY")
        self.assertFalse(record["claim_rejected_by_barrier"])
        self.assertFalse(record["empirical_physics_established"])
        self.assertTrue(validate_stateprep_lower_bound_methodology(record))

    def test_non_natural_method_is_outside_stated_scope(self):
        record = self._build(
            naturalness_status="NON_NATURAL",
            holds_for_sufficient_fraction_of_haar_random_states=False,
        )
        self.assertEqual(record["scope_classification"], "OUTSIDE_STATED_SCOPE")

    def test_unresolved_naturalness_stays_unresolved(self):
        record = self._build(
            naturalness_status="UNRESOLVED",
            holds_for_sufficient_fraction_of_haar_random_states=None,
            efficiently_testable_given_all_amplitudes=None,
        )
        self.assertEqual(record["scope_classification"], "UNRESOLVED")

    def test_unadopted_crypto_assumption_is_not_invoked(self):
        record = self._build(standard_cryptographic_assumption_adopted=False)
        self.assertEqual(record["scope_classification"], "ASSUMPTION_NOT_ADOPTED")

    def test_non_fixed_hierarchy_target_is_outside_scope(self):
        record = self._build(against_fixed_magic_hierarchy_level=False)
        self.assertEqual(record["scope_classification"], "OUTSIDE_STATED_SCOPE")

    def test_non_superpolynomial_target_is_outside_scope(self):
        record = self._build(target_is_superpolynomial_lower_bound=False)
        self.assertEqual(record["scope_classification"], "OUTSIDE_STATED_SCOPE")

    def test_approximation_regime_mismatch_is_outside_scope(self):
        record = self._build(approximation_regime_matches_source=False)
        self.assertEqual(record["scope_classification"], "OUTSIDE_STATED_SCOPE")

    def test_non_polynomial_size_target_is_outside_scope(self):
        record = self._build(target_uses_polynomial_size_circuits=False)
        self.assertEqual(record["scope_classification"], "OUTSIDE_STATED_SCOPE")

    def test_cryptographic_assumption_mismatch_is_outside_scope(self):
        record = self._build(cryptographic_assumption_matches_source=False)
        self.assertEqual(record["scope_classification"], "OUTSIDE_STATED_SCOPE")

    def test_unknown_cryptographic_scope_stays_unresolved(self):
        record = self._build(cryptographic_assumption_matches_source=None)
        self.assertEqual(record["scope_classification"], "UNRESOLVED")

    def test_natural_label_requires_both_naturalness_criteria(self):
        with self.assertRaisesRegex(ValueError, "NATURAL requires both"):
            self._build(efficiently_testable_given_all_amplitudes=None)

    def test_non_natural_label_requires_a_failed_criterion(self):
        with self.assertRaisesRegex(ValueError, "NON_NATURAL requires"):
            self._build(naturalness_status="NON_NATURAL")

    def test_validator_rejects_inconsistent_naturalness_even_with_rehashed_record(self):
        record = self._build()
        record["holds_for_sufficient_fraction_of_haar_random_states"] = False
        body = {key: value for key, value in record.items() if key != "record_sha256"}
        encoded = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        record["record_sha256"] = hashlib.sha256(encoded).hexdigest()
        with self.assertRaisesRegex(ValueError, "NATURAL requires both"):
            validate_stateprep_lower_bound_methodology(record)

    def test_tampered_record_is_rejected(self):
        record = self._build()
        record["proof_method"] = "tampered"
        with self.assertRaisesRegex(ValueError, "record_sha256"):
            validate_stateprep_lower_bound_methodology(record)

    def test_scope_field_tampering_is_rejected_even_before_digest_check(self):
        record = self._build()
        record["standard_cryptographic_assumption_adopted"] = False
        with self.assertRaisesRegex(ValueError, "scope_classification"):
            validate_stateprep_lower_bound_methodology(record)

    def test_empty_claim_id_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "claim_id is required"):
            self._build(claim_id=" ")


if __name__ == "__main__":
    unittest.main()
