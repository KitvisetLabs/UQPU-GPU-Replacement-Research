import unittest

from uqpu.benchmark_pipeline import BenchmarkRunPlan
from uqpu.output_accounting import (
    OutputInformationContract,
    OutputMeasurement,
    audit_output_accounting,
)
from uqpu.state_accounting import StateAccounting
from uqpu.workload_contracts import ClassicalRole, WorkloadContract


def _state() -> StateAccounting:
    return StateAccounting(0, 0, 0, 0)


def _workload(output: OutputInformationContract | None) -> WorkloadContract:
    return WorkloadContract(
        workload_id="fnd002-output-audit",
        roles=(ClassicalRole.CPU,),
        input_semantics="seeded accepted-outcome source",
        output_semantics="one accepted outcome label",
        quality_metric="accepted-outcome identity",
        exactness_required=output.exactness_required if output is not None else False,
        output_information=output,
    )


class OutputAccountingTests(unittest.TestCase):
    def test_exact_contract_exposes_fixed_width_rate(self):
        contract = OutputInformationContract(
            distinguishable_outcomes=2**512,
            exactness_required=True,
            required_results_per_second=1_000_000,
        )
        self.assertEqual(contract.information_lower_bound_bits, 512.0)
        self.assertEqual(contract.fixed_width_label_bitrate_lower_bound_bps, 512_000_000.0)

    def test_approximate_uniform_contract_uses_fano_bound(self):
        contract = OutputInformationContract(
            distinguishable_outcomes=64,
            exactness_required=False,
            allowed_error_probability=0.01,
            uniform_prior_assumed=True,
        )
        self.assertAlmostEqual(contract.information_lower_bound_bits, 5.85943406486909, places=12)

    def test_approximate_nonuniform_contract_does_not_invent_bound(self):
        contract = OutputInformationContract(
            distinguishable_outcomes=64,
            exactness_required=False,
            allowed_error_probability=0.01,
            uniform_prior_assumed=False,
        )
        self.assertIsNone(contract.information_lower_bound_bits)

    def test_fixed_width_payload_audit_and_egress_rate(self):
        contract = OutputInformationContract(
            distinguishable_outcomes=64,
            exactness_required=True,
            required_results_per_second=10,
        )
        measurement = OutputMeasurement(
            measured_output_bytes_per_accepted_result=1,
            reconstruction_seconds_per_accepted_result=0.002,
            measured_accepted_results_per_second=10,
            measured_error_probability=0.0,
        )
        audit = audit_output_accounting(contract, measurement)
        self.assertEqual(audit.fixed_width_label_floor_bits, 6)
        self.assertEqual(audit.fixed_width_label_status, "PASS")
        self.assertEqual(audit.error_budget_status, "PASS")
        self.assertEqual(audit.measured_egress_bits_per_accepted_result, 8)
        self.assertEqual(audit.measured_egress_bitrate_bps, 80.0)
        self.assertAlmostEqual(audit.reconstruction_seconds_per_accepted_result, 0.002)

    def test_below_floor_is_flagged_not_silently_accepted(self):
        contract = OutputInformationContract(distinguishable_outcomes=64)
        audit = audit_output_accounting(
            contract,
            OutputMeasurement(0, 0.0),
        )
        self.assertEqual(audit.fixed_width_label_status, "BELOW_FLOOR_REQUIRES_REVIEW")

    def test_side_information_or_non_fixed_encoding_is_not_compared(self):
        for contract in (
            OutputInformationContract(
                distinguishable_outcomes=64,
                side_information_available=True,
                side_information_description="receiver has a shared immutable lookup table",
            ),
            OutputInformationContract(
                distinguishable_outcomes=64,
                encoding_mode="variable_length",
            ),
        ):
            audit = audit_output_accounting(
                contract,
                OutputMeasurement(0, 0.0),
            )
            self.assertEqual(audit.fixed_width_label_status, "NOT_COMPARABLE")
            self.assertIsNone(audit.fixed_width_label_floor_bits)

    def test_side_information_bytes_require_declared_side_information(self):
        contract = OutputInformationContract(distinguishable_outcomes=8)
        with self.assertRaisesRegex(ValueError, "side-information bytes require"):
            audit_output_accounting(
                contract,
                OutputMeasurement(
                    1, 0.0, side_information_bytes_per_accepted_result=2
                ),
            )

    def test_side_information_is_counted_in_egress_rate(self):
        contract = OutputInformationContract(
            distinguishable_outcomes=64,
            side_information_available=True,
            side_information_description="receiver has a shared immutable lookup table",
            required_results_per_second=10,
        )
        audit = audit_output_accounting(
            contract,
            OutputMeasurement(
                1, 0.002,
                side_information_bytes_per_accepted_result=2,
                measured_accepted_results_per_second=10,
            ),
        )
        self.assertEqual(audit.fixed_width_label_status, "NOT_COMPARABLE")
        self.assertEqual(audit.measured_egress_bitrate_bps, 240.0)

    def test_error_budget_failure_is_explicit(self):
        contract = OutputInformationContract(
            distinguishable_outcomes=8,
            exactness_required=False,
            allowed_error_probability=0.05,
        )
        audit = audit_output_accounting(
            contract,
            OutputMeasurement(1, 0.0, measured_error_probability=0.1),
        )
        self.assertEqual(audit.error_budget_status, "FAIL")

    def test_workload_contract_requires_measurement_at_benchmark_boundary(self):
        output = OutputInformationContract(distinguishable_outcomes=8)
        contract = _workload(output)
        plan = BenchmarkRunPlan(
            contract, "local", "deterministic-reference", 1, _state(), _state()
        )
        with self.assertRaisesRegex(ValueError, "output_measurement is required"):
            plan.validate()

    def test_workload_exactness_must_match_output_contract(self):
        contract = WorkloadContract(
            workload_id="fnd002-mismatch",
            roles=(ClassicalRole.CPU,),
            input_semantics="seeded accepted-outcome source",
            output_semantics="one accepted outcome label",
            quality_metric="accepted-outcome identity",
            exactness_required=False,
            output_information=OutputInformationContract(
                distinguishable_outcomes=8,
                exactness_required=True,
            ),
        )
        with self.assertRaisesRegex(ValueError, "must match output_information"):
            contract.validate()

    def test_benchmark_rejects_output_measurement_without_contract(self):
        plan = BenchmarkRunPlan(
            _workload(None), "local", "deterministic-reference", 1, _state(), _state(),
            output_measurement=OutputMeasurement(1, 0.0),
        )
        with self.assertRaisesRegex(ValueError, "requires a declared output_information"):
            plan.validate()

    def test_benchmark_rejects_payload_below_fixed_width_floor(self):
        contract = _workload(OutputInformationContract(distinguishable_outcomes=64))
        plan = BenchmarkRunPlan(
            contract, "local", "deterministic-reference", 1, _state(), _state(),
            output_measurement=OutputMeasurement(0, 0.0),
        )
        with self.assertRaisesRegex(ValueError, "below the declared fixed-width"):
            plan.validate()

    def test_benchmark_rejects_error_budget_violation(self):
        contract = _workload(OutputInformationContract(
            distinguishable_outcomes=8,
            exactness_required=False,
            allowed_error_probability=0.05,
        ))
        plan = BenchmarkRunPlan(
            contract, "local", "deterministic-reference", 1, _state(), _state(),
            output_measurement=OutputMeasurement(
                1, 0.0, measured_error_probability=0.1
            ),
        )
        with self.assertRaisesRegex(ValueError, "exceeds the declared contract budget"):
            plan.validate()

    def test_invalid_contract_and_measurements_fail_closed(self):
        with self.assertRaises(ValueError):
            OutputInformationContract(0).validate()
        with self.assertRaises(ValueError):
            OutputInformationContract(
                4, exactness_required=False, allowed_error_probability=None
            ).validate()
        with self.assertRaises(ValueError):
            OutputInformationContract(4, encoding_mode="unknown").validate()
        with self.assertRaises(ValueError):
            OutputInformationContract(4, encoding_mode=[]).validate()
        with self.assertRaises(ValueError):
            OutputInformationContract(
                4, side_information_available=True
            ).validate()
        with self.assertRaises(ValueError):
            OutputInformationContract(
                4, side_information_description="orphaned description"
            ).validate()
        with self.assertRaises(ValueError):
            OutputMeasurement(-1, 0.0).validate()
        with self.assertRaises(ValueError):
            OutputMeasurement(1, float("nan")).validate()
        with self.assertRaises(ValueError):
            OutputMeasurement(1, 0.0, measured_error_probability=1.1).validate()


if __name__ == "__main__":
    unittest.main()
