import struct
import tempfile
import unittest
from pathlib import Path

from uqpu.cycle014_delta01 import (
    LANES, ai_lineage_manifest, covariance_product_dimension, custody_expiry_boundary,
    fictional_transcript, matched_output_contract, model_interval_grid,
    provider_receipt_envelope, qos_certificate_v4, rank_stability_bounds,
    rational_interval_add, run_cycle014_fixture, subprocess_replace_boundary,
    zip64_metadata_gate,
)
from uqpu.cycle013_delta01 import canonical_hash


class Cycle014Tests(unittest.TestCase):
    def test_a_matched_output_contract_binds_workload_and_result(self):
        workload = {
            "workload_id": "task-1", "baseline": "exact-classical",
            "accepted_output": "objective", "output_unit": "integer",
            "max_states": 32, "seed": 0,
        }
        result = matched_output_contract(workload, {"objective": 18})
        self.assertEqual(result["baseline"], "exact-classical")
        self.assertIsNone(result["scaling_claim"])
        with self.assertRaises(ValueError):
            matched_output_contract({**workload, "max_states": True}, {"objective": 18})
        with self.assertRaises(ValueError):
            matched_output_contract(workload, {"objective": float("nan")})

    def test_b_receipt_keeps_unexecuted_job_and_invoice_null(self):
        request = canonical_hash({"request": "fixture"})
        receipt = {"schema": "receipt-v1", "request_sha256": request, "provider_status": "NOT_EXECUTED",
                   "job_id": None, "invoice": None}
        self.assertIsNone(provider_receipt_envelope(request, receipt)["invoice"])
        with self.assertRaises(ValueError):
            provider_receipt_envelope(request, {**receipt, "request_sha256": "0" * 64})
        with self.assertRaises(ValueError):
            provider_receipt_envelope(request, {**receipt, "provider_status": "NOT_EXECUTED", "job_id": "made-up"})

    def test_c_subprocess_termination_preserves_complete_old_or_new_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "payload.bin"
            target.write_bytes(b"old-complete")
            before = subprocess_replace_boundary(root, target.name, b"new-complete", "before_replace")
            self.assertEqual(before["visible"], b"old-complete")
            self.assertEqual(before["status"], "OLD_COMPLETE")
            active = list(root.glob(".payload.bin.tmp.active.*"))
            self.assertEqual(len(active), 1)
            active[0].unlink()
            after = subprocess_replace_boundary(root, target.name, b"new-complete", "after_replace")
            self.assertEqual(after["visible"], b"new-complete")
            self.assertEqual(after["status"], "NEW_COMPLETE")
            self.assertEqual(after["durability"], "PROCESS_TERMINATION_ONLY")

    def test_d_zip64_metadata_width_locator_and_comment_are_exact(self):
        zip64 = struct.pack("<4sQHHIIQQQQ", b"PK\x06\x06", 44, 45, 45, 0, 0, 1, 1, 60, 100)
        locator = struct.pack("<4sIQI", b"PK\x06\x07", 0, 100, 1)
        eocd = struct.pack("<4sHHHHIIH", b"PK\x05\x06", 0, 0, 1, 1, 60, 100, 3) + b"abc"
        result = zip64_metadata_gate(zip64, locator, eocd, 100, 156, 176)
        self.assertEqual(result["eocd_comment_bytes"], 3)
        self.assertFalse(result["payload_read"])
        with self.assertRaises(ValueError):
            zip64_metadata_gate(zip64, locator, eocd[:-1], 100, 156, 176)
        with self.assertRaises(ValueError):
            zip64_metadata_gate(zip64[:-1], locator, eocd, 100, 155, 175)
        bad_locator = struct.pack("<4sIQI", b"PK\x06\x07", 0, 101, 1)
        with self.assertRaises(ValueError):
            zip64_metadata_gate(zip64, bad_locator, eocd, 100, 156, 176)

    def test_e_custody_expiry_is_compared_to_injected_date(self):
        self.assertEqual(custody_expiry_boundary({"expiry": "2030-01-01"}, "2026-09-28")["valid"], True)
        self.assertEqual(custody_expiry_boundary({"expiry": "2026-09-28"}, "2026-09-28")["valid"], False)
        with self.assertRaises(ValueError):
            custody_expiry_boundary({"expiry": "yesterday"}, "2026-09-28")

    def test_f_interval_grid_keeps_nonpositive_outputs_null(self):
        rows = model_interval_grid([7, 12], [1, 2, 4, 0, -1])
        self.assertEqual(rows[1]["per_output_usd"], [3.5, 6.0])
        self.assertIsNone(rows[3]["per_output_usd"])
        with self.assertRaises(ValueError):
            model_interval_grid([12, 7], [1])

    def test_g_covariance_dimension_is_pairwise_product(self):
        velocity = [1, 0, -1, 0, 0, 0, 0]
        time = [0, 0, 1, 0, 0, 0, 0]
        self.assertEqual(covariance_product_dimension(velocity, time), [1, 0, 0, 0, 0, 0, 0])
        with self.assertRaises(ValueError):
            covariance_product_dimension([1, 0, 0], time)

    def test_h_rank_stability_grid_is_not_capital_advice(self):
        result = rank_stability_bounds(["a", "b"], [["a", "b"], ["b", "a"], ["a", "b"]])
        self.assertEqual(result["stability_bounds"], [2 / 3, 2 / 3])
        self.assertIsNone(result["capital"])
        with self.assertRaises(ValueError):
            rank_stability_bounds(["a", "b"], [["a", "c"]])

    def test_fnd_rational_interval_add_preserves_sort_and_source(self):
        source = {"unit": "1", "dimension": [0] * 10, "domain_sort": "RealModel",
                  "evidence_sort": "Model", "source_sha256": "a" * 64}
        result = rational_interval_add({**source, "lower": [1, 2], "upper": [3, 2]},
                                       {**source, "lower": [1, 4], "upper": [1, 2]})
        self.assertEqual(result["lower"], [3, 4])
        self.assertEqual(result["upper"], [2, 1])
        fic = {**source, "domain_sort": "Fiction", "evidence_sort": "Fiction",
               "lower": [0, 1], "upper": [1, 1]}
        empirical = {**source, "lower": [0, 1], "upper": [1, 1]}
        with self.assertRaises(ValueError):
            rational_interval_add(fic, empirical)
        with self.assertRaises(ValueError):
            rational_interval_add({**source, "lower": [0, 1], "upper": [1, 1]},
                                  {**source, "source_sha256": "b" * 64, "lower": [0, 1], "upper": [1, 1]})

    def test_scm_fictional_challenge_needs_fresh_scoped_consent(self):
        consent = {"fiction_only": True, "empirical_coupling": None, "seen": set(), "scope": "scene-1",
                   "active": True, "expires_at": "2030-01-01"}
        self.assertEqual(fictional_transcript(consent, "n1", "scene-1", "q", "q", "2026-09-28")["sort"], "Fiction")
        for args in (({**consent, "seen": {"n1"}}, "n1", "scene-1", "q", "q", "2026-09-28"),
                     (consent, "n2", "wrong-scope", "q", "q", "2026-09-28"),
                     (consent, "n2", "scene-1", "q", "wrong", "2026-09-28"),
                     ({**consent, "expires_at": "2020-01-01"}, "n2", "scene-1", "q", "q", "2026-09-28"),
                     ({**consent, "active": False}, "n2", "scene-1", "q", "q", "2026-09-28")):
            with self.assertRaises(ValueError):
                fictional_transcript(*args)
        with self.assertRaises(ValueError):
            fictional_transcript({**consent, "empirical_coupling": True}, "n2", "scene-1", "q", "q", "2026-09-28")

    def test_ai_cost_manifest_binds_source_splits_metrics_and_config(self):
        splits = {"train": ["t1"], "validation": ["v1"], "test": ["x1"]}
        metrics = {"train": {"loss": 1}, "validation": {"loss": 1.1}, "test": {"loss": 1.2}}
        config = {"optimizer": "fixture", "seed": 0}
        manifest = ai_lineage_manifest(b"model-v4", splits, metrics, config)
        self.assertEqual(manifest["version"], 4)
        self.assertNotEqual(manifest["config_sha256"], ai_lineage_manifest(b"model-v4", splits, metrics, {"optimizer": "other"})["config_sha256"])
        with self.assertRaises(ValueError):
            ai_lineage_manifest(b"model-v4", {"train": ["x"], "validation": ["x"], "test": ["z"]}, metrics, config)
        with self.assertRaises(ValueError):
            ai_lineage_manifest(b"model-v4", splits, {**metrics, "test": {"loss": float("inf")}}, config)

    def test_qos_v4_certificate_binds_map_and_resource_values(self):
        previous = {"qubits": 6, "bits": 6, "depth": 16, "gates": 34}
        resources = {"qubits": 6, "bits": 6, "depth": 14, "gates": 30}
        cert = qos_certificate_v4(b"source-v4", {"map": "v4"}, resources, previous)
        self.assertEqual(cert["version"], 4)
        self.assertEqual(cert["resources"], resources)
        self.assertIsNone(cert["hardware"])
        with self.assertRaises(ValueError):
            qos_certificate_v4(b"source-v4", {"map": "v4"}, {**resources, "gates": True}, previous)
        with self.assertRaises(ValueError):
            qos_certificate_v4(b"source-v4", {"map": "v4"}, {**resources, "depth": 17}, previous)

    def test_integrated_fixture_advances_all_twelve_lanes(self):
        result = run_cycle014_fixture()
        self.assertEqual(set(result), set(LANES))
        self.assertTrue(all(result[lane] is not None for lane in LANES))
        self.assertEqual(result["A"]["evidence_class"], "LOCAL_EXACT_CLASSICAL_FIXTURE")
        self.assertIsNone(result["B"]["invoice"])
        self.assertIsNone(result["QOS/QSVT"]["hardware"])


if __name__ == "__main__":
    unittest.main()
