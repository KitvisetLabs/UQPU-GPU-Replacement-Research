import unittest

from uqpu.memory import (
    MemoryCostProfile,
    MemoryFootprint,
    estimate_memory_cost,
    materialization_avoidance_ratio,
)


class MemoryTests(unittest.TestCase):
    def setUp(self):
        self.profile = MemoryCostProfile(
            accelerator_memory_usd_per_gb_second=1e-6,
            host_ram_usd_per_gb_second=1e-7,
            movement_joules_per_gb=5.0,
        )

    def test_memory_cost_positive(self):
        f = MemoryFootprint(
            accelerator_bytes=80 * 1024**3,
            host_ram_bytes=256 * 1024**3,
            bytes_moved=100 * 1024**3,
        )
        c = estimate_memory_cost(f, 1.0, self.profile)
        self.assertGreater(c.total, 0)

    def test_zero_runtime_zero_capacity_cost(self):
        f = MemoryFootprint(accelerator_bytes=1024**3)
        c = estimate_memory_cost(f, 0.0, self.profile)
        self.assertEqual(c.accelerator_memory, 0.0)

    def test_materialization_avoidance(self):
        ratio = materialization_avoidance_ratio(1000, 100)
        self.assertAlmostEqual(ratio, 0.9)

    def test_rejects_negative(self):
        with self.assertRaises(ValueError):
            MemoryFootprint(accelerator_bytes=-1).validate()
