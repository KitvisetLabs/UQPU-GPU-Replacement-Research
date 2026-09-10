import math
import unittest

from uqpu.output_information import (
    binary_entropy_bits,
    bitstring_assignment_output_floor_bits,
    fano_mutual_information_lower_bound_bits,
    fixed_width_output_bitrate_bps,
    minimum_bits_for_distinguishable_outcomes,
)


class OutputInformationTests(unittest.TestCase):
    def test_exact_distinguishable_outcome_floor(self):
        expected = {
            1: 0,
            2: 1,
            3: 2,
            4: 2,
            8: 3,
            64: 6,
            256: 8,
            2**32: 32,
            2**128: 128,
            2**512: 512,
        }
        for outcomes, bits in expected.items():
            self.assertEqual(minimum_bits_for_distinguishable_outcomes(outcomes), bits)

    def test_full_bitstring_assignment_floor(self):
        for n in (0, 1, 6, 8, 32, 128, 512):
            self.assertEqual(bitstring_assignment_output_floor_bits(n), n)

    def test_fixed_width_bitrate(self):
        self.assertEqual(fixed_width_output_bitrate_bps(2**32, 1_000_000), 32_000_000)
        self.assertEqual(fixed_width_output_bitrate_bps(2**512, 1_000_000), 512_000_000)
        self.assertEqual(fixed_width_output_bitrate_bps(64, 0), 0)

    def test_binary_entropy_boundaries(self):
        self.assertEqual(binary_entropy_bits(0), 0)
        self.assertEqual(binary_entropy_bits(1), 0)
        self.assertAlmostEqual(binary_entropy_bits(0.5), 1.0)

    def test_fano_zero_error_matches_log_for_power_of_two(self):
        self.assertAlmostEqual(fano_mutual_information_lower_bound_bits(64, 0), 6.0)
        self.assertAlmostEqual(fano_mutual_information_lower_bound_bits(256, 0), 8.0)

    def test_fano_known_scenarios(self):
        self.assertAlmostEqual(
            fano_mutual_information_lower_bound_bits(64, 0.01),
            5.85943406486909,
            places=12,
        )
        self.assertAlmostEqual(
            fano_mutual_information_lower_bound_bits(64, 0.10),
            4.933276414060727,
            places=12,
        )
        self.assertLess(
            fano_mutual_information_lower_bound_bits(64, 0.10),
            fano_mutual_information_lower_bound_bits(64, 0.01),
        )

    def test_invalid_inputs(self):
        for bad in (0, -1, True, 1.5):
            with self.assertRaises(ValueError):
                minimum_bits_for_distinguishable_outcomes(bad)
        for bad in (-1, True, 1.5):
            with self.assertRaises(ValueError):
                bitstring_assignment_output_floor_bits(bad)
        for bad in (-1.0, float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                fixed_width_output_bitrate_bps(2, bad)
        for bad in (-0.1, 1.1, float("nan")):
            with self.assertRaises(ValueError):
                binary_entropy_bits(bad)
            with self.assertRaises(ValueError):
                fano_mutual_information_lower_bound_bits(2, bad)


if __name__ == "__main__":
    unittest.main()
