import unittest

from uqpu.multivariate_query_contract import (
    MultiOracleQueryContract,
    compare_query_contracts,
)

HASH_A = "a" * 64
HASH_B = "b" * 64
HASH_C = "c" * 64


def contract(**overrides):
    values = dict(
        contract_id="MOPC-001",
        source_id="arXiv:2610.08714",
        source_reference="https://arxiv.org/abs/2610.08714",
        source_sha256=HASH_A,
        polynomial_sha256=HASH_B,
        output_semantics_sha256=HASH_C,
        theorem_scope="finite-degree polynomial under joint block access",
        oracle_model="JOINT_BLOCK_ACCESS",
        variable_names=("A", "B"),
        degree_by_variable=(2, 3),
        bound_class="ASYMPTOTIC_UPPER",
        symbolic_query_bound="O(D/sqrt(tau))",
        normalization_tau=0.25,
        approximation_error=1e-6,
    )
    values.update(overrides)
    return MultiOracleQueryContract(**values)


class MultiOracleQueryContractTests(unittest.TestCase):
    def test_joint_block_access_preserves_asymptotic_scope(self):
        contract().validate()

    def test_joint_block_access_rejects_invalid_tau(self):
        with self.assertRaisesRegex(ValueError, "normalization_tau"):
            contract(normalization_tau=1.0).validate()

    def test_joint_block_access_rejects_rewritten_bound(self):
        with self.assertRaisesRegex(ValueError, "O\\(D/sqrt"):
            contract(symbolic_query_bound="D").validate()

    def test_row_block_access_records_exact_D_without_calling_it_measured(self):
        contract(
            oracle_model="ROW_BLOCK_ACCESS",
            bound_class="EXACT_QUERY_COUNT",
            symbolic_query_bound="D",
            normalization_tau=None,
            declared_degree=5,
        ).validate()

    def test_row_block_access_requires_declared_degree(self):
        with self.assertRaisesRegex(ValueError, "declared_degree"):
            contract(
                oracle_model="ROW_BLOCK_ACCESS",
                bound_class="EXACT_QUERY_COUNT",
                symbolic_query_bound="D",
                normalization_tau=None,
            ).validate()

    def test_per_variable_optimal_query_vector_matches_degrees(self):
        contract(
            source_id="arXiv:2610.03393",
            source_reference="https://arxiv.org/abs/2610.03393",
            oracle_model="MULTIVARIABLE_SIGNAL_ORACLE",
            bound_class="OPTIMAL_PER_VARIABLE",
            symbolic_query_bound="queries_j = degree_j for each variable j",
            normalization_tau=None,
            exact_query_count_by_variable=(2, 3),
        ).validate()

    def test_per_variable_bound_rejects_mismatched_query_vector(self):
        with self.assertRaisesRegex(ValueError, "degree vector"):
            contract(
                source_id="arXiv:2610.03393",
                source_reference="https://arxiv.org/abs/2610.03393",
                oracle_model="MULTIVARIABLE_SIGNAL_ORACLE",
                bound_class="OPTIMAL_PER_VARIABLE",
                symbolic_query_bound="queries_j = degree_j for each variable j",
                normalization_tau=None,
                exact_query_count_by_variable=(2, 2),
            ).validate()

    def test_mqsp_feasibility_does_not_claim_application_query_bound(self):
        with self.assertRaisesRegex(ValueError, "cannot be silently converted"):
            contract(
                source_id="Quantum 10, 2102 (2026)",
                oracle_model="M_QSP_SIGNAL_OPERATORS",
                bound_class="ASYMPTOTIC_UPPER",
                symbolic_query_bound="polynomial time decision algorithm",
                normalization_tau=None,
            ).validate()

    def test_literature_asymptotic_cannot_be_labelled_measured(self):
        with self.assertRaisesRegex(ValueError, "literature-only"):
            contract(measured_query_count=10).validate()

    def test_measured_query_count_requires_execution_record(self):
        with self.assertRaisesRegex(ValueError, "execution record"):
            contract(
                evidence_class="SIMULATION",
                measured_query_count=10,
            ).validate()

    def test_real_qpu_count_requires_target_identity(self):
        with self.assertRaisesRegex(ValueError, "provider/target"):
            contract(
                evidence_class="REAL_QPU",
                measured_query_count=10,
                execution_record_reference="run:123",
            ).validate()

    def test_duplicate_variables_rejected(self):
        with self.assertRaisesRegex(ValueError, "unique"):
            contract(variable_names=("A", "A")).validate()

    def test_contracts_with_different_oracle_models_are_incomparable(self):
        left = contract()
        right = contract(
            oracle_model="ROW_BLOCK_ACCESS",
            bound_class="EXACT_QUERY_COUNT",
            symbolic_query_bound="D",
            normalization_tau=None,
            declared_degree=5,
        )
        decision = compare_query_contracts(left, right)
        self.assertFalse(decision.comparable)
        self.assertEqual(decision.status, "INCOMPARABLE")
        self.assertIn("oracle_model", decision.reason)

    def test_contracts_with_different_evidence_classes_are_incomparable(self):
        decision = compare_query_contracts(
            contract(),
            contract(evidence_class="SIMULATION"),
        )
        self.assertFalse(decision.comparable)
        self.assertIn("evidence_class", decision.reason)

    def test_contracts_with_different_polynomial_hashes_are_incomparable(self):
        decision = compare_query_contracts(
            contract(),
            contract(polynomial_sha256="d" * 64),
        )
        self.assertFalse(decision.comparable)
        self.assertIn("polynomial_sha256", decision.reason)

    def test_matched_contracts_are_comparable_even_when_source_ids_differ(self):
        decision = compare_query_contracts(contract(), contract(source_id="independent-check"))
        self.assertTrue(decision.comparable)
        self.assertEqual(decision.status, "MATCHED_CONTRACT")


if __name__ == "__main__":
    unittest.main()
