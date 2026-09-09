import unittest
from uqpu.eight_lane_scoreboard import LaneProgress, validate_complete_cycle
from uqpu.state_service import StatePlan, StateStrategy, choose_lower_materialization
from uqpu.workload_contracts import first_verified_win_candidates
from uqpu.manufacturing_equipment import baseline_quantum_chip_toolchain


class EightLaneBatchTests(unittest.TestCase):
    def test_eight_lane_cycle_requires_all_lanes(self):
        rows=tuple(LaneProgress(x,1,0,1,1) for x in "ABCDEFGH")
        validate_complete_cycle(rows)

    def test_missing_lane_rejected(self):
        rows=tuple(LaneProgress(x,1,0,1,1) for x in "ABCDEFG")
        with self.assertRaises(ValueError):
            validate_complete_cycle(rows)

    def test_state_plan_minimizes_materialization(self):
        chosen=choose_lower_materialization((
            StatePlan(StateStrategy.MATERIALIZE_CLASSICAL,1000,0,True),
            StatePlan(StateStrategy.RECOMPUTE,100,2,False),
        ))
        self.assertEqual(chosen.strategy,StateStrategy.RECOMPUTE)

    def test_first_win_candidates_exist(self):
        self.assertGreaterEqual(len(first_verified_win_candidates()),4)

    def test_lane_g_toolchain_is_full_stack(self):
        self.assertGreaterEqual(len(baseline_quantum_chip_toolchain()),8)


if __name__=="__main__":
    unittest.main()
