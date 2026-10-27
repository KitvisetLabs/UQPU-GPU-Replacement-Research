import math
import unittest

from uqpu.frontier_hypothesis import FrontierHypothesis
from uqpu.fundamental_limits import (
    BOLTZMANN_CONSTANT_J_PER_K,
    HBAR_J_S,
    PLANCK_CONSTANT_J_S,
    low_temperature_gap_thermalization_min_seconds,
    planckian_thermalization_min_seconds,
    landauer_max_bit_erasures_per_joule,
    landauer_minimum_joule,
    landauer_minimum_joule_per_bit,
    margolus_levitin_min_seconds,
    fault_tolerance_memory_log_overhead_term,
    bounded_observable_hoeffding_radii,
)



class BoundedObservableConfidenceTests(unittest.TestCase):
    def test_hoeffding_radius_matches_published_formula(self):
        radii = bounded_observable_hoeffding_radii([10000, 20000, 5000], 0.01)
        expected = math.sqrt(2.0 * math.log(2.0 * 3 / 0.01) / 10000)
        self.assertAlmostEqual(radii[0], expected)
        self.assertAlmostEqual(
            radii[1],
            math.sqrt(2.0 * math.log(2.0 * 3 / 0.01) / 20000),
        )
        self.assertAlmostEqual(
            radii[2],
            math.sqrt(2.0 * math.log(2.0 * 3 / 0.01) / 5000),
        )

    def test_radius_respects_shots_observable_count_and_confidence(self):
        base = bounded_observable_hoeffding_radii([1000, 1000], 0.05)
        more_shots = bounded_observable_hoeffding_radii([4000, 4000], 0.05)
        more_observables = bounded_observable_hoeffding_radii([1000] * 4, 0.05)
        tighter_confidence = bounded_observable_hoeffding_radii([1000, 1000], 0.001)
        self.assertAlmostEqual(more_shots[0], base[0] / 2.0)
        self.assertGreater(more_observables[0], base[0])
        self.assertGreater(tighter_confidence[0], base[0])

    def test_invalid_shot_counts_and_failure_probabilities_are_rejected(self):
        for shots in ([], [0], [-1], [True], [1.0], "100"):
            with self.assertRaises(ValueError):
                bounded_observable_hoeffding_radii(shots, 0.05)
        for delta in (0.0, 1.0, -0.1, float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                bounded_observable_hoeffding_radii([100], delta)


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

    def test_planckian_thermalization_bound_is_conditional_and_scales_as_inverse_temperature(self):
        at_300_k = planckian_thermalization_min_seconds(300.0)
        self.assertAlmostEqual(
            at_300_k,
            HBAR_J_S / (2.0 * BOLTZMANN_CONSTANT_J_PER_K * 300.0),
        )
        self.assertAlmostEqual(
            planckian_thermalization_min_seconds(600.0),
            at_300_k / 2.0,
        )

    def test_low_temperature_gap_bound(self):
        self.assertAlmostEqual(
            low_temperature_gap_thermalization_min_seconds(2.0),
            HBAR_J_S / 2.0,
        )

    def test_invalid_physical_inputs(self):
        for bad in (0.0, -1.0, float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                landauer_minimum_joule_per_bit(bad)
            with self.assertRaises(ValueError):
                margolus_levitin_min_seconds(bad)
            with self.assertRaises(ValueError):
                planckian_thermalization_min_seconds(bad)
            with self.assertRaises(ValueError):
                low_temperature_gap_thermalization_min_seconds(bad)
        with self.assertRaises(ValueError):
            landauer_minimum_joule(-1.0, 300.0)


class FaultToleranceMemoryScalingTests(unittest.TestCase):
    def test_published_width_duration_examples(self):
        expected_term = math.log(1e12)
        self.assertAlmostEqual(
            fault_tolerance_memory_log_overhead_term(1, 10**9, 1e-3),
            expected_term,
        )
        self.assertAlmostEqual(
            fault_tolerance_memory_log_overhead_term(1024, 10**9, 1e-3),
            expected_term / 1024,
        )

    def test_reliability_term_increases_with_duration_and_tighter_error(self):
        baseline = fault_tolerance_memory_log_overhead_term(32, 10**6, 1e-3)
        self.assertGreater(
            fault_tolerance_memory_log_overhead_term(32, 10**9, 1e-3),
            baseline,
        )
        self.assertGreater(
            fault_tolerance_memory_log_overhead_term(32, 10**6, 1e-6),
            baseline,
        )
        self.assertLess(
            fault_tolerance_memory_log_overhead_term(64, 10**6, 1e-3),
            baseline,
        )

    def test_invalid_width_duration_and_error_are_rejected(self):
        for width in (0, -1, True, 1.0):
            with self.assertRaises(ValueError):
                fault_tolerance_memory_log_overhead_term(width, 10, 1e-3)
        for steps in (0, -1, True, 1.0):
            with self.assertRaises(ValueError):
                fault_tolerance_memory_log_overhead_term(1, steps, 1e-3)
        for epsilon in (0.0, 1.0, -1.0, float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                fault_tolerance_memory_log_overhead_term(1, 10, epsilon)


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
