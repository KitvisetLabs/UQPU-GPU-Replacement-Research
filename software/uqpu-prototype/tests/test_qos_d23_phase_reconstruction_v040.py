import unittest
import importlib.metadata

from uqpu.qos_d23_phase_reconstruction_v040 import (
    EXPECTED_PHASE_FINGERPRINT,
    FROZEN_PHASES_V040,
    phase_fingerprint,
    qsp_real_response,
    reconstruct_on_grid,
    synthesize_with_pinned_qsppack_v040,
    target_polynomial,
)


class QOSD23PhaseReconstructionV040Tests(unittest.TestCase):
    def test_optional_degree_one_odd_parity_dimension_control(self):
        try:
            version = importlib.metadata.version("qsppack")
        except importlib.metadata.PackageNotFoundError:
            self.skipTest("optional qsppack dependency is not installed")
        if version != "0.4.0":
            self.skipTest(f"requires qsppack 0.4.0, found {version}")
        import numpy as np
        from qsppack import solve

        phases, info = solve(
            np.asarray([0.5], dtype=float),
            1,
            {
                "method": "Newton",
                "criteria": 1e-12,
                "targetPre": True,
                "typePhi": "full",
                "print": False,
                "maxiter": 100,
            },
        )
        self.assertEqual(len(phases), 2)
        self.assertTrue(info["converged"])
        self.assertLessEqual(float(info["value"]), 1e-12)

    def test_frozen_phase_vector_is_bound_and_symmetric(self):
        self.assertEqual(len(FROZEN_PHASES_V040), 82)
        self.assertEqual(phase_fingerprint(), EXPECTED_PHASE_FINGERPRINT)
        self.assertEqual(FROZEN_PHASES_V040, tuple(reversed(FROZEN_PHASES_V040)))

    def test_repository_owned_response_matches_key_points(self):
        for x in (-1.0, -0.75, 0.0, 0.75, 1.0):
            self.assertAlmostEqual(qsp_real_response(x), target_polynomial(x), delta=2e-12)

    def test_independent_grid_reconstruction_passes(self):
        certificate = reconstruct_on_grid(grid_points=2_001)
        self.assertTrue(certificate.passed)
        self.assertLessEqual(certificate.max_real_residual, certificate.residual_tolerance)
        self.assertLessEqual(certificate.max_unitarity_residual, certificate.unitarity_tolerance)

    def test_optional_solver_is_fail_closed_or_exactly_reproduces_frozen_phases(self):
        result = synthesize_with_pinned_qsppack_v040()
        if result["status"] in {"DEPENDENCY_NOT_INSTALLED", "PINNED_VERSION_MISMATCH"}:
            self.assertFalse(result["synthesized"])
        else:
            self.assertEqual(result["status"], "SYNTHESIS_CONVERGED")
            self.assertTrue(result["synthesized"])
            self.assertEqual(result["phase_fingerprint"], EXPECTED_PHASE_FINGERPRINT)
            self.assertTrue(result["independent_reconstruction"]["passed"])


if __name__ == "__main__":
    unittest.main()
