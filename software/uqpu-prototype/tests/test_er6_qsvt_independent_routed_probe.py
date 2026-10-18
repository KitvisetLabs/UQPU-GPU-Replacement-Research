import copy
import importlib.util
import json
import unittest

from uqpu.er6_qsvt_independent_routed_probe import (
    CZ_MATRIX,
    PERSISTED_CERTIFICATE,
    SX_MATRIX,
    X_MATRIX,
    evaluate_result,
    rz_matrix,
    reproduce_with_qulacs,
)
from uqpu.er6_qsvt_independent_routed_preregistration import PERSISTED_PREREGISTRATION


class IndependentRoutedProbeUnitTests(unittest.TestCase):
    def test_explicit_matrices_are_bound_to_expected_entries(self):
        self.assertEqual(X_MATRIX, ((0j, 1 + 0j), (1 + 0j, 0j)))
        self.assertEqual(CZ_MATRIX[3][3], -1 + 0j)
        self.assertAlmostEqual(abs(SX_MATRIX[0][0]), 2 ** -0.5)
        self.assertAlmostEqual(abs(rz_matrix(0.7)[0][0]), 1.0)

    def test_evaluator_rejects_residual_and_missing_counterexample(self):
        contract = json.loads(PERSISTED_PREREGISTRATION.read_text(encoding="utf-8"))
        resources = {
            "observed_gate_set": ["cz", "rz", "sx", "x"],
            "observed_final_index_layout": list(range(10)),
            "completed_probe_count": 4,
            "host_runtime_seconds": 1.0,
            "host_peak_traced_bytes": 1000,
            "probes": [{
                "id": str(index),
                "phase_aligned_l2_residual": 1e-12,
                "reference_state_norm": 1.0,
                "candidate_state_norm": 1.0,
            } for index in range(4)],
            "counterexamples": [{"contract_requirement_satisfied": True} for _ in range(5)],
            "authorization": dict(contract["authorization"]),
        }
        self.assertTrue(evaluate_result(contract, resources)["independent_sdk_bounded_probe_gate_passed"])
        changed = copy.deepcopy(resources)
        changed["probes"][0]["phase_aligned_l2_residual"] = 1e-8
        self.assertIn("probe:0:residual", evaluate_result(contract, changed)["failures"])
        changed = copy.deepcopy(resources)
        changed["counterexamples"][0]["contract_requirement_satisfied"] = False
        self.assertIn("counterexample_detection", evaluate_result(contract, changed)["failures"])

    def test_persisted_certificate_keeps_stronger_claims_closed(self):
        if not PERSISTED_CERTIFICATE.exists():
            self.skipTest("hosted result is produced by the optional CI job")
        certificate = json.loads(PERSISTED_CERTIFICATE.read_text(encoding="utf-8"))
        self.assertFalse(certificate["evaluation"]["full_operator_equivalence_accepted"])
        self.assertFalse(certificate["evaluation"]["useful_output_quality_accepted"])


@unittest.skipUnless(
    importlib.util.find_spec("qulacs") and importlib.util.find_spec("qiskit_ibm_runtime"),
    "optional independent routed SDKs",
)
class PinnedIndependentRoutedProbeTests(unittest.TestCase):
    def test_frozen_independent_routed_probes(self):
        result = reproduce_with_qulacs()
        self.assertTrue(result["passed"], result["evaluation"])
        self.assertEqual(result["resources"]["authorization"]["provider_jobs"], 0)
        self.assertFalse(result["evaluation"]["full_operator_equivalence_accepted"])


if __name__ == "__main__":
    unittest.main()
