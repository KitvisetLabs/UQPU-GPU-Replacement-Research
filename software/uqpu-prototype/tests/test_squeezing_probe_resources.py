import math
import unittest

from uqpu.fundamental_limits import (
    squeezed_vacuum_mean_photon_number,
    squeezed_vacuum_squeezing_for_mean_photon_number,
)


class SqueezingProbeResourceTests(unittest.TestCase):
    def test_single_mode_squeezed_vacuum_formula_and_inverse(self):
        for r in (0.0, 0.1, 1.0, 3.0):
            nbar = squeezed_vacuum_mean_photon_number(r)
            self.assertAlmostEqual(nbar, math.sinh(r) ** 2)
            self.assertAlmostEqual(
                squeezed_vacuum_squeezing_for_mean_photon_number(nbar),
                r,
            )

    def test_source_log_squeezing_example_scales_probe_photons_with_instance_size(self):
        # Source Appendix E.4 uses r = 0.5*log(n) in a separate squeezing-only
        # example. The identity below shows nbar=(n + 1/n - 2)/4 = Theta(n).
        ratios = []
        for n in (100.0, 10_000.0, 1_000_000.0):
            r = 0.5 * math.log(n)
            nbar = squeezed_vacuum_mean_photon_number(r)
            expected = (n + 1.0 / n - 2.0) / 4.0
            self.assertAlmostEqual(nbar, expected, places=7)
            ratios.append(nbar / n)

        self.assertGreater(ratios[1], ratios[0])
        self.assertGreater(ratios[2], ratios[1])
        self.assertAlmostEqual(ratios[2], 0.25, delta=1e-6)

    def test_invalid_probe_resource_inputs_fail_closed(self):
        for bad in (-1.0, float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                squeezed_vacuum_mean_photon_number(bad)
        for bad in (-1.0, float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                squeezed_vacuum_squeezing_for_mean_photon_number(bad)


if __name__ == "__main__":
    unittest.main()
