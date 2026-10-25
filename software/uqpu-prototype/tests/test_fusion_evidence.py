import unittest

from uqpu.fusion_evidence import (
    FusionEvidenceLevel,
    FusionEvidenceRecord,
    classify_fusion_evidence,
)


class FusionEvidenceTests(unittest.TestCase):
    def test_empty_record_is_not_system_evidence(self):
        self.assertEqual(
            classify_fusion_evidence(FusionEvidenceRecord("source:empty")),
            FusionEvidenceLevel.NO_SYSTEM_DATA,
        )

    def test_lm26_temperature_milestone_does_not_promote_to_net_electricity(self):
        record = FusionEvidenceRecord(
            "https://arxiv.org/abs/2610.11890",
            electron_temperature_kev=1.180,
            ion_temperature_kev=0.459,
            fusion_power_w=1.0,
        )
        self.assertEqual(
            classify_fusion_evidence(record),
            FusionEvidenceLevel.PLASMA_OR_FUSION_MILESTONE_ONLY,
        )

    def test_partial_electric_record_fails_closed(self):
        record = FusionEvidenceRecord("source:partial", gross_electric_power_w=100.0)
        self.assertEqual(
            classify_fusion_evidence(record),
            FusionEvidenceLevel.ELECTRIC_ACCOUNTING_INCOMPLETE,
        )

    def test_consistent_positive_net_power_accounting(self):
        record = FusionEvidenceRecord(
            "source:metered",
            gross_electric_power_w=1000.0,
            recirculating_electric_power_w=300.0,
            other_parasitic_power_w=100.0,
            grid_delivery_losses_w=10.0,
            net_delivered_electric_power_w=590.0,
            meter_boundary="plant export meter",
            averaging_duration_s=3600.0,
        )
        self.assertEqual(
            classify_fusion_evidence(record),
            FusionEvidenceLevel.NET_ELECTRICITY_ACCOUNTING_CONSISTENT,
        )

    def test_inconsistent_net_power_accounting_is_rejected(self):
        record = FusionEvidenceRecord(
            "source:bad-meter-balance",
            gross_electric_power_w=1000.0,
            recirculating_electric_power_w=300.0,
            other_parasitic_power_w=100.0,
            grid_delivery_losses_w=10.0,
            net_delivered_electric_power_w=600.0,
            meter_boundary="plant export meter",
            averaging_duration_s=3600.0,
        )
        self.assertEqual(
            classify_fusion_evidence(record),
            FusionEvidenceLevel.ELECTRIC_ACCOUNTING_INCONSISTENT,
        )

    def test_nonpositive_net_output_is_not_a_positive_export(self):
        record = FusionEvidenceRecord(
            "source:net-import",
            gross_electric_power_w=100.0,
            recirculating_electric_power_w=100.0,
            other_parasitic_power_w=10.0,
            grid_delivery_losses_w=0.0,
            net_delivered_electric_power_w=-10.0,
            meter_boundary="plant export meter",
            averaging_duration_s=60.0,
        )
        self.assertEqual(
            classify_fusion_evidence(record),
            FusionEvidenceLevel.NET_OUTPUT_NONPOSITIVE,
        )

    def test_meter_boundary_is_required(self):
        record = FusionEvidenceRecord(
            "source:no-boundary",
            gross_electric_power_w=1000.0,
            recirculating_electric_power_w=100.0,
            other_parasitic_power_w=100.0,
            grid_delivery_losses_w=0.0,
            net_delivered_electric_power_w=800.0,
            averaging_duration_s=60.0,
        )
        self.assertEqual(
            classify_fusion_evidence(record),
            FusionEvidenceLevel.ELECTRIC_ACCOUNTING_INCOMPLETE,
        )

    def test_negative_gross_electric_power_is_invalid(self):
        record = FusionEvidenceRecord("source:negative", gross_electric_power_w=-1.0)
        with self.assertRaises(ValueError):
            record.validate()

    def test_capacity_factor_must_be_in_unit_interval(self):
        record = FusionEvidenceRecord("source:capacity-factor", capacity_factor=1.01)
        with self.assertRaises(ValueError):
            record.validate()

    def test_nan_temperature_is_invalid(self):
        record = FusionEvidenceRecord("source:nan", electron_temperature_kev=float("nan"))
        with self.assertRaises(ValueError):
            record.validate()

    def test_boolean_is_not_a_pulse_count(self):
        record = FusionEvidenceRecord("source:bool-count", repeated_pulses=True)
        with self.assertRaises(ValueError):
            record.validate()

    def test_negative_tolerance_is_invalid(self):
        with self.assertRaises(ValueError):
            classify_fusion_evidence(FusionEvidenceRecord("source:tol"), relative_tolerance=-0.1)


if __name__ == "__main__":
    unittest.main()
