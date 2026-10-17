import copy
import json
from pathlib import Path
import unittest

from uqpu.er6_lcu_qsvt_spectral_sector import (
    TOLERANCE,
    build_spectral_sector_contract,
    explicit_two_query_amplitude,
    signal_involution,
    validate_spectral_sector_contract,
)


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "benchmarks/experiments/cycle002-delta01-er6-frozen-contract.json"
ARTIFACT = ROOT / "benchmarks/results/cycle008-delta09-er6-lcu-qsvt-spectral-sector-contract.json"
SDK_ARTIFACT = ROOT / "benchmarks/results/cycle008-delta09-er6-lcu-qsvt-spectral-sector-qiskit.json"


class ER6QSVTSpectralSectorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = json.loads(SOURCE.read_text(encoding="utf-8"))

    def test_committed_contract_is_deterministic_and_valid(self):
        expected = build_spectral_sector_contract(self.source)
        actual = json.loads(ARTIFACT.read_text(encoding="utf-8"))
        self.assertEqual(actual, expected)
        self.assertEqual(validate_spectral_sector_contract(actual), [])

    def test_signal_operator_is_involutory(self):
        for value in (0.0, 1.0 / 9.0, 4.0 / 9.0, 7.0 / 9.0, 1.0):
            u = signal_involution(value)
            self.assertAlmostEqual(u[0][0] * u[0][0] + u[0][1] * u[1][0], 1.0)
            self.assertAlmostEqual(u[0][0] * u[0][1] + u[0][1] * u[1][1], 0.0)

    def test_all_64_sectors_and_acceptance_boundary(self):
        contract = build_spectral_sector_contract(self.source)
        rows = contract["spectral_contract"]["rows"]
        self.assertEqual(len(rows), 64)
        self.assertEqual([row["system_index"] for row in rows], list(range(64)))
        self.assertLessEqual(
            contract["verification"]["explicit_vs_closed_form_max_abs_residual"],
            TOLERANCE,
        )
        self.assertFalse(contract["authorization"]["provider_submission"])

    def test_phase_or_sector_mutation_fails_closed(self):
        contract = build_spectral_sector_contract(self.source)
        mutated = copy.deepcopy(contract)
        mutated["spectral_contract"]["rows"].pop()
        self.assertIn("sector_coverage_mismatch", validate_spectral_sector_contract(mutated))
        self.assertIn("contract_digest_mismatch", validate_spectral_sector_contract(mutated))

    def test_out_of_domain_eigenvalue_rejected(self):
        with self.assertRaises(ValueError):
            explicit_two_query_amplitude(1.0001)

    def test_persisted_sdk_certificate_is_provenance_bound_and_fail_closed(self):
        result = json.loads(SDK_ARTIFACT.read_text(encoding="utf-8"))
        spectral = result["spectral_sector_agreement"]
        contract = json.loads(ARTIFACT.read_text(encoding="utf-8"))
        self.assertTrue(result["passed"])
        self.assertEqual(result["evidence_class"], "SIMULATION_INDEPENDENT_SDK_SPECTRAL_SECTOR_CHECK")
        self.assertEqual(spectral["contract_sha256"], contract["contract_sha256"])
        self.assertEqual(spectral["workload_sectors_checked"], 64)
        self.assertEqual(result["provenance"]["commit"], "14970dc30e5764799ec8aa962aa72eff6fd81a18")
        for key, value in spectral.items():
            if key.endswith("residual"):
                self.assertLessEqual(value, spectral["tolerance"])
        self.assertEqual(result["resources"]["provider_jobs"], 0)
        self.assertEqual(result["resources"]["shots"], 0)
        self.assertIsNone(result["resources"]["provider_cost"])
        self.assertIsNone(result["resources"]["energy_j"])


if __name__ == "__main__":
    unittest.main()
