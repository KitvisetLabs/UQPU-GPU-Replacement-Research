import json
from copy import deepcopy
from decimal import Decimal
from pathlib import Path
import unittest

from uqpu.cycle003_delta01 import (
    ai_cost_ceiling,
    bosonic_qec_source_analysis,
    braket_rigetti_tariff_sensitivity,
    build_cycle003_manifest,
    build_synthetic_cal001_fixture,
    end_to_end_cost_result,
    materials_readiness_gate,
)


ROOT = Path(__file__).resolve().parents[3]
FREEZE = ROOT / "benchmarks/experiments/cycle002-delta01-er6-frozen-contract.json"
PROTOCOL = ROOT / "benchmarks/experiments/batch020-er6-mean-vs-cvar-real-qpu-protocol.json"
CIRCUIT_ARTIFACT = ROOT / "benchmarks/experiments/cycle003-delta01-er6-provider-neutral-manifest.json"
SCM_ARTIFACT = ROOT / "benchmarks/results/cycle003-delta01-scm-cal001-synthetic.json"


class Cycle003Delta01Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.freeze = json.loads(FREEZE.read_text(encoding="utf-8"))
        cls.protocol = json.loads(PROTOCOL.read_text(encoding="utf-8"))

    def test_provider_neutral_pair_preserves_frozen_er6_contract_and_gate_counts(self):
        packet = build_cycle003_manifest(self.freeze, self.protocol)
        qaoa = packet["lane_a_b_c_qos"]
        self.assertEqual(qaoa["source_contract"]["instance_sha256"],
                         "bc3fb615b6fd2530694b097fde804e62f165fd7d0953bf66aff4602cd77fa201")
        self.assertEqual(qaoa["source_contract"]["output_contract_id"], "8efaa94bb3306d25")
        self.assertEqual(qaoa["source_contract"]["accepted_bitstrings_v5_to_v0"],
                         ["001011", "001110", "110001", "110100"])
        self.assertEqual(len(qaoa["paired_circuits"]), 2)
        for circuit in qaoa["paired_circuits"]:
            self.assertEqual(circuit["logical_gate_counts"], {"h": 6, "cx": 18, "rz": 9, "rx": 6})
            self.assertEqual(circuit["logical_gate_instruction_count"], 39)
            self.assertEqual(circuit["measure_all_instructions"], 1)
            self.assertTrue(circuit["openqasm_3"].startswith("OPENQASM 3.0;\n"))
            self.assertEqual(circuit["openqasm_3_utf8_bytes"],
                             len(circuit["openqasm_3"].encode("utf-8")))
            self.assertIsNone(circuit["provider_transpilation"])
            self.assertIsNone(circuit["physical_depth"])
            self.assertIsNone(circuit["physical_two_qubit_gate_count"])
        self.assertEqual(qaoa["readout_payload_bounds"]["packed_raw_measurement_bytes_per_candidate"], 6144)
        self.assertEqual(qaoa["readout_payload_bounds"]["packed_raw_measurement_bytes_for_pair"], 12288)
        self.assertEqual(qaoa["readout_payload_bounds"]["minimum_bits_to_label_one_of_four_accepted_outputs"], 2)
        self.assertIsNone(qaoa["readout_payload_bounds"]["transfer_time_seconds"])
        self.assertFalse(qaoa["provider_execution"]["real_qpu_executed"])

    def test_official_braket_task_and_shot_tariff_is_sensitivity_only(self):
        cost = braket_rigetti_tariff_sensitivity(task_count=2, shots_per_task=8192)
        self.assertEqual(cost["qpu_task_plus_shot_tariff_usd"], "7.5632")
        self.assertEqual(cost["total_shots"], 16384)
        self.assertIsNone(cost["full_aws_bill_usd"])
        self.assertIsNone(cost["cost_per_accepted_output_usd"])
        with self.assertRaises(ValueError):
            braket_rigetti_tariff_sensitivity(task_count=0, shots_per_task=8192)

    def test_missing_full_stack_cost_and_accepted_hits_stay_null(self):
        result = end_to_end_cost_result(
            {
                "provider_qpu": Decimal("7.5632"),
                "host_orchestration": None,
                "queue": None,
                "transfer_storage": None,
                "mitigation_decoder": None,
                "retry_failure": None,
                "energy_cooling": None,
                "capital_amortization": None,
            },
            accepted_outputs=None,
        )
        self.assertIsNone(result["total_cost_usd"])
        self.assertIsNone(result["cost_per_accepted_output_usd"])
        self.assertIn("accepted_output_count", result["missing_components"])

    def test_published_bosonic_metric_is_separated_from_memory_lifetime(self):
        row = bosonic_qec_source_analysis()
        self.assertEqual(row["reported_overall_error_definition"],
                         "epsilon_L = (epsilon_L_phase_flip + epsilon_L_bit_flip) / 2")
        self.assertAlmostEqual(row["derived_T_X_lower_bound_us_from_central_value"], 42.4242424242, places=8)
        self.assertIsNone(row["project_logical_error_target"])
        self.assertIsNone(row["project_retention_horizon_cycles"])
        self.assertFalse(row["zenodo_raw_files_fetched"])
        self.assertIn("confidence level is inferred", row["uncertainty_interpretation"])

    def test_latest_astm_catalog_metadata_blocks_unlicensed_compliance_claim(self):
        row = materials_readiness_gate()
        self.assertEqual(row["current_displayed_edition"], "ASTM D4935-18(2026)")
        self.assertEqual(row["catalog_designation"], "D4935-18R26")
        self.assertEqual(row["official_page_price_usd"], "80.00")
        self.assertFalse(row["full_standard_text_available_to_project"])
        self.assertFalse(row["purchase_authorized"])
        self.assertFalse(row["compliance_claim_allowed"])

    def test_ai_cost_ceiling_does_not_turn_er6_into_ai_equivalence(self):
        row = ai_cost_ceiling()
        self.assertEqual(row["owner_defined_budget_thb"], 50000)
        self.assertEqual(row["planning_fx_thb_per_usd"], "33.045")
        self.assertEqual(row["maximum_residual_share_if_every_fixed_cost_were_zero"]["10T"],
                         "1.513088213043E-10")
        self.assertIsNone(row["functional_equivalence_workload"])
        self.assertIsNone(row["adjusted_residual_share_after_fixed_costs"])

    def test_synthetic_calibration_observation_payload_omits_hidden_condition(self):
        first = build_synthetic_cal001_fixture()
        second = build_synthetic_cal001_fixture()
        self.assertEqual(first, second)
        self.assertEqual(first["condition_count"], 256)
        self.assertEqual(first["evidence_class"], "SYNTHETIC_PIPELINE_VALIDATION_ONLY")
        self.assertNotIn("condition", first["blinded_observations"][0]["payload"])
        self.assertEqual(len(first["trial_ledger"]), 256)
        self.assertEqual(first["summary_after_truth_unseal"]["sensitivity"], 1.0)
        self.assertFalse(first["independent_site_manifest"]["source_claim_supported"])
        self.assertEqual(first["independent_site_manifest"]["status"], "NOT_EXECUTED_NO_SECOND_SITE")

    def test_synthetic_replication_manifest_binds_data_and_code_without_claiming_a_replication(self):
        result = build_synthetic_cal001_fixture(code_commit="a" * 40)
        self.assertEqual(result["replication_manifest"]["code_commit"], "a" * 40)
        self.assertEqual(result["replication_manifest"]["data_sha256"], result["dataset_bundle_sha256"])
        self.assertEqual(result["replication_manifest_validation_errors"], [])
        self.assertEqual(result["independent_site_manifest"]["replication_site_id"], None)

    def test_paid_execution_or_contract_drift_is_rejected(self):
        protocol = deepcopy(self.protocol)
        protocol["paid_job_submitted"] = True
        with self.assertRaisesRegex(ValueError, "paid execution"):
            build_cycle003_manifest(self.freeze, protocol)
        protocol = deepcopy(self.protocol)
        protocol["frozen_candidates"][0]["gamma"] += 0.01
        with self.assertRaisesRegex(ValueError, "candidate drift"):
            build_cycle003_manifest(self.freeze, protocol)

    def test_committed_reproducibility_artifacts_match_builder(self):
        if not CIRCUIT_ARTIFACT.exists() or not SCM_ARTIFACT.exists():
            self.skipTest("Final Cycle 003 artifacts are added after the code commit is identified.")
        circuit = json.loads(CIRCUIT_ARTIFACT.read_text(encoding="utf-8"))
        scm = json.loads(SCM_ARTIFACT.read_text(encoding="utf-8"))
        code_sha = scm["replication_manifest"]["code_commit"]
        self.assertEqual(circuit, build_cycle003_manifest(self.freeze, self.protocol))
        self.assertEqual(scm, build_synthetic_cal001_fixture(code_commit=code_sha))


if __name__ == "__main__":
    unittest.main()
