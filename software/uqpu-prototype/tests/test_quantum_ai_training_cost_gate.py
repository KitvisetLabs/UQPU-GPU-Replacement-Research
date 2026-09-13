import math
import unittest

from uqpu.quantum_ai_training_cost_gate import (
    build_contract,
    canonical_batch038_result,
    normalized_cost_fraction,
    required_accelerated_reduction,
)


class QuantumAITrainingCostGateTests(unittest.TestCase):
    def test_canonical_required_reduction(self):
        low = build_contract(
            baseline_usd=10_000_000_000_000.0,
            target_thb=50_000.0,
            thb_per_usd=33.045,
        )
        high = build_contract(
            baseline_usd=100_000_000_000_000.0,
            target_thb=50_000.0,
            thb_per_usd=33.045,
        )
        self.assertTrue(math.isclose(low.required_reduction, 6_609_000_000.0, rel_tol=1e-12))
        self.assertTrue(math.isclose(high.required_reduction, 66_090_000_000.0, rel_tol=1e-12))
        self.assertTrue(math.isclose(low.maximum_residual_fraction, 1.5130882130428204e-10, rel_tol=1e-12))
        self.assertTrue(math.isclose(high.maximum_residual_fraction, 1.5130882130428203e-11, rel_tol=1e-12))

    def test_100_million_x_is_not_enough_for_canonical_target(self):
        result = canonical_batch038_result()
        self.assertEqual(result["one_hundred_million_x_cost_thb"]["from_10_trillion_usd"], 3_304_500.0)
        self.assertEqual(result["one_hundred_million_x_cost_thb"]["from_100_trillion_usd"], 33_045_000.0)
        self.assertGreater(result["one_hundred_million_x_cost_thb"]["from_10_trillion_usd"], 50_000.0)

    def test_residual_floor_can_make_target_impossible(self):
        target_fraction = 1.0 / 6_609_000_000.0
        self.assertIsNone(required_accelerated_reduction(residual_fraction=1e-6, target_fraction=target_fraction))

    def test_amdahl_cost_fraction(self):
        observed = normalized_cost_fraction(residual_fraction=0.01, accelerated_reduction=100.0)
        self.assertTrue(math.isclose(observed, 0.0199, rel_tol=1e-12))

    def test_rejects_invalid_inputs(self):
        with self.assertRaises(ValueError):
            build_contract(baseline_usd=0, target_thb=50_000, thb_per_usd=33.045)
        with self.assertRaises(ValueError):
            normalized_cost_fraction(residual_fraction=-0.1, accelerated_reduction=2)


if __name__ == "__main__":
    unittest.main()
