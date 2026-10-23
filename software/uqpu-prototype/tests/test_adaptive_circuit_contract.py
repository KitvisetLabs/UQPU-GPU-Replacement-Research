import unittest

from uqpu.adaptive_circuit_contract import AdaptiveCircuitCapability


class AdaptiveCircuitCapabilityTests(unittest.TestCase):
    def valid(self, **overrides):
        values = dict(
            provider_id="provider-x",
            target_id="target-y",
            api_version="v1",
            evidence_class="OFFICIAL_PROVIDER_DOCUMENTATION",
            source_uri="https://provider.example/docs/dynamic-circuits",
            source_checked_utc="2026-10-23T10:00:00Z",
            source_sha256="a" * 64,
            supports_mid_circuit_measurement=True,
            supports_reset=True,
            supports_classical_conditionals=True,
            max_mid_circuit_measurements=10,
            max_conditional_depth=10,
            measurement_feedback_latency_seconds=None,
        )
        values.update(overrides)
        return AdaptiveCircuitCapability(**values)

    def test_official_target_documentation_can_pass_capability_gate(self):
        record = self.valid()
        record.validate()
        self.assertTrue(record.supports_adaptive_control)

    def test_simulation_does_not_claim_provider_capability(self):
        record = self.valid(evidence_class="SIMULATION_ONLY")
        self.assertFalse(record.supports_adaptive_control)

    def test_dry_run_does_not_claim_provider_capability(self):
        record = self.valid(evidence_class="DRY_RUN_ONLY")
        self.assertFalse(record.supports_adaptive_control)

    def test_unknown_capability_fails_closed(self):
        record = self.valid(supports_reset=None)
        self.assertFalse(record.supports_adaptive_control)

    def test_hardware_result_requires_separate_execution_certificate(self):
        with self.assertRaisesRegex(ValueError, "separate execution certificate"):
            self.valid(evidence_class="HARDWARE_RESULT").validate()

    def test_missing_target_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "target_id"):
            self.valid(target_id=" ").validate()

    def test_non_https_source_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "HTTPS"):
            self.valid(source_uri="http://provider.example/docs").validate()

    def test_space_separated_timestamp_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "RFC3339"):
            self.valid(source_checked_utc="2026-10-23 10:00:00Z").validate()

    def test_impossible_calendar_timestamp_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "valid timestamp"):
            self.valid(source_checked_utc="2026-13-40T10:00:00Z").validate()

    def test_bad_digest_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            self.valid(source_sha256="not-a-digest").validate()

    def test_measurement_limit_contradiction_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "contradicts unsupported"):
            self.valid(
                supports_mid_circuit_measurement=False,
                max_mid_circuit_measurements=3,
            ).validate()

    def test_conditional_limit_contradiction_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "contradicts unsupported"):
            self.valid(
                supports_classical_conditionals=False,
                max_conditional_depth=3,
            ).validate()

    def test_negative_or_non_integer_limits_are_rejected(self):
        for value in (-1, 1.5, True):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    self.valid(max_mid_circuit_measurements=value).validate()

    def test_nonfinite_latency_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "finite"):
            self.valid(measurement_feedback_latency_seconds=float("nan")).validate()

    def test_capability_gate_does_not_claim_quality_or_economics(self):
        record = self.valid()
        self.assertTrue(record.supports_adaptive_control)
        self.assertFalse(hasattr(record, "quality_accepted"))
        self.assertFalse(hasattr(record, "cost_advantage"))
