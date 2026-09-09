import unittest
from uqpu.hardware import QuantumHardwareProfile, GPUHardwareProfile


class HardwareProfileTests(unittest.TestCase):
    def test_quantum_profile_validates(self):
        p = QuantumHardwareProfile(
            "q", 1e-4, 1e-2, 1e-6, 1e-6, 1e9, 1e9,
            100, 1000, 1_000_000, 10_000_000, 0.5
        )
        p.validate()
        self.assertGreater(p.amortized_capex_per_second, 0)

    def test_rejects_error_above_threshold(self):
        p = QuantumHardwareProfile(
            "q", 2e-2, 1e-2, 1e-6, 1e-6, 1e9, 1e9,
            100, 1000, 1, 10, 0.5
        )
        with self.assertRaises(ValueError):
            p.validate()

    def test_gpu_profile(self):
        p = GPUHardwareProfile("g", 10_000, 10_000_000, 0.5, 500, 200)
        p.validate()
        self.assertGreater(p.amortized_capex_per_second, 0)
