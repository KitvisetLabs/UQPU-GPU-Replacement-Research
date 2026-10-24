import json
from fractions import Fraction
from pathlib import Path
import unittest

from uqpu.fnd_qfi_001 import AncillaQfiCase, case_from_scores, run_reference_cases
from uqpu.equation_discovery import EquationHypothesis
from uqpu.frontier_hypothesis import FrontierHypothesis


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


    def test_frontier_hypothesis_contract_keeps_fixture_model_only(self):
        hypothesis = FrontierHypothesis(
            name="FND-QFI-001 exact score-class transfer",
            layer="quantum metrology and mathematical information",
            evidence_level="MODEL_ONLY",
            mathematical_formulation="q_i = p_i'/p_i; I = sum_i p_i q_i^2",
            causal_mechanism=(
                "Unequal local score values require orthogonal conditional ancilla states "
                "under the stated protocol."
            ),
            target_bottleneck="Ancilla dimension may be insufficient to preserve Fisher information.",
            known_constraints=(
                "p_i > 0",
                "sum_i p_i = 1",
                "sum_i p_i' = 0",
                "q_i = 0 is reviewed separately",
            ),
            scaling_law=(
                "The tested orthogonal score-class encoding requires one dimension per "
                "distinct score class."
            ),
            falsifier=(
                "An independently derived protocol satisfying the same assumptions transfers "
                "the exact information with fewer dimensions."
            ),
            observable="System-versus-ancilla Fisher-information gap under matched assumptions",
            baseline="Classical Fisher information in the already-optimal measurement basis",
            resource_accounting=("exact rational arithmetic", "zero provider jobs and shots"),
        )
        hypothesis.validate()
        self.assertTrue(hypothesis.testable)

    def test_equation_discovery_gate_forbids_physical_promotion(self):
        candidate = EquationHypothesis(
            equation_id="FND-QFI-001",
            baseline_model="Classical Fisher information in the optimal projective basis",
            proposed_equation="q_i = p_i'/p_i; I = sum_i (p_i')^2/p_i",
            variables_and_units=(
                "p_i: dimensionless probability",
                "p_i': derivative with respect to dimensionless local parameter x",
                "q_i: inverse units of x",
            ),
            domain_and_assumptions=(
                "finite strictly-positive probability distribution",
                "already-optimal system measurement",
                "parameter-independent conditional ancilla states",
            ),
            known_constraints_checked=(
                "probability normalization",
                "derivative normalization",
                "pairwise score-class orthogonality",
            ),
            scaling_or_limiting_cases=(
                "m_nonzero > n",
                "m_nonzero <= n with q = 0 present",
                "near-degenerate exact rational scores",
            ),
            falsifier="Independent exact/numerical counterexample under the same assumptions",
            discriminating_observables=(
                "distinct score-class count",
                "system classical Fisher information",
                "ancilla quantum Fisher information",
            ),
            evidence_level="MODEL_ONLY",
            data_or_proof_provenance=(
                "benchmarks/results/fnd-qfi-001-exact-fixture-2026-10-23.json",
            ),
            independent_validation_plan=(
                "independent implementation",
                "numerical controlled-unitary optimization",
            ),
            claimed_mechanism="orthogonality-limited information transfer in the stated protocol",
            independent_validation_count=0,
        )
        candidate.validate()
        self.assertTrue(candidate.testable)
        self.assertFalse(candidate.ready_for_physical_candidate_claim)


if __name__ == "__main__":
    unittest.main()
