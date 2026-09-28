from copy import deepcopy
from datetime import date
import hashlib
from io import BytesIO
import json
from pathlib import Path
import re
import unittest
import zipfile

from uqpu.cycle005_delta01 import (
    benchmark_scale_case,
    build_capital_dependency_graph,
    build_material_evidence_registry,
)
from uqpu.cycle003_delta01 import canonical_json_bytes
from uqpu.cycle006_delta01 import (
    benchmark_directory_durable_io,
    build_cost_adversarial_gate,
    build_custody_adversarial_gate,
    build_provider_receipt_gate,
    build_qasm_roundtrip_gate,
    build_scm_role_packages,
    derive_capital_blockers,
    freeze_ai_dataset_contract,
    parse_frozen_qasm_subset,
    parse_zip_central_directory_tail,
    recover_zip_member_from_range,
    summarize_scale_repetitions,
    validate_material_registry_v2,
    validate_scm_role_packages,
)


ROOT = Path(__file__).resolve().parents[3]
MANIFEST = ROOT / "benchmarks/experiments/cycle003-delta01-er6-provider-neutral-manifest.json"
AI_BASELINE = ROOT / "benchmarks/results/batch039-ai-cost-002-classical-baseline.json"
CYCLE005_PACKET = ROOT / "benchmarks/results/cycle005-delta01-integrated-gates.json"
SOURCE = ROOT / "benchmarks/evidence/cycle006-delta01-zenodo-range-metadata.json"
PACKET = ROOT / "benchmarks/results/cycle006-delta01-integrated-gates.json"
SCORER = ROOT / "benchmarks/experiments/cycle006-delta01-scm-scorer-package.json"
CUSTODIAN = ROOT / "benchmarks/results/cycle006-delta01-scm-custodian-package.json"
REVEAL_AUDIT = ROOT / "benchmarks/results/cycle006-delta01-scm-reveal-audit.json"


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class Cycle006Delta01Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = _load(MANIFEST)
        cls.ai = _load(AI_BASELINE)
        cls.cycle005 = _load(CYCLE005_PACKET)

    def test_repeated_scale_summary_separates_complete_from_capped_claims(self):
        complete = [
            benchmark_scale_case(6, 42, max_states=64, deadline_seconds=10)
            for _ in range(3)
        ]
        complete_summary = summarize_scale_repetitions(complete)
        self.assertTrue(complete_summary["exact"]["complete"])
        self.assertTrue(complete_summary["exact"]["optimum_claim_allowed"])
        capped = [
            benchmark_scale_case(6, 42, max_states=7, deadline_seconds=10)
            for _ in range(3)
        ]
        capped_summary = summarize_scale_repetitions(capped)
        self.assertFalse(capped_summary["exact"]["complete"])
        self.assertFalse(capped_summary["exact"]["optimum_claim_allowed"])
        self.assertIsNone(capped_summary["heuristic"]["objective_gap_to_exact"])

    def test_provider_receipt_gate_rejects_all_negative_requests(self):
        gate = build_provider_receipt_gate(self.manifest)
        self.assertTrue(all(row["errors"] for row in gate["negative_request_corpus"]))
        self.assertFalse(gate["receipt_complete"])
        self.assertFalse(gate["submission_surface_present"])
        self.assertIsNone(gate["execution_receipt"]["task_arn_or_job_id"])

    def test_directory_durability_records_directory_fsync_and_cache_boundary(self):
        result = benchmark_directory_durable_io({"fixture": [1, 2, 3]}, repetitions=3)
        boundary = result["durability_boundary"]
        self.assertTrue(boundary["file_fsync_completed"])
        self.assertTrue(boundary["atomic_replace_completed"])
        self.assertFalse(boundary["device_flush_attested"])
        self.assertFalse(boundary["power_loss_survival_tested"])
        self.assertFalse(result["cache_control"]["attempted"])
        self.assertGreater(result["process_peak_rss"]["value"], 0)

    def test_zip_tail_parser_and_member_recovery_use_no_full_extract(self):
        output = BytesIO()
        payload = b"range-recovered README fixture\n"
        with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.writestr("data_upload/README.md", payload)
            archive.writestr("data_upload/other.bin", b"other")
        raw = output.getvalue()
        parsed = parse_zip_central_directory_tail(raw, range_start=0, archive_size=len(raw))
        self.assertEqual(parsed["inventory_summary"]["files"], 2)
        readme = next(
            row for row in parsed["entries"] if row["path"] == "data_upload/README.md"
        )
        recovered = recover_zip_member_from_range(
            raw[readme["local_header_offset"] :], "data_upload/README.md"
        )
        self.assertEqual(recovered["content"], payload)
        self.assertEqual(recovered["crc32"], readme["crc32"])

    def test_material_registry_v2_rejects_missing_scope_expiry_and_lot(self):
        registry = build_material_evidence_registry()
        registry["study_lot_id"] = None
        result = validate_material_registry_v2(registry, as_of=date(2026, 9, 28))
        self.assertFalse(result["ready"])
        self.assertEqual(result["passing_count"], 0)
        self.assertIn("valid_until_missing_or_invalid", result["errors_by_prerequisite"]["DMF-PR-01"])
        self.assertIn("study_lot_id_missing", result["errors_by_prerequisite"]["DMF-PR-02"])

    def test_cost_adversarial_corpus_refuses_all_seven_cases(self):
        gate = build_cost_adversarial_gate()
        self.assertEqual(len(gate["negative_corpus"]), 7)
        self.assertTrue(all(row["errors"] for row in gate["negative_corpus"]))
        self.assertTrue(gate["synthetic_arithmetic_control"]["complete"])
        self.assertTrue(gate["current_evidence"]["refusal_active"])
        self.assertIsNone(gate["current_evidence"]["total_cost"])

    def test_custody_adversarial_corpus_rejects_chain_expiry_and_control(self):
        gate = build_custody_adversarial_gate()
        self.assertEqual(len(gate["negative_corpus"]), 3)
        self.assertTrue(all(row["errors"] for row in gate["negative_corpus"]))
        self.assertFalse(gate["operational_ready"])
        self.assertEqual(gate["operational_events"], [])

    def test_capital_blockers_are_derived_from_unsatisfied_ids(self):
        graph = build_capital_dependency_graph()
        statuses = {"DMF-PR-01": True}
        result = derive_capital_blockers(graph, statuses)
        self.assertFalse(result["funding_or_purchase_authorized"])
        self.assertTrue(all(row["status"] == "NOT_AUTHORIZED" for row in result["gates"]))
        self.assertTrue(any(row["unresolved_prerequisite_ids"] for row in result["gates"]))

    def test_scm_packages_are_hash_chained_and_reveal_order_tamper_fails(self):
        scorer, custodian, audit = build_scm_role_packages(
            self.cycle005["lanes"]["SCM"]
        )
        self.assertEqual(validate_scm_role_packages(scorer, custodian, audit), [])
        self.assertFalse(scorer["condition_labels_or_truth_present"])
        self.assertFalse(audit["separate_repository_or_site"])
        tampered = deepcopy(custodian)
        tampered["events"][0]["artifact_sha256"] = "0" * 64
        errors = validate_scm_role_packages(scorer, tampered, audit)
        self.assertIn("reveal_before_or_without_scorer_close", errors)
        self.assertIn("custodian:event_hash_mismatch", errors)

    def test_ai_dataset_contract_freezes_exact_content_hashes_and_null_metrics(self):
        result = freeze_ai_dataset_contract(
            self.ai,
            baseline_file_sha256="a" * 64,
            generator_module_sha256="b" * 64,
        )
        self.assertEqual(result["train"]["examples"], 256)
        self.assertEqual(result["held_out"]["examples"], 256)
        self.assertRegex(result["train"]["canonical_sha256"], r"^[0-9a-f]{64}$")
        self.assertNotEqual(
            result["train"]["canonical_sha256"], result["held_out"]["canonical_sha256"]
        )
        self.assertIsNone(result["candidate_result"])
        self.assertIsNone(result["measured_candidate_energy"])

    def test_qasm_subset_roundtrip_passes_manifest_and_rejects_unknown_input(self):
        gate = build_qasm_roundtrip_gate(self.manifest)
        self.assertTrue(gate["all_roundtrips_passed"])
        self.assertTrue(all(row["roundtrip_ast_equal"] for row in gate["rows"]))
        self.assertFalse(gate["provider_transpile_receipt_complete"])
        with self.assertRaisesRegex(ValueError, "unsupported QASM"):
            parse_frozen_qasm_subset("OPENQASM 3.0;\nreset q[0];\n")

    def test_committed_cycle006_artifacts_are_hash_bound_and_cover_all_lanes(self):
        expected_hashes = {
            SOURCE: "cc5ee23fb9b2f3d8e75fc80c749aa299dd146e52cc5b468e9d9f4a433b96d52c",
            PACKET: "1dc1ffc37680200b5103b89db7f168a0ff0180c009c94216777f1ff7aeae226a",
            SCORER: "b42f21ff14b468346ae1f4937edaee5c62efb150245a5f1302075fcd8707b2f3",
            CUSTODIAN: "198f0ed1d840b816cd92236882498994a5681c6d02ecc70f0f69f15daed965cb",
            REVEAL_AUDIT: "3f5eab3053a6c2a728501d42bbfbba704761dca76c3ff87c3c9014709076145b",
        }
        for path, expected in expected_hashes.items():
            self.assertTrue(path.exists(), f"missing committed artifact: {path}")
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), expected)

        source = _load(SOURCE)
        packet = _load(PACKET)
        scorer = _load(SCORER)
        custodian = _load(CUSTODIAN)
        audit = _load(REVEAL_AUDIT)
        self.assertEqual(packet["cycle"], "006")
        self.assertEqual(packet["delta"], "01")
        self.assertEqual(
            set(packet["lanes"]),
            {
                "A", "B", "C", "D", "E", "F", "G", "H",
                "FND/EQN", "SCM", "AI-COST", "QOS/QSVT",
            },
        )
        self.assertEqual(
            packet["generator_code_commit"],
            "f336b6ddbda555aaba212b5c05bd0a818e9c6368",
        )
        self.assertTrue(packet["lanes"]["A"]["repeated_scale_cases"][0]["exact"]["complete"])
        self.assertFalse(packet["lanes"]["A"]["repeated_scale_cases"][1]["exact"]["complete"])
        self.assertEqual(
            packet["lanes"]["A"]["repeated_scale_cases"][1]["exact"]["stop_reason"],
            "STATE_CAP",
        )
        self.assertEqual(source["source"]["license"], {"id": "cc-by-4.0"})
        self.assertEqual(source["central_directory"]["inventory_summary"]["entries"], 502)
        self.assertFalse(source["analysis_state"]["parquet_payload_retrieved"])
        self.assertEqual(
            audit["scorer_package_canonical_sha256"],
            hashlib.sha256(canonical_json_bytes(scorer)).hexdigest(),
        )
        self.assertEqual(
            audit["custodian_package_canonical_sha256"],
            hashlib.sha256(canonical_json_bytes(custodian)).hexdigest(),
        )
        self.assertEqual(
            packet["lanes"]["AI-COST"]["train"]["canonical_sha256"],
            "57470ff96e059ff9f112a935fd1512c7208235fe9417018ef92d25e4c5dd82fe",
        )
        self.assertEqual(
            packet["lanes"]["AI-COST"]["held_out"]["canonical_sha256"],
            "791cd18405f5de38bf8df95cd9d419b86c446350b4fba89f74e9416a3819adce",
        )
        self.assertFalse(packet["lanes"]["H"]["funding_or_purchase_authorized"])
        self.assertFalse(packet["lanes"]["QOS/QSVT"]["hardware_executed"])


if __name__ == "__main__":
    unittest.main()
