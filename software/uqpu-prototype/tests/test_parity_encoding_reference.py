"""Independent reference checks for graph-parity encoding.

These tests validate classical mapping identities only. They do not implement
QAOA, estimate hardware resources, or claim quantum advantage.
"""
from itertools import combinations, product
import unittest

from uqpu.parity_encoding import build_parity_encoding


def _independent_gf2_rank(cycle_constraints):
    """Compute row rank over GF(2) without using the encoder's graph algorithm."""
    pivots = {}
    for constraint in cycle_constraints:
        row = 0
        for column in constraint:
            row ^= 1 << column
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


class ParityEncodingIndependentReferenceTests(unittest.TestCase):
    def test_all_simple_graphs_through_five_vertices_match_independent_gf2_rank(self):
        # All 1,099 labelled simple graphs with 1..5 vertices are covered.
        # The rank implementation is independent of the encoder's union-find
        # and spanning-forest construction.
        for vertex_count in range(1, 6):
            possible_edges = list(combinations(range(vertex_count), 2))
            for edge_mask in range(1 << len(possible_edges)):
                edges = [
                    edge for index, edge in enumerate(possible_edges)
                    if (edge_mask >> index) & 1
                ]
                with self.subTest(vertex_count=vertex_count, edge_mask=edge_mask):
                    encoding = build_parity_encoding(vertex_count, edges)
                    rank = _independent_gf2_rank(encoding.cycle_constraints)
                    expected_cycle_rank = (
                        len(encoding.edges) - vertex_count + len(encoding.components)
                    )
                    self.assertEqual(encoding.cycle_rank, rank)
                    self.assertEqual(rank, expected_cycle_rank)

                    # Each declared constraint must be a cycle: every vertex
                    # has even incidence in that constraint.
                    for cycle in encoding.cycle_constraints:
                        incidence = [0] * vertex_count
                        for edge_index in cycle:
                            u, v = encoding.edges[edge_index]
                            incidence[u] ^= 1
                            incidence[v] ^= 1
                        self.assertEqual(incidence, [0] * vertex_count)

    def test_signed_maxcut_edge_preferences_are_preserved_by_encode_decode(self):
        # Each edge is (u, v, positive weight, preferred parity). Preference 1
        # means a cut edge; preference 0 means an uncut edge. This explicit
        # convention makes signed-edge semantics independent of QAOA internals.
        fixtures = [
            (3, [
                (0, 1, 5, 1), (1, 2, 2, 0), (0, 2, 3, 1),
            ]),
            (4, [
                (0, 1, 2, 1), (1, 2, 7, 0), (2, 3, 1, 1),
                (0, 3, 4, 1), (0, 2, 3, 0),
            ]),
            (5, [
                (0, 1, 3, 1), (1, 2, 2, 0), (2, 3, 5, 1),
                (3, 4, 4, 0), (0, 4, 1, 1), (0, 2, 2, 0),
            ]),
        ]

        for vertex_count, signed_edges in fixtures:
            edges = [(u, v) for u, v, _, _ in signed_edges]
            encoding = build_parity_encoding(vertex_count, edges)
            edge_index = {edge: index for index, edge in enumerate(encoding.edges)}
            edge_terms = {
                tuple(sorted((u, v))): (weight, preferred)
                for u, v, weight, preferred in signed_edges
            }

            def logical_score(bits):
                return sum(
                    weight
                    for u, v, weight, preferred in signed_edges
                    if (bits[u] ^ bits[v]) == preferred
                )

            def physical_score(bits):
                return sum(
                    edge_terms[edge][0]
                    for edge, index in edge_index.items()
                    if bits[index] == edge_terms[edge][1]
                )

            for logical in product((0, 1), repeat=vertex_count):
                physical = encoding.encode_logical(logical)
                self.assertEqual(logical_score(logical), physical_score(physical))

                # A component-wise global flip is a gauge degeneracy: edge
                # parities and the signed objective must remain unchanged.
                for component in encoding.components:
                    flipped = list(logical)
                    for vertex in component:
                        flipped[vertex] ^= 1
                    self.assertEqual(encoding.encode_logical(flipped), physical)
                    self.assertEqual(logical_score(flipped), logical_score(logical))

            for physical in product((0, 1), repeat=encoding.physical_qubit_count):
                if not encoding.is_valid_physical(physical):
                    continue
                decoded = encoding.decode_physical(physical)
                self.assertEqual(encoding.encode_logical(decoded), physical)
                self.assertEqual(logical_score(decoded), physical_score(physical))


if __name__ == "__main__":
    unittest.main()
