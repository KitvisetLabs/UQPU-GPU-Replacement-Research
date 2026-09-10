import unittest

from uqpu.equation_recovery_benchmark import (
    combine_dimensions,
    fit_scalar_power_law,
    kinetic_energy_calibration,
    recover_power_law,
)


class EquationRecoveryBenchmarkTests(unittest.TestCase):
    def test_dimension_composition(self):
        mass = (1, 0, 0)
        velocity = (0, 1, -1)
        self.assertEqual(combine_dimensions(((mass, 1), (velocity, 2))), (1, 2, -2))

    def test_kinetic_energy_hidden_power_is_recovered(self):
        result = kinetic_energy_calibration()
        self.assertEqual(result["selected_power"], 2)
        self.assertAlmostEqual(result["coefficient"], 1.5, places=12)
        self.assertAlmostEqual(result["holdout_rmse"], 0.0, places=12)
        self.assertEqual(result["dimensionally_allowed_powers"], [2])
        self.assertEqual(result["evidence_level"], "MODEL_ONLY")
        self.assertFalse(result["new_physical_law_claim"])

    def test_heldout_selection_recovers_structure_without_dimension_filter(self):
        x = (1.0, 2.0, 3.0, 4.0, 5.0)
        y = tuple(7.0 * value**3 for value in x)
        fit = recover_power_law(
            x,
            y,
            candidate_powers=(1, 2, 3, 4),
            train_indices=(0, 2, 4),
            holdout_indices=(1, 3),
        )
        self.assertEqual(fit.power, 3)
        self.assertAlmostEqual(fit.coefficient, 7.0, places=12)
        self.assertAlmostEqual(fit.holdout_rmse, 0.0, places=12)

    def test_train_and_holdout_must_be_disjoint(self):
        with self.assertRaises(ValueError):
            fit_scalar_power_law(
                (1.0, 2.0),
                (1.0, 4.0),
                power=2,
                train_indices=(0, 1),
                holdout_indices=(1,),
            )

    def test_dimension_gate_can_reject_best_curve_fit(self):
        x = (1.0, 2.0, 3.0, 4.0)
        y = tuple(5.0 * value**2 for value in x)
        fit = recover_power_law(
            x,
            y,
            candidate_powers=(1, 2),
            train_indices=(0, 1),
            holdout_indices=(2, 3),
            allowed_powers={1},
        )
        self.assertEqual(fit.power, 1)
        self.assertGreater(fit.holdout_rmse, 0.0)


if __name__ == "__main__":
    unittest.main()
