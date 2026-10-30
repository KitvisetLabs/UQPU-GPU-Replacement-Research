"""Exhaustive logical-to-edge-parity audit for the frozen Batch 143 manifest.

Exact small-instance correctness only; this is not a QAOA performance run.
"""
import itertools
import json
import hashlib
from pathlib import Path
import unittest

from uqpu.optimization_baseline import QuboInstance, exact_qubo_baseline
from uqpu.parity_encoding import build_parity_encoding
from uqpu.parity_qaoa import parity_qaoa_objective

ROOT = Path(__file__).resolve().parents[3]
MANIFEST_PATH = ROOT / "benchmarks/manifests/qaoa-parity-heldout-2026-10-30.json"
REFERENCE_PATH = ROOT / "benchmarks/references/qaoa-parity-exact-references-2026-10-30.json"


def cut_score(bits, edges, weights):
    return sum(float(w) * (bits[u] ^ bits[v]) for (u, v), w in zip(edges, weights))


class QAOAParityHeldoutMappingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        cls.references = json.loads(REFERENCE_PATH.read_text(encoding="utf-8"))
        cls.by_id = {x["instance_id"]: x for x in cls.references["certificates"]}

    def test_every_manifest_graph_has_exact_logical_physical_equivalence(self):
        self.assertEqual(self.references["workload_contract_id"], self.manifest["workload_contract_id"])
        self.assertEqual(self.references["manifest_sha256"], hashlib.sha256(MANIFEST_PATH.read_bytes()).hexdigest())
        self.assertEqual({x["id"] for x in self.manifest["instances"]}, set(self.by_id))
        total_logical = 0
        for item in self.manifest["instances"]:
            with self.subTest(instance=item["id"]):
                n = item["vertex_count"]
                edges = [tuple(e) for e in item["edges"]]
                weights = tuple(float(w) for w in item["weights"])
                ref = self.by_id[item["id"]]
                encoding = build_parity_encoding(n, edges)
                linear = {v: 0.0 for v in range(n)}
                quadratic = {}
                for (u, v), w in zip(edges, weights):
                    linear[u] -= w
                    linear[v] -= w
                    quadratic[(u, v)] = 2.0 * w
                direct = exact_qubo_baseline(QuboInstance(linear, quadratic), max_variables=12)
                logical = [(bits, cut_score(bits, edges, weights))
                           for bits in itertools.product((0, 1), repeat=n)]
                optimum = max(score for _, score in logical)
                self.assertAlmostEqual(optimum, ref["optimum_score"])
                self.assertEqual(ref["states_evaluated"], 1 << n)
                self.assertAlmostEqual(direct.objective, -optimum)

                costs = tuple(-w for w in weights)
                penalty = 2.0 * sum(abs(w) for w in costs) + 1.0
                parity = parity_qaoa_objective(encoding, costs, penalty_weight=penalty)
                cert = parity.exact_certificate(max_qubits=12)
                self.assertEqual(cert.states_evaluated, 1 << encoding.physical_qubit_count)
                self.assertTrue(cert.all_ground_states_feasible)
                self.assertAlmostEqual(cert.optimum_energy, -optimum)
                self.assertAlmostEqual(cert.feasible_optimum_energy, -optimum)
                expected_argmax = {
                    encoding.encode_logical(tuple(int(b) for b in s))
                    for s in ref["optimal_assignments"]
                }
                self.assertEqual(set(cert.feasible_optimal_assignments), expected_argmax)

                for bits, score in logical:
                    physical = encoding.encode_logical(bits)
                    self.assertTrue(encoding.is_valid_physical(physical))
                    decoded = encoding.decode_physical(physical)
                    self.assertEqual(encoding.encode_logical(decoded), physical)
                    self.assertAlmostEqual(cut_score(decoded, edges, weights), score)
                    self.assertAlmostEqual(parity.energy(physical), -score)
                    total_logical += 1

                feasible = 0
                for physical in itertools.product((0, 1), repeat=encoding.physical_qubit_count):
                    if encoding.is_valid_physical(physical):
                        feasible += 1
                        decoded = encoding.decode_physical(physical)
                        self.assertEqual(encoding.encode_logical(decoded), physical)
                        self.assertAlmostEqual(parity.energy(physical), -cut_score(decoded, edges, weights))
                    else:
                        with self.assertRaises(ValueError):
                            encoding.decode_physical(physical)
                self.assertEqual(feasible, 1 << (n - len(encoding.components)))
        self.assertEqual(total_logical, 688)


if __name__ == "__main__":
    unittest.main()
