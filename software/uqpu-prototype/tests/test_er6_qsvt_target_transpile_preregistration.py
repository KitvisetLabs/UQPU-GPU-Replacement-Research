import copy
import json
import unittest

from uqpu.er6_qsvt_target_transpile_preregistration import (
    PERSISTED_PREREGISTRATION,
    TARGET_IDENTITY_SHA256,
    build_preregistration,
    validate_preregistration,
)


class TargetTranspilePreregistrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = build_preregistration()

    def test_contract_is_valid_and_binds_target_before_routing(self):
        self.assertEqual(validate_preregistration(self.contract), [])
        self.assertEqual(
            self.contract["inputs"]["saved_target_identity"]["target_identity_sha256"],
            TARGET_IDENTITY_SHA256,
        )
        self.assertEqual(self.contract["inputs"]["logical_source"]["queries"], 10)
        self.assertEqual(self.contract["evidence_class"], "MODEL_ONLY_PREREGISTRATION")

    def test_transpiler_and_authorization_are_frozen(self):
        transpiler = self.contract["transpiler"]
        self.assertEqual(transpiler["optimization_level"], 0)
        self.assertEqual(transpiler["routing_method"], "basic")
        self.assertEqual(transpiler["initial_layout"], list(range(10)))
        self.assertFalse(any(self.contract["authorization"].values()))

    def test_mutations_fail_closed(self):
        changed = copy.deepcopy(self.contract)
        changed["transpiler"]["seed_transpiler"] += 1
        errors = validate_preregistration(changed)
        self.assertIn("transpiler_contract", errors)
        self.assertIn("contract_sha256", errors)

        changed = copy.deepcopy(self.contract)
        changed["authorization"]["provider_jobs"] = 1
        self.assertIn("authorization", validate_preregistration(changed))

    def test_persisted_contract_matches_generator(self):
        persisted = json.loads(PERSISTED_PREREGISTRATION.read_text(encoding="utf-8"))
        self.assertEqual(persisted, self.contract)


if __name__ == "__main__":
    unittest.main()
