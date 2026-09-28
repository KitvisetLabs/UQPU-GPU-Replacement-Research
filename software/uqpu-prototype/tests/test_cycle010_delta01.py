from __future__ import annotations

from copy import deepcopy
from datetime import date
import json
from pathlib import Path
import unittest

from uqpu.cycle010_delta01 import (
    ZIP64_SENTINEL,
    atomic_write_local,
    build_ai_source_manifest,
    canonical_sha256,
    derive_dimension_vector,
    generate_maxcut_instance,
    migrate_request_envelope,
    parse_json_reject_duplicates,
    propagate_cost_interval,
    rank_assumed_gate_grid,
    run_local_atomic_write_protocol,
    run_maxcut_restart_sweep,
    sha256_bytes,
    simulate_interrupted_atomic_write,
    validate_correlation_matrix,
    validate_er6_register_certificate,
    validate_fictional_state_graph,
    validate_http_range_response,
    validate_material_provenance,
    validate_request_replay,
    validate_sourced_quantity,
    validate_uncertainty_budget,
    validate_ai_source_manifest,
    validate_zip64_metadata,
)


ROOT = Path(__file__).resolve().parents[3]
FIXTURE = json.loads((ROOT / "benchmarks/experiments/cycle010-delta01-preregistered-gates.json").read_text())


class Cycle010Delta01Tests(unittest.TestCase):
    def test_lane_a_three_preregistered_instances_keep_restart_prefix(self):
        lane = FIXTURE["lanes"]["A"]
        result = run_maxcut_restart_sweep(lane["instances"], lane["restart_budgets"], lane["exact_state_cap"])
        self.assertEqual(len(result["instances"]), 3)
        self.assertTrue(all(row["instance_sha256"] for row in result["instances"]))
        for instance in result["instances"]:
            rows = instance["results"]
            self.assertEqual([row["restarts"] for row in rows], [1, 4, 16, 64])
            self.assertTrue(all(row["exact_complete"] and row["exact_states_evaluated"] == 256 for row in rows))
            self.assertTrue(all(row["host_elapsed_ns"] >= 0 for row in rows))
            self.assertEqual(rows[1]["restart_start_sha256"][:1], rows[0]["restart_start_sha256"])
            self.assertEqual(rows[2]["restart_start_sha256"][:4], rows[1]["restart_start_sha256"])
            self.assertEqual(rows[3]["restart_start_sha256"][:16], rows[2]["restart_start_sha256"])
            self.assertEqual(rows[1]["restart_objectives"][:1], rows[0]["restart_objectives"])
            self.assertEqual(rows[2]["restart_objectives"][:4], rows[1]["restart_objectives"])
            self.assertEqual(rows[3]["restart_objectives"][:16], rows[2]["restart_objectives"])
            self.assertTrue(all(row["gap_to_exact"] >= 0 for row in rows))

    def test_lane_b_duplicate_keys_reject_and_supported_versions_migrate(self):
        lane = FIXTURE["lanes"]["B"]
        with self.assertRaisesRegex(ValueError, "duplicate_json_key"):
            parse_json_reject_duplicates('{"schema_version":1,"schema_version":2}')
        v1 = lane["schema_v1"]
        migrated = migrate_request_envelope(v1)
        self.assertEqual(migrated["schema_version"], 2)
        self.assertEqual(migrated["payload_sha256"], canonical_sha256(v1["request"]))
        reordered = {"request": v1["request"], "source_commit": v1["source_commit"], "idempotency_token": v1["idempotency_token"], "schema_version": 1}
        self.assertEqual(migrate_request_envelope(reordered), migrated)
        self.assertTrue(validate_request_replay(v1, reordered)["valid"])
        changed = deepcopy(v1)
        changed["request"]["shots"] += 1
        self.assertIn("request_payload_changed", validate_request_replay(v1, changed)["errors"])
        unsupported = dict(v1, schema_version=99)
        self.assertIn("unsupported_envelope_schema_version", migrate_request_envelope_error(unsupported))

    def test_lane_c_named_process_scopes_and_interruption_rows_are_labeled(self):
        result = run_local_atomic_write_protocol()
        self.assertTrue(result["all_hashes_match"])
        self.assertTrue(result["all_interrupted_payloads_preserved"])
        self.assertEqual([row["process_scope"] for row in result["rows"]], ["same_process_repeated", "fresh_child_process"])
        self.assertEqual(result["cache_state"], "UNCONTROLLED")
        for scope in result["rows"]:
            for row in scope["rows"]:
                self.assertEqual(row["expected_sha256"], row["readback_sha256"])
                self.assertIsInstance(row["file_fsync"], bool)
                self.assertIsInstance(row["directory_fsync"], bool)

    def test_lane_d_zip64_bounds_and_valid_unsatisfied_range_response(self):
        lane = FIXTURE["lanes"]["D"]
        valid = lane["zip64"]
        self.assertTrue(validate_zip64_metadata(valid)["valid"])
        unsatisfied = lane["valid_unsatisfied_range"]
        self.assertTrue(validate_http_range_response(**unsatisfied)["valid"])
        bad = deepcopy(valid)
        bad["entries"][0]["zip64_extra"]["local_header_offset"] = bad["central_directory_start"] + 1
        self.assertFalse(validate_zip64_metadata(bad)["valid"])
        bad = deepcopy(valid)
        bad["entries"][0]["zip64_extra"]["compressed_size"] = 1 << 64
        self.assertFalse(validate_zip64_metadata(bad)["valid"])
        bad = deepcopy(valid)
        bad["zip64_locator_offset"] += 1
        self.assertFalse(validate_zip64_metadata(bad)["valid"])
        invalid_416 = dict(unsatisfied, content_range="bytes */127")
        self.assertFalse(validate_http_range_response(**invalid_416)["valid"])
        bad_206 = validate_http_range_response(206, "bytes 0-7/128", 128, 7, start=0, end=7)
        self.assertFalse(bad_206["valid"])

    def test_lane_e_material_provenance_mutations_fail_closed(self):
        lane = FIXTURE["lanes"]["E"]
        valid = validate_material_provenance(lane["record"], date.fromisoformat(lane["as_of"]))
        self.assertTrue(valid["valid"])
        mutations = []
        row = dict(lane["record"], control_id=lane["record"]["sample_id"]); mutations.append(row)
        row = dict(lane["record"], calibration_issuer=""); mutations.append(row)
        row = dict(lane["record"], calibration_scope=["density"]); mutations.append(row)
        row = dict(lane["record"], calibration_expiry="2020-01-01"); mutations.append(row)
        row = dict(lane["record"], uncertainty_unit="mS/m"); mutations.append(row)
        for row in mutations:
            self.assertFalse(validate_material_provenance(row, date.fromisoformat(lane["as_of"]))["valid"])

    def test_lane_f_correlated_cost_interval_separates_cost_from_uncertainty(self):
        lane = FIXTURE["lanes"]["F"]
        independent = propagate_cost_interval(dict(lane, correlation_matrix=lane["independent_correlation_matrix"]))
        correlated = propagate_cost_interval(dict(lane, correlation_matrix=lane["correlated_correlation_matrix"]))
        invalid = propagate_cost_interval(dict(lane, correlation_matrix=lane["non_psd_correlation_matrix"]))
        missing = dict(lane); missing.pop("independent_correlation_matrix", None); missing.pop("correlation_matrix", None)
        missing_result = propagate_cost_interval(missing)
        zero = propagate_cost_interval(dict(lane, accepted_outputs=0, correlation_matrix=lane["independent_correlation_matrix"]))
        incomplete = propagate_cost_interval(dict(lane, required_components=["compute", "data", "missing"], correlation_matrix=lane["independent_correlation_matrix"]))
        unit_mismatch = propagate_cost_interval(dict(lane, uncertainty_unit="J", correlation_matrix=lane["independent_correlation_matrix"]))
        self.assertEqual(independent["total_interval"], ["1.00", "1.50"])
        self.assertIsNotNone(independent["uncertainty"])
        self.assertGreater(float(correlated["uncertainty"]), float(independent["uncertainty"]))
        self.assertIsNone(invalid["uncertainty"])
        self.assertEqual(invalid["total_interval"], independent["total_interval"])
        self.assertIsNone(missing_result["uncertainty"])
        self.assertIsNone(zero["total_interval"])
        self.assertIsNone(incomplete["total_interval"])
        self.assertIsNone(unit_mismatch["total_interval"])
        self.assertEqual(validate_correlation_matrix([[1, 1.2], [1.2, 1]])["valid"], False)

    def test_lane_g_uncertainty_budget_checks_scope_units_expiry_and_psd(self):
        lane = FIXTURE["lanes"]["G"]
        budget = lane["budget"]
        as_of = date.fromisoformat(lane["as_of"])
        self.assertTrue(validate_uncertainty_budget(budget, as_of)["valid"])
        for mutation in (
            dict(budget, components=budget["components"][:1]),
            dict(budget, scope="wrong-scope"),
            dict(budget, expected_unit="kg"),
            dict(budget, certificate_expiry="2020-01-01"),
            dict(budget, correlation_matrix=[[1, 1.5], [1.5, 1]]),
        ):
            self.assertFalse(validate_uncertainty_budget(mutation, as_of)["valid"])

    def test_lane_h_larger_assumed_grid_records_sensitivity_and_no_capital(self):
        lane = FIXTURE["lanes"]["H"]
        result = rank_assumed_gate_grid(lane["gates"], lane["multipliers"])
        self.assertEqual(result["scenario_count"], 729)
        self.assertGreater(result["reversal_scenario_count"], 0)
        self.assertGreater(result["distinct_order_count"], 1)
        self.assertTrue(any(value < 1.0 for value in result["pairwise_rank_stability"].values()))
        self.assertFalse(result["capital_authorized"])
        self.assertIsNone(result["capital_amount"])

    def test_lane_fnd_eqn_source_linked_cost_and_energy_units_are_exact(self):
        lane = FIXTURE["lanes"]["FND/EQN"]
        registry = json.loads((ROOT / lane["unit_registry"]).read_text())
        basis = registry["dimension_basis"]
        registry["unit_registry"]["USD/count"] = {"dimension_vector": derive_dimension_vector(registry, ["USD"], ["count"])}
        registry["unit_registry"]["J/count"] = {"dimension_vector": derive_dimension_vector(registry, ["W", "s"], ["count"])}
        for item in lane["quantities"]:
            vector = derive_dimension_vector(registry, item["numerator_units"], item["denominator_units"])
            declaration = {"quantity_id": item["quantity_id"], "quantity_kind": item["quantity_kind"], "unit_code": item["unit_code"], "dimension_vector": vector, "domain_sort": "REAL_MODEL", "source_locator": lane["primary_sources"][item["source_index"]], "source_sha256": sha256_bytes((ROOT / lane["primary_sources"][item["source_index"]].split("#")[0]).read_bytes())}
            self.assertTrue(validate_sourced_quantity(declaration, registry)["valid"])
            bad = dict(declaration, dimension_vector={key: "0" for key in basis})
            self.assertFalse(validate_sourced_quantity(bad, registry)["valid"])
            self.assertTrue((ROOT / declaration["source_locator"].split("#")[0]).exists())

    def test_lane_scm_versioned_graph_requires_all_volume_links_consent_and_firewall(self):
        graph = FIXTURE["lanes"]["SCM"]["graph"]
        self.assertTrue(validate_fictional_state_graph(graph, used_nonces=set())["valid"])
        mutations = []
        row = deepcopy(graph); row["volume_equation_links"].pop("V5"); mutations.append(row)
        row = deepcopy(graph); row["edges"][0]["to_state"] = "unknown"; mutations.append(row)
        row = deepcopy(graph); row["edges"][0]["consent_required"] = False; mutations.append(row)
        row = deepcopy(graph); row["edges"][0]["domain_sort"] = "REAL_MODEL"; mutations.append(row)
        row = deepcopy(graph); row["empirical_coupling"] = 0.1; mutations.append(row)
        for row in mutations:
            self.assertFalse(validate_fictional_state_graph(row, used_nonces=set())["valid"])
        self.assertFalse(validate_fictional_state_graph(graph, used_nonces={"fic-010-nonce-a"})["valid"])

    def test_lane_ai_cost_manifest_binds_raw_synthetic_bytes_before_scoring(self):
        lane = FIXTURE["lanes"]["AI-COST"]
        manifest, source_bytes = build_ai_source_manifest(lane["source_records"], lane["record_ids"], lane["required_metrics"])
        self.assertTrue(validate_ai_source_manifest(manifest, source_bytes)["valid"])
        altered = dict(source_bytes, train=source_bytes["train"] + b"x")
        self.assertFalse(validate_ai_source_manifest(manifest, altered)["valid"])
        overlap = deepcopy(manifest); overlap["splits"]["test"]["record_ids"] = [overlap["splits"]["train"]["record_ids"][0]]
        self.assertFalse(validate_ai_source_manifest(overlap, source_bytes)["valid"])
        missing = deepcopy(manifest); missing["splits"]["validation"]["metrics"].pop("energy_complete")
        self.assertFalse(validate_ai_source_manifest(missing, source_bytes)["valid"])
        unsupported = dict(manifest, schema_version=2)
        self.assertFalse(validate_ai_source_manifest(unsupported, source_bytes)["valid"])

    def test_lane_qos_er6_certificate_checks_source_register_measurement_and_bounds(self):
        lane = FIXTURE["lanes"]["QOS/QSVT"]
        source = lane["source"]
        candidate = {
            "source_sha256": canonical_sha256(source),
            "registers": {"qubit_count": source["qubit_count"], "bit_count": source["bit_count"]},
            "measurement_destinations": source["measurement_destinations"],
            "resources": lane["candidate_resources"],
        }
        self.assertTrue(validate_er6_register_certificate(source, candidate, lane["resource_bounds"])["valid"])
        mutations = []
        row = deepcopy(candidate); row["source_sha256"] = "0" * 64; mutations.append(row)
        row = deepcopy(candidate); row["registers"]["qubit_count"] += 1; mutations.append(row)
        row = deepcopy(candidate); row["measurement_destinations"][0]["bit"] = "c[1]"; mutations.append(row)
        row = deepcopy(candidate); row["resources"]["depth"] = lane["resource_bounds"]["depth"] + 1; mutations.append(row)
        for row in mutations:
            self.assertFalse(validate_er6_register_certificate(source, row, lane["resource_bounds"])["valid"])


def migrate_request_envelope_error(envelope):
    try:
        migrate_request_envelope(envelope)
    except ValueError as exc:
        return [str(exc)]
    return []


if __name__ == "__main__":
    unittest.main()
