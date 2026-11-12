"""Regression guards for the 2026-10-27 literature integration records.

These tests check repository linkage and evidence labels only. They do not
reproduce the external simulator or material-model experiments.
"""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[3]
INTEGRATION_RECORDS = (
    "integration/INT-20261027-QUASARQ-SIMULATOR.json",
    "integration/INT-20261027-NEURAL-MATERIAL-HYPERREDUCTION.json",
)
PERMANENT_ROOT_FILES = (
    "00_ULTIMATE_NORTH_STAR_DATA_CENTER_TO_PHONE.md",
    "00A_PERMANENT_AI_EQUATION_DISCOVERY_PRINCIPLE.md",
    "01_PANGOLA_BIOMASS_CARBON_TECHNOLOGY_STRATEGY.md",
    "02_ULTRA_LOW_COST_BIOMASS_BIO_OIL_STRATEGY.md",
    "03_FUSION_ELECTRICITY_COST_STRATEGY.md",
    "04_INTEREST_COST_AND_RND_FINANCE_STRATEGY.md",
    "05_FOUNDATIONAL_PHYSICS_MATHEMATICS_DEEP_FRONTIER.md",
    "06_AI_ASSISTED_PHYSICS_EQUATION_DISCOVERY.md",
    "docs/KANUSANAN_PONGPANNA_MODEL.md",
    "STRATEGIC_PLAN_REFERENCES.md",
)


class ResearchIntegrationRecordTests(unittest.TestCase):
    def test_records_parse_have_unique_ids_and_remain_evidence_bounded(self):
        records = []
        for relative_path in INTEGRATION_RECORDS:
            path = ROOT / relative_path
            self.assertTrue(path.is_file(), f"missing integration record: {relative_path}")
            record = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(record.get("schema"), "uqpu-eight-lane-integration-v1")
            self.assertEqual(record.get("date"), "2026-10-27")
            self.assertTrue(record.get("integration_id"))
            self.assertTrue(record.get("work_item_id"))
            self.assertEqual(record.get("status"), "PROPOSED")
            self.assertIn("LITERATURE_ONLY", record.get("evidence_class", ""))
            self.assertTrue(record.get("next_gate"))
            self.assertTrue(record.get("non_claims"))
            records.append(record)

        integration_ids = [record["integration_id"] for record in records]
        work_item_ids = [record["work_item_id"] for record in records]
        self.assertEqual(len(integration_ids), len(set(integration_ids)))
        self.assertEqual(len(work_item_ids), len(set(work_item_ids)))

    def test_declared_artifacts_and_permanent_root_files_exist(self):
        records = [
            json.loads((ROOT / relative_path).read_text(encoding="utf-8"))
            for relative_path in INTEGRATION_RECORDS
        ]
        for record in records:
            for key, value in record["artifacts"].items():
                if isinstance(value, str):
                    self.assertTrue(
                        (ROOT / value).is_file(),
                        f"{record['integration_id']} artifact {key} missing: {value}",
                    )

        for relative_path in PERMANENT_ROOT_FILES:
            self.assertTrue((ROOT / relative_path).is_file(), f"permanent file missing: {relative_path}")

    def test_daily_report_explicitly_covers_all_required_lanes(self):
        report = (ROOT / "integration/DAILY_CYCLE_2026-10-27_QUASARQ.md").read_text(encoding="utf-8")
        for lane in "ABCDEFGH":
            self.assertIn(f"**{lane} —", report, f"daily report missing Lane {lane}")
        self.assertIn("FND-001", report)
        self.assertIn("FND-006", report)
        self.assertIn("EQN-001", report)
        self.assertIn("INV-029", report)
        self.assertIn("INV-035", report)


if __name__ == "__main__":
    unittest.main()
