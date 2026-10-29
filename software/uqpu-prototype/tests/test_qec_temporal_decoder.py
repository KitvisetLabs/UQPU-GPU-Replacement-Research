import unittest

from uqpu.qec_temporal_decoder import (
    DecoderObservation,
    is_physical_device_evidence,
    latency_reduction_percent,
)

URL = "https://arxiv.org/abs/2607.27930"


def observation(name, mean, worst, **overrides):
    values = dict(
        study_id="paper-2607.27930",
        decoder_name=name,
        code_family="rotated-surface-code",
        code_distance=21,
        noise_model="phenomenological-p=0.01",
        physical_error_rate=0.01,
        syndrome_rounds=21,
        target_process="TSMC-CMOS-22nm",
        implementation_stage="LOGIC_SYNTHESIS",
        measurement_basis="synthesized-frequency-times-RTL-cycle-count",
        mean_latency_ns=mean,
        worst_latency_ns=worst,
        source_url=URL,
        evidence_class="SYNTHESIS_ESTIMATE",
        circuit_area_mm2=2.5,
    )
    values.update(overrides)
    return DecoderObservation(**values)


class TemporalDecoderContractTests(unittest.TestCase):
    def test_matched_mean_latency_reduction(self):
        baseline = observation("batch", 200, 1200)
        candidate = observation("sandwich", 130, 1000)
        self.assertAlmostEqual(latency_reduction_percent(baseline, candidate), 35.0)

    def test_worst_case_can_regress_despite_mean_improvement(self):
        baseline = observation("batch", 200, 1000)
        candidate = observation("sandwich", 130, 1100)
        self.assertAlmostEqual(latency_reduction_percent(baseline, candidate, "worst"), -10.0)

    def test_rejects_different_noise_models(self):
        with self.assertRaisesRegex(ValueError, "noise_model"):
            latency_reduction_percent(
                observation("batch", 200, 1200),
                observation("sandwich", 130, 1000, noise_model="circuit-level"),
            )

    def test_rejects_different_process_nodes(self):
        with self.assertRaisesRegex(ValueError, "target_process"):
            latency_reduction_percent(
                observation("batch", 200, 1200),
                observation("sandwich", 130, 1000, target_process="ASAP7-FinFET-7nm"),
            )

    def test_rejects_synthesis_vs_silicon_mixing(self):
        with self.assertRaisesRegex(ValueError, "implementation_stage"):
            latency_reduction_percent(
                observation("batch", 200, 1200),
                observation(
                    "sandwich", 130, 1000,
                    implementation_stage="ASIC_MEASURED",
                    evidence_class="DEVICE_MEASURED",
                ),
            )

    def test_rejects_mean_above_worst(self):
        with self.assertRaisesRegex(ValueError, "mean_latency_ns"):
            observation("bad", 1000, 900).validate()

    def test_rejects_boolean_code_distance(self):
        with self.assertRaisesRegex(ValueError, "code_distance"):
            observation("bad", 100, 200, code_distance=True).validate()

    def test_synthesis_is_not_physical_device_evidence(self):
        self.assertFalse(is_physical_device_evidence(observation("sandwich", 130, 1000)))

    def test_measured_physical_stage_is_separately_labeled(self):
        measured = observation(
            "device", 130, 1000,
            implementation_stage="ASIC_MEASURED",
            evidence_class="DEVICE_MEASURED",
        )
        self.assertTrue(is_physical_device_evidence(measured))

    def test_invalid_metric_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "metric"):
            latency_reduction_percent(
                observation("batch", 200, 1200),
                observation("sandwich", 130, 1000),
                "p99",
            )


if __name__ == "__main__":
    unittest.main()
