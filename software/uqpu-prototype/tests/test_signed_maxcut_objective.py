import itertools
import math
import unittest

from uqpu.signed_maxcut_objective import compile_signed_maxcut


class SignedMaxCutObjectiveTests(unittest.TestCase):
    def assert_all_forms_agree(self, n, edges):
        lowering = compile_signed_maxcut(n, edges)
        rows = []
        for bits in itertools.product((0, 1), repeat=n):
            direct = lowering.direct_score(bits)
            qubo = lowering.qubo_score(bits)
            ising = lowering.ising_score(bits)
            self.assertTrue(math.isclose(direct, qubo, rel_tol=0, abs_tol=1e-12),
                            (n, edges, bits, direct, qubo))
            self.assertTrue(math.isclose(direct, ising, rel_tol=0, abs_tol=1e-12),
                            (n, edges, bits, direct, ising))
            rows.append((bits, direct))
        maximum = max(score for _, score in rows)
        maximizers = {bits for bits, score in rows if math.isclose(score, maximum, rel_tol=0, abs_tol=1e-12)}
        qubo_max = max(lowering.qubo_score(bits) for bits, _ in rows)
        ising_max = max(lowering.ising_score(bits) for bits, _ in rows)
        self.assertTrue(math.isclose(maximum, qubo_max, rel_tol=0, abs_tol=1e-12))
        self.assertTrue(math.isclose(maximum, ising_max, rel_tol=0, abs_tol=1e-12))
        self.assertEqual(maximizers, {
            bits for bits, _ in rows
            if math.isclose(lowering.qubo_score(bits), maximum, rel_tol=0, abs_tol=1e-12)
        })
        self.assertEqual(maximizers, {
            bits for bits, _ in rows
            if math.isclose(lowering.ising_score(bits), maximum, rel_tol=0, abs_tol=1e-12)
        })
        return lowering

    def test_signed_weighted_graphs_exhaustively_preserve_objective_and_maximizers(self):
        fixtures = [
            (1, []),
            (3, [(0, 1, 2), (1, 2, -3), (0, 2, 0.5)]),
            (4, [(0, 1, -2), (1, 2, 0), (2, 3, 4), (0, 3, -0.25)]),
            (4, [(0, 2, 1.25), (1, 3, -1.75)]),
        ]
        for n, edges in fixtures:
            with self.subTest(n=n, edges=edges):
                self.assert_all_forms_agree(n, edges)

    def test_all_signed_weight_patterns_on_a_triangle(self):
        edges = ((0, 1), (0, 2), (1, 2))
        for weights in itertools.product((-2, 0, 3), repeat=3):
            with self.subTest(weights=weights):
                self.assert_all_forms_agree(
                    3, [(u, v, weight) for (u, v), weight in zip(edges, weights)]
                )

    def test_edge_order_and_orientation_are_canonical(self):
        first = compile_signed_maxcut(3, [(0, 1, 2), (1, 2, -3), (0, 2, 0.5)])
        second = compile_signed_maxcut(3, [(2, 1, -3), (2, 0, 0.5), (1, 0, 2)])
        self.assertEqual(first, second)

    def test_empty_edge_set_is_zero_objective(self):
        lowering = compile_signed_maxcut(3, [])
        for bits in itertools.product((0, 1), repeat=3):
            self.assertEqual(lowering.direct_score(bits), 0.0)
            self.assertEqual(lowering.qubo_score(bits), 0.0)
            self.assertEqual(lowering.ising_score(bits), 0.0)

    def test_invalid_graphs_and_weights_fail_closed(self):
        for n in (0, -1, True, 2.0):
            with self.subTest(n=n), self.assertRaises(ValueError):
                compile_signed_maxcut(n, [])
        invalid_edge_sets = [
            [(0, 0, 1)],
            [(0, 2, 1)],
            [(-1, 0, 1)],
            [(0, True, 1)],
            [(0, 1)],
            [(0, 1, 1), (1, 0, 2)],
            [(0, 1, float("nan"))],
            [(0, 1, float("inf"))],
            [(0, 1, True)],
            [(0, 1, "2")],
        ]
        for edges in invalid_edge_sets:
            with self.subTest(edges=edges), self.assertRaises(ValueError):
                compile_signed_maxcut(2, edges)

    def test_invalid_bit_inputs_fail_closed(self):
        lowering = compile_signed_maxcut(2, [(0, 1, -2)])
        for bits in ("02", "0", [0, True], [0, 1.0], [0, 2]):
            with self.subTest(bits=bits), self.assertRaises(ValueError):
                lowering.direct_score(bits)


    def test_finite_inputs_that_overflow_lowering_fail_closed(self):
        with self.assertRaisesRegex(ValueError, "derived QUBO/Ising coefficient"):
            compile_signed_maxcut(2, [(0, 1, 1e308)])

        # Each pair coefficient remains finite, but the accumulated linear
        # coefficient at vertex 0 cannot be represented as a finite float.
        star = [(0, 1, 8e307), (0, 2, 8e307), (0, 3, 8e307)]
        with self.assertRaisesRegex(ValueError, "QUBO linear coefficient"):
            compile_signed_maxcut(4, star)

        # Conversion of an integer outside the float range must use the same
        # fail-closed public error contract as other invalid weights.
        with self.assertRaisesRegex(ValueError, "finite real number"):
            compile_signed_maxcut(2, [(0, 1, 10**1000)])

    def test_finite_input_weights_that_overflow_scores_fail_closed(self):
        edges = [(0, 1, 8e307), (2, 3, 8e307), (4, 5, 8e307)]
        lowering = compile_signed_maxcut(6, edges)
        bits = (0, 1, 0, 1, 0, 1)
        for score in (lowering.direct_score, lowering.qubo_score, lowering.ising_score):
            with self.subTest(score=score.__name__), self.assertRaisesRegex(
                ValueError, "outside finite floating-point range"
            ):
                score(bits)


if __name__ == "__main__":
    unittest.main()
