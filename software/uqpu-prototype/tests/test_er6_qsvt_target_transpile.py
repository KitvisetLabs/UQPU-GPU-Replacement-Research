import copy
import importlib.util
import json
import unittest

from uqpu.er6_qsvt_target_transpile import evaluate_result, reproduce_with_qiskit
from uqpu.er6_qsvt_target_transpile_preregistration import PERSISTED_PREREGISTRATION


class TargetTranspileEvaluationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = json.loads(PERSISTED_PREREGISTRATION.read_text(encoding="utf-8"))
        cls.resources = {
            "logical_qubits": 10,
            "host_runtime_seconds": 1.0,
            "host_peak_traced_bytes": 1000,
            "routed_depth": 100,
            "routed_size": 200,
            "two_qubit_operations": 50,
            "serialized_qasm2_bytes": 1000,
            "target_conformance_failures": [],
            "authorization": dict(cls.contract["authorization"]),
        }

    def test_resource_gate_passes_but_quality_stays_unaccepted(self):
        evaluation = evaluate_result(self.contract, self.resources)
        self.assertTrue(evaluation["resource_and_authorization_gate_passed"])
        self.assertFalse(evaluation["useful_output_quality_accepted"])

    def test_each_capacity_or_authorization_failure_is_retained(self):
        changed = copy.deepcopy(self.resources)
        changed["routed_depth"] = self.contract["acceptance"]["maximum_routed_depth"] + 1
        self.assertIn("routed_depth", evaluate_result(self.contract, changed)["failures"])

        changed = copy.deepcopy(self.resources)
        changed["target_conformance_failures"] = [{"operation": "unknown", "qargs": [0]}]
        self.assertIn("target_conformance", evaluate_result(self.contract, changed)["failures"])

        changed = copy.deepcopy(self.resources)
        changed["authorization"]["shots"] = 1
        self.assertIn("authorization", evaluate_result(self.contract, changed)["failures"])


@unittest.skipUnless(importlib.util.find_spec("qiskit_ibm_runtime"), "optional saved-target SDK")
class PinnedTargetTranspileTests(unittest.TestCase):
    def test_preregistered_saved_target_transpilation(self):
        result = reproduce_with_qiskit()
        self.assertEqual(result["resources"]["authorization"]["provider_jobs"], 0)
        self.assertEqual(result["resources"]["target_conformance_failures"], [])


if __name__ == "__main__":
    unittest.main()
