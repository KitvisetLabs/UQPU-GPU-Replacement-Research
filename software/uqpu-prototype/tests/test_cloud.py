import unittest

from uqpu.cloud import Capability, ExecutionRequirements, ProviderStatus, QuantumParadigm
from uqpu.providers import default_provider_registry


class CloudCompatibilityTests(unittest.TestCase):
    def test_registry_contains_major_clouds(self):
        r = default_provider_registry()
        ids = {p.provider_id for p in r.all()}
        for expected in {"ibm_quantum","aws_braket","azure_quantum","dwave_leap","quantinuum_nexus","pasqal_cloud","quandela_cloud"}:
            self.assertIn(expected, ids)

    def test_gate_requirement_filters_annealer(self):
        r = default_provider_registry()
        results = {x.provider_id:x for x in r.compatible(ExecutionRequirements(QuantumParadigm.GATE_MODEL))}
        self.assertFalse(results["dwave_leap"].compatible)
        self.assertTrue(results["ibm_quantum"].compatible)

    def test_analog_requirement(self):
        r = default_provider_registry()
        results = {x.provider_id:x for x in r.compatible(ExecutionRequirements(QuantumParadigm.ANALOG,{Capability.ANALOG_HAMILTONIAN}))}
        self.assertTrue(results["aws_braket"].compatible)
        self.assertTrue(results["pasqal_cloud"].compatible)

    def test_preview_hidden_by_default(self):
        r = default_provider_registry()
        ids = {x.provider_id for x in r.compatible(ExecutionRequirements(QuantumParadigm.GATE_MODEL))}
        self.assertNotIn("quantum_circuits_azure", ids)

    def test_preview_visible_when_requested(self):
        r = default_provider_registry()
        ids = {x.provider_id for x in r.compatible(ExecutionRequirements(QuantumParadigm.GATE_MODEL), active_only=False)}
        self.assertIn("quantum_circuits_azure", ids)
