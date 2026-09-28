from copy import deepcopy
import json
from pathlib import Path
import unittest

from uqpu.cycle008_delta01 import (
    audit_dimension_equation,
    audit_five_volume_contracts,
    audit_scm_equation_extensions,
    build_cycle008_math_audit,
    validate_consent_request,
    validate_domain_bridge,
    validate_fictional_conservation,
    validate_quantity_type,
)


ROOT = Path(__file__).resolve().parents[3]
REGISTRY_PATH = ROOT / "benchmarks/experiments/cycle008-delta01-typed-math-scm-registry.json"
ARTIFACT_PATH = ROOT / "benchmarks/results/cycle008-delta01-typed-math-scm-audit.json"


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
        self.assertEqual(result["scm_equation_extensions"]["equation_ids"], [
            "SCM-MATH-020", "SCM-MATH-021", "SCM-MATH-022", "SCM-MATH-023",
        ])
        self.assertEqual(result["five_volume_contract"]["volume_count"], 5)
        self.assertEqual(result["consent_gate"]["negative_cases_rejected"], 5)
        self.assertEqual(result["fictional_conservation"]["negative_cases_rejected"], 3)
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
        fictional["dimension_vector"] = self.registry["unit_registry"]["m"]["dimension_vector"]
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


if __name__ == "__main__":
    unittest.main()
