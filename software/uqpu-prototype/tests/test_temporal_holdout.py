import copy
import math
import unittest

from uqpu.temporal_holdout import validate_temporal_holdout


def _records():
    return [
        {"record_id": "tr-1", "group_id": "time-tr-1", "split": "train",
         "payload": {"timestamp": "2026-01-01T00:00:00Z", "value": 1.0}},
        {"record_id": "tr-2", "group_id": "time-tr-2", "split": "train",
         "payload": {"timestamp": "2026-01-02T00:00:00Z", "value": 2.0}},
        {"record_id": "va-1", "group_id": "time-va-1", "split": "validation",
         "payload": {"timestamp": "2026-01-04T00:00:00Z", "value": 4.0}},
        {"record_id": "va-2", "group_id": "time-va-2", "split": "validation",
         "payload": {"timestamp": "2026-01-05T00:00:00Z", "value": 5.0}},
        {"record_id": "te-1", "group_id": "time-te-1", "split": "test",
         "payload": {"timestamp": "2026-01-08T00:00:00Z", "value": 8.0}},
        {"record_id": "te-2", "group_id": "time-te-2", "split": "test",
         "payload": {"timestamp": "2026-01-09T00:00:00Z", "value": 9.0}},
    ]


class TemporalHoldoutTests(unittest.TestCase):
    def test_strict_order_and_embargo_certificate(self):
        result = validate_temporal_holdout(_records(), embargo_seconds=86400)
        self.assertEqual(result["status"], "PASS")
        self.assertTrue(result["strict_temporal_order"])
        self.assertEqual(result["holdout_unit"], "TIME_BLOCK")
        self.assertEqual(result["split_summary"]["train"]["record_count"], 2)
        self.assertEqual(result["gaps_seconds"]["train_to_validation"], 172800.0)
        self.assertEqual(result["gaps_seconds"]["validation_to_test"], 259200.0)
        self.assertTrue(result["raw_record_binding_verified"])
        self.assertFalse(result["scientific_generalization_verified"])

    def test_certificate_is_deterministic_under_record_reordering(self):
        rows = _records()
        first = validate_temporal_holdout(rows)
        second = validate_temporal_holdout(list(reversed(rows)))
        self.assertEqual(first, second)

    def test_equivalent_timezone_offsets_normalize_to_utc(self):
        rows = _records()
        rows[0]["payload"]["timestamp"] = "2026-01-01T02:00:00+02:00"
        result = validate_temporal_holdout(rows)
        self.assertEqual(
            result["split_summary"]["train"]["start_utc"],
            "2026-01-01T00:00:00+00:00",
        )

    def test_rejects_overlapping_or_out_of_order_partitions(self):
        rows = _records()
        rows[2]["payload"]["timestamp"] = "2026-01-01T12:00:00Z"
        with self.assertRaisesRegex(ValueError, "strictly positive"):
            validate_temporal_holdout(rows)

    def test_rejects_gap_shorter_than_requested_embargo(self):
        rows = _records()
        rows[2]["payload"]["timestamp"] = "2026-01-02T12:00:00Z"
        with self.assertRaisesRegex(ValueError, "below requested embargo"):
            validate_temporal_holdout(rows, embargo_seconds=86400)

    def test_rejects_timezone_naive_timestamps(self):
        rows = _records()
        rows[0]["payload"]["timestamp"] = "2026-01-01T00:00:00"
        with self.assertRaisesRegex(ValueError, "explicit UTC offset"):
            validate_temporal_holdout(rows)

    def test_rejects_malformed_timestamps(self):
        rows = _records()
        rows[0]["payload"]["timestamp"] = "yesterday-ish"
        with self.assertRaisesRegex(ValueError, "valid ISO-8601"):
            validate_temporal_holdout(rows)

    def test_rejects_missing_timestamp_field(self):
        rows = _records()
        rows[0]["payload"].pop("timestamp")
        with self.assertRaisesRegex(ValueError, "must contain timestamp field"):
            validate_temporal_holdout(rows)

    def test_rejects_group_leakage_across_partitions(self):
        rows = _records()
        rows[2]["group_id"] = rows[0]["group_id"]
        with self.assertRaises(ValueError):
            validate_temporal_holdout(rows)

    def test_rejects_empty_partition(self):
        rows = [row for row in _records() if row["split"] != "train"]
        with self.assertRaises(ValueError):
            validate_temporal_holdout(rows)

    def test_rejects_invalid_embargo_values(self):
        for value in (True, -1, math.nan, math.inf):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    validate_temporal_holdout(_records(), embargo_seconds=value)


if __name__ == "__main__":
    unittest.main()
