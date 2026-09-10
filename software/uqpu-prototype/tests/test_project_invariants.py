import pathlib
import re
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[3]


def invariant_ids(text: str) -> set[str]:
    return set(re.findall(r"INV-\d{3}", text))


class ProjectInvariantTests(unittest.TestCase):
    def test_project_charter_exists(self):
        self.assertTrue((ROOT / "PROJECT_CHARTER.md").exists())

    def test_permanent_mission_markers(self):
        text = (ROOT / "PROJECT_CHARTER.md").read_text(encoding="utf-8")
        markers = [
            "Functional Replacement",
            "Quantum Cloud Portability",
            "100×",
            "100,000,000×",
            "Continuous Provider Discovery",
            "Evidence Discipline",
        ]
        for marker in markers:
            self.assertIn(marker, text)

    def test_version_invariants_match_charter(self):
        charter = (ROOT / "PROJECT_CHARTER.md").read_text(encoding="utf-8")
        table = (ROOT / "VERSION_INVARIANTS.md").read_text(encoding="utf-8")
        charter_ids = invariant_ids(charter)
        table_ids = invariant_ids(table)
        self.assertTrue(charter_ids)
        self.assertTrue(charter_ids.issubset(table_ids))
        self.assertIn("INV-024", charter_ids)

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

    def test_ultimate_north_star_and_biomass_carbon_pillar_are_permanent(self):
        invariants = (ROOT / "VERSION_INVARIANTS.md").read_text(encoding="utf-8")
        goals = (ROOT / "GOALS.md").read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        north_star_path = ROOT / "00_ULTIMATE_NORTH_STAR_DATA_CENTER_TO_PHONE.md"
        carbon_path = ROOT / "01_PANGOLA_BIOMASS_CARBON_TECHNOLOGY_STRATEGY.md"
        self.assertIn("INV-029", invariants)
        self.assertIn("INV-030", invariants)
        self.assertTrue(north_star_path.exists())
        self.assertTrue(carbon_path.exists())
        self.assertIn(north_star_path.name, readme)
        self.assertIn(carbon_path.name, readme)
        self.assertIn("INV-029", goals)
        self.assertIn("INV-030", goals)
        carbon = carbon_path.read_text(encoding="utf-8")
        for material in ("Gold (Au)", "Copper (Cu)", "Silver (Ag)", "Lithium (Li)", "Cobalt (Co)", "Nickel (Ni)", "Rare-earth"):
            self.assertIn(material, carbon)
        self.assertIn("does **not** claim", carbon)
        moonshot = (ROOT / "software" / "uqpu-prototype" / "uqpu" / "moonshot_contract.py").read_text(encoding="utf-8")
        self.assertIn('"npu"', moonshot)

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
        self.assertIn("eight-lane", readme.lower())
        for lane in ["Lane A", "Lane B", "Lane C", "Lane D", "Lane E", "Lane F", "Lane G", "Lane H"]:
            self.assertIn(lane, ros)


if __name__ == "__main__":
    unittest.main()
