import unittest

from uqpu.equation_identifiability import (
    SensitivityDesign,
    assess_local_identifiability,
)


class EquationIdentifiabilityTests(unittest.TestCase):
    def _design(self, design_id, matrix, provenance=None):
        return SensitivityDesign(
            design_id=design_id,
            dimensionless_sensitivity_matrix=tuple(tuple(row) for row in matrix),
            normalization_provenance=tuple(
                provenance
                or (
                    "unitless synthetic observation scale = 1",
                    "theta_a parameter scale = 1",
                    "theta_b parameter scale = 1",
                )
            ),
        )

    def test_full_rank_converged_candidate_is_locally_identifiable(self):
        report = assess_local_identifiability(
            self._design("quadratic", [[1.0, 1.0], [2.0, 4.0]]),
            solver_converged=True,
        )
        self.assertEqual(report.verdict, "IDENTIFIABLE")
        self.assertEqual(report.rank, 2)
        self.assertEqual(report.nullspace_basis, ())

    def test_confounded_parameters_return_a_null_direction(self):
        report = assess_local_identifiability(
            self._design("linear-a-plus-b", [[1.0, 1.0], [2.0, 2.0]]),
            solver_converged=True,
        )
        self.assertEqual(report.verdict, "LOCALLY_NON_IDENTIFIABLE")
        self.assertEqual(report.rank, 1)
        self.assertEqual(len(report.nullspace_basis), 1)
        direction = report.nullspace_basis[0]
        self.assertAlmostEqual(direction[0] + direction[1], 0.0, places=9)

    def test_complete_bounded_class_is_exhausted_only_if_all_designs_are_singular(self):
        report = assess_local_identifiability(
            self._design("linear-1", [[1.0, 1.0], [2.0, 2.0]]),
            solver_converged=True,
            alternative_designs=(
                self._design("linear-2", [[3.0, 3.0], [4.0, 4.0]]),
            ),
            experiment_class_complete=True,
        )
        self.assertEqual(report.verdict, "EXPERIMENT_CLASS_EXHAUSTED")
        self.assertEqual(report.design_ranks, (("linear-1", 1), ("linear-2", 1)))

    def test_full_rank_alternative_prevents_experiment_class_exhaustion(self):
        report = assess_local_identifiability(
            self._design("linear", [[1.0, 1.0], [2.0, 2.0]]),
            solver_converged=True,
            alternative_designs=(
                self._design("quadratic", [[1.0, 1.0], [2.0, 4.0]]),
            ),
            experiment_class_complete=True,
        )
        self.assertEqual(report.verdict, "LOCALLY_NON_IDENTIFIABLE")
        self.assertEqual(report.design_ranks, (("linear", 1), ("quadratic", 2)))

    def test_incomplete_design_class_cannot_be_called_exhausted(self):
        report = assess_local_identifiability(
            self._design("linear", [[1.0, 1.0], [2.0, 2.0]]),
            solver_converged=True,
            alternative_designs=(
                self._design("linear-2", [[3.0, 3.0], [4.0, 4.0]]),
            ),
            experiment_class_complete=False,
        )
        self.assertEqual(report.verdict, "LOCALLY_NON_IDENTIFIABLE")

    def test_unconverged_solver_is_not_yet_solved_even_with_full_rank(self):
        report = assess_local_identifiability(
            self._design("quadratic", [[1.0, 1.0], [2.0, 4.0]]),
            solver_converged=False,
        )
        self.assertEqual(report.verdict, "NOT_YET_SOLVED")

    def test_zero_matrix_returns_full_parameter_nullspace(self):
        report = assess_local_identifiability(
            self._design("no-sensitivity", [[0.0, 0.0], [0.0, 0.0]]),
            solver_converged=True,
        )
        self.assertEqual(report.rank, 0)
        self.assertEqual(len(report.nullspace_basis), 2)

    def test_ragged_matrix_is_rejected(self):
        with self.assertRaises(ValueError):
            assess_local_identifiability(
                self._design("ragged", [[1.0, 1.0], [2.0]]),
                solver_converged=True,
            )

    def test_nonfinite_matrix_entry_is_rejected(self):
        with self.assertRaises(ValueError):
            assess_local_identifiability(
                self._design("nonfinite", [[1.0, float("nan")], [2.0, 4.0]]),
                solver_converged=True,
            )

    def test_duplicate_design_ids_are_rejected(self):
        design = self._design("same", [[1.0, 1.0], [2.0, 2.0]])
        with self.assertRaises(ValueError):
            assess_local_identifiability(
                design,
                solver_converged=True,
                alternative_designs=(design,),
                experiment_class_complete=True,
            )

    def test_inconsistent_parameter_bases_are_rejected(self):
        with self.assertRaises(ValueError):
            assess_local_identifiability(
                self._design("two-parameters", [[1.0, 1.0], [2.0, 2.0]]),
                solver_converged=True,
                alternative_designs=(
                    self._design("one-parameter", [[1.0], [2.0]]),
                ),
            )

    def test_normalization_provenance_is_required(self):
        with self.assertRaises(ValueError):
            assess_local_identifiability(
                self._design("no-provenance", [[1.0, 1.0], [2.0, 4.0]], ()),
                solver_converged=True,
            )


if __name__ == "__main__":
    unittest.main()
