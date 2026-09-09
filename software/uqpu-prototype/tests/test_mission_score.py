import unittest

from uqpu.mission_score import MissionImpact, mission_gate


class MissionScoreTests(unittest.TestCase):
    def test_higher_benefit_same_effort_scores_higher(self):
        a = MissionImpact(cost_reduction_leverage=1, estimated_effort=1)
        b = MissionImpact(cost_reduction_leverage=2, estimated_effort=1)
        self.assertGreater(b.score, a.score)

    def test_effort_penalizes_score(self):
        a = MissionImpact(uncertainty_reduction=2, estimated_effort=1)
        b = MissionImpact(uncertainty_reduction=2, estimated_effort=4)
        self.assertGreater(a.score, b.score)

    def test_mission_gate_rejects_no_impact(self):
        r = mission_gate()
        self.assertFalse(r.advances_original_mission)

    def test_mission_gate_accepts_real_impact(self):
        r = mission_gate(improves_cost=True, removes_blocker=True)
        self.assertTrue(r.advances_original_mission)
        self.assertIn("cost_per_useful_task", r.reasons)


if __name__ == "__main__":
    unittest.main()
