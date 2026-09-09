import unittest
from uqpu.inverse_system import allocate_inverse_budget
from uqpu.system_baseline import ConventionalSystemCost,UQCSSystemCost,compare_system_cost

class SystemBaselineTests(unittest.TestCase):
    def test_complete_stack_total(self):
        self.assertEqual(ConventionalSystemCost(cpu=1,gpu=2,accelerator_memory=3,host_memory=4,storage=5).total,15)
    def test_advantage(self):
        r=compare_system_cost(ConventionalSystemCost(gpu=100,host_memory=10),UQCSSystemCost(quantum_compute=.5,memory=.5))
        self.assertEqual(r.ratio,110); self.assertTrue(r.reaches_100x); self.assertFalse(r.reaches_100m_x)
    def test_inverse_budget_ladder(self):
        b=allocate_inverse_budget(1.0); self.assertEqual(len(b),7); self.assertAlmostEqual(b[0].total_uqcs_budget,.01); self.assertAlmostEqual(b[-1].total_uqcs_budget,1e-8)
    def test_budget_components_sum(self):
        b=allocate_inverse_budget(2.0)[0]
        self.assertAlmostEqual(b.compute_budget+b.memory_budget+b.storage_budget+b.fabric_budget+b.control_qec_budget+b.power_operations_budget,b.total_uqcs_budget)
if __name__=="__main__": unittest.main()
