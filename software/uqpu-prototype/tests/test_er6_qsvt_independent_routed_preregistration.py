import copy
import json
import unittest

from uqpu.er6_qsvt_independent_routed_preregistration import (
    PERSISTED_PREREGISTRATION,
    build_preregistration,
    validate_preregistration,
)


class IndependentRoutedPreregistrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = build_preregistration()

    def test_contract_binds_source_sdk_gates_and_counterexamples(self):
        self.assertEqual(validate_preregistration(self.contract), [])
        self.assertEqual(self.contract["method"]["independent_simulator"], "qulacs==0.6.14")
        self.assertEqual(len(self.contract["method"]["counterexamples"]), 4)

    def test_threshold_and_authorization_mutations_fail_closed(self):
        changed = copy.deepcopy(self.contract)
        changed["acceptance"]["maximum_phase_aligned_l2_residual_per_probe"] = 1e-6
        self.assertIn("residual_threshold", validate_preregistration(changed))
        changed = copy.deepcopy(self.contract)
        changed["authorization"]["shots"] = 1
        self.assertIn("authorization", validate_preregistration(changed))

    def test_gate_translation_and_counterexample_requirements_are_bound(self):
        changed = copy.deepcopy(self.contract)
        del changed["method"]["gate_translation"]["sx"]
        self.assertIn("gate_translation", validate_preregistration(changed))
        changed = copy.deepcopy(self.contract)
        changed["method"]["counterexamples"].pop()
        self.assertIn("counterexamples", validate_preregistration(changed))

    def test_persisted_contract_matches_generator(self):
        persisted = json.loads(PERSISTED_PREREGISTRATION.read_text(encoding="utf-8"))
        self.assertEqual(persisted, self.contract)


if __name__ == "__main__":
    unittest.main()
