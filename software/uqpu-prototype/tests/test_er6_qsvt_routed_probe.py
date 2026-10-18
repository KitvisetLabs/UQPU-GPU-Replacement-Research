import copy
import importlib.util
import json
import cmath
import math
import unittest

from uqpu.er6_qsvt_routed_probe import (
    PERSISTED_CERTIFICATE,
    evaluate_result,
    inverse_layout_state,
    phase_aligned_l2,
    reproduce_with_qiskit,
)
from uqpu.er6_qsvt_routed_probe_preregistration import PERSISTED_PREREGISTRATION


class RoutedProbeUnitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = json.loads(PERSISTED_PREREGISTRATION.read_text(encoding="utf-8"))

    def test_inverse_layout_moves_bit_positions(self):
        physical = [0j] * 8
        physical[4] = 1.0  # physical q2=1
        logical = inverse_layout_state(physical, [2, 0, 1])
        self.assertEqual(max(range(len(logical)), key=lambda index: abs(logical[index])), 1)

    def test_inverse_layout_rejects_non_bijection(self):
        with self.assertRaises(ValueError):
            inverse_layout_state([0j] * 8, [0, 0, 2])

    def test_global_phase_is_removed(self):
        reference = [1 / math.sqrt(2), 1j / math.sqrt(2)]
        candidate = [value * cmath.exp(0.37j) for value in reference]
        self.assertLess(phase_aligned_l2(reference, candidate), 1e-12)

    def test_evaluator_passes_bounded_gate_but_not_full_equivalence(self):
        resources = {
            "observed_active_physical_qubits": list(range(10)),
            "observed_final_index_layout": list(range(10)),
            "host_runtime_seconds": 1.0,
            "host_peak_traced_bytes": 1000,
            "completed_probe_count": 4,
            "probes": [{
                "id": probe["id"],
                "phase_aligned_l2_residual": 1e-12,
                "logical_state_norm": 1.0,
                "routed_state_norm": 1.0,
            } for probe in self.contract["method"]["probes"]],
            "authorization": dict(self.contract["authorization"]),
        }
        result = evaluate_result(self.contract, resources)
        self.assertTrue(result["bounded_probe_gate_passed"])
        self.assertFalse(result["full_operator_equivalence_accepted"])
        self.assertFalse(result["useful_output_quality_accepted"])

        changed = copy.deepcopy(resources)
        changed["probes"][0]["phase_aligned_l2_residual"] = 1e-8
        self.assertIn("probe:computational_zero:residual", evaluate_result(self.contract, changed)["failures"])

    def test_persisted_certificate_keeps_stronger_claims_closed(self):
        certificate = json.loads(PERSISTED_CERTIFICATE.read_text(encoding="utf-8"))
        self.assertTrue(certificate["passed"])
        self.assertFalse(certificate["evaluation"]["full_operator_equivalence_accepted"])
        self.assertFalse(certificate["evaluation"]["useful_output_quality_accepted"])
        self.assertEqual(certificate["resources"]["authorization"]["provider_jobs"], 0)
        self.assertEqual(certificate["provenance"]["workflow_job_id"], 117572935487)


@unittest.skipUnless(importlib.util.find_spec("qiskit_ibm_runtime"), "optional saved-target SDK")
class PinnedRoutedProbeTests(unittest.TestCase):
    def test_frozen_routed_probes(self):
        result = reproduce_with_qiskit()
        self.assertTrue(result["passed"])
        self.assertFalse(result["evaluation"]["full_operator_equivalence_accepted"])
        self.assertEqual(result["resources"]["authorization"]["provider_jobs"], 0)


if __name__ == "__main__":
    unittest.main()
