import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[3]


class ProjectInvariantTests(unittest.TestCase):
    def test_project_charter_exists(self):
        self.assertTrue((ROOT / "PROJECT_CHARTER.md").exists())

    def test_permanent_mission_markers(self):
        text = (ROOT / "PROJECT_CHARTER.md").read_text(encoding="utf-8")
        markers = [
            "GPU Functional Replacement",
            "Quantum Cloud Portability",
            "100×",
            "100,000,000×",
            "Continuous Provider Discovery",
            "Evidence Discipline",
        ]
        for marker in markers:
            self.assertIn(marker, text)

    def test_version_invariants_include_all_ids(self):
        text = (ROOT / "VERSION_INVARIANTS.md").read_text(encoding="utf-8")
        for i in range(1, 14):
            self.assertIn(f"INV-{i:03d}", text)

    def test_goals_preserve_cloud_and_cost_targets(self):
        text = (ROOT / "GOALS.md").read_text(encoding="utf-8")
        self.assertIn("quantum cloud", text.lower())
        self.assertIn("100×", text)
        self.assertIn("100,000,000×", text)


    def test_memory_scope_is_permanent(self):
        charter = (ROOT / "PROJECT_CHARTER.md").read_text(encoding="utf-8")
        goals = (ROOT / "GOALS.md").read_text(encoding="utf-8")
        self.assertIn("VRAM/HBM", charter)
        self.assertIn("host-RAM", charter)
        self.assertIn("MEMORY_REPLACEMENT.md", goals)

if __name__ == "__main__":
    unittest.main()
