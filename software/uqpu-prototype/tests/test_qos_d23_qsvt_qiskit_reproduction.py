import unittest

try:
    import qiskit
except ImportError:  # pragma: no cover - exercised by the core dependency job
    qiskit = None

from uqpu.qos_d23_qsvt_qiskit_reproduction import (
    BASIS_GATES,
    build_qiskit_fixture_circuit,
    reproduce_with_qiskit,
)


@unittest.skipUnless(qiskit is not None, "optional pinned Qiskit dependency")
class QOSD23QSVTQiskitReproductionTests(unittest.TestCase):
    def test_independent_operator_and_decomposition_pass(self):
        result = reproduce_with_qiskit()
        self.assertTrue(result["passed"], result)
        agreement = result["operator_agreement"]
        self.assertLessEqual(agreement["repository_vs_qiskit_max_abs_residual"], 2e-12)
        self.assertLessEqual(agreement["decomposed_vs_repository_max_abs_residual"], 2e-12)
        self.assertEqual(result["resources"]["provider_jobs"], 0)
        self.assertIsNone(result["resources"]["provider_cost"])
        self.assertTrue(set(result["resources"]["decomposed_operation_counts"]).issubset(BASIS_GATES))

    def test_contract_rejects_truncated_phase_sequence(self):
        with self.assertRaisesRegex(ValueError, "exactly 82 phases"):
            build_qiskit_fixture_circuit((0.0, 1.0))


if __name__ == "__main__":
    unittest.main()
