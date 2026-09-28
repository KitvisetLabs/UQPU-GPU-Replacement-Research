from copy import deepcopy
from datetime import date
import unittest
import json
from pathlib import Path

from uqpu.cycle007_delta01 import validate_content_range
from uqpu.cycle009_delta01 import (
    build_three_way_ai_manifest,
    build_versioned_request_receipt,
    compare_preregistered_restart_budgets,
    compute_cost_interval_with_uncertainty,
    rank_evidence_gate_sensitivity_grid,
    simulate_interrupted_atomic_publication,
    validate_er6_semantic_certificate,
    validate_fictional_state_transition,
    validate_io_process_record,
    validate_offline_zip_metadata,
    validate_synthetic_material_provenance,
    validate_synthetic_uncertainty_budget,
    validate_three_way_ai_manifest,
    validate_typed_quantity_declaration,
    validate_versioned_request_envelope,
    validate_versioned_request_replay,
    canonical_json_sha256,
    LANES,
    measure_local_io_scope_screen,
)


class Cycle009Delta01Tests(unittest.TestCase):
    def test_preregistered_fixture_catalog_is_versioned_and_covers_every_lane(self):
        root = Path(__file__).resolve().parents[3]
        fixture = json.loads((root / "benchmarks/experiments/cycle009-delta01-preregistered-gates.json").read_text())
        self.assertEqual(fixture["schema"], "uqpu-cycle009-delta01-preregistered-gates-v1")
        self.assertEqual(set(fixture["lanes"]), set(LANES))
        self.assertEqual(fixture["base_closeout_commit"], "47c3efd2d7f369ce4797bace321302ef139a6e84")
        locator = fixture["lanes"]["FND/EQN"]["declaration"]["source_locator"].split("#", 1)[0]
        source_doc = root / locator
        self.assertTrue(source_doc.is_file())
        self.assertIn("T_{\\mathrm{acc}}", source_doc.read_text())
        lane_b = fixture["lanes"]["B"]
        self.assertEqual(lane_b["request"]["payload_sha256"], canonical_json_sha256(lane_b["request"]["payload"]))
        lane_f = fixture["lanes"]["F"]
        self.assertEqual(lane_f["accepted_output_contract_sha256"], canonical_json_sha256(lane_f["accepted_output_contract"]))
        lane_ai = fixture["lanes"]["AI-COST"]
        self.assertEqual(lane_ai["source_hashes"], {key: canonical_json_sha256(value) for key, value in lane_ai["source_payloads"].items()})
        lane_qos = fixture["lanes"]["QOS/QSVT"]
        self.assertEqual(lane_qos["candidate"]["source_sha256"], canonical_json_sha256(lane_qos["source"]))
        lane_a = fixture["lanes"]["A"]
        replay = compare_preregistered_restart_budgets(
            seed=lane_a["seed"], node_count=lane_a["node_count"],
            edge_probability=lane_a["edge_probability"],
            budgets=tuple(lane_a["restart_budgets"]), state_cap=lane_a["exact_state_cap"])
        self.assertEqual(replay["exact_control"]["best_objective"], lane_a["expected_exact_objective"])
        self.assertEqual([row["objective"] for row in replay["budget_results"]], lane_a["expected_objectives_by_budget"])

    def test_lane_a_preregistered_budgets_include_a_falsifying_gap(self):
        result = compare_preregistered_restart_budgets()
        self.assertEqual(result["exact_control"]["states_evaluated"], 256)
        self.assertEqual(result["exact_control"]["best_objective"], 9)
        self.assertEqual([row["objective"] for row in result["budget_results"]], [8, 9, 9])
        self.assertEqual([row["gap_to_exact"] for row in result["budget_results"]], [1, 0, 0])
        self.assertTrue(result["falsification_fixture"])

    def test_lane_b_canonical_order_is_stable_and_payload_mutation_fails(self):
        payload = {"sample": "synthetic", "value": 1}
        request = {"client_token": "cycle009-fixture", "operation": "sample",
                   "payload": payload, "payload_sha256": canonical_json_sha256(payload),
                   "tags": {"b": "2", "a": "1"}}
        envelope = build_versioned_request_receipt(request, source_commit="47c3efd2d7f369c")
        self.assertTrue(validate_versioned_request_envelope(envelope)["valid"])
        permuted = deepcopy(envelope)
        permuted["request"] = {"tags": {"a": "1", "b": "2"}, "payload_sha256": request["payload_sha256"],
                                "payload": payload, "operation": "sample", "client_token": "cycle009-fixture"}
        self.assertTrue(validate_versioned_request_envelope(permuted)["valid"])
        self.assertTrue(validate_versioned_request_replay(request, permuted["request"])["valid"])
        changed = deepcopy(envelope)
        changed["request"]["payload"]["value"] = 2
        changed["request"]["payload_sha256"] = canonical_json_sha256(changed["request"]["payload"])
        self.assertIn("request_hash_mismatch", validate_versioned_request_envelope(changed)["errors"])
        self.assertIn("same_token_payload_mutated", validate_versioned_request_replay(request, changed["request"])["errors"])
        missing = deepcopy(envelope)
        missing["source_commit"] = ""
        self.assertIn("source_commit_missing", validate_versioned_request_envelope(missing)["errors"])

    def test_lane_c_labels_process_scope_and_injected_interruption_boundaries(self):
        record = {"process_scope": "REPEATED_PROCESS", "cache_state": "UNCONTROLLED",
                  "device_flush_claim": False, "power_loss_claim": False,
                  "readback_sha256": "abc", "expected_sha256": "abc"}
        self.assertEqual(validate_io_process_record(record), [])
        fresh = dict(record, process_scope="FRESH_PROCESS")
        self.assertEqual(validate_io_process_record(fresh), [])
        bad = dict(record, power_loss_claim=True)
        self.assertIn("power_loss_claim_untested", validate_io_process_record(bad))
        probe = measure_local_io_scope_screen({"fixture": "cycle009-io", "payload": "synthetic"})
        self.assertEqual([row["process_scope"] for row in probe["rows"]],
                         ["REPEATED_PROCESS", "REPEATED_PROCESS", "FRESH_PROCESS"])
        self.assertTrue(all(row["sha256_matches"] for row in probe["rows"]))
        self.assertEqual(probe["cache_state"], "UNCONTROLLED")
        self.assertIn("directory_fsync_supported", probe["platform_capabilities"])
        self.assertTrue(simulate_interrupted_atomic_publication(b"old", b"new", interrupt_after="before_write")["old_or_new_payload_preserved"])
        self.assertTrue(simulate_interrupted_atomic_publication(b"old", b"new", interrupt_after="after_staging_fsync")["old_or_new_payload_preserved"])
        replaced = simulate_interrupted_atomic_publication(b"old", b"new", interrupt_after="after_replace")
        self.assertTrue(replaced["replace_completed"] and replaced["old_or_new_payload_preserved"])

    def test_lane_d_offline_range_and_zip_mutations_reject(self):
        self.assertEqual(validate_content_range(status=206, content_range="bytes 0-7/64",
                                                start=0, end=7, total=64, body_length=8), [])
        self.assertIn("http_status_must_be_206", validate_content_range(
            status=200, content_range="bytes 0-7/64", start=0, end=7, total=64, body_length=8))
        self.assertIn("range_body_length_mismatch", validate_content_range(
            status=206, content_range="bytes 0-7/64", start=0, end=7, total=64, body_length=7))
        valid = {"archive_size_bytes": 2000, "declared_archive_size_bytes": 2000,
                 "central_start": 1800, "central_end": 2000,
                 "entries": [{"local_header_offset": 100, "compressed_size_bytes": 50}],
                 "archive_downloaded": False, "payload_read": False}
        self.assertEqual(validate_offline_zip_metadata(valid), [])
        bad_offset = deepcopy(valid); bad_offset["entries"][0]["local_header_offset"] = 1900
        self.assertIn("zip_local_header_offset_invalid:0", validate_offline_zip_metadata(bad_offset))
        truncated = deepcopy(valid); truncated["declared_archive_size_bytes"] = 1999
        self.assertIn("zip_declared_archive_size_mismatch", validate_offline_zip_metadata(truncated))
        truncated["entries"][0].update(local_header_offset=1750, compressed_size_bytes=100)
        self.assertIn("zip_entry_truncated_before_central_directory:0", validate_offline_zip_metadata(truncated))

    def test_lane_e_material_control_calibration_and_units_are_scoped(self):
        valid = {"sample_id": "synthetic-sample", "control_id": "synthetic-control",
                 "measurand": "fixture-length", "unit_code": "m", "method_id": "method-1",
                 "calibration_id": "cal-1", "calibration_scope": "method-1",
                 "valid_until": "2026-10-01", "uncertainty": "1/100", "uncertainty_unit": "m",
                 "evidence_class": "SYNTHETIC", "synthetic": True, "physical_measurement": False}
        self.assertTrue(validate_synthetic_material_provenance(valid, as_of=date(2026, 9, 28))["valid"])
        for field, value, error in (
            ("control_id", "", "field_missing:control_id"),
            ("uncertainty_unit", "cm", "uncertainty_unit_mismatch"),
            ("calibration_scope", "other-method", "calibration_scope_mismatch"),
            ("valid_until", "2026-09-27", "calibration_expired"),
        ):
            mutated = dict(valid, **{field: value})
            self.assertIn(error, validate_synthetic_material_provenance(mutated, as_of=date(2026, 9, 28))["errors"])

    def test_lane_f_zero_outputs_and_incomplete_cost_keep_totals_null(self):
        contract = {"schema": "synthetic-accepted-output-contract-v1", "output": "fixture-result", "fixture_only": True}
        record = {"currency": "USD", "accepted_outputs": 2,
                  "accepted_output_contract": contract,
                  "accepted_output_contract_sha256": canonical_json_sha256(contract),
                  "required_components": ["compute", "storage"],
                  "components": {"compute": {"currency": "USD", "low": "6/5", "high": "8/5", "standard_uncertainty": "1/10"},
                                "storage": {"currency": "USD", "low": "1/2", "high": "7/10", "standard_uncertainty": "1/5"}},
                  "coverage_factor": 2}
        result = compute_cost_interval_with_uncertainty(record)
        self.assertTrue(result["complete"], result["errors"])
        self.assertEqual(result["total_interval"], ["17/10", "23/10"])
        self.assertEqual(result["per_accepted_output_interval"], ["17/20", "23/20"])
        self.assertEqual(result["variance_sum_exact"], "1/20")
        self.assertEqual(result["accepted_output_contract_sha256"], canonical_json_sha256(contract))
        zero = dict(record, accepted_outputs=0)
        self.assertIsNone(compute_cost_interval_with_uncertainty(zero)["total_interval"])
        incomplete = deepcopy(record); del incomplete["components"]["storage"]
        self.assertIsNone(compute_cost_interval_with_uncertainty(incomplete)["per_accepted_output_interval"])
        bad_coverage = dict(record, coverage_factor=-1)
        self.assertIn("coverage_factor_invalid", compute_cost_interval_with_uncertainty(bad_coverage)["errors"])

    def test_lane_g_uncertainty_budget_requires_method_coverage_scope_and_all_components(self):
        budget = {"evidence_class": "SYNTHETIC_UNCERTAINTY_BUDGET", "scope_id": "method-1",
                  "required_scope_id": "method-1", "valid_until": "2026-10-01", "unit_code": "m",
                  "combination_method": "ROOT_SUM_SQUARES_UNCORRELATED", "coverage_factor": "2",
                  "components": [{"component_id": "u1", "unit_code": "m", "standard_uncertainty": "0.3"},
                                 {"component_id": "u2", "unit_code": "m", "standard_uncertainty": "0.4"}],
                  "reported_component_ids": ["u1", "u2"]}
        result = validate_synthetic_uncertainty_budget(budget, as_of=date(2026, 9, 28))
        self.assertTrue(result["valid"], result["errors"])
        self.assertEqual(result["expanded_uncertainty_model_only"], "1.0")
        missing = dict(budget); missing["combination_method"] = None
        self.assertIn("uncertainty_combination_method_missing", validate_synthetic_uncertainty_budget(missing, as_of=date(2026, 9, 28))["errors"])
        unreported = dict(budget, reported_component_ids=["u1"])
        self.assertIn("unreported_uncertainty_component", validate_synthetic_uncertainty_budget(unreported, as_of=date(2026, 9, 28))["errors"])
        expired = dict(budget, valid_until="2026-09-27")
        self.assertIn("uncertainty_budget_expired", validate_synthetic_uncertainty_budget(expired, as_of=date(2026, 9, 28))["errors"])

    def test_lane_h_assumption_grid_records_rank_reversal_without_capital(self):
        gates = [{"gate_id": "BILL_RECEIPT"}, {"gate_id": "MATERIAL_SAMPLE"}]
        scenarios = [
            {"scenario_id": "base", "effort_cost": {"BILL_RECEIPT": 4, "MATERIAL_SAMPLE": 4},
             "blocker_impact": {"BILL_RECEIPT": 8, "MATERIAL_SAMPLE": 4}},
            {"scenario_id": "sample_favorable", "effort_cost": {"BILL_RECEIPT": 8, "MATERIAL_SAMPLE": 1},
             "blocker_impact": {"BILL_RECEIPT": 4, "MATERIAL_SAMPLE": 2}},
        ]
        result = rank_evidence_gate_sensitivity_grid(gates, scenarios)
        self.assertEqual(result["base_ranking"], ["BILL_RECEIPT", "MATERIAL_SAMPLE"])
        self.assertEqual(result["rankings"][1]["ranking"], ["MATERIAL_SAMPLE", "BILL_RECEIPT"])
        self.assertLess(result["pairwise_order_stability"], 1)
        self.assertFalse(result["capital_authorized"])
        self.assertIsNone(result["capital_amount"])

    def test_lane_fnd_eqn_requires_source_linked_explicit_dimension_type(self):
        registry = {"count/s": {"count": "1", "time": "-1"}}
        valid = {"quantity_id": "T_acc", "unit_code": "count/s", "dimension_vector": registry["count/s"],
                 "source_locator": "docs/CYCLE008_TYPED_MATH_AND_SCM_STATE_CONTRACT_2026-09-28.md#1-typed-project-quantities/008-MATH-1",
                 "evidence_type": "FORMAL_MODEL_DECLARATION"}
        self.assertTrue(validate_typed_quantity_declaration(valid, registry)["valid"])
        prose = dict(valid, unit_code=None, dimension_vector=None)
        self.assertIn("unit_unclassified_or_unregistered", validate_typed_quantity_declaration(prose, registry)["errors"])
        mismatch = dict(valid, dimension_vector={"count": "0", "time": "-1"})
        self.assertIn("dimension_vector_does_not_match_registered_unit", validate_typed_quantity_declaration(mismatch, registry)["errors"])

    def test_lane_scm_version_state_volume_links_consent_and_replay_fail_closed(self):
        equations = {"SCM-MATH-020", "SCM-MATH-021", "SCM-MATH-022", "SCM-MATH-023"}
        states = {"chi0", "chi1"}
        record = {"domain_sort": "FICTION_CANON", "from_state": "chi0", "to_state": "chi1",
                  "equation_id": "SCM-MATH-020", "canon_version": "v1", "source_version": "v1",
                  "target_version": "v1", "cross_domain_cast": False, "consent": True,
                  "consent_nonce": "nonce-1",
                  "volume_equation_links": {f"V{i}": "SCM-MATH-022" for i in range(1, 6)}}
        self.assertTrue(validate_fictional_state_transition(record, states=states, equations=equations, used_nonces=set())["valid"])
        for field, value, error in (("to_state", "chi-unknown", "transition_state_unknown"),
                                   ("target_version", "v2", "transition_canon_version_mismatch"),
                                   ("cross_domain_cast", True, "transition_cross_domain_cast_forbidden"),
                                   ("equation_id", "SCM-UNKNOWN", "transition_equation_reference_unknown")):
            changed = dict(record, **{field: value})
            self.assertIn(error, validate_fictional_state_transition(changed, states=states, equations=equations, used_nonces=set())["errors"])
        self.assertIn("transition_consent_nonce_replayed", validate_fictional_state_transition(record, states=states, equations=equations, used_nonces={"nonce-1"})["errors"])

    def test_lane_ai_cost_three_way_splits_hashes_and_metrics_are_checked(self):
        ids = {"train": ["a", "b"], "validation": ["c"], "test": ["d"]}
        payloads = {"dataset": {"version": 1, "examples": ["a", "b", "c", "d"]},
                    "labels": {"version": 1, "labels": {"a": "0", "b": "1", "c": "0", "d": "1"}}}
        hashes = {name: canonical_json_sha256(value) for name, value in payloads.items()}
        manifest = build_three_way_ai_manifest(ids, hashes, ["loss", "quality"])
        for split in ids:
            manifest["metric_values"][split] = {"loss": 0.1, "quality": 0.9}
        self.assertTrue(validate_three_way_ai_manifest(manifest, expected_source_hashes=hashes)["valid"])
        overlap = deepcopy(manifest); overlap["split_ids"]["test"] = ["a"]
        overlap["split_hashes"]["test"] = canonical_json_sha256(["a"])
        self.assertIn("split_overlap:train:test", validate_three_way_ai_manifest(overlap, expected_source_hashes=hashes)["errors"])
        altered = deepcopy(manifest); altered["source_hashes"]["dataset"] = "c" * 64
        self.assertIn("source_hash_map_mismatch", validate_three_way_ai_manifest(altered, expected_source_hashes=hashes)["errors"])
        missing_metric = deepcopy(manifest); missing_metric["metric_values"]["test"]["loss"] = None
        self.assertIn("metrics_incomplete:test", validate_three_way_ai_manifest(missing_metric, expected_source_hashes=hashes)["errors"])

    def test_lane_qos_er6_register_measurement_and_resource_mutations_reject(self):
        source = {"grammar_subset_id": "ER6-FROZEN-V1", "register_map": {"q[0]": "logical-0"},
                  "measurement_destinations": [{"qubit": "q[0]", "bit": "c[0]"}]}
        candidate = {**source, "source_sha256": canonical_json_sha256(source),
                     "resources": {"logical_qubits": 1, "gate_count": 8, "depth": 5}}
        bounds = {"logical_qubits": 2, "gate_count": 10, "depth": 6}
        self.assertTrue(validate_er6_semantic_certificate(source, candidate, bounds)["valid"])
        for field, value, error in (
            ("register_map", {"q[0]": "logical-1"}, "er6_semantics_changed:register_map"),
            ("measurement_destinations", [{"qubit": "q[0]", "bit": "c[1]"}], "er6_semantics_changed:measurement_destinations"),
        ):
            changed = dict(candidate, **{field: value})
            self.assertIn(error, validate_er6_semantic_certificate(source, changed, bounds)["errors"])
        over = deepcopy(candidate); over["resources"]["depth"] = 7
        self.assertIn("er6_resource_bound_exceeded:depth", validate_er6_semantic_certificate(source, over, bounds)["errors"])
        bad_hash = dict(candidate, source_sha256="d" * 64)
        self.assertIn("er6_source_hash_mismatch", validate_er6_semantic_certificate(source, bad_hash, bounds)["errors"])


if __name__ == "__main__":
    unittest.main()
