import json
from pathlib import Path
import unittest


CONTRACT_PATH = (
    Path(__file__).resolve().parents[3]
    / "research_lanes"
    / "A_quantum_programming_runtime"
    / "RAG_CONTEXT_SELECTION_CONTRACT_2026-10-29.json"
)


class RAGContextSelectionContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with CONTRACT_PATH.open(encoding="utf-8") as stream:
            cls.contract = json.load(stream)

    def test_contract_is_preregistered_and_source_scoped(self):
        self.assertEqual(self.contract["schema_version"], 1)
        self.assertEqual(self.contract["status"], "PREREGISTERED_NOT_RUN")
        self.assertEqual(
            self.contract["source"]["url"],
            "https://arxiv.org/abs/2610.37033",
        )
        self.assertFalse(self.contract["source"]["independently_reproduced_by_uqpu"])

    def test_classical_quantum_and_reference_baselines_are_separate(self):
        methods = self.contract["methods"]
        for name in (
            "brute_force_exact_small",
            "cpu_classical",
            "gpu_classical",
            "p_dcim_silicon",
            "p_dcim_behavioral_model",
            "qaoa_simulator",
            "real_qpu_or_dwave",
        ):
            with self.subTest(method=name):
                self.assertIn(name, methods)
        self.assertEqual(methods["p_dcim_behavioral_model"]["evidence_class"], "MODEL_ONLY")
        self.assertTrue(methods["p_dcim_behavioral_model"]["never_promote_to_silicon_measurement"])
        self.assertTrue(methods["p_dcim_silicon"]["require_direct_on_chip_instance"])

    def test_output_quality_and_manifest_hashes_are_frozen_before_run(self):
        workload = self.contract["workload"]
        self.assertIn("qubo_manifest_sha256", workload["required_hashes_before_run"])
        self.assertIn("acceptance_contract_sha256", workload["required_hashes_before_run"])
        acceptance = self.contract["acceptance"]
        self.assertEqual(acceptance["status"], "THRESHOLDS_MUST_BE_PREREGISTERED_BEFORE_RUN")
        self.assertIn("exact_match", acceptance["quality_metrics"])
        self.assertIn("token_f1", acceptance["quality_metrics"])
        self.assertIn("same model, prompt, decoding and token limits", " ".join(acceptance["constraints"]))

    def test_unknown_costs_and_paid_qpu_execution_fail_closed(self):
        rules = self.contract["evidence_rules"]
        self.assertFalse(rules["unknown_cost_or_energy_is_zero"])
        self.assertFalse(rules["cross_provider_probability_price_mixing_allowed"])
        self.assertTrue(rules["external_infrastructure_must_be_counted_for_inv029"])
        hardware = self.contract["methods"]["real_qpu_or_dwave"]
        self.assertTrue(hardware["requires_credentials"])
        self.assertTrue(hardware["requires_explicit_user_consent"])
        self.assertTrue(hardware["requires_bounded_budget"])
        self.assertFalse(hardware["paid_submission_allowed_now"])

    def test_source_metrics_are_not_promoted_to_uqpu_evidence(self):
        metrics = self.contract["source_reported_metrics_not_uqpu_results"]
        self.assertEqual(metrics["status"], "SOURCE_REPORTED_ONLY_NOT_INDEPENDENTLY_REPRODUCED")
        self.assertIn("not complete system energy", metrics["selection_energy_boundary"])
        self.assertEqual(
            self.contract["methods"]["p_dcim_behavioral_model"]["evidence_class"],
            "MODEL_ONLY",
        )


if __name__ == "__main__":
    unittest.main()
