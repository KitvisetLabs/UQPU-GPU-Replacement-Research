import math
import unittest

from uqpu.frontier_hypothesis import FrontierHypothesis
from uqpu.fundamental_limits import (
    PLANCK_CONSTANT_J_S,
    landauer_max_bit_erasures_per_joule,
    landauer_minimum_joule,
    landauer_minimum_joule_per_bit,
    margolus_levitin_min_seconds,
)


class FundamentalLimitTests(unittest.TestCase):
    def test_landauer_room_temperature(self):
        value = landauer_minimum_joule_per_bit(300.0)
        self.assertAlmostEqual(value, 2.870978885078724e-21, places=32)
        self.assertAlmostEqual(
            landauer_max_bit_erasures_per_joule(300.0),
            3.4831325482652566e20,
            delta=1e7,
        )

    def test_landauer_scales_linearly(self):
        one = landauer_minimum_joule_per_bit(300.0)
        self.assertAlmostEqual(landauer_minimum_joule(10.0, 300.0), 10.0 * one)
        self.assertAlmostEqual(
            landauer_minimum_joule_per_bit(150.0), 0.5 * one
        )

    def test_margolus_levitin_bound(self):
        self.assertAlmostEqual(
            margolus_levitin_min_seconds(1.0), PLANCK_CONSTANT_J_S / 4.0
        )
        self.assertAlmostEqual(
            margolus_levitin_min_seconds(2.0), PLANCK_CONSTANT_J_S / 8.0
        )

    def test_invalid_physical_inputs(self):
        for bad in (0.0, -1.0, float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                landauer_minimum_joule_per_bit(bad)
            with self.assertRaises(ValueError):
                margolus_levitin_min_seconds(bad)
        with self.assertRaises(ValueError):
            landauer_minimum_joule(-1.0, 300.0)


class FrontierContractTests(unittest.TestCase):
    def candidate(self, **changes):
        data = dict(
            name="many-body primitive candidate",
            layer="F5",
            evidence_level="THEORY",
            mathematical_formulation="H(lambda) with encoded workload subspace",
            causal_mechanism="controlled many-body dynamics concentrates useful output",
            target_bottleneck="accepted-output repetitions",
            known_constraints=("unitarity", "measurement", "energy-time bound"),
            scaling_law="resource count R(n) must be measured against baseline",
            falsifier="show no accepted-output improvement at equal total resources",
            observable="accepted-output probability and total joule/accepted result",
            baseline="best matched conventional and gate-model baseline",
            resource_accounting=("state preparation", "control", "measurement", "I/O"),
        )
        data.update(changes)
        return FrontierHypothesis(**data)

    def test_complete_hypothesis_is_testable(self):
        h = self.candidate()
        h.validate()
        self.assertTrue(h.testable)

    def test_missing_mechanism_blocks_promotion(self):
        h = self.candidate(causal_mechanism="")
        self.assertFalse(h.testable)
        self.assertIn("causal_mechanism", h.missing_required_fields())
        with self.assertRaises(ValueError):
            h.validate()

    def test_unknown_evidence_label_is_rejected(self):
        with self.assertRaises(ValueError):
            self.candidate(evidence_level="MAGICAL_BREAKTHROUGH").validate()


class FrontierInvariantTests(unittest.TestCase):
    def test_deep_frontier_is_permanent_and_prominent(self):
        from pathlib import Path

        root = Path(__file__).resolve().parents[3]
        directive = root / "05_FOUNDATIONAL_PHYSICS_MATHEMATICS_DEEP_FRONTIER.md"
        self.assertTrue(directive.exists())
        self.assertIn("INV-034", (root / "VERSION_INVARIANTS.md").read_text())
        self.assertIn(directive.name, (root / "README.md").read_text())
        self.assertIn(directive.name, (root / "GOALS.md").read_text())
        text = directive.read_text()
        for marker in (
            "elementary-particle physics",
            "Landauer",
            "No-cloning",
            "Quantum speed limits",
            "falsifier",
            "FND-001",
            "FND-006",
        ):
            self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
