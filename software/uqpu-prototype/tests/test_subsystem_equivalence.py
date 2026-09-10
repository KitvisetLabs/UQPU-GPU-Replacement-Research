import unittest

from uqpu.subsystem_equivalence import (
    ComputeServiceContract,
    ComputeServiceMeasurement,
    StateServiceContract,
    StateServiceMeasurement,
)


class SubsystemEquivalenceTests(unittest.TestCase):
    def test_compute_requires_throughput_latency_and_quality(self):
        contract = ComputeServiceContract(100.0, 0.01, 0.99)
        self.assertTrue(contract.accepts(ComputeServiceMeasurement(120.0, 0.008, 0.995)))
        self.assertFalse(contract.accepts(ComputeServiceMeasurement(120.0, 0.02, 0.995)))
        self.assertFalse(contract.accepts(ComputeServiceMeasurement(90.0, 0.008, 0.995)))
        self.assertFalse(contract.accepts(ComputeServiceMeasurement(120.0, 0.008, 0.98)))

    def test_state_service_rejects_capacity_only_equivalence(self):
        contract = StateServiceContract(
            min_capacity_bytes=1_000_000,
            min_read_bandwidth_bytes_per_second=1_000_000_000.0,
            min_write_bandwidth_bytes_per_second=500_000_000.0,
            max_read_latency_seconds=0.001,
            max_write_latency_seconds=0.002,
            min_retention_seconds=3600.0,
            random_access_required=True,
            persistence_required=True,
            min_recovery_probability=0.999,
        )
        capacity_only = StateServiceMeasurement(
            capacity_bytes=10_000_000,
            read_bandwidth_bytes_per_second=1.0,
            write_bandwidth_bytes_per_second=1.0,
            read_latency_seconds=10.0,
            write_latency_seconds=10.0,
            retention_seconds=1.0,
            random_access=False,
            persistent=False,
            recovery_probability=0.5,
        )
        self.assertFalse(contract.accepts(capacity_only))

    def test_state_service_full_semantics_can_pass(self):
        contract = StateServiceContract(
            1_000,
            100.0,
            50.0,
            0.1,
            0.2,
            60.0,
            True,
            True,
            0.99,
        )
        measurement = StateServiceMeasurement(
            2_000,
            200.0,
            100.0,
            0.05,
            0.1,
            120.0,
            True,
            True,
            0.999,
        )
        self.assertTrue(contract.accepts(measurement))


if __name__ == "__main__":
    unittest.main()
