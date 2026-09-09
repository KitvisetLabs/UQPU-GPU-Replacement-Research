import unittest

from uqpu.cloud import ExecutionRequirements, QuantumParadigm
from uqpu.provider_adapters import ADAPTERS, adapter_for, adapter_health_matrix
from uqpu.provider_runtime import RuntimeConfig, SubmissionGuard


EXPECTED = {
    "ibm_quantum","aws_braket","azure_quantum","ionq_direct","rigetti_qcs",
    "dwave_leap","iqm_resonance","quantinuum_nexus","pasqal_cloud",
    "quera","quandela_cloud","oqc_cloud",
}


class ProviderAdapterTests(unittest.TestCase):
    def test_all_seed_direct_providers_have_adapter(self):
        self.assertTrue(EXPECTED.issubset(set(ADAPTERS)))

    def test_every_adapter_can_discover_and_dry_run_without_vendor_sdk(self):
        req = ExecutionRequirements(QuantumParadigm.GATE_MODEL)
        for pid in EXPECTED:
            adapter = adapter_for(pid, RuntimeConfig(pid, target="test-target", shots=100))
            self.assertEqual(adapter.discover().provider_id, pid)
            lowered = adapter.lower({"program": "portable"}, req)
            dry = adapter.dry_run(lowered)
            self.assertEqual(dry["provider_id"], pid)
            self.assertEqual(dry["status"], "DRY_RUN_ONLY")

    def test_paid_execution_guard_rejects_without_explicit_consent(self):
        with self.assertRaises(PermissionError):
            SubmissionGuard(paid_execution=True, explicit_consent=False).assert_allowed()

    def test_paid_execution_guard_accepts_explicit_consent(self):
        SubmissionGuard(paid_execution=True, explicit_consent=True, max_budget_usd=1).assert_allowed()

    def test_health_matrix_complete(self):
        ids={x.provider_id for x in adapter_health_matrix()}
        self.assertEqual(ids, EXPECTED)


if __name__ == "__main__":
    unittest.main()
