"""Tests for Batch 044 / FND-007B3 quality-adjusted hardware ledger.

Research Attribution:
- Research Owner / Principal Investigator / Research Direction: Kanutsanan Pongpanna
- AI Research Agent: OpenAI GPT-5.6 Sol
- AI-assisted contribution: conditional hardware-threshold tests and evidence checks.
"""

import math
import unittest

from uqpu.lattice_gauge_qudit_quality_ledger import (
    FULL_GAUGE_D3,
    PURE_GAUGE_D3,
    SourceHardwareContext,
    batch044_certificate,
    bounded_mean_sampling_envelope,
    circuit_survival_proxy,
    expected_heating_over_interval,
    native_qudit_success_threshold,
    quality_adjusted_entangler_cost,
    repetitions_for_hoeffding,
    serial_duration_ceiling_seconds,
)


class LatticeGaugeQuditQualityLedgerTests(unittest.TestCase):
    def test_source_hardware_context_frozen_values(self):
        context = SourceHardwareContext()
        self.assertEqual(context.qutrit_repetitions, 150)
        self.assertEqual(context.ququint_repetitions, 300)
        self.assertEqual(context.time_evolution_repetitions, 150)
        self.assertTrue(math.isclose(context.motional_coherence_seconds, 0.0274))
        self.assertTrue(math.isclose(context.heating_rate_phonons_per_second, 2.7))
        self.assertTrue(math.isclose(context.optical_t1_seconds, 1.1))
        self.assertTrue(math.isclose(context.optical_t2_seconds, 0.092))
        self.assertTrue(math.isclose(context.representative_blue_sideband_rabi_hz, 4000.0))

    def test_batch042_resource_pairs_are_frozen(self):
        self.assertEqual(FULL_GAUGE_D3.native_qudit_entangler_equivalents, 26)
        self.assertEqual(FULL_GAUGE_D3.one_hot_qubit_entanglers, 90)
        self.assertEqual(PURE_GAUGE_D3.native_qudit_entangler_equivalents, 8)
        self.assertEqual(PURE_GAUGE_D3.one_hot_qubit_entanglers, 84)

    def test_survival_and_quality_cost_are_monotonic(self):
        self.assertTrue(math.isclose(circuit_survival_proxy(10, 1.0), 1.0))
        self.assertGreater(circuit_survival_proxy(26, 0.99), circuit_survival_proxy(90, 0.99))
        self.assertLess(
            quality_adjusted_entangler_cost(26, 0.99),
            quality_adjusted_entangler_cost(90, 0.99),
        )

    def test_break_even_thresholds_match_frozen_diagnostics(self):
        self.assertTrue(
            math.isclose(
                native_qudit_success_threshold(26, 90, 0.99),
                0.9207674043211239,
                rel_tol=0.0,
                abs_tol=1e-15,
            )
        )
        self.assertTrue(
            math.isclose(
                native_qudit_success_threshold(26, 90, 0.999),
                0.9500682377259113,
                rel_tol=0.0,
                abs_tol=1e-15,
            )
        )
        self.assertTrue(
            math.isclose(
                native_qudit_success_threshold(8, 84, 0.99),
                0.6706885326500162,
                rel_tol=0.0,
                abs_tol=1e-15,
            )
        )

    def test_break_even_threshold_is_actual_cost_equality(self):
        for pair in (FULL_GAUGE_D3, PURE_GAUGE_D3):
            qubit_success = 0.995
            qudit_success = native_qudit_success_threshold(
                pair.native_qudit_entangler_equivalents,
                pair.one_hot_qubit_entanglers,
                qubit_success,
            )
            qudit_cost = quality_adjusted_entangler_cost(
                pair.native_qudit_entangler_equivalents,
                qudit_success,
            )
            qubit_cost = quality_adjusted_entangler_cost(
                pair.one_hot_qubit_entanglers,
                qubit_success,
            )
            self.assertTrue(
                math.isclose(qudit_cost, qubit_cost, rel_tol=1e-12, abs_tol=1e-12)
            )

    def test_serial_coherence_budget_is_only_a_count_based_ceiling(self):
        context = SourceHardwareContext()
        full_qudit = serial_duration_ceiling_seconds(
            context.motional_coherence_seconds,
            FULL_GAUGE_D3.native_qudit_entangler_equivalents,
        )
        full_qubit = serial_duration_ceiling_seconds(
            context.motional_coherence_seconds,
            FULL_GAUGE_D3.one_hot_qubit_entanglers,
        )
        self.assertTrue(math.isclose(full_qudit * 1e6, 1053.8461538461538))
        self.assertTrue(math.isclose(full_qubit * 1e6, 304.44444444444446))
        self.assertGreater(full_qudit, full_qubit)

    def test_source_repetition_sampling_envelopes_and_hoeffding_requirements(self):
        qutrit = bounded_mean_sampling_envelope(150)
        ququint = bounded_mean_sampling_envelope(300)
        self.assertTrue(math.isclose(qutrit.worst_case_standard_error, 0.08164965809277261))
        self.assertTrue(math.isclose(qutrit.hoeffding_half_width, 0.22177704883099564))
        self.assertTrue(math.isclose(ququint.worst_case_standard_error, 0.05773502691896257))
        self.assertTrue(math.isclose(ququint.hoeffding_half_width, 0.1568200551399371))
        self.assertEqual(repetitions_for_hoeffding(0.10), 738)
        self.assertEqual(repetitions_for_hoeffding(0.05), 2952)
        self.assertEqual(repetitions_for_hoeffding(0.02), 18445)
        self.assertEqual(repetitions_for_hoeffding(0.01), 73778)

    def test_motional_heating_context_value(self):
        context = SourceHardwareContext()
        self.assertTrue(
            math.isclose(
                expected_heating_over_interval(
                    context.heating_rate_phonons_per_second,
                    context.motional_coherence_seconds,
                ),
                0.07398,
            )
        )

    def test_certificate_preserves_conditional_boundary_and_nonclaims(self):
        certificate = batch044_certificate()
        self.assertEqual(
            certificate["classification"],
            "LATTICE_QED_QUDIT_QUALITY_ADJUSTED_HARDWARE_THRESHOLD_LEDGER",
        )
        self.assertEqual(
            certificate["evidence_level"],
            "SOURCE_GROUNDED_CONDITIONAL_HARDWARE_DIAGNOSTIC",
        )
        self.assertIn(
            "If measured native-qudit entangler quality",
            certificate["interpretation"]["falsifier"],
        )
        self.assertIn(
            "does not pin directly comparable",
            certificate["interpretation"]["unresolved"],
        )
        self.assertTrue(all(value is False for value in certificate["non_claims"].values()))

    def test_invalid_inputs_raise(self):
        calls = (
            lambda: circuit_survival_proxy(0, 0.99),
            lambda: circuit_survival_proxy(1, 0.0),
            lambda: quality_adjusted_entangler_cost(1, 1.01),
            lambda: native_qudit_success_threshold(90, 26, 0.99),
            lambda: native_qudit_success_threshold(26, 90, 0.0),
            lambda: serial_duration_ceiling_seconds(0.0, 10),
            lambda: bounded_mean_sampling_envelope(0),
            lambda: bounded_mean_sampling_envelope(10, confidence=1.0),
            lambda: repetitions_for_hoeffding(0.0),
            lambda: expected_heating_over_interval(-1.0, 1.0),
        )
        for call in calls:
            with self.subTest(call=repr(call)):
                with self.assertRaises(ValueError):
                    call()


if __name__ == "__main__":
    unittest.main()
