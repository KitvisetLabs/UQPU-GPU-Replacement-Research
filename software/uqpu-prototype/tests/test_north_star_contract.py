import unittest
from uqpu.north_star_contract import (
    DeviceEnvelope,
    DeviceMeasurement,
    ServiceMetric,
    assess_north_star,
)


class NorthStarContractTests(unittest.TestCase):
    def setUp(self):
        self.envelope = DeviceEnvelope(50_000, 300, 250, 20)
        self.local_device = DeviceMeasurement(40_000, 220, 180, 12, False, True)

    def test_full_measured_contract_can_pass(self):
        metrics = (
            ServiceMetric("accepted AI throughput", "accepted_outputs/s", 100, 120, "at_least", "MEASURED_END_TO_END", True),
            ServiceMetric("service latency", "ms", 10, 8, "at_most", "MEASURED_END_TO_END", True),
        )
        result = assess_north_star(metrics, self.envelope, self.local_device)
        self.assertEqual(result.coverage_fraction, 1.0)
        self.assertTrue(result.demonstrated)

    def test_remote_terminal_cannot_pass_final_physical_claim(self):
        metrics = (ServiceMetric("service", "tasks/s", 1, 2, "at_least", "MEASURED_END_TO_END", True),)
        remote = DeviceMeasurement(40_000, 220, 180, 12, True, True)
        self.assertFalse(assess_north_star(metrics, self.envelope, remote).demonstrated)

    def test_simulated_metric_cannot_be_demonstrated(self):
        metrics = (ServiceMetric("service", "tasks/s", 1, 2, "at_least", "SIMULATION", False),)
        result = assess_north_star(metrics, self.envelope, self.local_device)
        self.assertTrue(result.coverage_fraction == 1.0)
        self.assertFalse(result.evidence_complete)
        self.assertFalse(result.demonstrated)

    def test_failed_service_metric_blocks_claim(self):
        metrics = (ServiceMetric("latency", "ms", 10, 11, "at_most", "MEASURED_END_TO_END", True),)
        self.assertFalse(assess_north_star(metrics, self.envelope, self.local_device).demonstrated)

    def test_requires_explicit_metrics(self):
        with self.assertRaises(ValueError):
            assess_north_star((), self.envelope, self.local_device)


if __name__ == "__main__":
    unittest.main()
