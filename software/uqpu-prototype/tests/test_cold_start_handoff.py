import json
from pathlib import Path
import tempfile
import unittest

from uqpu.cold_start_handoff import audit_repository, validate_commit_message


ROOT = Path(__file__).resolve().parents[3]


class ColdStartHandoffTests(unittest.TestCase):
    def test_canonical_repository_passes_cold_start_audit(self):
        report = audit_repository(ROOT)
        self.assertEqual(report["errors"], [])
        self.assertEqual(report["status"], "READY_FOR_COLD_START")
        self.assertEqual(report["lanes_checked"], list("ABCDEFGHI"))
        self.assertEqual(report["integration_pairs_checked"], 36)

    def test_main_and_non_main_commit_trailers_are_distinct(self):
        self.assertEqual(validate_commit_message("x\n\nResearch-Sync: main", "main"), [])
        self.assertEqual(
            validate_commit_message("x\n\nResearch-Sync: pending-main", "research/test"), []
        )
        self.assertIn(
            "missing_commit_trailer:Research-Sync: main",
            validate_commit_message("Research-Sync: pending-main", "main"),
        )

    def test_commit_trailer_uses_canonical_main_ancestry(self):
        # A stale sync ref can point to a commit already canonical on main.
        self.assertEqual(
            validate_commit_message(
                """x

Research-Sync: main""", "sync/stale-ref", commit_is_on_main=True
            ),
            [],
        )
        # An unmerged branch must still declare pending-main.
        self.assertEqual(
            validate_commit_message(
                """x

Research-Sync: pending-main""", "sync/new-work"
            ),
            [],
        )
        self.assertIn(
            "missing_commit_trailer:Research-Sync: pending-main",
            validate_commit_message(
                """x

Research-Sync: main""", "sync/new-work"
            ),
        )

    def test_missing_lane_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "integration").mkdir()
            manifest = json.loads((ROOT / "integration/COLD_START_HANDOFF_MANIFEST.json").read_text())
            manifest["lanes"].pop("I")
            (root / "integration/COLD_START_HANDOFF_MANIFEST.json").write_text(json.dumps(manifest))
            (root / "integration/eight_lane_manifest.json").write_text(
                (ROOT / "integration/eight_lane_manifest.json").read_text()
            )
            (root / "AGENTS.md").write_text("# empty")
            report = audit_repository(root)
            self.assertEqual(report["status"], "HANDOFF_INCOMPLETE")
            self.assertIn("handoff_lanes_must_equal_A_through_I", report["errors"])


if __name__ == "__main__":
    unittest.main()
