import unittest

from uqpu.quantum_state_scope import tripartite_haar_no_go_size_condition_applies


class TripartiteHaarNoGoScopeTests(unittest.TestCase):
    def test_all_subsystems_strictly_below_half(self):
        self.assertTrue(tripartite_haar_no_go_size_condition_applies(4, 4, 2))
        self.assertTrue(tripartite_haar_no_go_size_condition_applies(3, 3, 3))

    def test_equal_half_is_outside_strict_size_condition(self):
        self.assertFalse(tripartite_haar_no_go_size_condition_applies(2, 2, 4))

    def test_dominant_subsystem_is_outside_size_condition(self):
        self.assertFalse(tripartite_haar_no_go_size_condition_applies(7, 2, 2))

    def test_result_is_permutation_invariant(self):
        values = (4, 4, 2)
        results = {
            tripartite_haar_no_go_size_condition_applies(*p)
            for p in ((4, 4, 2), (4, 2, 4), (2, 4, 4))
        }
        self.assertEqual(results, {True})

    def test_invalid_dimensions_fail_closed(self):
        for values in ((0, 1, 1), (-1, 2, 2), (True, 2, 2), (1.0, 2, 2)):
            with self.subTest(values=values):
                with self.assertRaises(ValueError):
                    tripartite_haar_no_go_size_condition_applies(*values)


if __name__ == "__main__":
    unittest.main()
