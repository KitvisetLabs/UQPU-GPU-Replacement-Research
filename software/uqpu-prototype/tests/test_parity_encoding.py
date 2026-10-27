import itertools
import unittest

from uqpu.parity_encoding import build_parity_encoding


class ParityEncodingTests(unittest.TestCase):
    def test_triangle_cycle_and_logical_mapping(self):
        encoding = build_parity_encoding(3, [(0, 1), (1, 2), (0, 2)])
        self.assertEqual(encoding.edges, ((0, 1), (0, 2), (1, 2)))
        self.assertEqual(encoding.cycle_constraints, ((0, 1, 2),))
        self.assertEqual(encoding.encode_logical("101"), (1, 0, 1))
        self.assertTrue(encoding.is_valid_physical((1, 0, 1)))
        self.assertFalse(encoding.is_valid_physical((1, 0, 0)))
        with self.assertRaisesRegex(ValueError, "cycle-parity"):
            encoding.decode_physical((1, 0, 0))

    def test_exhaustive_connected_graph_matches_exact_valid_count(self):
        encoding = build_parity_encoding(
            4, [(0, 1), (1, 2), (2, 3), (0, 3), (0, 2)]
        )
        self.assertEqual(
            encoding.cycle_rank,
            len(encoding.edges) - encoding.vertex_count + 1,
        )
        valid = {
            bits for bits in itertools.product((0, 1), repeat=encoding.physical_qubit_count)
            if encoding.is_valid_physical(bits)
        }
        encoded = {
            encoding.encode_logical(bits)
            for bits in itertools.product((0, 1), repeat=encoding.vertex_count)
        }
        self.assertEqual(len(valid), 2 ** (encoding.vertex_count - 1))
        self.assertEqual(valid, encoded)
        for physical in valid:
            decoded = encoding.decode_physical(physical)
            self.assertEqual(encoding.encode_logical(decoded), physical)
            self.assertEqual(decoded[0], 0)

    def test_disconnected_cycle_tree_and_isolated_vertex(self):
        encoding = build_parity_encoding(
            6, [(0, 1), (1, 2), (0, 2), (3, 4)]
        )
        self.assertEqual(encoding.components, ((0, 1, 2), (3, 4), (5,)))
        self.assertEqual(encoding.cycle_rank, 1)
        valid = [
            bits for bits in itertools.product((0, 1), repeat=encoding.physical_qubit_count)
            if encoding.is_valid_physical(bits)
        ]
        self.assertEqual(
            len(valid),
            2 ** (encoding.vertex_count - len(encoding.components)),
        )
        for physical in valid:
            self.assertEqual(encoding.encode_logical(encoding.decode_physical(physical)), physical)

    def test_tree_has_no_cycle_constraints(self):
        encoding = build_parity_encoding(4, [(2, 3), (0, 1), (1, 2)])
        self.assertEqual(encoding.cycle_constraints, ())
        self.assertEqual(encoding.cycle_rank, 0)
        self.assertTrue(all(
            encoding.is_valid_physical(bits)
            for bits in itertools.product((0, 1), repeat=encoding.physical_qubit_count)
        ))

    def test_edge_and_constraint_order_is_canonical(self):
        first = build_parity_encoding(3, [(0, 1), (1, 2), (0, 2)])
        second = build_parity_encoding(3, [(2, 1), (2, 0), (1, 0)])
        self.assertEqual(first, second)

    def test_rejects_invalid_graphs(self):
        for vertex_count in (0, -1, True, 2.0):
            with self.subTest(vertex_count=vertex_count), self.assertRaises(ValueError):
                build_parity_encoding(vertex_count, [])
        invalid_edges = [
            [(0, 0)],
            [(0, 3)],
            [(-1, 0)],
            [(0, 1), (1, 0)],
            [(0, True)],
            [(0,)],
        ]
        for edges in invalid_edges:
            with self.subTest(edges=edges), self.assertRaises(ValueError):
                build_parity_encoding(3, edges)

    def test_rejects_invalid_bit_sequences(self):
        encoding = build_parity_encoding(2, [(0, 1)])
        for bits in ("02", "1", [0, 2], [0, True]):
            with self.subTest(bits=bits), self.assertRaises(ValueError):
                encoding.encode_logical(bits)
        with self.assertRaises(ValueError):
            encoding.is_valid_physical((True,))
        with self.assertRaises(ValueError):
            encoding.decode_physical((0, 1))


if __name__ == "__main__":
    unittest.main()
