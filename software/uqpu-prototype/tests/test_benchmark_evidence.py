import unittest
from uqpu.benchmark_evidence import BenchmarkEvidence, EvidenceKind


class BenchmarkEvidenceTests(unittest.TestCase):
    def test_model_only_cannot_be_verified_win(self):
        r=BenchmarkEvidence("w","p",100,1,True,EvidenceKind.MODEL_ONLY)
        self.assertFalse(r.verified_win)

    def test_real_qpu_quality_and_cost_can_verify_win(self):
        r=BenchmarkEvidence("w","p",100,10,True,EvidenceKind.REAL_QPU)
        self.assertTrue(r.verified_win)
        self.assertFalse(r.verified_100x)

    def test_100x_requires_real_qpu(self):
        r=BenchmarkEvidence("w","p",100,1,True,EvidenceKind.REAL_QPU)
        self.assertTrue(r.verified_100x)

    def test_failed_output_quality_blocks_win(self):
        r=BenchmarkEvidence("w","p",100,0.5,False,EvidenceKind.REAL_QPU)
        self.assertFalse(r.verified_win)


if __name__=="__main__":
    unittest.main()
