import hashlib
import json
from pathlib import Path
import unittest

from uqpu.cycle005_delta01 import (
    benchmark_durable_io,
    benchmark_scale_case,
    build_ai_candidate_gate,
    build_braket_dry_run_packet,
    build_capital_dependency_graph,
    build_chain_of_custody_schema,
    build_material_evidence_registry,
    build_qos_gate,
    build_scm_rehearsal,
    complete_cost_gate,
    exact_enumeration_with_cap,
    grammar_check_openqasm3,
    validate_ai_candidate,
    zenodo_archive_inventory_gate,
)
from uqpu.scalable_qubo import seeded_erdos_renyi_maxcut


ROOT = Path(__file__).resolve().parents[3]
MANIFEST = ROOT / "benchmarks/experiments/cycle003-delta01-er6-provider-neutral-manifest.json"
AI_BASELINE = ROOT / "benchmarks/results/batch039-ai-cost-002-classical-baseline.json"
CYCLE004_PUBLIC = ROOT / "benchmarks/experiments/cycle004-delta01-scm-cal001-public-handoff.json"
CYCLE004_TRUTH = ROOT / "benchmarks/results/cycle004-delta01-scm-cal001-custodian-truth.json"
PERSISTED_QISKIT = ROOT / "benchmarks/results/cycle005-delta01-cycle004-qiskit-ci-parse.json"


def _load(path):
    return json.loads(path.read_text(encoding="utf-8"))


class Cycle005Delta01Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest_raw = MANIFEST.read_bytes()
        cls.manifest = json.loads(cls.manifest_raw)
        cls.ai_raw = AI_BASELINE.read_bytes()
        cls.ai = json.loads(cls.ai_raw)

    def test_exact_enumeration_fails_closed_at_state_cap(self):
        instance = seeded_erdos_renyi_maxcut(6, 0.5, 42)
        row = exact_enumeration_with_cap(instance, max_states=7, deadline_seconds=10)
        self.assertEqual(row["stop_reason"], "STATE_CAP")
        self.assertEqual(row["states_evaluated"], 7)
        self.assertFalse(row["complete"])
        self.assertFalse(row["optimum_claim_allowed"])

    def test_scale_case_records_exact_heuristic_gap_and_peak_rss_boundary(self):
        row = benchmark_scale_case(6, 42, deadline_seconds=10)
        self.assertTrue(row["exact"]["complete"])
        self.assertEqual(row["exact"]["states_evaluated"], 64)
        self.assertGreaterEqual(row["heuristic"]["objective_gap_to_exact"], 0)
        self.assertGreater(row["process_peak_rss"]["value"], 0)
        self.assertIn("high-water", row["process_peak_rss"]["semantics"])

    def test_durable_io_labels_fsync_and_does_not_claim_cache_state(self):
        row = benchmark_durable_io({"payload": [1, 2, 3]}, repetitions=3)
        self.assertTrue(row["durability_boundary"]["file_data_fsync_called"])
        self.assertFalse(row["durability_boundary"]["power_loss_survival_tested"])
        self.assertEqual(row["cache_labels"]["first_read"], "NOT_VERIFIED_OS_COLD")
        self.assertEqual(row["cache_labels"]["repeat_read"], "NOT_VERIFIED_CACHE_HIT")
        self.assertIn("write_fsync", row["python_allocation_incremental_peak_bytes"])

    def test_braket_dry_run_is_incomplete_and_has_no_submit_surface(self):
        row = build_braket_dry_run_packet(self.manifest)
        self.assertEqual(
            row["validation"]["missing_required_fields"],
            ["clientToken", "deviceArn", "outputS3Bucket", "outputS3KeyPrefix"],
        )
        self.assertFalse(row["validation"]["submission_allowed"])
        self.assertFalse(row["authorization"]["credentials_used"])
        self.assertIsNone(row["provider_observations"]["bill"])

    def test_cost_gate_refuses_partial_ledger_and_computes_only_complete_fixture(self):
        partial = {name: None for name in (
            "provider_actual_bill", "classical_host_orchestration", "queue",
            "network_transfer", "storage", "retry_failure", "mitigation_decoder",
            "energy_cooling", "labor", "capital_amortization",
        )}
        partial["observed_accepted_outputs"] = None
        refused = complete_cost_gate(partial)
        self.assertTrue(refused["refusal_active"])
        self.assertIsNone(refused["total_cost_usd"])
        fixture = {name: 1.0 for name in refused["required_cost_components"]}
        fixture.update({
            "observed_accepted_outputs": 5,
            "same_provider_execution_and_bill": True,
            "matched_classical_baseline": True,
        })
        complete = complete_cost_gate(fixture)
        self.assertFalse(complete["refusal_active"])
        self.assertEqual(complete["total_cost_usd"], 10.0)
        self.assertEqual(complete["cost_per_accepted_output_usd"], 2.0)

    def test_material_custody_and_capital_schemas_fail_closed(self):
        registry = build_material_evidence_registry()
        self.assertEqual(registry["required_count"], 9)
        self.assertEqual(registry["satisfied_count"], 0)
        self.assertEqual(len({row["prerequisite_id"] for row in registry["slots"]}), 9)
        custody = build_chain_of_custody_schema()
        self.assertFalse(custody["ready"])
        self.assertIsNone(custody["calibration"]["valid_at_measurement"])
        capital = build_capital_dependency_graph()
        self.assertFalse(capital["funding_or_purchase_authorized"])
        self.assertTrue(all(row["capital_at_risk_thb"] is None for row in capital["gates"]))

    def test_zenodo_inventory_preserves_download_license_and_analysis_boundaries(self):
        row = zenodo_archive_inventory_gate()
        self.assertEqual(row["archive"]["response_content_length_bytes"], 145469232)
        self.assertFalse(row["archive"]["downloaded"])
        self.assertIsNone(row["archive"]["locally_recomputed_md5"])
        self.assertIsNone(row["provenance_gates"]["license"])
        self.assertFalse(row["service_contract_mapping"]["project_reproduction"])

    def test_scm_rehearsal_has_separate_hash_linked_logs_but_no_independent_actor_claim(self):
        public = _load(CYCLE004_PUBLIC)
        truth = _load(CYCLE004_TRUTH)
        row = build_scm_rehearsal(
            public,
            truth,
            public_file_sha256=hashlib.sha256(CYCLE004_PUBLIC.read_bytes()).hexdigest(),
            custodian_file_sha256=hashlib.sha256(CYCLE004_TRUTH.read_bytes()).hexdigest(),
        )
        self.assertTrue(row["pre_registered_reveal_rule"]["rule_satisfied_in_rehearsal"])
        self.assertEqual(len(row["access_logs"]["scorer"]), 3)
        self.assertEqual(len(row["access_logs"]["custodian"]), 2)
        self.assertFalse(row["separate_operating_system_principals"])
        self.assertFalse(row["independent_site"])

    def test_ai_candidate_schema_rejects_mismatch_and_accepts_quality_fixture(self):
        gate = build_ai_candidate_gate(self.ai, hashlib.sha256(self.ai_raw).hexdigest())
        self.assertIn("dataset_or_generator_sha256_mismatch", validate_ai_candidate(gate, {}))
        result = dict(gate["required_inputs"])
        result.update({
            "held_out_accuracy": 0.99,
            "held_out_binary_cross_entropy": 0.18,
            "end_to_end_cost_usd": None,
            "end_to_end_energy_joules": None,
        })
        self.assertEqual(validate_ai_candidate(gate, result), [])
        self.assertTrue(gate["publication_policy"]["slower_or_more_expensive_candidate_publishable"])

    def test_limited_grammar_check_rejects_unknown_statement(self):
        qasm = self.manifest["lane_a_b_c_qos"]["paired_circuits"][0]["openqasm_3"]
        good = grammar_check_openqasm3(qasm)
        self.assertTrue(good["passed"])
        self.assertEqual(good["counts"]["cx"], 18)
        bad = grammar_check_openqasm3(qasm + "reset q[0];\n")
        self.assertFalse(bad["passed"])
        self.assertEqual(bad["errors"], ["unsupported_statement"])

    def test_persisted_qiskit_output_and_second_grammar_check_cross_validate(self):
        row = build_qos_gate(
            self.manifest,
            _load(PERSISTED_QISKIT),
            hashlib.sha256(self.manifest_raw).hexdigest(),
        )
        self.assertTrue(row["all_checks_passed"], row["errors"])
        self.assertEqual(row["persisted_ci_parse"]["qiskit_version"], "2.5.2")
        self.assertIsNone(row["provider_transpile"]["physical_depth"])
        self.assertFalse(row["hardware_executed"])


if __name__ == "__main__":
    unittest.main()
