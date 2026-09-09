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
        for i in range(1, 19):
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


    def test_strategic_master_plan_preserved(self):
        master = ROOT / "docs" / "KANUSANAN_PONGPANNA_MODEL.md"
        self.assertTrue(master.exists())
        text = master.read_text(encoding="utf-8")
        required_ids = [
            "15BBwIquwt5BJufn3HrPac5zc9tUX67Yo",
            "1RcCJwpw0D2VTvAZVfrYlhVKEd77bKzZG",
            "1YdzFgO_oeoA-oq7B_qR2L3lOavzJuzh5",
            "134q6qkQe8NntWS_yQFLHZVqFRlXGce-1",
            "1uoVrjHbS5b2g2T75roUqdGwZZ-uyDQ0f",
            "195qPMZ4JvitQENpJRpQL1JhMTbNwmZa8",
            "1vP3l4kwEaqeJteduj8ShOAhV3WUSELkB",
            "1mlG8-dqyA-dprBf-e9fOWgzyJHMy-RyX",
            "1Etc0gaOG5KsaLM3LGichsksYQXPvC6-9",
            "1MCfNJ-9x1G3Ap09Xho2lgz00tBSFzSJu",
            "1I9oE9c2OxZZPub5Gxg4SW00RhVdbT34z",
            "1iy9TaBIn3oUdzoUPbTlsnDHVLSxNXE41",
        ]
        for file_id in required_ids:
            self.assertIn(file_id, text)
        self.assertIn("https://abacus.ai/", text)
        self.assertIn("deep-agents-langchain", text)
        self.assertIn("youtube.com/playlist", text)

    def test_readme_links_strategic_master_plan(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/KANUSANAN_PONGPANNA_MODEL.md", readme)


    def test_cross_chat_operating_system_bootstrap(self):
        charter = (ROOT / "PROJECT_CHARTER.md").read_text(encoding="utf-8")
        invariants = (ROOT / "VERSION_INVARIANTS.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        ros = (ROOT / "docs" / "RESEARCH_OPERATING_SYSTEM.md").read_text(encoding="utf-8")
        self.assertIn("INV-018", charter)
        self.assertIn("INV-018", invariants)
        self.assertIn("GitHub is the canonical project memory", readme)
        self.assertIn("docs/RESEARCH_OPERATING_SYSTEM.md", readme)
        self.assertIn("six-lane Parallel Simple Mode", readme)
        for lane in ["Lane A", "Lane B", "Lane C", "Lane D", "Lane E", "Lane F"]:
            self.assertIn(lane, ros)

if __name__ == "__main__":
    unittest.main()
