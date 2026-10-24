import math
import unittest

from uqpu.qfi_ancilla_transfer_audit import (
    audit_ghz_qfi_transfer,
    distinct_nonzero_score_classes,
    ghz_direct_measurement_cfi,
    ghz_outcome_probabilities,
)


class QFIAncillaTransferAuditTests(unittest.TestCase):
    def test_probabilities_normalize_for_generic_phase(self):
        probabilities = ghz_outcome_probabilities(4, 0.173)
        self.assertTrue(all(p > 0 for p in probabilities))
        self.assertAlmostEqual(math.fsum(probabilities), 1.0, places=12)

    def test_direct_measurement_cfi_matches_known_ghz_qfi(self):
        for n in (1, 2, 3, 5, 8):
            with self.subTest(n=n):
                self.assertAlmostEqual(ghz_direct_measurement_cfi(n, 0.173), n*n, places=8)

    def test_generic_ghz_measurement_has_two_score_classes(self):
        self.assertEqual(distinct_nonzero_score_classes(6, 0.173), 2)

    def test_ancilla_dimension_precondition_is_reported_without_promotion(self):
        qubit_ancilla = audit_ghz_qfi_transfer(6, 0.173, 2)
        self.assertTrue(qubit_ancilla.ghz_formula_check_passed)
        self.assertFalse(qubit_ancilla.theorem_2_precondition_m_gt_n)
        self.assertEqual(qubit_ancilla.evidence_class, "MODEL_ONLY")
        scalar_ancilla = audit_ghz_qfi_transfer(6, 0.173, 1)
        self.assertTrue(scalar_ancilla.theorem_2_precondition_m_gt_n)
        self.assertEqual(scalar_ancilla.provider_jobs, 0)

    def test_singular_phase_is_rejected_for_regular_score(self):
        with self.assertRaises(ValueError):
            ghz_direct_measurement_cfi(2, 0.0)

    def test_invalid_dimensions_are_rejected(self):
        with self.assertRaises(ValueError):
            audit_ghz_qfi_transfer(0, 0.173, 2)
        with self.assertRaises(ValueError):
            audit_ghz_qfi_transfer(3, 0.173, 0)


if __name__ == "__main__":
    unittest.main()
