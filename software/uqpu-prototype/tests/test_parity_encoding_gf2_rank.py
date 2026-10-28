"""Independent GF(2) rank checks for the graph-parity encoding oracle.

These bounded exhaustive tests validate cycle-space dimension independently of
the spanning-forest implementation. They do not implement a parity-QAOA circuit
or imply a quantum advantage.
"""
from itertools import combinations, product
import unittest

from uqpu.parity_encoding import build_parity_encoding


def _gf2_rank(vectors):
    """Rank of integer bit-vectors over GF(2), using independent elimination."""
    pivots = {}
    for vector in vectors:
        value = vector
        while value:
            pivot = value.bit_length() - 1
            if pivot in pivots:
                value ^= pivots[pivot]
            else:
                pivots[pivot] = value
                break
    return len(pivots)


def _component_count(vertex_count, edges):
    adjacency = [[] for _ in range(vertex_count)]
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    seen = set()
    count = 0
    for start in range(vertex_count):
        if start in seen:
            continue
        count += 1
        stack = [start]
        seen.add(start)
        while stack:
            vertex = stack.pop()
            for neighbor in adjacency[vertex]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
    return count


class ParityEncodingGF2RankTests(unittest.TestCase):
    def test_cycle_constraints_are_independent_for_every_simple_graph_through_five_vertices(self):
        # There are only 1 + 2 + 8 + 64 + 1024 graphs over vertex counts 1..5.
        # This exhaustive bound is a small algebraic oracle, not a scale claim.
        for vertex_count in range(1, 6):
            possible_edges = tuple(combinations(range(vertex_count), 2))
            for edge_mask in range(1 << len(possible_edges)):
                edges = tuple(
                    edge for index, edge in enumerate(possible_edges)
                    if (edge_mask >> index) & 1
                )
                with self.subTest(vertex_count=vertex_count, edges=edges):
                    encoding = build_parity_encoding(vertex_count, edges)
                    edge_count = len(encoding.edges)
                    components = _component_count(vertex_count, encoding.edges)

                    # Columns of the vertex-edge incidence matrix, represented
                    # as bit-vectors. Its GF(2) rank must be V - components.
                    incidence_columns = [
                        (1 << u) | (1 << v) for u, v in encoding.edges
                    ]
                    incidence_rank = _gf2_rank(incidence_columns)
                    self.assertEqual(incidence_rank, vertex_count - components)

                    # Each cycle is a vector in edge-space. The cycle-space
                    # dimension is E - rank(incidence), and the returned
                    # fundamental cycles must form an independent basis.
                    cycle_vectors = []
                    for cycle in encoding.cycle_constraints:
                        cycle_mask = 0
                        vertex_boundary = 0
                        for edge_index in cycle:
                            cycle_mask ^= 1 << edge_index
                            u, v = encoding.edges[edge_index]
                            vertex_boundary ^= (1 << u) | (1 << v)
                        self.assertEqual(vertex_boundary, 0)
                        cycle_vectors.append(cycle_mask)

                    expected_cycle_rank = edge_count - incidence_rank
                    self.assertEqual(len(encoding.cycle_constraints), expected_cycle_rank)
                    self.assertEqual(_gf2_rank(cycle_vectors), expected_cycle_rank)


    def test_all_simple_graphs_through_five_vertices_have_exact_encode_decode_bijection(self):
        # Exhaustively verify the logical-to-edge-parity map for all 1,099
        # labelled simple graphs with 1..5 vertices. The physical feasible
        # set must equal the image of logical assignments, with one canonical
        # representative per component-wise global-flip equivalence class.
        for vertex_count in range(1, 6):
            possible_edges = list(combinations(range(vertex_count), 2))
            for edge_mask in range(1 << len(possible_edges)):
                edges = [
                    edge for index, edge in enumerate(possible_edges)
                    if (edge_mask >> index) & 1
                ]
                with self.subTest(vertex_count=vertex_count, edge_mask=edge_mask):
                    encoding = build_parity_encoding(vertex_count, edges)
                    encoded = {
                        encoding.encode_logical(bits)
                        for bits in product((0, 1), repeat=vertex_count)
                    }
                    valid = {
                        bits for bits in product((0, 1), repeat=len(encoding.edges))
                        if encoding.is_valid_physical(bits)
                    }
                    expected_count = 2 ** (vertex_count - len(encoding.components))
                    self.assertEqual(len(encoded), expected_count)
                    self.assertEqual(len(valid), expected_count)
                    self.assertEqual(encoded, valid)
                    for physical in valid:
                        logical = encoding.decode_physical(physical)
                        self.assertEqual(encoding.encode_logical(logical), physical)
                        for component in encoding.components:
                            self.assertEqual(logical[min(component)], 0)

if __name__ == "__main__":
    unittest.main()
