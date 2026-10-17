import copy
import json
import unittest
from pathlib import Path

from uqpu.er6_qsvt_next_boundary_preregistration import (
    ABSOLUTE_SAFETY_CEILINGS,
    build_preregistration,
    validate_preregistration,
)


class NextBoundaryPreregistrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = build_preregistration()

    def test_contract_is_valid_and_uses_all_measured_prefixes(self):
        self.assertEqual(validate_preregistration(self.contract), [])
        self.assertEqual(self.contract["measured_query_counts"], [1, 2, 3, 5, 8])
        self.assertEqual(len(self.contract["source_certificates"]), 4)
        self.assertEqual(self.contract["evidence_class"], "MODEL_ONLY")

    def test_persisted_contract_matches_generator(self):
        root = Path(__file__).resolve().parents[3]
        path = root / "benchmarks/results/cycle008-delta13-er6-qsvt-next-boundary-preregistration.json"
        self.assertEqual(json.loads(path.read_text(encoding="utf-8")), self.contract)

    def test_ten_is_last_planned_prefix_below_unchanged_stops(self):
        selection = self.contract["selection"]
        self.assertEqual(selection["selected_query_count"], 10)
        self.assertEqual(selection["first_blocked_query_count"], 11)
        self.assertIn("serialized_openqasm2_bytes", selection["first_blocked_metrics"])
        self.assertLessEqual(
            selection["selected_conservative_upper"]["serialized_openqasm2_bytes"],
            ABSOLUTE_SAFETY_CEILINGS["serialized_openqasm2_bytes"],
        )

    def test_selected_limits_are_frozen_and_provider_is_disabled(self):
        limits = self.contract["acceptance"]["deterministic_metric_model_limits"]
        self.assertEqual(limits["cx"], 10160)
        self.assertEqual(limits["decomposed_depth"], 23477)
        self.assertEqual(limits["serialized_openqasm2_bytes"], 470551)
        self.assertFalse(self.contract["authorization"]["provider_submission"])
        self.assertFalse(self.contract["authorization"]["paid_execution"])

    def test_digest_and_threshold_mutations_fail_closed(self):
        changed = copy.deepcopy(self.contract)
        changed["acceptance"]["absolute_safety_ceilings"][
            "serialized_openqasm2_bytes"
        ] += 1
        errors = validate_preregistration(changed)
        self.assertIn("absolute_safety_ceiling_mismatch", errors)
        self.assertIn("contract_digest_mismatch", errors)


if __name__ == "__main__":
    unittest.main()
