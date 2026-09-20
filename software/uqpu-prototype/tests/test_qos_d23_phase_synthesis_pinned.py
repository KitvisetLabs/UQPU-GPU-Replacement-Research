import unittest

from uqpu.qos_d23_phase_synthesis_contract import synthesize_with_pinned_qsppack


class PinnedQSPPackExecutionTests(unittest.TestCase):
    def test_degree_81_newton_failure_is_preserved(self):
        result = synthesize_with_pinned_qsppack()
        if result["status"] == "DEPENDENCY_NOT_INSTALLED":
            self.skipTest("isolated qsppack environment only")

        self.assertEqual(result["dependency_versions"]["qsppack"], "0.3.0")
        self.assertEqual(result["status"], "SYNTHESIS_EXCEPTION")
        self.assertEqual(result["exception_type"], "ValueError")
        self.assertIn("could not broadcast input array", result["exception_message"])
        self.assertFalse(result["qsp_phase_sequence_synthesized"])
        self.assertFalse(result["independent_reconstruction_passed"])


if __name__ == "__main__":
    unittest.main()
