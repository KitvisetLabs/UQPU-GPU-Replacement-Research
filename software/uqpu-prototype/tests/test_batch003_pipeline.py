import unittest

from uqpu.benchmark_evidence import BenchmarkEvidence, EvidenceKind
from uqpu.benchmark_pipeline import BenchmarkRunPlan, evaluate_gate
from uqpu.provider_fit import rank_provider_fits
from uqpu.state_accounting import StateAccounting, materialization_reduction_ratio
from uqpu.workload_contracts import first_verified_win_candidates
from uqpu.cloud import QuantumParadigm


class Batch003Tests(unittest.TestCase):
    def test_provider_fit_prioritizes_matching_paradigm(self):
        c=first_verified_win_candidates()[0]
        rows=rank_provider_fits(c,{"dwave":QuantumParadigm.ANNEALING,"x":QuantumParadigm.PHOTONIC})
        self.assertEqual(rows[0].provider_id,"dwave")

    def test_materialization_reduction(self):
        c=StateAccounting(100,900,100,100,transfer_bytes=200)
        q=StateAccounting(100,100,100,100,transfer_bytes=100)
        self.assertGreater(materialization_reduction_ratio(c,q),0.5)

    def test_simulation_never_passes_verified_gate(self):
        c=first_verified_win_candidates()[0]
        plan=BenchmarkRunPlan(c,"test","sim",100,StateAccounting(1,1,1,0),StateAccounting(1,0,1,0))
        ev=BenchmarkEvidence(c.workload_id,"test",1.0,0.001,True,EvidenceKind.SIMULATION)
        gate=evaluate_gate(plan,ev)
        self.assertFalse(gate.economic_win)
        self.assertFalse(gate.verified_100x)

    def test_real_qpu_100x_gate(self):
        c=first_verified_win_candidates()[0]
        plan=BenchmarkRunPlan(c,"test","qpu",100,StateAccounting(1,1,1,0),StateAccounting(1,0,1,0))
        ev=BenchmarkEvidence(c.workload_id,"test",1.0,0.01,True,EvidenceKind.REAL_QPU)
        gate=evaluate_gate(plan,ev)
        self.assertTrue(gate.verified_100x)


if __name__=="__main__":
    unittest.main()
