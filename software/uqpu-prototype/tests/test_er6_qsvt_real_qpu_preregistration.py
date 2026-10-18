import copy
import json
import unittest

from uqpu.er6_qsvt_real_qpu_preregistration import (
    PERSISTED_PREREGISTRATION,
    REQUIRED_EXECUTION_FIELDS,
    build_preregistration,
    validate_preregistration,
)


class RealQpuPreregistrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = build_preregistration()

    def test_contract_is_valid_and_execution_is_disabled(self):
        self.assertEqual(validate_preregistration(self.contract), [])
        self.assertFalse(self.contract["phases"][1]["enabled"])
        self.assertEqual(self.contract["authorization"]["maximum_jobs"], 0)
        self.assertEqual(self.contract["authorization"]["maximum_shots"], 0)

    def test_measurement_contract_is_complete_and_provider_consistent(self):
        measurement = self.contract["measurement_contract"]
        self.assertEqual(measurement["required_execution_fields"], REQUIRED_EXECUTION_FIELDS)
        self.assertTrue(measurement["cross_provider_probability_price_join_forbidden"])
        self.assertTrue(measurement["execution_success_is_not_quality_acceptance"])

    def test_authorization_and_quality_mutations_fail_closed(self):
        changed = copy.deepcopy(self.contract)
        changed["authorization"]["maximum_jobs"] = 1
        self.assertIn("authorization", validate_preregistration(changed))
        changed = copy.deepcopy(self.contract)
        changed["measurement_contract"]["execution_success_is_not_quality_acceptance"] = False
        self.assertIn("quality_gate", validate_preregistration(changed))

    def test_persisted_contract_matches_generator(self):
        persisted = json.loads(PERSISTED_PREREGISTRATION.read_text(encoding="utf-8"))
        self.assertEqual(persisted, self.contract)


if __name__ == "__main__":
    unittest.main()
