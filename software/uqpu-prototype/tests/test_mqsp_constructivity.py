import cmath
import math
import unittest

from uqpu.mqsp_constructivity import mqsp_constructivity_decision


def _single_signal_pair(phi0, phi1):
    p_lead = cmath.exp(1j * (phi0 + phi1)) / 2
    q_lead = cmath.exp(1j * (phi0 - phi1)) / 2
    return ({(1,): p_lead, (-1,): p_lead},
            {(1,): q_lead, (-1,): -q_lead})


def _published_nonconstructible_pair():
    # Ito et al., arXiv:2410.02332v3, Sec. 4, Eqs. (16)-(17).
    # c = (6/25)*sqrt(37/493). The pair is not constructible by M-QSP.
    c = (6.0 / 25.0) * math.sqrt(37.0 / 493.0)
    p = {
        (2, 2): c,
        (-2, -2): c,
        (0, 2): -c * complex(122 / 37, 8 / 37),
        (0, -2): -c * complex(122 / 37, 8 / 37),
        (-2, 2): c * complex(114 / 37, 56 / 37),
        (2, -2): c * complex(114 / 37, 56 / 37),
        (2, 0): c * complex(362 / 111, -248 / 111),
        (-2, 0): c * complex(362 / 111, -248 / 111),
        (0, 0): c * complex(692 / 111, -719 / 222),
    }
    q = {
        (2, 2): c,
        (-2, -2): -c,
        (0, 2): -c * complex(122 / 37, 66 / 37),
        (0, -2): c * complex(122 / 37, 66 / 37),
        (-2, 2): c * complex(56 / 37, 114 / 37),
        (2, -2): -c * complex(56 / 37, 114 / 37),
        (2, 0): c * complex(362 / 111, -418 / 111),
        (-2, 0): -c * complex(362 / 111, -418 / 111),
    }
    return p, q


def _poly_add_scaled(*terms):
    result = {}
    for poly, scale in terms:
        for exponent, coefficient in poly.items():
            result[exponent] = result.get(exponent, 0j) + scale * coefficient
    return {key: value for key, value in result.items() if abs(value) > 1e-10}


def _shift(poly, axis, amount):
    result = {}
    for exponent, coefficient in poly.items():
        shifted = exponent[:axis] + (exponent[axis] + amount,) + exponent[axis + 1:]
        result[shifted] = result.get(shifted, 0j) + coefficient
    return result


def _pair_from_sequence(phases, signal_indices, variable_count):
    p = {(0,) * variable_count: cmath.exp(1j * phases[0])}
    q = {}
    for step, axis in enumerate(signal_indices):
        p_plus, p_minus = _shift(p, axis, 1), _shift(p, axis, -1)
        q_plus, q_minus = _shift(q, axis, 1), _shift(q, axis, -1)
        s_scale = 0.5 * cmath.exp(1j * phases[step + 1])
        t_scale = 0.5 * cmath.exp(-1j * phases[step + 1])
        p = _poly_add_scaled(
            (p_plus, s_scale), (p_minus, s_scale),
            (q_plus, s_scale), (q_minus, -s_scale),
        )
        q = _poly_add_scaled(
            (p_plus, t_scale), (p_minus, -t_scale),
            (q_plus, t_scale), (q_minus, t_scale),
        )
    return p, q


def _assert_polynomials_close(testcase, left, right, tolerance=1e-8):
    for exponent in set(left) | set(right):
        testcase.assertLessEqual(
            abs(left.get(exponent, 0j) - right.get(exponent, 0j)),
            tolerance,
            msg=f"coefficient mismatch at exponent {exponent}",
        )


class MQSPConstructivityDecisionTests(unittest.TestCase):
    def test_feasible_one_signal_pair_reconstructs_independently(self):
        phi0, phi1 = 0.2, -0.4
        p, q = _single_signal_pair(phi0, phi1)
        result = mqsp_constructivity_decision(p, q, variable_count=1, n_steps=1)
        self.assertTrue(result.candidate_feasible, result.reason)
        self.assertEqual(result.signal_indices, (0,))
        self.assertEqual(len(result.phase_angles), 2)
        self.assertTrue(math.isclose(result.phase_angles[0], phi0, abs_tol=1e-8))
        self.assertTrue(math.isclose(result.phase_angles[1], phi1, abs_tol=1e-8))
        reconstructed_p, reconstructed_q = _single_signal_pair(*result.phase_angles)
        _assert_polynomials_close(self, p, reconstructed_p)
        _assert_polynomials_close(self, q, reconstructed_q)

    def test_two_variable_two_signal_candidate_reconstructs(self):
        phases = (0.15, -0.35, 0.25)
        indices = (1, 0)
        p, q = _pair_from_sequence(phases, indices, variable_count=2)
        result = mqsp_constructivity_decision(p, q, variable_count=2, n_steps=2)
        self.assertTrue(result.candidate_feasible, result.reason)
        reconstructed_p, reconstructed_q = _pair_from_sequence(
            result.phase_angles, result.signal_indices, variable_count=2
        )
        _assert_polynomials_close(self, p, reconstructed_p, tolerance=1e-7)
        _assert_polynomials_close(self, q, reconstructed_q, tolerance=1e-7)

    def test_zero_step_nonunit_scalar_is_infeasible(self):
        result = mqsp_constructivity_decision(
            {(0,): 0.5}, {}, variable_count=1, n_steps=0
        )
        self.assertFalse(result.candidate_feasible)
        self.assertEqual(result.signal_indices, ())
        self.assertEqual(result.phase_angles, ())

    def test_term_insertion_order_does_not_change_classification_or_witness(self):
        p, q = _single_signal_pair(0.2, -0.4)
        first = mqsp_constructivity_decision(p, q, 1, 1)
        second = mqsp_constructivity_decision(
            dict(reversed(list(p.items()))),
            dict(reversed(list(q.items()))),
            1,
            1,
        )
        self.assertEqual(first.candidate_feasible, second.candidate_feasible)
        self.assertEqual(first.signal_indices, second.signal_indices)
        for left, right in zip(first.phase_angles, second.phase_angles):
            self.assertTrue(math.isclose(left, right, abs_tol=1e-12))

    def test_invalid_contract_inputs_fail_closed(self):
        for variable_count, n_steps in ((0, 1), (True, 1), (1, -1), (1, True)):
            with self.assertRaises(ValueError):
                mqsp_constructivity_decision({}, {}, variable_count, n_steps)
        with self.assertRaises(ValueError):
            mqsp_constructivity_decision({(0, 0): 1}, {}, 1, 0)
        with self.assertRaises(ValueError):
            mqsp_constructivity_decision({(0,): complex(float("inf"), 0)}, {}, 1, 0)
        with self.assertRaises(ValueError):
            mqsp_constructivity_decision({}, {}, 1, 0, tolerance=0)


    def test_published_nonconstructible_pair_rejected_across_tolerances(self):
        p, q = _published_nonconstructible_pair()
        for tolerance in (1e-12, 1e-9, 1e-6):
            with self.subTest(tolerance=tolerance):
                result = mqsp_constructivity_decision(
                    p, q, variable_count=2, n_steps=4, tolerance=tolerance
                )
                self.assertFalse(result.candidate_feasible, result.reason)
                self.assertEqual(result.signal_indices, ())
                self.assertEqual(result.phase_angles, ())

    def test_feasible_one_signal_pair_reconstructs_across_tolerances(self):
        for tolerance in (1e-12, 1e-9, 1e-6):
            with self.subTest(tolerance=tolerance):
                p, q = _single_signal_pair(0.2, -0.4)
                result = mqsp_constructivity_decision(
                    p, q, variable_count=1, n_steps=1, tolerance=tolerance
                )
                self.assertTrue(result.candidate_feasible, result.reason)
                reconstructed_p, reconstructed_q = _single_signal_pair(*result.phase_angles)
                _assert_polynomials_close(self, p, reconstructed_p, tolerance=1e-8)
                _assert_polynomials_close(self, q, reconstructed_q, tolerance=1e-8)


if __name__ == "__main__":
    unittest.main()
