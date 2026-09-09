import unittest

from uqpu.inverse_hardware import derive_hardware_requirements
from uqpu.inverse_system import allocate_inverse_budget
from uqpu.photonics_budget import derive_photonics_budget
from uqpu.qec_budget import derive_qec_budget


class InverseHardwareTests(unittest.TestCase):
    def test_harder_targets_reduce_power_budget(self):
        budgets = allocate_inverse_budget(1.0)
        reqs = derive_hardware_requirements(
            budgets,
            reference_task_seconds=1.0,
            reference_bandwidth_gbps=1000,
            reference_power_watts=10000,
            reference_loss_db=3.0,
        )
        self.assertLess(reqs[-1].max_operating_power_watts, reqs[0].max_operating_power_watts)
        self.assertGreater(reqs[-1].min_effective_bandwidth_gbps, reqs[0].min_effective_bandwidth_gbps)

    def test_qec_budget(self):
        r = derive_qec_budget(
            100,
            0.001,
            qec_cost_per_second=0.0001,
            physical_qubit_cost_per_task=1e-9,
            non_clifford_cost_per_op=1e-12,
        )
        self.assertGreater(r.max_qec_runtime_seconds, 0)
        self.assertGreater(r.max_physical_qubits, 0)
        self.assertGreater(r.max_non_clifford_operations, 0)

    def test_photonics_tightens_with_target(self):
        a = derive_photonics_budget(100, 0.001)
        b = derive_photonics_budget(100_000_000, 1e-9)
        self.assertLess(b.max_total_loss_db, a.max_total_loss_db)
        self.assertGreaterEqual(b.min_detector_efficiency, a.min_detector_efficiency)


if __name__ == "__main__":
    unittest.main()
