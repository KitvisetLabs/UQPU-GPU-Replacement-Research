import unittest
from uqpu.hardware import QuantumHardwareProfile
from uqpu.qec import SurfaceCodeEstimator


class QECTests(unittest.TestCase):
    def setUp(self):
        self.profile = QuantumHardwareProfile(
            "q", 1e-4, 1e-2, 1e-6, 1e-6, 1e9, 1e9,
            100, 1000, 1_000_000, 10_000_000, 0.5
        )

    def test_distance_is_odd(self):
        e = SurfaceCodeEstimator(self.profile)
        d = e.choose_distance(1e-10)
        self.assertGreaterEqual(d, 3)
        self.assertEqual(d % 2, 1)

    def test_more_stringent_target_never_reduces_distance(self):
        e = SurfaceCodeEstimator(self.profile)
        self.assertGreaterEqual(e.choose_distance(1e-12), e.choose_distance(1e-8))

    def test_total_physical_qubits(self):
        e = SurfaceCodeEstimator(self.profile)
        r = e.estimate(100, 1000)
        self.assertEqual(
            r.total_physical_qubits,
            100 * r.physical_qubits_per_logical,
        )
        self.assertGreater(r.qec_runtime_seconds, 0)
