import copy
import json
import unittest

from uqpu.er6_qsvt_routed_probe_preregistration import (
    PERSISTED_PREREGISTRATION,
    build_preregistration,
    validate_preregistration,
)


class RoutedProbePreregistrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = build_preregistration()

    def test_contract_binds_source_routing_and_four_probes(self):
        self.assertEqual(validate_preregistration(self.contract), [])
        self.assertEqual(self.contract["inputs"]["logical_source"]["queries"], 10)
        self.assertEqual(len(self.contract["method"]["probes"]), 4)
        self.assertEqual(self.contract["evidence_class"], "MODEL_ONLY_PREREGISTRATION")

    def test_layout_and_authorization_fail_closed(self):
        changed = copy.deepcopy(self.contract)
        changed["method"]["compact_only_frozen_active_physical_qubits"][-1] = 10
        self.assertIn("active_physical_qubits", validate_preregistration(changed))

        changed = copy.deepcopy(self.contract)
        changed["authorization"]["shots"] = 1
        self.assertIn("authorization", validate_preregistration(changed))

    def test_threshold_mutation_is_detected(self):
        changed = copy.deepcopy(self.contract)
        changed["acceptance"]["maximum_phase_aligned_l2_residual_per_probe"] = 1e-6
        errors = validate_preregistration(changed)
        self.assertIn("residual_threshold", errors)
        self.assertIn("contract_sha256", errors)

    def test_persisted_contract_matches_generator(self):
        persisted = json.loads(PERSISTED_PREREGISTRATION.read_text(encoding="utf-8"))
        self.assertEqual(persisted, self.contract)


if __name__ == "__main__":
    unittest.main()
