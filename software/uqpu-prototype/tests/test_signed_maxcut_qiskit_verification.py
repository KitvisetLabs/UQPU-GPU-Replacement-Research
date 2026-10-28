import importlib.util
import itertools
import math
import unittest

from uqpu.sdk_signed_maxcut import (
    DEFAULT_TOLERANCE,
    MAX_EXHAUSTIVE_VERTICES,
    qiskit_signed_maxcut_scores,
    tiny_signed_maxcut_fixtures,
)
from uqpu.signed_maxcut_objective import compile_signed_maxcut


@unittest.skipUnless(importlib.util.find_spec("qiskit"), "optional pinned Qiskit dependency")
class SignedMaxCutQiskitVerificationTests(unittest.TestCase):
    def test_sdk_diagonal_matches_all_objective_forms_and_complete_argmax_sets(self):
        for name, vertex_count, edges in tiny_signed_maxcut_fixtures():
            with self.subTest(fixture=name):
                lowering = compile_signed_maxcut(vertex_count, edges)
                sdk_scores = qiskit_signed_maxcut_scores(lowering)
                assignments = list(itertools.product((0, 1), repeat=vertex_count))
                direct_scores = [lowering.direct_score(bits) for bits in assignments]
                qubo_scores = [lowering.qubo_score(bits) for bits in assignments]
                ising_scores = [lowering.ising_score(bits) for bits in assignments]
                self.assertEqual(len(sdk_scores), len(assignments))
                for bits, direct, qubo, ising, sdk in zip(
                    assignments, direct_scores, qubo_scores, ising_scores, sdk_scores
                ):
                    self.assertTrue(math.isclose(direct, qubo, rel_tol=0, abs_tol=DEFAULT_TOLERANCE), (name, bits))
                    self.assertTrue(math.isclose(direct, ising, rel_tol=0, abs_tol=DEFAULT_TOLERANCE), (name, bits))
                    self.assertTrue(math.isclose(direct, sdk, rel_tol=0, abs_tol=DEFAULT_TOLERANCE), (name, bits))

                maximum = max(direct_scores)
                direct_argmax = {
                    bits for bits, score in zip(assignments, direct_scores)
                    if math.isclose(score, maximum, rel_tol=0, abs_tol=DEFAULT_TOLERANCE)
                }
                sdk_maximum = max(sdk_scores)
                sdk_argmax = {
                    bits for bits, score in zip(assignments, sdk_scores)
                    if math.isclose(score, sdk_maximum, rel_tol=0, abs_tol=DEFAULT_TOLERANCE)
                }
                negative_sdk = [-score for score in sdk_scores]
                minimum_negative = min(negative_sdk)
                minimize_negative = {
                    bits for bits, score in zip(assignments, negative_sdk)
                    if math.isclose(score, minimum_negative, rel_tol=0, abs_tol=DEFAULT_TOLERANCE)
                }
                self.assertEqual(direct_argmax, sdk_argmax, name)
                self.assertEqual(direct_argmax, minimize_negative, name)

    def test_pauli_qubit_order_and_constant_are_detected_by_nonadjacent_edge(self):
        lowering = compile_signed_maxcut(4, [(0, 3, -2.5)])
        scores = qiskit_signed_maxcut_scores(lowering)
        for basis_index, score in enumerate(scores):
            bits = tuple((basis_index >> qubit) & 1 for qubit in range(4))
            self.assertEqual(score, -2.5 if bits[0] != bits[3] else 0.0)

    def test_exhaustive_state_allocation_limit_fails_closed(self):
        lowering = compile_signed_maxcut(MAX_EXHAUSTIVE_VERTICES + 1, [])
        with self.assertRaisesRegex(ValueError, "limited to"):
            qiskit_signed_maxcut_scores(lowering)

    def test_invalid_tolerance_fails_closed(self):
        lowering = compile_signed_maxcut(2, [(0, 1, 1.0)])
        for tolerance in (True, -1.0, float("nan"), float("inf"), "1e-12"):
            with self.subTest(tolerance=tolerance), self.assertRaises(ValueError):
                qiskit_signed_maxcut_scores(lowering, tolerance=tolerance)


if __name__ == "__main__":
    unittest.main()
