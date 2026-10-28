import math
import unittest

from uqpu.hamiltonian_lower_bound import coefficient_tail_tradeoff_proxy


class HamiltonianLowerBoundProxyTests(unittest.TestCase):
    def test_uniform_profile_matches_hand_calculated_tradeoff(self):
        result = coefficient_tail_tradeoff_proxy(
            (0.25, 0.25, 0.25, 0.25),
            simulation_time=1.0,
            trace_distance_error=0.1,
        )
        self.assertEqual(result.evidence_label, "ASYMPTOTIC_TRADEOFF_PROXY_ONLY")
        self.assertEqual(result.coefficient_count, 4)
        self.assertEqual([point.cut for point in result.candidates], [0, 1, 2, 3, 4])
        self.assertAlmostEqual(result.candidates[0].tail_weight, 1.0)
        self.assertAlmostEqual(result.candidates[2].tail_weight, 0.5)
        self.assertAlmostEqual(result.candidates[4].tail_weight, 0.0)
        self.assertEqual(result.minimizing_cut, 3)
        self.assertAlmostEqual(result.minimum_proxy_value, 3.625)

    def test_nonuniform_profile_is_normalized_and_tail_is_monotone(self):
        result = coefficient_tail_tradeoff_proxy(
            (0.5, 0.25, 0.125, 0.0625, 0.0625),
            simulation_time=0.8,
            trace_distance_error=0.05,
        )
        tails = [point.tail_weight for point in result.candidates]
        self.assertTrue(all(left >= right for left, right in zip(tails, tails[1:])))
        self.assertAlmostEqual(tails[0], 1.0)
        self.assertAlmostEqual(tails[-1], 0.0)
        self.assertTrue(all(math.isfinite(point.proxy_value) for point in result.candidates))
        self.assertEqual(
            result.minimum_proxy_value,
            min(point.proxy_value for point in result.candidates),
        )

    def test_rejects_invalid_physics_model_inputs(self):
        invalid_profiles = (
            (),
            (0.25, 0.5, 0.25),
            (0.2, 0.2, 0.2),
            (0.5, 0.5, 0.0),
            (0.5, float("nan"), 0.5),
            (True,),
        )
        for profile in invalid_profiles:
            with self.subTest(profile=profile):
                with self.assertRaises(ValueError):
                    coefficient_tail_tradeoff_proxy(profile, 1.0, 0.1)
        for time_value, epsilon in ((0.0, 0.1), (-1.0, 0.1), (1.0, 0.0), (1.0, 1.0)):
            with self.subTest(time_value=time_value, epsilon=epsilon):
                with self.assertRaises(ValueError):
                    coefficient_tail_tradeoff_proxy((1.0,), time_value, epsilon)

    def test_proxy_does_not_claim_finite_instance_or_physical_bound(self):
        result = coefficient_tail_tradeoff_proxy((1.0,), 2.0, 0.2)
        self.assertEqual(result.evidence_label, "ASYMPTOTIC_TRADEOFF_PROXY_ONLY")
        self.assertEqual(len(result.candidates), 2)
        self.assertEqual(result.candidates[-1].tail_weight, 0.0)


if __name__ == "__main__":
    unittest.main()
