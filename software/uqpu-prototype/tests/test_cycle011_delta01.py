import copy
import hashlib
import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT / "software" / "uqpu-prototype") not in sys.path:
    sys.path.insert(0, str(ROOT / "software" / "uqpu-prototype"))

from uqpu.cycle011_delta01 import (
    atomic_publish, canonical_bytes, canonical_sha256, migrate_er6_certificate,
    migrate_request_v2_to_current, propagate_component_covariance,
    rank_four_gate_priority, run_weighted_maxcut, sha256_bytes,
    validate_ai_source_migration, validate_consent_revocation,
    validate_material_custody, validate_multimeasurand_budget,
    validate_sourced_interval, validate_zip64_directory,
)

FIXTURE = json.loads((ROOT / "benchmarks/experiments/cycle011-delta01-preregistered-gates.json").read_text())


def request_v2():
    spec = FIXTURE["lanes"]["B"]
    request = copy.deepcopy(spec["request"])
    return {"schema_version": 2, "idempotency_token": spec["idempotency_token"],
            "source_commit": spec["source_commit"], "request": request,
            "payload_sha256": canonical_sha256(request)}


def build_ai_manifests():
    spec = FIXTURE["lanes"]["AI-COST"]
    required = spec["required_metrics"]
    records1, records2 = {}, {}
    for split, ids in spec["splits"].items():
        records1[split] = [{"id": row_id, "source_version": 1, "input": f"synthetic-{row_id}"} for row_id in ids]
        records2[split] = [{"id": row_id, "source_version": 2, "input": f"synthetic-{row_id}"} for row_id in ids]
    def make(version, records):
        payloads = {split: canonical_bytes(rows) for split, rows in records.items()}
        manifest = {"schema_version": version, "required_metrics": required, "splits": {}}
        for split, rows in records.items():
            manifest["splits"][split] = {"record_ids": [row["id"] for row in rows],
                "source_sha256": sha256_bytes(payloads[split]), "source_bytes_length": len(payloads[split]),
                "metrics": {name: {"complete": True, "value": 0.5} for name in required}}
        return manifest, payloads
    old, old_bytes = make(1, records1)
    new, new_bytes = make(2, records2)
    new["lineage_from"] = canonical_sha256(old)
    return old, new, old_bytes, new_bytes


class Cycle011AllLaneTests(unittest.TestCase):
    def test_lane_a_fourth_weighted_graph_is_exact_capped_and_deterministic(self):
        spec = FIXTURE["lanes"]["A"]
        first = run_weighted_maxcut(spec["weighted_seed"], spec["state_cap"], spec["restart_budgets"])
        second = run_weighted_maxcut(spec["weighted_seed"], spec["state_cap"], spec["restart_budgets"])
        self.assertTrue(first["complete"])
        self.assertEqual(first["states_evaluated"], 256)
        self.assertEqual(first["graph_sha256"], second["graph_sha256"])
        self.assertTrue(all(1 <= edge[2] <= 5 for edge in first["graph"]["edges"]))
        self.assertEqual([row["restarts"] for row in first["results"]], [1, 4, 16, 64])
        self.assertEqual([row["restart_prefix_sha256"] for row in first["results"]], [row["restart_prefix_sha256"] for row in second["results"]])
        self.assertFalse(run_weighted_maxcut(spec["weighted_seed"], 128)["complete"])

    def test_lane_b_v2_migration_rejects_unknown_and_rebound_token(self):
        migrated = migrate_request_v2_to_current(request_v2())
        self.assertEqual(migrated, migrate_request_v2_to_current(request_v2()))
        self.assertEqual(migrated["schema_version"], 3)
        unknown = request_v2(); unknown["surprise"] = True
        with self.assertRaisesRegex(ValueError, "fields_not_exact"):
            migrate_request_v2_to_current(unknown)
        token_changed = copy.deepcopy(migrated); token_changed["idempotency_token"] += "-tamper"
        with self.assertRaisesRegex(ValueError, "token_binding_mismatch"):
            migrate_request_v2_to_current(token_changed)
        request_changed = request_v2(); request_changed["request"]["shots"] += 1
        with self.assertRaisesRegex(ValueError, "payload_binding_mismatch"):
            migrate_request_v2_to_current(request_changed)

    def test_lane_c_atomic_publication_cleans_temp_and_preserves_old_or_new(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "artifact.bin"
            target.write_bytes(b"old")
            published = atomic_publish(target, b"new")
            self.assertTrue(published["published"])
            self.assertTrue(published["integrity_preserved"])
            self.assertEqual(published["temp_files_remaining"], 0)
            self.assertEqual(published["final_sha256"], hashlib.sha256(b"new").hexdigest())
            failed = atomic_publish(target, b"staged", fail_after_stage=True)
            self.assertFalse(failed["published"])
            self.assertTrue(failed["integrity_preserved"])
            self.assertEqual(failed["final_sha256"], hashlib.sha256(b"new").hexdigest())
            self.assertEqual(failed["temp_files_remaining"], 0)
            self.assertEqual(failed["cache_state"], "UNCONTROLLED")

    def test_lane_d_zip64_multi_entry_order_overlap_truncation_and_locator(self):
        base = FIXTURE["lanes"]["D"]
        self.assertTrue(validate_zip64_directory(base)["valid"])
        bad = copy.deepcopy(base); bad["entries"][1]["offset"] = 1320
        self.assertFalse(validate_zip64_directory(bad)["valid"])
        bad = copy.deepcopy(base); bad["entries"][1]["offset"] = 1250
        self.assertIn("central_directory_overlap:1", validate_zip64_directory(bad)["errors"])
        bad = copy.deepcopy(base); bad["entries"][2]["record_size"] = 100
        self.assertIn("central_directory_record_truncated:2", validate_zip64_directory(bad)["errors"])
        bad = copy.deepcopy(base); bad["zip64_locator_offset"] = 2000
        self.assertIn("zip64_locator_record_boundary_invalid", validate_zip64_directory(bad)["errors"])

    def test_lane_e_custody_chain_rejects_disconnection_and_superseded_method(self):
        spec = FIXTURE["lanes"]["E"]
        record = copy.deepcopy(spec["record"])
        self.assertTrue(validate_material_custody(record, expected_method_version=spec["expected_method_version"], as_of=date.fromisoformat(spec["as_of"]))["valid"])
        bad = copy.deepcopy(record); bad["custody_chain"][1]["from_id"] = "unknown-transfer"
        self.assertIn("custody_chain_link_disconnected:1", validate_material_custody(bad, expected_method_version=spec["expected_method_version"], as_of=date(2026, 9, 28))["errors"])
        bad = copy.deepcopy(record); bad["method_version"] = "SUPERSEDED-V1"
        self.assertIn("custody_method_version_superseded", validate_material_custody(bad, expected_method_version=spec["expected_method_version"], as_of=date(2026, 9, 28))["errors"])
        bad = copy.deepcopy(record); bad["uncertainty_unit"] = "K"
        self.assertIn("custody_uncertainty_unit_mismatch", validate_material_custody(bad, expected_method_version=spec["expected_method_version"], as_of=date(2026, 9, 28))["errors"])

    def test_lane_f_covariance_matrix_partial_non_psd_units_and_zero_outputs_fail_closed(self):
        spec = FIXTURE["lanes"]["F"]
        result = propagate_component_covariance(spec)
        self.assertTrue(result["complete"])
        self.assertEqual(result["total_interval"], ["1.30", "2.20"])
        self.assertIsNotNone(result["expanded_uncertainty"])
        bad = copy.deepcopy(spec); bad["correlation_matrix"][0][1] = None
        self.assertIsNone(propagate_component_covariance(bad)["expanded_uncertainty"])
        bad = copy.deepcopy(spec); bad["correlation_matrix"] = [[1, 1.2, 0], [1.2, 1, 0], [0, 0, 1]]
        self.assertIn("covariance_matrix_not_psd", propagate_component_covariance(bad)["uncertainty_errors"])
        bad = copy.deepcopy(spec); bad["components"][0]["unit"] = "EUR"
        self.assertFalse(propagate_component_covariance(bad)["complete"])
        bad = copy.deepcopy(spec); bad["accepted_outputs"] = 0
        self.assertIsNone(propagate_component_covariance(bad)["total_interval"])
        bad = copy.deepcopy(spec); bad["currency"] = "EUR"
        self.assertIn("cost_currency_unit_mismatch", propagate_component_covariance(bad)["errors"])

    def test_lane_g_multimeasurand_budget_checks_scope_dimension_expiry_and_psd(self):
        spec = FIXTURE["lanes"]["G"]
        budget = copy.deepcopy(spec["budget"])
        self.assertTrue(validate_multimeasurand_budget(budget, date.fromisoformat(spec["as_of"]))["valid"])
        bad = copy.deepcopy(budget); bad["components"][0]["unit"] = "s"
        self.assertFalse(validate_multimeasurand_budget(bad, date(2026, 9, 28))["valid"])
        bad = copy.deepcopy(budget); bad["expected_scope"] = "other"
        self.assertIn("budget_scope_mismatch", validate_multimeasurand_budget(bad, date(2026, 9, 28))["errors"])
        bad = copy.deepcopy(budget); bad["expiry"] = "2025-01-01"
        self.assertIn("budget_expired", validate_multimeasurand_budget(bad, date(2026, 9, 28))["errors"])
        bad = copy.deepcopy(budget); bad["correlation_matrix"] = [[1, 1.3], [1.3, 1]]
        self.assertIn("budget_covariance_not_psd", validate_multimeasurand_budget(bad, date(2026, 9, 28))["errors"])

    def test_lane_h_four_gate_grid_reports_held_out_rankings_without_capital(self):
        spec = FIXTURE["lanes"]["H"]
        result = rank_four_gate_priority(spec["gates"], spec["levels"], spec["held_out_scenarios"])
        self.assertEqual(result["scenario_count"], 6561)
        self.assertEqual(len(result["held_out_scenarios"]), 3)
        self.assertFalse(result["capital_authorized"])
        self.assertIsNone(result["capital_amount"])

    def test_lane_fnd_eqn_source_intervals_bind_exact_units_and_primary_docs(self):
        spec = FIXTURE["lanes"]["FND/EQN"]
        source_bytes = {}
        for locator in spec["source_locators"]:
            path = locator.split("#", 1)[0]
            source_bytes[locator] = (ROOT / path).read_bytes()
        for declaration in spec["quantities"]:
            declaration = dict(declaration)
            declaration["source_locator"] = spec["source_locators"][1 if declaration["unit_code"] == "J/count" else 0]
            declaration["source_sha256"] = sha256_bytes(source_bytes[declaration["source_locator"]])
            self.assertTrue(validate_sourced_interval(declaration, source_bytes)["valid"])
            declaration["dimension_vector"] = {"USD": 0}
            self.assertIn("quantity_dimension_balance_invalid", validate_sourced_interval(declaration, source_bytes)["errors"])

    def test_lane_scm_revocation_invalidates_replayed_and_later_transitions(self):
        events = copy.deepcopy(FIXTURE["lanes"]["SCM"]["events"])
        self.assertTrue(validate_consent_revocation(events)["valid"])
        events.append({"action": "transition", "nonce": "fic-011-nonce-a", "domain_sort": "FICTION_CANON"})
        self.assertIn("scm_transition_without_active_consent:6", validate_consent_revocation(events)["errors"])
        replay = copy.deepcopy(FIXTURE["lanes"]["SCM"]["events"])
        replay.append({"action": "grant", "nonce": "fic-011-nonce-a", "domain_sort": "FICTION_CANON"})
        self.assertIn("scm_consent_nonce_replayed:6", validate_consent_revocation(replay)["errors"])
        replay[0]["domain_sort"] = "REAL_MODEL"
        self.assertIn("scm_cross_sort_transition:0", validate_consent_revocation(replay)["errors"])

    def test_lane_ai_cost_migration_binds_second_bytes_and_heldout_metrics(self):
        old, new, old_bytes, new_bytes = build_ai_manifests()
        result = validate_ai_source_migration(old, new, old_bytes, new_bytes)
        self.assertTrue(result["valid"])
        self.assertFalse(result["scoring_performed"])
        drifted = dict(new_bytes); drifted["test"] += b"drift"
        self.assertIn("ai_v2_source_hash_invalid:test", validate_ai_source_migration(old, new, old_bytes, drifted)["errors"])
        bad = copy.deepcopy(new); bad["splits"]["test"]["metrics"]["energy_complete"]["complete"] = False
        self.assertIn("ai_v2_heldout_metrics_incomplete:test", validate_ai_source_migration(old, bad, old_bytes, new_bytes)["errors"])
        bad = copy.deepcopy(new); bad["lineage_from"] = "0" * 64
        self.assertIn("ai_lineage_parent_hash_mismatch", validate_ai_source_migration(old, bad, old_bytes, new_bytes)["errors"])

    def test_lane_qos_qsvt_second_er6_source_migrates_append_only_certificate(self):
        spec = FIXTURE["lanes"]["QOS/QSVT"]
        source1 = copy.deepcopy(spec["source_v1"])
        source2 = {"grammar": "ER6_CYCLE011_FROZEN_SUBSET", "source_id": spec["source_v2_id"],
                   "qubit_count": 7, "bit_count": 7,
                   "measurement_destinations": source1["measurement_destinations"] + [{"qubit": "q[6]", "bit": "c[6]"}],
                   "candidate_resources": spec["candidate_resources"]}
        certificate = {"source_sha256": canonical_sha256(source1), "resources": spec["previous_resources"]}
        result = migrate_er6_certificate(source1, source2, certificate, spec["resource_bounds"])
        self.assertTrue(result["valid"])
        self.assertEqual(result["candidate"]["registers"]["qubit_count"], 7)
        bad = copy.deepcopy(source2); bad["measurement_destinations"][-1] = {"qubit": "q[0]", "bit": "c[6]"}
        self.assertIn("er6_migration_measurement_map_not_append_only", migrate_er6_certificate(source1, bad, certificate, spec["resource_bounds"])["errors"])
        bad_cert = dict(certificate); bad_cert["source_sha256"] = "0" * 64
        self.assertIn("er6_previous_certificate_source_mismatch", migrate_er6_certificate(source1, source2, bad_cert, spec["resource_bounds"])["errors"])
        bad = copy.deepcopy(source2); bad["candidate_resources"]["depth"] = -1
        self.assertIn("er6_migrated_resource_invalid:depth", migrate_er6_certificate(source1, bad, certificate, spec["resource_bounds"])["errors"])


if __name__ == "__main__":
    unittest.main()
