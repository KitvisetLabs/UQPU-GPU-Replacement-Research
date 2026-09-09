import unittest

from uqpu.market_snapshot import market_snapshot_2026_09
from uqpu.provider_hardware import RequirementVector, compare_snapshot, rank_known_gaps


class ProviderHardwareGapTests(unittest.TestCase):
    def test_paradigm_prevents_bad_qubit_comparison(self):
        snapshots = market_snapshot_2026_09()
        dwave = next(s for s in snapshots if s.provider_id == "dwave_leap")
        gap = compare_snapshot(dwave, RequirementVector("gate_model", min_physical_qubits=100))
        self.assertFalse(gap.paradigm_match)
        self.assertFalse(gap.meets_known_requirements)

    def test_quantinuum_known_metrics(self):
        q = next(s for s in market_snapshot_2026_09() if s.provider_id == "quantinuum_nexus")
        gap = compare_snapshot(q, RequirementVector(
            "gate_model",
            min_logical_qubits=50,
            min_two_qubit_fidelity=0.999,
        ))
        self.assertTrue(gap.meets_known_requirements)

    def test_unknown_is_not_pass(self):
        ibm = next(s for s in market_snapshot_2026_09() if s.provider_id == "ibm_quantum")
        gap = compare_snapshot(ibm, RequirementVector("gate_model", min_logical_qubits=1))
        self.assertIn("logical_qubits", gap.unknown_fields)
        self.assertFalse(gap.meets_known_requirements)

    def test_ranking_returns_all(self):
        snapshots = market_snapshot_2026_09()
        ranked = rank_known_gaps(snapshots, RequirementVector("gate_model", min_physical_qubits=100))
        self.assertEqual(len(ranked), len(snapshots))


if __name__ == "__main__":
    unittest.main()
