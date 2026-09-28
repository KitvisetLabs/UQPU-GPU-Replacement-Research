from copy import deepcopy
from datetime import date
import hashlib
import json
from pathlib import Path
import unittest

from uqpu.cycle005_delta01 import (
    benchmark_scale_case,
    build_capital_dependency_graph,
    build_material_evidence_registry,
)
from uqpu.cycle006_delta01 import (
    COST_COMPONENTS,
    _valid_cost_fixture,
    build_custody_adversarial_gate,
    build_provider_receipt_gate,
    build_synthetic_custody_fixture,
    derive_capital_blockers,
    dump_frozen_qasm_subset,
    freeze_ai_dataset_contract,
    parse_frozen_qasm_subset,
    summarize_scale_repetitions,
    validate_provider_request_shape,
    validate_unified_math_registries,
)
from uqpu.cycle007_delta01 import (
    audit_dimension_contracts,
    measure_fresh_process_durability,
    qasm_measurement_map,
    validate_ai_dataset_replay,
    validate_content_range,
    validate_cycle007_complete_cost,
    validate_cycle007_custody_fixture,
    validate_cycle007_material_registry,
)


ROOT = Path(__file__).resolve().parents[3]
UMRL_PATH = ROOT / "benchmarks/experiments/cycle006-delta01-unified-math-goal-registry.json"
SCM_PATH = ROOT / "benchmarks/experiments/cycle006-delta01-scm-lokathibodi-math-registry.json"
MANIFEST_PATH = ROOT / "benchmarks/experiments/cycle003-delta01-er6-provider-neutral-manifest.json"
AI_BASELINE_PATH = ROOT / "benchmarks/results/batch039-ai-cost-002-classical-baseline.json"
ARTIFACT = ROOT / "benchmarks/results/cycle007-delta01-umrl-dimension-audit.json"
ZENODO_RANGE = ROOT / "benchmarks/evidence/cycle007-delta01-zenodo-range-verification.json"
REPRODUCIBILITY = ROOT / "benchmarks/results/cycle007-delta01-local-reproducibility.json"
LEDGER = ROOT / "benchmarks/results/cycle007-delta01-synchronized-lane-ledger.json"


def _read(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class Cycle007Delta01Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.umrl = _read(UMRL_PATH)
        cls.scm = _read(SCM_PATH)
        cls.manifest = _read(MANIFEST_PATH)
        cls.ai_baseline = _read(AI_BASELINE_PATH)

    def test_existing_registries_are_typed_but_not_machine_dimensioned(self):
        result = audit_dimension_contracts(self.umrl, self.scm)
        self.assertTrue(result["valid_registry_structure"], result["errors"])
        self.assertEqual(result["equation_count"], {"umrl": 30, "scm": 19})
        self.assertEqual(result["goal_count"], 23)
        self.assertEqual(result["variable_declaration_count"], 134)
        self.assertEqual(result["unit_or_type_present_count"], 134)
        self.assertEqual(result["quantity_kind_count"], 0)
        self.assertEqual(result["unit_code_count"], 0)
        self.assertEqual(result["machine_dimension_vector_count"], 0)
        self.assertFalse(result["dimensionally_auditable"])
        self.assertFalse(result["dimensional_consistency_claim"])
        self.assertEqual(set(result["lane_audit"]), {
            "A", "B", "C", "D", "E", "F", "G", "H",
            "FND/EQN", "SCM", "AI-COST", "QOS/QSVT",
        })
        self.assertTrue(all(row["umrl_variables"] for row in result["lane_audit"].values()))
        self.assertEqual(result["lane_audit"]["SCM"]["scm_variables"], 55)

    def test_dimension_vectors_require_exact_rational_exponents(self):
        umrl = deepcopy(self.umrl)
        variable = umrl["equations"][0]["variables"][0]
        variable["dimension_vector"] = {"length": "not-a-rational"}
        result = audit_dimension_contracts(umrl, self.scm)
        self.assertFalse(result["valid_registry_structure"])
        self.assertEqual(result["invalid_machine_dimension_vector_count"], 1)
        self.assertFalse(result["dimensional_consistency_claim"])

    def test_missing_free_text_label_fails_the_audit(self):
        scm = deepcopy(self.scm)
        del scm["equations"][0]["variables"][0]["unit_or_type"]
        result = audit_dimension_contracts(self.umrl, scm)
        self.assertFalse(result["valid_registry_structure"])
        self.assertTrue(any("scm_variable_type_label_missing" in e for e in result["errors"]))

    def test_lane_d_range_gate_requires_exact_bounded_http_206(self):
        self.assertEqual(validate_content_range(
            status=206,
            content_range="bytes 0-0/145469232",
            start=0,
            end=0,
            total=145469232,
            body_length=1,
        ), [])
        errors = validate_content_range(
            status=200,
            content_range=None,
            start=0,
            end=0,
            total=145469232,
            body_length=1,
        )
        self.assertIn("http_status_must_be_206", errors)
        self.assertIn("content_range_header_invalid", errors)
        errors = validate_content_range(
            status=206,
            content_range="bytes 0-1/145469233",
            start=0,
            end=0,
            total=145469232,
            body_length=2,
        )
        self.assertIn("content_range_coordinates_mismatch", errors)
        self.assertIn("range_body_length_mismatch", errors)

    def test_live_lane_d_range_artifact_preserves_crc_and_nonclaims(self):
        evidence = _read(ZENODO_RANGE)
        archive = evidence["archive"]
        readme = evidence["readme_range"]
        self.assertEqual(evidence["schema"], "uqpu-cycle007-primary-source-range-verification-v1")
        self.assertEqual(archive["bytes"], 145469232)
        self.assertEqual(archive["publisher_checksum_metadata"], "md5:d4f051ba40bf3d1940f90f9da4e9953c")
        self.assertEqual(archive["tail_range"]["status"], 206)
        self.assertEqual(archive["tail_range"]["returned_bytes"], 65557)
        self.assertEqual(archive["central_directory"]["inventory_summary"]["entries"], 502)
        self.assertEqual(readme["status"], 206)
        self.assertEqual(readme["member_bytes"], 3065)
        self.assertEqual(readme["semantic_anchors_missing"], [])
        self.assertEqual(readme["member_crc32"], readme["central_directory_crc32"])
        self.assertFalse(archive["full_archive_checksum_recomputed"])
        self.assertFalse(evidence["analysis_state"]["parquet_payload_retrieved"])

    def test_lane_a_two_fixtures_separate_exact_control_from_64_restart_baseline(self):
        for node_count, seed in ((8, 7101), (9, 7102)):
            repetitions = [
                benchmark_scale_case(
                    node_count,
                    seed,
                    max_states=1 << node_count,
                    deadline_seconds=10,
                    heuristic_restarts=64,
                )
                for _ in range(3)
            ]
            summary = summarize_scale_repetitions(repetitions)
            self.assertTrue(summary["exact"]["complete"])
            self.assertTrue(summary["exact"]["optimum_claim_allowed"])
            self.assertEqual(summary["heuristic"]["restarts"], 64)
            self.assertIsNotNone(summary["heuristic"]["objective_gap_to_exact"])
            self.assertIn(
                "No power, energy, GPU, provider, QPU, or hardware-neutral result is measured.",
                summary["non_claims"],
            )

    def test_lane_b_idempotency_shape_and_null_provider_receipt_fail_closed(self):
        gate = build_provider_receipt_gate(self.manifest)
        request = {
            "action": gate["dry_run"]["request_body"]["action"],
            "clientToken": "SYNTHETIC-NOT-SUBMITTED",
            "deviceArn": "SYNTHETIC-NOT-ROUTABLE",
            "outputS3Bucket": "synthetic-not-created",
            "outputS3KeyPrefix": "cycle007/schema-test-only",
            "shots": 32,
        }
        self.assertEqual(validate_provider_request_shape(request), [])
        invalid = deepcopy(request)
        invalid["clientToken"] = ""
        self.assertIn("clientToken_missing_or_empty", validate_provider_request_shape(invalid))
        self.assertFalse(gate["submission_surface_present"])
        self.assertFalse(gate["submission_authorized"])
        self.assertTrue(all(value is None for value in gate["execution_receipt"].values()))

    def test_lane_c_repeats_local_publication_in_fresh_processes(self):
        result = measure_fresh_process_durability({"fixture": [1, 2, 3]}, repetitions=3)
        self.assertTrue(result["fresh_process_per_repetition"])
        self.assertEqual(len(result["rows"]), 3)
        self.assertTrue(all(row["readback_sha256_matches"] for row in result["rows"]))
        self.assertFalse(result["platform_capabilities"]["cache_control_attempted"])
        self.assertEqual(result["platform_capabilities"]["cache_state"], "UNCONTROLLED")
        self.assertGreater(result["timing_summary_ns"]["publication_median"], 0)

    def test_local_reproducibility_artifact_records_a_and_c_controls(self):
        result = _read(REPRODUCIBILITY)
        fixtures = result["lane_a"]["fixtures"]
        self.assertEqual([row["fixture_id"] for row in fixtures], ["seeded-maxcut-8", "seeded-maxcut-9"])
        self.assertTrue(all(row["exact"]["complete"] for row in fixtures))
        self.assertTrue(all(row["heuristic"]["restarts"] == 64 for row in fixtures))
        storage = result["lane_c"]
        self.assertTrue(storage["fresh_process_per_repetition"])
        self.assertEqual(storage["repetitions"], 3)
        self.assertFalse(storage["platform_capabilities"]["cache_control_attempted"])

    def _complete_synthetic_material_registry(self):
        registry = build_material_evidence_registry()
        registry["study_lot_id"] = "SYNTHETIC-LOT-1"
        registry["method_scope_id"] = "SYNTHETIC-METHOD-V1"
        for slot in registry["slots"]:
            prerequisite = slot["prerequisite_id"]
            digest = hashlib.sha256(prerequisite.encode()).hexdigest()
            evidence = {
                "sha256": digest,
                "artifact_uri": f"artifact://sha256/{digest}",
                "issuer_or_operator": f"issuer-{prerequisite}",
                "date": "2026-09-28",
                "reviewer": f"reviewer-{prerequisite}",
                "scope_id": registry["study_id"],
                "method_scope_id": registry["method_scope_id"],
            }
            if prerequisite in {"DMF-PR-02", "DMF-PR-03"}:
                evidence["sample_lot_id"] = registry["study_lot_id"]
            if prerequisite in {"DMF-PR-01", "DMF-PR-07"}:
                evidence["valid_until"] = "2026-12-31"
            slot["evidence"] = evidence
        return registry

    def test_lane_e_material_gate_rejects_lot_role_scope_and_expiry_mutations(self):
        valid = self._complete_synthetic_material_registry()
        passed = validate_cycle007_material_registry(valid, as_of=date(2026, 9, 28))
        self.assertTrue(passed["ready"], passed["errors_by_prerequisite"])
        self.assertFalse(passed["fabrication_authorized"])

        mutations = (
            ("DMF-PR-02", "sample_lot_id", "OTHER-LOT", "sample_lot_id_mismatch"),
            ("DMF-PR-03", "reviewer", "issuer-DMF-PR-03", "issuer_reviewer_collision"),
            ("DMF-PR-04", "method_scope_id", "OTHER-METHOD", "method_scope_mismatch"),
            ("DMF-PR-01", "valid_until", "2026-09-27", "evidence_expired"),
        )
        for prerequisite, field, value, expected_error in mutations:
            broken = deepcopy(valid)
            slot = next(row for row in broken["slots"] if row["prerequisite_id"] == prerequisite)
            slot["evidence"][field] = value
            rejected = validate_cycle007_material_registry(broken, as_of=date(2026, 9, 28))
            self.assertIn(expected_error, rejected["errors_by_prerequisite"][prerequisite])

    def test_lane_f_cost_contract_rejects_units_currency_receipt_and_denominator(self):
        valid = _valid_cost_fixture()
        valid["amount_unit"] = "USD"
        valid["provider_receipt"] = {"receipt_id": "SYNTHETIC-RECEIPT"}
        valid["accepted_outputs"]["unit_code"] = "count"
        for component in valid["components"].values():
            component["unit_code"] = "USD"
        valid["components"]["provider_actual_bill"]["receipt_id"] = "SYNTHETIC-RECEIPT"
        self.assertTrue(validate_cycle007_complete_cost(valid)["complete"])

        mutations = []
        broken = deepcopy(valid)
        broken["components"]["storage"]["unit_code"] = "THB"
        mutations.append((broken, "unit_code_mismatch:storage"))
        broken = deepcopy(valid)
        broken["components"]["storage"]["currency"] = "EUR"
        mutations.append((broken, "currency_mismatch:storage"))
        broken = deepcopy(valid)
        broken["components"]["provider_actual_bill"]["receipt_id"] = "OTHER"
        mutations.append((broken, "provider_receipt_mismatch"))
        broken = deepcopy(valid)
        broken["components"]["queue"]["amount"] = float("nan")
        mutations.append((broken, "amount_invalid:queue"))
        broken = deepcopy(valid)
        broken["accepted_outputs"]["count"] = 0
        mutations.append((broken, "accepted_output_count_invalid"))
        for ledger, expected_error in mutations:
            rejected = validate_cycle007_complete_cost(ledger)
            self.assertFalse(rejected["complete"])
            self.assertIn(expected_error, rejected["errors"])
            self.assertIsNone(rejected["total_cost"])

    def test_lane_g_custody_gate_rejects_duplicate_predecessor_expiry_and_control(self):
        valid = build_synthetic_custody_fixture()
        self.assertEqual(validate_cycle007_custody_fixture(valid), [])
        duplicate = deepcopy(valid)
        duplicate["events"][1]["event_id"] = duplicate["events"][0]["event_id"]
        self.assertIn("duplicate_event_id", validate_cycle007_custody_fixture(duplicate))

        gates = build_custody_adversarial_gate()
        ids = {row["case_id"] for row in gates["negative_corpus"]}
        self.assertTrue({"broken_hash_chain", "expired_calibration", "unmatched_control"} <= ids)

    def test_lane_h_capital_stays_unauthorized_even_if_schema_prerequisites_pass(self):
        graph = build_capital_dependency_graph()
        prerequisites = {
            prerequisite
            for gate in graph["gates"]
            for prerequisite in gate["prerequisite_ids"]
        }
        result = derive_capital_blockers(graph, {item: True for item in prerequisites})
        self.assertFalse(result["funding_or_purchase_authorized"])
        self.assertTrue(all(row["status"] == "NOT_AUTHORIZED" for row in result["gates"]))
        self.assertTrue(all(row["capital_at_risk_thb"] is None for row in result["gates"]))

    def test_scm_equation_and_volume_references_reject_unknown_canon_ids(self):
        broken = deepcopy(self.scm)
        broken["volume_map"][0]["equation_ids"] = ["SCM-MATH-999"]
        result = validate_unified_math_registries(self.umrl, broken)
        self.assertFalse(result["formal_specification_valid"])
        self.assertIn("volume_equation_reference_invalid:1", result["errors"])

    def test_ai_cost_dataset_replay_rejects_frozen_hash_mismatch(self):
        frozen = freeze_ai_dataset_contract(
            self.ai_baseline,
            baseline_file_sha256="a" * 64,
            generator_module_sha256="b" * 64,
        )
        replayed = freeze_ai_dataset_contract(
            self.ai_baseline,
            baseline_file_sha256="a" * 64,
            generator_module_sha256="b" * 64,
        )
        self.assertTrue(validate_ai_dataset_replay(frozen, replayed)["replay_valid"])
        changed = deepcopy(replayed)
        changed["held_out"]["canonical_sha256"] = "0" * 64
        rejected = validate_ai_dataset_replay(frozen, changed)
        self.assertFalse(rejected["replay_valid"])
        self.assertIn("replay_hash_mismatch:held_out", rejected["errors"])
        self.assertFalse(rejected["candidate_result_admissible"])

    def test_qos_roundtrip_preserves_measurement_map_and_detects_ast_mutation(self):
        source = self.manifest["lane_a_b_c_qos"]["paired_circuits"][0]["openqasm_3"]
        original_ast = parse_frozen_qasm_subset(source)
        whitespace_ast = parse_frozen_qasm_subset("\n".join(f"  {line}  " for line in source.splitlines()))
        self.assertEqual(original_ast, whitespace_ast)
        canonical_ast = parse_frozen_qasm_subset(dump_frozen_qasm_subset(original_ast))
        self.assertEqual(qasm_measurement_map(original_ast), qasm_measurement_map(canonical_ast))

        mutated = deepcopy(original_ast)
        measurement = next(row for row in mutated if row["kind"] == "measure")
        measurement["arguments"][0] = str(100 + int(measurement["arguments"][0]))
        self.assertNotEqual(qasm_measurement_map(original_ast), qasm_measurement_map(mutated))

    def test_committed_audit_artifact_matches_the_generator(self):
        artifact = _read(ARTIFACT)
        regenerated = audit_dimension_contracts(self.umrl, self.scm)
        regenerated["source_registries"] = artifact["source_registries"]
        self.assertEqual(artifact, regenerated)

    def test_checkpoint_ledger_records_progress_in_all_twelve_lanes(self):
        ledger = _read(LEDGER)
        self.assertEqual(ledger["cycle"], "007")
        self.assertFalse(ledger["full_cycle_closeout_pending"])
        self.assertTrue(ledger["status"].startswith("CLOSED_"))
        self.assertEqual(ledger["next_cycle"], "008")
        self.assertFalse(ledger["closeout"]["scientific_goal_promotion"])
        self.assertEqual(ledger["closeout"]["tested_commit"], "d8b7d0e0b084be05fb4a52db382aaa18f7a737b6")
        self.assertEqual(ledger["closeout"]["push_ci"]["conclusion"], "success")
        self.assertEqual(ledger["closeout"]["push_ci"]["jobs_passed"], 8)
        self.assertEqual(ledger["validation"]["cycle007_focused_tests"]["passed"], 18)
        self.assertEqual(ledger["validation"]["full_prototype_suite"]["passed"], 457)
        self.assertEqual(ledger["validation"]["full_prototype_suite"]["skipped_optional"], 8)
        self.assertEqual(set(ledger["lanes"]), {
            "A", "B", "C", "D", "E", "F", "G", "H",
            "FND/EQN", "SCM", "AI-COST", "QOS/QSVT",
        })
        acceptance = ledger["cycle007_lane_acceptance"]
        self.assertEqual(set(acceptance), set(ledger["lanes"]))
        self.assertTrue(all(row["status"] == "PASS" for row in acceptance.values()))
        self.assertTrue(all(
            row["status"] == "BLOCKED_WITH_PROGRESS"
            and row["machine_dimension_vectors"] == 0
            for row in ledger["lanes"].values()
        ))
        self.assertEqual(
            ledger["audit_artifact_sha256"],
            hashlib.sha256(ARTIFACT.read_bytes()).hexdigest(),
        )


if __name__ == "__main__":
    unittest.main()
