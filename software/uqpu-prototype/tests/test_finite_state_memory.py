import math
import unittest

from uqpu.finite_state_memory import (
    entropy_bits,
    evaluate_finite_state_channel,
    evaluate_policy_set,
    make_environment,
    policy_fixtures,
    stationary_distribution,
)


class FiniteStateMemoryTests(unittest.TestCase):
    def test_stationary_two_state_chain_matches_closed_form(self):
        pi = stationary_distribution(((0.9, 0.1), (0.2, 0.8)))
        self.assertAlmostEqual(pi[0], 2 / 3, places=12)
        self.assertAlmostEqual(pi[1], 1 / 3, places=12)

    def test_nonunique_stationary_distribution_fails_closed(self):
        with self.assertRaises(ValueError):
            stationary_distribution(((1.0, 0.0), (0.0, 1.0)))

    def test_finite_state_rows_and_stationarity(self):
        result = evaluate_finite_state_channel(**policy_fixtures(0.8)["PREDICTIVE"])
        self.assertEqual(len(result.joint_transition), 4)
        for row in result.joint_transition:
            self.assertAlmostEqual(math.fsum(row), 1.0, places=12)
        self.assertLessEqual(result.stationary_residual, 1e-9)
        self.assertAlmostEqual(math.fsum(result.stationary_joint), 1.0, places=12)

    def test_objectives_are_finite_and_nonclaims_remain_null(self):
        report = evaluate_policy_set(0.8)
        for result in report["results"].values():
            self.assertTrue(math.isfinite(result["work_rate_kbt_ln2_per_round"]))
        self.assertIsNone(report["measured_energy_joules"])
        self.assertIsNone(report["accepted_useful_task_quality"])
        self.assertEqual(report["paid_qpu_jobs"], 0)

    def test_memoryless_limit_matches_HA_minus_HS(self):
        p0 = 1 / math.sqrt(2)
        policy = (((p0, 1 - p0), (p0, 1 - p0)),)
        env = (((1.0, 0.0), (0.5, 0.5)), ((1.0, 0.0), (0.5, 0.5)))
        update = ((((1.0,), (1.0,)), ((1.0,), (1.0,))),)
        result = evaluate_finite_state_channel(policy, update, env)
        p_s0 = p0 + (1 - p0) * 0.5
        expected = entropy_bits((p0, 1 - p0)) - entropy_bits((p_s0, 1 - p_s0))
        self.assertAlmostEqual(result.work_rate_kbt_ln2_per_round, expected, places=12)

    def test_invalid_environment_parameter_rejected(self):
        with self.assertRaises(ValueError):
            make_environment(1.0)


if __name__ == "__main__":
    unittest.main()
