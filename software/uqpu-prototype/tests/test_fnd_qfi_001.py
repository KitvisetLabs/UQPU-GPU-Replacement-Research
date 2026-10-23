import json
from fractions import Fraction
from pathlib import Path
import unittest

from uqpu.fnd_qfi_001 import AncillaQfiCase, case_from_scores, run_reference_cases


ROOT = Path(__file__).resolve().parents[3]
RESULT_PATH = ROOT / "benchmarks/results/fnd-qfi-001-exact-fixture-2026-10-23.json"


class FndQfi001Tests(unittest.TestCase):
    def test_exact_score_grouping_preserves_classical_fisher_information(self):
        result = run_reference_cases()[0]
        self.assertEqual(result["system_classical_fisher_information"], "1")
        self.assertEqual(result["grouped_fisher_information_if_feasible"], "1")
        self.assertTrue(result["orthogonal_score_encoding_dimension_sufficient"])
        self.assertTrue(result["perfect_transfer_constructed_in_exact_classical_model"])

    def test_three_nonzero_score_classes_trigger_scoped_no_go_condition(self):
        result = run_reference_cases()[1]
        self.assertEqual(result["m_nonzero"], 3)
        self.assertEqual(result["ancilla_dimension"], 2)
        self.assertTrue(result["theorem_2_no_go_condition_triggered"])
        self.assertFalse(result["perfect_transfer_constructed_in_exact_classical_model"])

    def test_zero_score_class_is_not_silently_dropped_from_dimension_count(self):
        result = run_reference_cases()[2]
        self.assertEqual(result["m_nonzero"], 2)
        self.assertEqual(result["m_all"], 3)
        self.assertFalse(result["theorem_2_no_go_condition_triggered"])
        self.assertFalse(result["orthogonal_score_encoding_dimension_sufficient"])
        self.assertEqual(result["status"], "ZERO_SCORE_CLASS_DIMENSION_GAP")

    def test_near_degenerate_scores_remain_distinct_in_exact_arithmetic(self):
        result = run_reference_cases()[3]
        self.assertEqual(result["m_nonzero"], 3)
        self.assertTrue(result["theorem_2_no_go_condition_triggered"])
        self.assertEqual(len(result["distinct_nonzero_score_values"]), 3)

    def test_zero_probability_boundary_is_rejected(self):
        case = AncillaQfiCase(
            "zero_probability_boundary",
            (Fraction(0), Fraction(1)),
            (Fraction(0), Fraction(0)),
            2,
        )
        with self.assertRaisesRegex(ValueError, "strictly positive"):
            case.analyze()

    def test_float_inputs_are_rejected_to_avoid_score_merging(self):
        with self.assertRaisesRegex(TypeError, "floating-point"):
            case_from_scores("float_not_allowed", [0.5, 0.5], [1, -1], 2)

    def test_frozen_json_matches_executable_reference_cases(self):
        artifact = json.loads(RESULT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(artifact["results"], run_reference_cases())
        self.assertEqual(artifact["evidence_class"], "MODEL_ONLY")
        self.assertIs(artifact["physical_law_claim_allowed"], False)


if __name__ == "__main__":
    unittest.main()
