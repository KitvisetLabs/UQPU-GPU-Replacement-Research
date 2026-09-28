import hashlib
import json
from pathlib import Path
import unittest

from uqpu.cycle004_delta01 import (
    ai_cost_equivalence_contract,
    benchmark_er6_classical_baseline,
    benchmark_manifest_io,
    bosonic_data_record_gate,
    build_cycle004_packet,
    build_scm_two_party_handoff,
    logical_memory_service_contract,
    materials_and_fabrication_readiness_gate,
    provider_and_cost_gate,
    validate_scm_handoff,
)


ROOT = Path(__file__).resolve().parents[3]
FREEZE = ROOT / "benchmarks/experiments/cycle002-delta01-er6-frozen-contract.json"
CYCLE003 = ROOT / "benchmarks/experiments/cycle003-delta01-er6-provider-neutral-manifest.json"
CYCLE003_SCM = ROOT / "benchmarks/results/cycle003-delta01-scm-cal001-synthetic.json"
AI_BASELINE = ROOT / "benchmarks/results/batch039-ai-cost-002-classical-baseline.json"
PACKET = ROOT / "benchmarks/results/cycle004-delta01-er6-classical-io-and-gates.json"
PUBLIC = ROOT / "benchmarks/experiments/cycle004-delta01-scm-cal001-public-handoff.json"
TRUTH = ROOT / "benchmarks/results/cycle004-delta01-scm-cal001-custodian-truth.json"


def _load(path):
    return json.loads(path.read_text(encoding="utf-8"))


class Cycle004Delta01Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.freeze = _load(FREEZE)
        cls.cycle003 = _load(CYCLE003)
        cls.cycle003_scm = _load(CYCLE003_SCM)
        cls.ai_raw = AI_BASELINE.read_bytes()
        cls.ai = json.loads(cls.ai_raw)

    def test_exact_er6_baseline_preserves_all_four_accepted_outputs(self):
        row = benchmark_er6_classical_baseline(self.freeze, repetitions=3)
        self.assertEqual(row["result"]["states_evaluated"], 64)
        self.assertEqual(row["result"]["best_objective"], -7.0)
        self.assertEqual(row["result"]["accepted_bitstrings_v5_to_v0"],
                         ["001011", "001110", "110001", "110100"])
        self.assertGreaterEqual(row["timing"]["median_ns"], 0)
        self.assertIn("toy", " ".join(row["limitations"]).lower())

    def test_local_manifest_io_records_bytes_hash_and_timing_boundary(self):
        row = benchmark_manifest_io(self.cycle003, repetitions=3)
        self.assertGreater(row["payload"]["canonical_json_utf8_bytes"], 0)
        self.assertEqual(len(row["payload"]["canonical_json_sha256"]), 64)
        self.assertEqual(set(row["timing"]), {"serialize", "file_write", "file_read", "json_decode"})
        self.assertTrue(any("fsync" in item for item in row["limitations"]))

    def test_provider_tariff_does_not_fill_complete_cost_or_authorize_job(self):
        row = provider_and_cost_gate()
        self.assertEqual(row["task_plus_shot_tariff_usd"], "7.563200")
        self.assertEqual(row["reservation_price_usd_per_hour"], "4100.00")
        self.assertIsNone(row["complete_cost_ledger"]["total_cost_usd"])
        self.assertIsNone(row["complete_cost_ledger"]["cost_per_accepted_output_usd"])
        self.assertFalse(row["paid_job_submitted"])
        self.assertEqual(row["authorization_status"], "NOT_AUTHORIZED")

    def test_memory_service_target_is_explicitly_project_chosen_and_source_not_meeting_it(self):
        row = logical_memory_service_contract()
        self.assertEqual(row["project_chosen_service_contract"]["syndrome_cycles"], 100)
        self.assertAlmostEqual(row["model_only_translation"]["sufficient_per_cycle_error_by_union_bound"], 0.0005)
        self.assertGreater(row["model_only_translation"]["source_central_value_over_independent_limit_ratio"], 30)
        self.assertIn("DOES_NOT_MEET", row["conclusion"])
        self.assertFalse(row["project_reproduction"])

    def test_primary_data_record_metadata_does_not_claim_raw_reanalysis(self):
        row = bosonic_data_record_gate()
        self.assertEqual(row["file"]["name"], "data_upload.zip")
        self.assertEqual(row["file"]["md5"], "d4f051ba40bf3d1940f90f9da4e9953c")
        self.assertFalse(row["raw_archive_downloaded"])
        self.assertFalse(row["raw_archive_inspected"])

    def test_material_readiness_fails_closed_without_fabrication(self):
        row = materials_and_fabrication_readiness_gate()
        self.assertEqual(row["satisfied_count"], 0)
        self.assertEqual(row["required_count"], 9)
        self.assertEqual(row["readiness_status"], "NOT_READY_NO_FABRICATION_AUTHORIZED")
        self.assertIsNone(row["capital_at_risk_thb"])

    def test_ai_equivalence_contract_binds_existing_toy_baseline(self):
        digest = hashlib.sha256(self.ai_raw).hexdigest()
        row = ai_cost_equivalence_contract(self.ai, digest)
        self.assertEqual(row["contract_id"], "AI-COST-XOR-MLP-2-16-1-V1")
        self.assertEqual(row["functionally_equivalent_task"]["held_out_accuracy_minimum"], 0.98)
        self.assertEqual(row["baseline_provenance"]["reference_held_out_accuracy"], 0.98046875)
        self.assertFalse(row["frontier_ai_baseline"])
        self.assertIsNone(row["end_to_end_residual_cost_fraction"])

    def test_scm_public_and_custodian_packages_separate_labels_and_validate_commitment(self):
        public, truth = build_scm_two_party_handoff(
            self.cycle003_scm, "cycle004-synthetic-custodian-demo-v1"
        )
        self.assertFalse(public["condition_labels_present"])
        self.assertFalse(any("condition" in row["payload"] for row in public["observations"]))
        self.assertEqual(validate_scm_handoff(public, truth), [])
        self.assertEqual(truth["independent_site_status"], "NOT_EXECUTED_NO_SECOND_SITE")
        self.assertIn("DEMONSTRATION_ONLY", truth["operational_status"])

    def test_integrated_packet_covers_all_non_scm_lanes_with_null_boundaries(self):
        packet = build_cycle004_packet(
            self.freeze,
            self.cycle003,
            self.ai,
            hashlib.sha256(self.ai_raw).hexdigest(),
            repetitions=3,
            code_commit="a" * 40,
        )
        self.assertEqual(
            set(packet["lanes"]),
            {"A", "B", "C", "D", "E", "F", "G", "H", "FND/EQN", "AI-COST", "QOS/QSVT"},
        )
        self.assertFalse(packet["lanes"]["H"]["funding_or_purchase_authorized"])
        self.assertFalse(packet["lanes"]["QOS/QSVT"]["hardware_executed"])

    def test_committed_cycle004_artifacts_have_valid_cross_links(self):
        if not PACKET.exists() or not PUBLIC.exists() or not TRUTH.exists():
            self.skipTest("Cycle 004 generated artifacts are committed after generator SHA is known.")
        packet = _load(PACKET)
        public = _load(PUBLIC)
        truth = _load(TRUTH)
        self.assertEqual(packet["cycle"], "004")
        self.assertEqual(len(packet["generator_code_commit"]), 40)
        self.assertEqual(packet["lanes"]["A"]["result"]["states_evaluated"], 64)
        self.assertEqual(validate_scm_handoff(public, truth), [])


if __name__ == "__main__":
    unittest.main()
