import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[3]
RUNNER = ROOT / "software/uqpu-prototype/examples/run_cycle004_qiskit_validation.py"


@unittest.skipUnless(importlib.util.find_spec("qiskit"), "pinned optional Qiskit stack not installed")
class Cycle004QiskitValidationTests(unittest.TestCase):
    def test_cycle003_qasm_pair_parses_with_expected_counts_and_measurements(self):
        spec = importlib.util.spec_from_file_location("cycle004_qiskit_runner", RUNNER)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        result = module.run(module.DEFAULT_INPUT)
        self.assertTrue(result["all_passed"])
        self.assertEqual(result["qiskit_version"], "2.5.2")
        self.assertEqual(len(result["rows"]), 2)
        for row in result["rows"]:
            self.assertEqual(row["num_qubits"], 6)
            self.assertEqual(row["num_clbits"], 6)
            self.assertEqual(row["operation_counts"]["cx"], 18)
            self.assertEqual(row["measurement_map"], {index: index for index in range(6)})
        self.assertFalse(result["hardware_executed"])


if __name__ == "__main__":
    unittest.main()
