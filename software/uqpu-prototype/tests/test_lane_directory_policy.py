from __future__ import annotations

from itertools import combinations
import json
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[3]
LANE_ROOT = REPO_ROOT / "research_lanes"
MANIFEST = REPO_ROOT / "integration" / "eight_lane_manifest.json"
VERSION_INVARIANTS = REPO_ROOT / "VERSION_INVARIANTS.md"


class LaneDirectoryPolicyTests(unittest.TestCase):
    def test_all_eight_lane_directories_exist(self) -> None:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(set(manifest["lanes"]), set("ABCDEFGH"))
        for lane_id, lane in manifest["lanes"].items():
            folder = REPO_ROOT / lane["folder"]
            self.assertTrue(folder.is_dir(), f"Lane {lane_id} folder is missing: {folder}")
            self.assertTrue((folder / "README.md").is_file())

    def test_directory_depth_never_exceeds_policy(self) -> None:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        max_depth = int(manifest["max_directory_depth_from_repo_root"])
        self.assertEqual(max_depth, 16)
        violations = []
        for path in REPO_ROOT.rglob("*"):
            if not path.is_file():
                continue
            relative = path.relative_to(REPO_ROOT)
            directory_depth = len(relative.parts) - 1
            if directory_depth > max_depth:
                violations.append((str(relative), directory_depth))
        self.assertEqual(violations, [], f"Paths exceed {max_depth} directory levels: {violations}")

    def test_all_lane_pairs_are_reviewed_for_possible_integration(self) -> None:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        expected = {f"{a}<->{b}" for a, b in combinations("ABCDEFGH", 2)}
        actual = set(manifest["integration_review_pairs"])
        self.assertEqual(len(expected), 28)
        self.assertEqual(actual, expected)
        self.assertIn("D<->G", set(manifest["mandatory_high_leverage_links"]))

    def test_integration_contract_manifest_and_invariant_are_present(self) -> None:
        self.assertTrue((REPO_ROOT / "integration" / "LANE_INTERFACE_CONTRACT.md").is_file())
        self.assertTrue((REPO_ROOT / "integration" / "INTEGRATED_RESEARCH_BATCH_TEMPLATE.md").is_file())
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(manifest["priority_lane"], "A")
        invariants = VERSION_INVARIANTS.read_text(encoding="utf-8")
        self.assertIn("INV-028", invariants)
        self.assertIn("16 directory levels", invariants)


if __name__ == "__main__":
    unittest.main()
