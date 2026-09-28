import copy
import json
from pathlib import Path
import unittest
from uqpu.cycle013_goal_registry import validate_registry

ROOT = Path(__file__).resolve().parents[3]
REGISTRY = json.loads((ROOT / "benchmarks/experiments/cycle013-delta01-typed-goal-registry.json").read_text())

class TypedGoalRegistryTests(unittest.TestCase):
    def test_all_twelve_lane_contracts_are_defined(self):
        result = validate_registry(REGISTRY)
        self.assertEqual(result, {"goal_count": 12, "lane_count": 12, "status": "VALID_DEFINITION_ONLY"})

    def test_missing_lane_fails_closed(self):
        data = copy.deepcopy(REGISTRY)
        data["goals"].pop()
        with self.assertRaises(ValueError):
            validate_registry(data)

    def test_duplicate_lane_fails_closed(self):
        data = copy.deepcopy(REGISTRY)
        data["goals"][-1]["lane"] = data["goals"][0]["lane"]
        with self.assertRaises(ValueError):
            validate_registry(data)

    def test_missing_falsifier_fails_closed(self):
        data = copy.deepcopy(REGISTRY)
        data["goals"][0]["falsifier"] = ""
        with self.assertRaises(ValueError):
            validate_registry(data)

    def test_scm_cannot_be_promoted_by_registry_status(self):
        data = copy.deepcopy(REGISTRY)
        next(g for g in data["goals"] if g["lane"] == "SCM")["status"] = "MEASURED"
        with self.assertRaises(ValueError):
            validate_registry(data)

if __name__ == "__main__":
    unittest.main()
