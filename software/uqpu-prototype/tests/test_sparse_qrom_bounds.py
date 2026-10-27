import math
import unittest

from uqpu.sparse_qrom_bounds import (
    build_sparse_qrom_proxy_contract,
    sparse_qrom_t_count_scale_proxy,
    validate_sparse_qrom_proxy_contract,
)


def sample_manifest():
    return {
        "address_bits": 4,
        "data_bits": 8,
        "support_size": 3,
        "table_sha256_declared": "a" * 64,
        "output_contract_id": "TEST-OUTPUT-001",
        "sparse_promise_accepted": True,
        "sparse_promise_evidence_ref": "tests/fixtures/sparse-qrom-promise.md",
        "dense_fallback_available": True,
    }


class SparseQROMBoundsTests(unittest.TestCase):
    def test_scale_proxy_matches_the_stated_asymptotic_expression(self):
        result = sparse_qrom_t_count_scale_proxy(4, 8, 3)
        expected = 4 + min(3.0, math.sqrt(3.0) * math.sqrt(8.0 + 5.0 - math.log2(3.0)))
        self.assertTrue(math.isclose(result["asymptotic_scale_proxy"], expected))
        self.assertTrue(result["not_exact_t_count"])
        self.assertTrue(result["not_certified_numeric_upper_or_lower_bound"])
        self.assertEqual(result["evidence_class"], "MODEL_ONLY_ASYMPTOTIC_CIRCUIT_COMPLEXITY_PROXY")

    def test_valid_manifest_stays_model_only_and_fail_closed_on_unknown_resources(self):
        contract = build_sparse_qrom_proxy_contract(sample_manifest())
        self.assertEqual(validate_sparse_qrom_proxy_contract(contract), [])
        self.assertEqual(contract["evidence_class"], "MODEL_ONLY")
        self.assertIsNone(contract["unknown_resources"]["provider_cost"])
        self.assertIsNone(contract["unknown_resources"]["physical_memory_bytes"])
        self.assertEqual(contract["input_contract"]["table_hash_status"], "DECLARED_NOT_VERIFIED_BY_THIS_MODULE")
        self.assertEqual(contract["input_contract"]["sparse_promise_status"], "CALLER_DECLARED_NOT_INDEPENDENTLY_VERIFIED")

    def test_sparse_promise_is_mandatory(self):
        manifest = sample_manifest()
        manifest["sparse_promise_accepted"] = False
        with self.assertRaisesRegex(ValueError, "sparse address promise"):
            build_sparse_qrom_proxy_contract(manifest)

    def test_dense_fallback_is_mandatory(self):
        manifest = sample_manifest()
        manifest["dense_fallback_available"] = False
        with self.assertRaisesRegex(ValueError, "dense/no-promise fallback"):
            build_sparse_qrom_proxy_contract(manifest)

    def test_dimensions_and_support_are_validated(self):
        for args in ((0, 8, 1), (4, 1, 1), (4, 8, 0), (4, 8, 17), (True, 8, 1), (1001, 8, 1)):
            with self.subTest(args=args):
                with self.assertRaises(ValueError):
                    sparse_qrom_t_count_scale_proxy(*args)

    def test_manifest_hash_contract_and_output_identity_are_required(self):
        for field, value in (
            ("table_sha256_declared", "not-a-hash"),
            ("output_contract_id", ""),
            ("sparse_promise_evidence_ref", ""),
        ):
            manifest = sample_manifest()
            manifest[field] = value
            with self.subTest(field=field):
                with self.assertRaises(ValueError):
                    build_sparse_qrom_proxy_contract(manifest)

    def test_validator_rejects_mutated_resource_claims(self):
        contract = build_sparse_qrom_proxy_contract(sample_manifest())
        contract["unknown_resources"]["provider_cost"] = 1.0
        self.assertIn("unmeasured_resources_must_remain_null", validate_sparse_qrom_proxy_contract(contract))
        self.assertIn("contract_digest_mismatch", validate_sparse_qrom_proxy_contract(contract))

    def test_validator_rejects_false_exact_count_or_evidence_promotion(self):
        contract = build_sparse_qrom_proxy_contract(sample_manifest())
        contract["resource_proxy"]["not_exact_t_count"] = False
        contract["evidence_class"] = "MEASURED"
        errors = validate_sparse_qrom_proxy_contract(contract)
        self.assertIn("contract_digest_mismatch", errors)
        self.assertIn("resource_proxy_mismatch", errors)
        self.assertIn("evidence_class_overclaim", errors)


if __name__ == "__main__":
    unittest.main()
