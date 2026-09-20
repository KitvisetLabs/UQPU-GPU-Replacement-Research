import unittest

from uqpu.qos_d23_phase_synthesis_contract import (
    EXPECTED_FINGERPRINT,
    PINNED_CRITERIA,
    PINNED_METHOD,
    PINNED_PACKAGE,
    PINNED_PARITY,
    PINNED_PHASE_TYPE,
    PINNED_TARGET_PRE,
    PINNED_VERSION,
    frozen_contract,
    synthesize_with_pinned_qsppack,
)


class PhaseSynthesisContractTests(unittest.TestCase):
    def test_contract_is_explicit_and_bound_to_batch051_candidate(self):
        contract = frozen_contract()
        self.assertEqual(contract.package, PINNED_PACKAGE)
        self.assertEqual(PINNED_PACKAGE, "qsppack")
        self.assertEqual(contract.version, PINNED_VERSION)
        self.assertEqual(contract.method, PINNED_METHOD)
        self.assertEqual(PINNED_METHOD, "Newton")
        self.assertEqual(contract.parity, PINNED_PARITY)
        self.assertEqual(PINNED_PARITY, 1)
        self.assertIs(contract.target_pre, PINNED_TARGET_PRE)
        self.assertIs(PINNED_TARGET_PRE, True)
        self.assertEqual(contract.phase_type, PINNED_PHASE_TYPE)
        self.assertEqual(PINNED_PHASE_TYPE, "full")
        self.assertEqual(contract.criteria, PINNED_CRITERIA)
        self.assertEqual(PINNED_CRITERIA, 1e-12)
        self.assertEqual(contract.coefficient_fingerprint, EXPECTED_FINGERPRINT)
        self.assertTrue(contract.fingerprint_matches_batch051)

    def test_unpinned_environment_cannot_be_promoted_to_verified_phases(self):
        result = synthesize_with_pinned_qsppack()
        self.assertFalse(result["independent_reconstruction_passed"])
        if result["status"] == "SYNTHESIS_CONVERGED":
            self.assertTrue(result["qsp_phase_sequence_synthesized"])
            self.assertEqual(result["phase_count"], 82)
        else:
            self.assertFalse(result["qsp_phase_sequence_synthesized"])


if __name__ == "__main__":
    unittest.main()
