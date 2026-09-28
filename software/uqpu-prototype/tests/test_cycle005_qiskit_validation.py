import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[3]
RUNNER = ROOT / "software/uqpu-prototype/examples/run_cycle005_qiskit_validation.py"


@unittest.skipUnless(importlib.util.find_spec("qiskit"), "pinned optional Qiskit stack not installed")
class Cycle005QiskitValidationTests(unittest.TestCase):
    def test_persisted_qiskit_output_matches_live_sdk_and_second_grammar_gate(self):
        spec = importlib.util.spec_from_file_location("cycle005_qiskit_runner", RUNNER)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        result = module.run()
        self.assertTrue(result["all_passed"])
        self.assertEqual(result["qiskit_version"], "2.5.2")
        self.assertEqual(result["candidate_count"], 2)
        self.assertIsNone(result["provider_transpile"]["physical_depth"])
        self.assertFalse(result["hardware_executed"])


if __name__ == "__main__":
    unittest.main()
