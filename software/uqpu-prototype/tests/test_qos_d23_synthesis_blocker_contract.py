import unittest

from uqpu.qos_d23_synthesis_blocker_contract import (
    EXPECTED_EXCEPTION,
    EXPECTED_FINGERPRINT,
    classify_batch053_result,
)


class QOSSynthesisBlockerContractTests(unittest.TestCase):
    def test_reproduced_shape_exception_is_tool_blocker_not_infeasibility(self):
        result = {
            "status": "SYNTHESIS_EXCEPTION",
            "exception_message": EXPECTED_EXCEPTION,
            "contract": {"coefficient_fingerprint": EXPECTED_FINGERPRINT},
            "qsp_phase_sequence_synthesized": False,
        }
        decision = classify_batch053_result(result)
        self.assertEqual(decision.status, "TOOL_BLOCKED_REPRODUCED")
        self.assertFalse(decision.phase_vector_usable)
        self.assertFalse(decision.independent_reconstruction_allowed)
        self.assertFalse(decision.mathematical_infeasibility_claim_allowed)

    def test_wrong_fingerprint_fails_closed(self):
        decision = classify_batch053_result({
            "status": "SYNTHESIS_EXCEPTION",
            "exception_message": EXPECTED_EXCEPTION,
            "contract": {"coefficient_fingerprint": "wrong"},
        })
        self.assertEqual(decision.status, "PROVENANCE_INVALID")
        self.assertFalse(decision.phase_vector_usable)

    def test_converged_vector_only_unlocks_independent_reconstruction(self):
        decision = classify_batch053_result({
            "status": "SYNTHESIS_CONVERGED",
            "contract": {"coefficient_fingerprint": EXPECTED_FINGERPRINT},
            "qsp_phase_sequence_synthesized": True,
            "phases": [0.0] * 82,
        })
        self.assertEqual(decision.status, "PHASE_VECTOR_REQUIRES_RECONSTRUCTION")
        self.assertTrue(decision.phase_vector_usable)
        self.assertTrue(decision.independent_reconstruction_allowed)
        self.assertFalse(decision.mathematical_infeasibility_claim_allowed)

    def test_short_phase_vector_is_not_promotable(self):
        decision = classify_batch053_result({
            "status": "SYNTHESIS_CONVERGED",
            "contract": {"coefficient_fingerprint": EXPECTED_FINGERPRINT},
            "qsp_phase_sequence_synthesized": True,
            "phases": [0.0] * 81,
        })
        self.assertEqual(decision.status, "UNRESOLVED_SYNTHESIS_RESULT")
        self.assertFalse(decision.phase_vector_usable)


if __name__ == "__main__":
    unittest.main()
