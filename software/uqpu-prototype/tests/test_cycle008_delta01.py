from copy import deepcopy
import hashlib
import json
from pathlib import Path
import unittest

from uqpu.cycle008_delta01 import (
    audit_lane_links,
    audit_dimension_equation,
    audit_five_volume_contracts,
    audit_scm_equation_extensions,
    audit_umrl_extension,
    build_cycle008_math_audit,
    build_synthetic_request_receipt,
    compare_deterministic_solver_restarts,
    plan_archive_download,
    rank_evidence_gates,
    validate_ai_candidate_evidence,
    validate_calibration_uncertainty_gate,
    validate_consent_request,
    validate_domain_bridge,
    validate_fictional_conservation,
    validate_material_measurement_record,
    validate_quantity_type,
    validate_cost_interval,
    validate_qos_semantic_certificate,
    validate_synthetic_request_receipt,
)
from uqpu.cycle006_delta01 import parse_frozen_qasm_subset
from uqpu.cycle007_delta01 import measure_fresh_process_durability, qasm_measurement_map


ROOT = Path(__file__).resolve().parents[3]
REGISTRY_PATH = ROOT / "benchmarks/experiments/cycle008-delta01-typed-math-scm-registry.json"
ARTIFACT_PATH = ROOT / "benchmarks/results/cycle008-delta01-typed-math-scm-audit.json"
MANIFEST_PATH = ROOT / "benchmarks/experiments/cycle003-delta01-er6-provider-neutral-manifest.json"


def _read(path):
    return json.loads(path.read_text(encoding="utf-8"))


class Cycle008TypedMathTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = _read(REGISTRY_PATH)

    def test_supplemental_registry_passes_bounded_typed_audit(self):
        result = build_cycle008_math_audit(self.registry)
        self.assertEqual(result["status"], "PASS", result["errors"])
        self.assertEqual(result["dimension_equation_count"], 3)
        self.assertTrue(result["umrl_extension"]["valid"])
        self.assertEqual(result["lane_links"]["lane_count"], 12)
        self.assertEqual(result["scm_equation_extensions"]["equation_ids"], [
            "SCM-MATH-020", "SCM-MATH-021", "SCM-MATH-022", "SCM-MATH-023",
        ])
        self.assertEqual(result["five_volume_contract"]["volume_count"], 5)
        self.assertEqual(result["consent_gate"]["negative_cases_rejected"], 5)
        self.assertEqual(result["fictional_conservation"]["negative_cases_rejected"], 4)
        self.assertTrue(result["fiction_to_real_cast"]["unvalidated_cast_rejected"])
        self.assertTrue(result["fiction_to_real_cast"]["no_synthetic_valid_bridge_fixture"])

    def test_registry_subset_has_exact_equation_dimensions(self):
        result = build_cycle008_math_audit(self.registry)
        self.assertTrue(all(row["balanced"] for row in result["dimension_equations"]))
        throughput = next(row for row in result["dimension_equations"]
                          if row["equation_id"] == "UMRL-007:T_acc")
        self.assertEqual(throughput["lhs_dimension_vector"]["count"], "1")
        self.assertEqual(throughput["lhs_dimension_vector"]["time"], "-1")

    def test_float_exponents_and_unit_vector_mismatch_are_rejected(self):
        quantity = deepcopy(self.registry["quantities"][0])
        quantity["dimension_vector"]["time"] = 0.5
        self.assertIn(
            f"real_quantity_dimension_vector_invalid:{quantity['quantity_id']}",
            validate_quantity_type(quantity, self.registry["unit_registry"]),
        )
        quantity = deepcopy(self.registry["quantities"][0])
        quantity["unit_code"] = "s"
        self.assertIn(
            f"unit_dimension_mismatch:{quantity['quantity_id']}",
            validate_quantity_type(quantity, self.registry["unit_registry"]),
        )

    def test_dimension_mismatch_and_cross_sort_sum_are_rejected(self):
        quantities = {row["quantity_id"]: row for row in self.registry["quantities"]}
        units = self.registry["unit_registry"]
        equation = deepcopy(self.registry["dimension_equations"][0])
        equation["rhs_terms"][0]["factors"][0]["power"] = "2"
        mismatch = audit_dimension_equation(equation, quantities, units)
        self.assertFalse(mismatch["balanced"])
        self.assertIn("dimension_mismatch_in_rhs_term:0", mismatch["errors"])

        fictional = self.registry["quantities"][-1]
        equation = {
            "equation_id": "synthetic-sort-mismatch",
            "lhs": "T_acc",
            "rhs_terms": [{"factors": [{"quantity_id": fictional["quantity_id"], "power": 1}]}],
        }
        mixed = audit_dimension_equation(equation, quantities, units)
        self.assertFalse(mixed["balanced"])
        self.assertTrue(any(error.startswith("rhs:fiction_evidence_type_invalid") for error in mixed["errors"])
                        or "domain_sort_mismatch:0:fictional_route_cost" in mixed["errors"])

    def test_fictional_quantities_do_not_accept_si_units_or_dimension_vectors(self):
        fictional = deepcopy(self.registry["quantities"][-1])
        fictional["unit_code"] = "m"
        self.assertIn(
            f"fiction_unit_must_be_canon_scoped:{fictional['quantity_id']}",
            validate_quantity_type(fictional, self.registry["unit_registry"]),
        )
        fictional["unit_code"] = "CANON:route-point"
        fictional["dimension_vector"] = self.registry["unit_registry"]["s"]["dimension_vector"]
        self.assertIn(
            f"fiction_dimension_vector_requires_validated_bridge:{fictional['quantity_id']}",
            validate_quantity_type(fictional, self.registry["unit_registry"]),
        )

    def test_consent_requires_exact_scope_time_agency_safety_and_nonreplay(self):
        fixture = self.registry["consent_fixtures"]["valid"]
        grant = fixture["grant"]
        request = fixture["request"]
        accepted = validate_consent_request(grant, request)
        self.assertTrue(accepted["authorized"], accepted["errors"])

        replayed = validate_consent_request(
            grant, request, used_nonces={grant["nonce"]}
        )
        self.assertIn("consent_nonce_replayed", replayed["errors"])
        revoked = deepcopy(grant)
        revoked["revoked"] = True
        self.assertIn(
            "consent_revoked_or_unknown",
            validate_consent_request(revoked, request)["errors"],
        )
        expired = deepcopy(request)
        expired["now_tick"] = grant["expires_at_tick"]
        self.assertIn(
            "consent_outside_validity_window",
            validate_consent_request(grant, expired)["errors"],
        )
        unsafe = deepcopy(request)
        unsafe["safety_pass"] = False
        self.assertIn(
            "safety_gate_not_passed",
            validate_consent_request(grant, unsafe)["errors"],
        )

    def test_fictional_conservation_uses_one_canon_unit_and_exact_values(self):
        fixtures = self.registry["conservation_fixtures"]
        accepted = validate_fictional_conservation(
            fixtures["valid"], tolerance=fixtures["valid_tolerance"]
        )
        self.assertTrue(accepted["balanced"], accepted["errors"])
        for row in fixtures["negative"]:
            rejected = validate_fictional_conservation(
                row["ledger"], tolerance=row["tolerance"]
            )
            self.assertFalse(rejected["balanced"])
        broken = deepcopy(fixtures["valid"])
        broken["entries"][1]["quantity_id"] = "CANON:another-quantity"
        self.assertIn(
            "conservation_quantity_mismatch",
            validate_fictional_conservation(broken, tolerance="0")["errors"],
        )
        broken = deepcopy(fixtures["valid"])
        broken["entries"][1]["canon_version"] = "LOKATHIBODI-2.0"
        self.assertIn(
            "conservation_canon_version_mismatch",
            validate_fictional_conservation(broken, tolerance="0")["errors"],
        )
        self.assertIn(
            "conservation_delta_must_be_exact_rational",
            validate_fictional_conservation(
                {"domain_sort": "FICTION_CANON", "entries": [
                    {"quantity_id": "CANON:q", "canon_version": "v1",
                     "delta": 0.1, "unit_code": "CANON:unit"}
                ]},
                tolerance="0",
            )["errors"],
        )

    def test_five_volumes_each_require_their_invariant_and_firewall(self):
        volumes = self.registry["five_volume_contracts"]
        self.assertTrue(audit_five_volume_contracts(volumes)["valid"])
        broken = deepcopy(volumes)
        broken[2]["real_evidence_cast"] = "ALLOWED"
        result = audit_five_volume_contracts(broken)
        self.assertFalse(result["valid"])
        self.assertIn("volume_no_cast_rule_missing:3", result["errors"])

    def test_scm_equation_extension_requires_fiction_sort_and_falsifier(self):
        equations = deepcopy(self.registry["scm_equations"])
        self.assertTrue(audit_scm_equation_extensions(equations)["valid"])
        equations[1]["domain_sort"] = "REAL_EMPIRICAL"
        equations[1]["falsifier"] = ""
        rejected = audit_scm_equation_extensions(equations)
        self.assertFalse(rejected["valid"])
        self.assertIn("scm_extension_domain_sort_invalid:SCM-MATH-021", rejected["errors"])
        self.assertIn("scm_extension_falsifier_missing:SCM-MATH-021", rejected["errors"])
        known = {row["equation_id"] for row in self.registry["scm_equations"]}
        self.assertTrue(all(
            set(volume["equation_ids"]) <= known
            for volume in self.registry["five_volume_contracts"]
        ))

    def test_shared_math_mapping_covers_twelve_lanes_and_rejects_unknown_equations(self):
        links = deepcopy(self.registry["lane_links"])
        self.assertTrue(audit_lane_links(links)["valid"])
        links["SCM"].append("SCM-MATH-999")
        self.assertIn(
            "lane_link_equation_unknown:SCM:SCM-MATH-999",
            audit_lane_links(links)["errors"],
        )
        extension = deepcopy(self.registry["umrl_extension"])
        extension["falsifier"] = ""
        self.assertIn(
            "umrl_extension_field_missing:falsifier",
            audit_umrl_extension(extension)["errors"],
        )

    def test_unvalidated_fictional_to_real_bridge_is_rejected(self):
        self.assertFalse(validate_domain_bridge(None)["allowed"])
        self.assertFalse(
            validate_domain_bridge(self.registry["bridge_fixture_unvalidated"])["allowed"]
        )
        self.assertTrue(validate_domain_bridge(self.registry["bridge_fixture_unvalidated"])["errors"])

    def test_persisted_artifact_matches_generator(self):
        artifact = _read(ARTIFACT_PATH)
        expected = build_cycle008_math_audit(self.registry)
        for key in expected:
            self.assertEqual(artifact[key], expected[key], key)
        self.assertEqual(
            artifact["provenance"]["registry_sha256"],
            hashlib.sha256(REGISTRY_PATH.read_bytes()).hexdigest(),
        )
        for path_key, hash_key in (
            ("generator", "generator_sha256"),
            ("implementation", "implementation_sha256"),
            ("source_umrl_document", "source_umrl_sha256"),
            ("source_scm_document", "source_scm_sha256"),
            ("checkpoint_document", "checkpoint_document_sha256"),
            ("test_file", "test_file_sha256"),
        ):
            path = ROOT / artifact["provenance"][path_key]
            self.assertEqual(
                artifact["provenance"][hash_key],
                hashlib.sha256(path.read_bytes()).hexdigest(),
                path_key,
            )


class Cycle008LaneAcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = _read(REGISTRY_PATH)
        cls.manifest = _read(MANIFEST_PATH)

    def test_lane_a_restart_sensitivity_keeps_exact_completion_separate(self):
        results = [
            compare_deterministic_solver_restarts(node_count=12, seed=seed)
            for seed in (80812, 80813)
        ]
        self.assertTrue(all(row["exact_control"]["complete"] for row in results))
        self.assertTrue(all(row["exact_control"]["states_evaluated"] == 4096
                            for row in results))
        self.assertTrue(all(
            [variant["restarts"] for variant in row["solver_variants"]] == [32, 128]
            for row in results
        ))
        self.assertTrue(all(
            [variant["gap_to_exact"] for variant in row["solver_variants"]] == [0.0, 0.0]
            for row in results
        ))

    def test_lane_b_hash_link_and_idempotency_mutation_fail_closed(self):
        request = {
            "action": "CreateQuantumTask",
            "clientToken": "SYNTHETIC-NOT-SUBMITTED-008",
            "shots": 8192,
        }
        receipt = build_synthetic_request_receipt(request)
        accepted = validate_synthetic_request_receipt(request, receipt)
        self.assertTrue(accepted["valid"], accepted["errors"])
        self.assertFalse(accepted["submission_authorized"])

        changed_request = deepcopy(request)
        changed_request["shots"] = 8193
        rejected = validate_synthetic_request_receipt(changed_request, receipt)
        self.assertFalse(rejected["valid"])
        self.assertIn("request_hash_mismatch", rejected["errors"])

        changed_receipt = deepcopy(receipt)
        changed_receipt["submitted"] = True
        self.assertIn(
            "submission_must_remain_disabled",
            validate_synthetic_request_receipt(request, changed_receipt)["errors"],
        )

    def test_lane_c_process_scope_does_not_imply_cache_or_durability(self):
        result = measure_fresh_process_durability(
            {"cycle": "008", "fixture": "synthetic"}, repetitions=3
        )
        self.assertTrue(result["fresh_process_per_repetition"])
        self.assertFalse(result["platform_capabilities"]["cache_control_attempted"])
        self.assertEqual(result["platform_capabilities"]["cache_state"], "UNCONTROLLED")
        self.assertTrue(all(row["readback_sha256_matches"] for row in result["rows"]))

    def test_lane_d_archive_plan_enforces_resource_cap_and_never_downloads(self):
        blocked = plan_archive_download(145469232, max_bytes=33554432)
        self.assertFalse(blocked["allowed_by_size_cap"])
        self.assertFalse(blocked["download_performed"])
        bounded = plan_archive_download(4096, max_bytes=33554432)
        self.assertTrue(bounded["allowed_by_size_cap"])
        self.assertFalse(bounded["download_performed"])
        self.assertIn("archive_size_must_be_nonnegative_integer",
                      plan_archive_download("145MB", max_bytes=33554432)["errors"])

    def test_lane_e_material_record_requires_unit_matched_uncertainty(self):
        record = {
            "record_id": "SYNTHETIC-MATERIAL-008",
            "lot_id": "SYNTHETIC-LOT",
            "function_id": "EMI-SHIELDING",
            "quantity_id": "surface_resistance",
            "unit_code": "ohm/square",
            "value": "12",
            "expanded_uncertainty": "2",
            "uncertainty_unit_code": "ohm/square",
            "control_id": "SYNTHETIC-CONTROL",
            "calibration_id": "SYNTHETIC-CAL",
            "evidence_status": "SYNTHETIC_ONLY",
            "synthetic": True,
            "physical_sampled": False,
        }
        self.assertTrue(validate_material_measurement_record(record)["valid"])
        broken = deepcopy(record)
        broken["uncertainty_unit_code"] = "S"
        self.assertIn("material_uncertainty_unit_mismatch",
                      validate_material_measurement_record(broken)["errors"])
        self.assertFalse(validate_material_measurement_record(broken)["physical_measurement_claim"])

    def test_lane_f_cost_interval_requires_common_currency_and_outputs(self):
        ledger = {
            "currency": "USD",
            "required_components": ["compute", "storage"],
            "components": {
                "compute": {"lower": "2", "upper": "3", "currency": "USD", "unit_code": "USD"},
                "storage": {"lower": "1", "upper": "2", "currency": "USD", "unit_code": "USD"},
            },
            "accepted_outputs": 2,
            "accepted_output_provenance": {
                "contract_id": "SYNTHETIC-SERVICE-CONTRACT",
                "sha256": "e" * 64,
                "evidence_status": "SYNTHETIC",
            },
        }
        result = validate_cost_interval(ledger)
        self.assertTrue(result["complete"], result["errors"])
        self.assertEqual(result["total_interval"]["lower"], "3")
        self.assertEqual(result["per_accepted_output_interval"]["upper"], "5/2")
        self.assertFalse(result["funding_authorized"])
        broken = deepcopy(ledger)
        broken["components"]["storage"]["currency"] = "THB"
        self.assertFalse(validate_cost_interval(broken)["complete"])
        broken = deepcopy(ledger)
        broken["accepted_output_provenance"]["sha256"] = "bad"
        self.assertFalse(validate_cost_interval(broken)["complete"])
        broken = deepcopy(ledger)
        broken["accepted_outputs"] = 0
        self.assertIsNone(validate_cost_interval(broken)["total_interval"])

    def test_lane_g_calibration_gate_checks_scope_expiry_and_uncertainty(self):
        certificate = {
            "certificate_id": "SYNTHETIC-CERT",
            "instrument_id": "SYNTHETIC-INSTRUMENT",
            "method_scope": "EMI-SHIELDING-VNA",
            "valid_from_tick": 10,
            "valid_through_tick": 30,
            "uncertainty_budget": {
                "components": [
                    {"component_id": "TYPE-A", "standard_uncertainty": "3/100",
                     "unit_code": "ohm/square"},
                    {"component_id": "TYPE-B", "standard_uncertainty": "4/100",
                     "unit_code": "ohm/square"},
                ],
                "combination_rule": "ROOT_SUM_OF_SQUARES_UNCORRELATED",
                "combined_standard_uncertainty": "1/20",
                "coverage_factor": "2",
                "expanded_uncertainty": "1/10",
            },
            "issuer": "SYNTHETIC-ISSUER",
            "reviewer": "SYNTHETIC-REVIEWER",
        }
        result = validate_calibration_uncertainty_gate(
            certificate, as_of_tick=20, required_scope="EMI-SHIELDING-VNA",
            measurement_unit="ohm/square",
        )
        self.assertTrue(result["ready"], result["errors"])
        broken = deepcopy(certificate)
        broken["valid_through_tick"] = 19
        broken["method_scope"] = "OTHER"
        rejected = validate_calibration_uncertainty_gate(
            broken, as_of_tick=20, required_scope="EMI-SHIELDING-VNA",
            measurement_unit="ohm/square",
        )
        self.assertIn("calibration_expired_or_not_yet_valid", rejected["errors"])
        self.assertIn("calibration_scope_mismatch", rejected["errors"])
        self.assertFalse(rejected["physical_calibration_claim"])
        missing_combination_rule = deepcopy(certificate)
        missing_combination_rule["uncertainty_budget"].pop("combination_rule")
        self.assertIn(
            "calibration_combination_rule_missing_or_unsupported",
            validate_calibration_uncertainty_gate(
                missing_combination_rule, as_of_tick=20,
                required_scope="EMI-SHIELDING-VNA", measurement_unit="ohm/square",
            )["errors"],
        )
        broken_budget = deepcopy(certificate)
        broken_budget["uncertainty_budget"]["expanded_uncertainty"] = "1/20"
        self.assertIn(
            "calibration_expanded_uncertainty_mismatch",
            validate_calibration_uncertainty_gate(
                broken_budget, as_of_tick=20,
                required_scope="EMI-SHIELDING-VNA", measurement_unit="ohm/square",
            )["errors"],
        )

    def test_lane_h_gate_ranking_is_assumption_bound_and_never_authorizes(self):
        gates = [
            {"gate_id": "GATE-A", "information_gain_bits": "4", "illustrative_cost": "100",
             "currency": "THB", "assumptions": ["synthetic cost", "illustrative information"]},
            {"gate_id": "GATE-B", "information_gain_bits": "2", "illustrative_cost": "25",
             "currency": "THB", "assumptions": ["synthetic cost", "illustrative information"]},
        ]
        result = rank_evidence_gates(gates)
        self.assertTrue(result["valid"], result["errors"])
        self.assertEqual(result["ranking"][0]["gate_id"], "GATE-B")
        self.assertFalse(result["capital_authorized"])
        self.assertFalse(rank_evidence_gates(gates[:1] + [{
            **gates[1], "currency": "USD"
        }])["valid"])

    def test_lane_fnd_eqn_accepts_exact_homogeneous_units_and_keeps_counterexample(self):
        result = build_cycle008_math_audit(self.registry)
        self.assertTrue(all(row["balanced"] for row in result["dimension_equations"]))
        quantities = {row["quantity_id"]: row for row in self.registry["quantities"]}
        units = self.registry["unit_registry"]
        equation = deepcopy(self.registry["dimension_equations"][1])
        equation["rhs_terms"][0]["factors"][1]["power"] = "1"
        rejected = audit_dimension_equation(equation, quantities, units)
        self.assertFalse(rejected["balanced"])

    def test_lane_scm_five_volume_fixture_is_typed_and_real_null(self):
        result = build_cycle008_math_audit(self.registry)
        self.assertTrue(result["five_volume_contract"]["valid"])
        self.assertEqual(result["five_volume_contract"]["volume_count"], 5)
        self.assertTrue(result["fiction_to_real_cast"]["unvalidated_cast_rejected"])
        self.assertTrue(all(row["domain_sort"] == "FICTION_CANON"
                            for row in self.registry["five_volume_contracts"]))

    def test_lane_ai_cost_rejects_split_leakage_and_incomplete_candidate_evidence(self):
        candidate = {
            "train_ids": ["train-1", "train-2"],
            "held_out_ids": ["held-1"],
            "model_sha256": "a" * 64,
            "dataset_sha256": "b" * 64,
            "evaluation_sha256": "c" * 64,
            "quality": {"metric": "accuracy", "value": "0.91"},
            "runtime_seconds": "12",
            "energy_joules": "8",
            "total_cost": "0.25",
            "cost_currency": "USD",
            "accepted_outputs": 10,
        }
        valid_fixture = validate_ai_candidate_evidence(candidate)
        self.assertTrue(valid_fixture["schema_valid"], valid_fixture["errors"])
        self.assertFalse(valid_fixture["evidence_admissible"])
        self.assertFalse(valid_fixture["candidate_result_claimed"])
        leaked = deepcopy(candidate)
        leaked["held_out_ids"] = ["train-2"]
        self.assertIn("train_held_out_leakage",
                      validate_ai_candidate_evidence(leaked)["errors"])
        incomplete = deepcopy(candidate)
        incomplete["energy_joules"] = None
        self.assertFalse(validate_ai_candidate_evidence(incomplete)["schema_valid"])
        self.assertFalse(validate_ai_candidate_evidence(incomplete)["candidate_result_claimed"])

    def test_lane_qos_semantics_certificate_rejects_changed_measurement_map(self):
        source = self.manifest["lane_a_b_c_qos"]["paired_circuits"][0]["openqasm_3"]
        ast = parse_frozen_qasm_subset(source)
        expected_map = qasm_measurement_map(ast)
        certificate = {
            "contract_id": "ER6-SUBSET-SYNTHETIC",
            "source_sha256": "d" * 64,
            "qubit_count": 6,
            "gate_count": 12,
            "depth": 5,
        }
        valid = validate_qos_semantic_certificate(expected_map, expected_map, certificate)
        self.assertTrue(valid["valid"], valid["errors"])
        changed = dict(expected_map)
        first_bit = next(iter(changed))
        changed[first_bit] = (changed[first_bit] + 1) % 6
        rejected = validate_qos_semantic_certificate(changed, expected_map, certificate)
        self.assertIn("measurement_map_mismatch", rejected["errors"])
        self.assertIsNone(rejected["provider_transpile_receipt"])


if __name__ == "__main__":
    unittest.main()
