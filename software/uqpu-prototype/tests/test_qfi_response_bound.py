import math
import unittest

from uqpu.qfi_response_bound import QFIResponseAudit


class QFIResponseBoundTests(unittest.TestCase):
    def test_pure_qubit_z_observable_saturates_bound(self):
        # |psi(theta)> = cos(theta)|0> + sin(theta)|1>; QFI_theta = 4.
        # For Z: <Z>=cos(2 theta), derivative=-2 sin(2 theta),
        # Var(Z)=sin(2 theta)^2. The inequality is saturated analytically.
        for theta in (0.1, 0.25, 0.7, 1.1):
            slope = -2.0 * math.sin(2.0 * theta)
            variance = math.sin(2.0 * theta) ** 2
            audit = QFIResponseAudit(4.0, variance, slope)
            audit.validate()
            self.assertAlmostEqual(audit.response_utilization, 1.0, places=12)

    def test_pure_qubit_x_observable_saturates_bound(self):
        # For X: <X>=sin(2 theta), derivative=2 cos(2 theta),
        # Var(X)=cos(2 theta)^2 and QFI_theta=4.
        for theta in (0.1, 0.25, 0.7, 1.1):
            slope = 2.0 * math.cos(2.0 * theta)
            variance = math.cos(2.0 * theta) ** 2
            audit = QFIResponseAudit(4.0, variance, slope)
            audit.validate()
            self.assertAlmostEqual(audit.response_utilization, 1.0, places=12)

    def test_zero_qfi_direction_has_zero_first_order_response(self):
        QFIResponseAudit(0.0, 1.0, 0.0).validate()
        with self.assertRaisesRegex(ValueError, "bound violated"):
            QFIResponseAudit(0.0, 1.0, 1e-6).validate()

    def test_bound_violation_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "bound violated"):
            QFIResponseAudit(1.0, 1.0, 1.01).validate()

    def test_invalid_inputs_are_rejected(self):
        bad_records = (
            (-1.0, 1.0, 0.0),
            (1.0, -1.0, 0.0),
            (float("nan"), 1.0, 0.0),
            (1.0, float("inf"), 0.0),
            (1.0, 1.0, float("nan")),
        )
        for values in bad_records:
            with self.subTest(values=values), self.assertRaises(ValueError):
                QFIResponseAudit(*values).validate()
        with self.assertRaises(ValueError):
            QFIResponseAudit(1.0, 1.0, 0.5, relative_tolerance=-1.0).validate()
        with self.assertRaises(ValueError):
            QFIResponseAudit("not-a-number", 1.0, 0.0).validate()

    def test_small_floating_point_excess_is_tolerated(self):
        QFIResponseAudit(1.0, 1.0, 1.0 + 1e-12, relative_tolerance=1e-10).validate()


if __name__ == "__main__":
    unittest.main()
