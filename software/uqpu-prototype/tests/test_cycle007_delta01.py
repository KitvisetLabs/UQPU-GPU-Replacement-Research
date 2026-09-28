from copy import deepcopy
import hashlib
import json
from pathlib import Path
import unittest

from uqpu.cycle007_delta01 import audit_dimension_contracts


ROOT = Path(__file__).resolve().parents[3]
UMRL_PATH = ROOT / "benchmarks/experiments/cycle006-delta01-unified-math-goal-registry.json"
SCM_PATH = ROOT / "benchmarks/experiments/cycle006-delta01-scm-lokathibodi-math-registry.json"
ARTIFACT = ROOT / "benchmarks/results/cycle007-delta01-umrl-dimension-audit.json"
LEDGER = ROOT / "benchmarks/results/cycle007-delta01-synchronized-lane-ledger.json"


def _read(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class Cycle007Delta01Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.umrl = _read(UMRL_PATH)
        cls.scm = _read(SCM_PATH)

    def test_existing_registries_are_typed_but_not_machine_dimensioned(self):
        result = audit_dimension_contracts(self.umrl, self.scm)
        self.assertTrue(result["valid_registry_structure"], result["errors"])
        self.assertEqual(result["equation_count"], {"umrl": 30, "scm": 19})
        self.assertEqual(result["goal_count"], 23)
        self.assertEqual(result["variable_declaration_count"], 134)
        self.assertEqual(result["unit_or_type_present_count"], 134)
        self.assertEqual(result["quantity_kind_count"], 0)
        self.assertEqual(result["unit_code_count"], 0)
        self.assertEqual(result["machine_dimension_vector_count"], 0)
        self.assertFalse(result["dimensionally_auditable"])
        self.assertFalse(result["dimensional_consistency_claim"])
        self.assertEqual(set(result["lane_audit"]), {
            "A", "B", "C", "D", "E", "F", "G", "H",
            "FND/EQN", "SCM", "AI-COST", "QOS/QSVT",
        })
        self.assertTrue(all(row["umrl_variables"] for row in result["lane_audit"].values()))
        self.assertEqual(result["lane_audit"]["SCM"]["scm_variables"], 55)

    def test_dimension_vectors_require_exact_rational_exponents(self):
        umrl = deepcopy(self.umrl)
        variable = umrl["equations"][0]["variables"][0]
        variable["dimension_vector"] = {"length": "not-a-rational"}
        result = audit_dimension_contracts(umrl, self.scm)
        self.assertFalse(result["valid_registry_structure"])
        self.assertEqual(result["invalid_machine_dimension_vector_count"], 1)
        self.assertFalse(result["dimensional_consistency_claim"])

    def test_missing_free_text_label_fails_the_audit(self):
        scm = deepcopy(self.scm)
        del scm["equations"][0]["variables"][0]["unit_or_type"]
        result = audit_dimension_contracts(self.umrl, scm)
        self.assertFalse(result["valid_registry_structure"])
        self.assertTrue(any("scm_variable_type_label_missing" in e for e in result["errors"]))

    def test_committed_audit_artifact_matches_the_generator(self):
        artifact = _read(ARTIFACT)
        regenerated = audit_dimension_contracts(self.umrl, self.scm)
        regenerated["source_registries"] = artifact["source_registries"]
        self.assertEqual(artifact, regenerated)

    def test_checkpoint_ledger_records_progress_in_all_twelve_lanes(self):
        ledger = _read(LEDGER)
        self.assertEqual(ledger["cycle"], "007")
        self.assertTrue(ledger["full_cycle_closeout_pending"])
        self.assertEqual(ledger["validation"]["cycle007_focused_tests"]["passed"], 5)
        self.assertEqual(ledger["validation"]["full_prototype_suite"]["passed"], 444)
        self.assertEqual(ledger["validation"]["full_prototype_suite"]["skipped_optional"], 8)
        self.assertEqual(set(ledger["lanes"]), {
            "A", "B", "C", "D", "E", "F", "G", "H",
            "FND/EQN", "SCM", "AI-COST", "QOS/QSVT",
        })
        self.assertTrue(all(
            row["status"] == "BLOCKED_WITH_PROGRESS"
            and row["machine_dimension_vectors"] == 0
            for row in ledger["lanes"].values()
        ))
        self.assertEqual(
            ledger["audit_artifact_sha256"],
            hashlib.sha256(ARTIFACT.read_bytes()).hexdigest(),
        )


if __name__ == "__main__":
    unittest.main()
