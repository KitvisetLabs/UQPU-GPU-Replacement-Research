import unittest

from uqpu.external_benchmark_provenance import (
    llm_srbench_public_count_certificate,
    reconcile_benchmark_counts,
)


class ExternalBenchmarkProvenanceTests(unittest.TestCase):
    def test_generic_count_reconciliation(self):
        cert = reconcile_benchmark_counts(
            declared_total=3,
            split_counts={"a": 1, "b": 2},
        )
        self.assertTrue(cert["consistent"])
        self.assertEqual(cert["delta"], 0)

    def test_llm_srbench_public_metadata_is_240_not_239(self):
        cert = llm_srbench_public_count_certificate()
        self.assertEqual(cert["declared_total"], 239)
        self.assertEqual(cert["observed_total"], 240)
        self.assertEqual(cert["delta"], 1)
        self.assertFalse(cert["consistent"])
        self.assertEqual(cert["split_counts"]["lsr_synth_phys_osc"], 44)
        self.assertFalse(cert["official_dataset_bytes_accessed"])
        self.assertFalse(cert["external_execution_completed"])
        self.assertFalse(cert["fabricate_239_task_slice"])


if __name__ == "__main__":
    unittest.main()
