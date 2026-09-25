from __future__ import annotations

import cmath
import hashlib
import importlib.metadata
import json
import math
from dataclasses import asdict, dataclass

from .qos_d23_explicit_polynomial_candidate import ODD_CHEBYSHEV_COEFFICIENTS
from .qos_d23_phase_synthesis_contract import EXPECTED_FINGERPRINT

PINNED_PACKAGE = "qsppack"
PINNED_VERSION = "0.4.0"
PINNED_METHOD = "Newton"
PINNED_CRITERIA = 1e-12
EXPECTED_PHASE_COUNT = 82
EXPECTED_PHASE_FINGERPRINT = "268d1809a8d88309df001d2c63b1f78ba5101d2b9e254c304b014ba4e8397445"

# Produced by qsppack 0.4.0 Newton from the unchanged Batch-051 coefficients.
# The repository-owned evaluator below does not import qsppack.
FROZEN_PHASES_V040 = (
    0.6982494260684668, 0.14719190625316722, 0.5961603783867676,
    0.17048654140852598, -0.17106081139786045, 0.15420266099602692,
    -0.04004777380653064, -0.0508582655770187, 0.09711837074579804,
    -0.09168316375417267, 0.050898497094967625, 0.001831305261313484,
    -0.04528323250801944, 0.06630224745997501, -0.06147219264332453,
    0.036280775562968604, -0.0016994943861347819, -0.03021736499655165,
    0.04986869823137824, -0.05233954692385228, 0.03827385065392697,
    -0.013088674389675996, -0.015126320666769185, 0.0380396415634943,
    -0.04919308451456585, 0.045583640592381465, -0.028355657498624173,
    0.0023015958814149593, 0.025532160884366807, -0.04753670509649047,
    0.057253598156563903, -0.050973794984937836, 0.028738851229994488,
    0.005722876941996359, -0.04587159678556929, 0.08342247444449484,
    -0.10963639700753743, 0.11739644490877696, -0.10368993837231158,
    0.07077719220803369, -0.02506533641431317, -0.02506533641431317,
    0.07077719220803369, -0.10368993837231158, 0.11739644490877696,
    -0.10963639700753743, 0.08342247444449484, -0.04587159678556929,
    0.005722876941996359, 0.028738851229994488, -0.050973794984937836,
    0.057253598156563903, -0.04753670509649047, 0.025532160884366807,
    0.0023015958814149593, -0.028355657498624173, 0.045583640592381465,
    -0.04919308451456585, 0.0380396415634943, -0.015126320666769185,
    -0.013088674389675996, 0.03827385065392697, -0.05233954692385228,
    0.04986869823137824, -0.03021736499655165, -0.0016994943861347819,
    0.036280775562968604, -0.06147219264332453, 0.06630224745997501,
    -0.04528323250801944, 0.001831305261313484, 0.050898497094967625,
    -0.09168316375417267, 0.09711837074579804, -0.0508582655770187,
    -0.04004777380653064, 0.15420266099602692, -0.17106081139786045,
    0.17048654140852598, 0.5961603783867676, 0.14719190625316722,
    0.6982494260684668,
)


def phase_fingerprint(phases: tuple[float, ...] = FROZEN_PHASES_V040) -> str:
    payload = json.dumps([float(x).hex() for x in phases], separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def _matmul(a: tuple[complex, complex, complex, complex],
            b: tuple[complex, complex, complex, complex]) -> tuple[complex, complex, complex, complex]:
    return (
        a[0] * b[0] + a[1] * b[2],
        a[0] * b[1] + a[1] * b[3],
        a[2] * b[0] + a[3] * b[2],
        a[2] * b[1] + a[3] * b[3],
    )


def qsp_unitary(x: float, phases: tuple[float, ...] = FROZEN_PHASES_V040) -> tuple[complex, complex, complex, complex]:
    """Repository-owned 2x2 product for the frozen QSP Wx convention."""
    if not math.isfinite(x) or x < -1.0 or x > 1.0:
        raise ValueError("x must be finite and in [-1, 1]")
    if not phases or not all(math.isfinite(p) for p in phases):
        raise ValueError("phases must be finite and nonempty")
    signal_off_diagonal = 1j * math.sqrt(max(0.0, 1.0 - x * x))
    signal = (complex(x), signal_off_diagonal, signal_off_diagonal, complex(x))
    e = cmath.exp(1j * phases[0])
    unitary = (e, 0j, 0j, e.conjugate())
    for phase in phases[1:]:
        e = cmath.exp(1j * phase)
        rotation = (e, 0j, 0j, e.conjugate())
        unitary = _matmul(_matmul(unitary, signal), rotation)
    return unitary


def target_polynomial(x: float) -> float:
    if not math.isfinite(x) or x < -1.0 or x > 1.0:
        raise ValueError("x must be finite and in [-1, 1]")
    angle = math.acos(x)
    return math.fsum(
        coefficient * math.cos((2 * index + 1) * angle)
        for index, coefficient in enumerate(ODD_CHEBYSHEV_COEFFICIENTS)
    )


def qsp_real_response(x: float, phases: tuple[float, ...] = FROZEN_PHASES_V040) -> float:
    return qsp_unitary(x, phases)[0].real


def unitarity_residual(unitary: tuple[complex, complex, complex, complex]) -> float:
    a, b, c, d = unitary
    entries = (
        abs(a.conjugate() * a + c.conjugate() * c - 1.0),
        abs(b.conjugate() * b + d.conjugate() * d - 1.0),
        abs(a.conjugate() * b + c.conjugate() * d),
        abs(b.conjugate() * a + d.conjugate() * c),
    )
    return max(entries)


@dataclass(frozen=True)
class ReconstructionCertificate:
    coefficient_fingerprint: str
    phase_fingerprint: str
    phase_count: int
    grid_points: int
    max_real_residual: float
    residual_argmax_x: float
    max_unitarity_residual: float
    residual_tolerance: float
    unitarity_tolerance: float
    passed: bool
    evidence_level: str


def reconstruct_on_grid(
    grid_points: int = 20_001,
    residual_tolerance: float = 2e-12,
    unitarity_tolerance: float = 2e-13,
    phases: tuple[float, ...] = FROZEN_PHASES_V040,
) -> ReconstructionCertificate:
    if grid_points < 3 or grid_points % 2 == 0:
        raise ValueError("grid_points must be an odd integer >= 3")
    max_residual = -1.0
    argmax = 0.0
    max_unitarity = 0.0
    for index in range(grid_points):
        x = -1.0 + 2.0 * index / (grid_points - 1)
        unitary = qsp_unitary(x, phases)
        residual = abs(unitary[0].real - target_polynomial(x))
        if residual > max_residual:
            max_residual = residual
            argmax = x
        max_unitarity = max(max_unitarity, unitarity_residual(unitary))
    passed = (
        len(phases) == EXPECTED_PHASE_COUNT
        and all(math.isfinite(value) for value in phases)
        and max_residual <= residual_tolerance
        and max_unitarity <= unitarity_tolerance
    )
    return ReconstructionCertificate(
        coefficient_fingerprint=EXPECTED_FINGERPRINT,
        phase_fingerprint=phase_fingerprint(phases),
        phase_count=len(phases),
        grid_points=grid_points,
        max_real_residual=max_residual,
        residual_argmax_x=argmax,
        max_unitarity_residual=max_unitarity,
        residual_tolerance=residual_tolerance,
        unitarity_tolerance=unitarity_tolerance,
        passed=passed,
        evidence_level="INDEPENDENT_NUMERICAL_2X2_RECONSTRUCTION",
    )


def synthesize_with_pinned_qsppack_v040() -> dict[str, object]:
    """Execute the exact 0.4.0 candidate while keeping reconstruction separate."""
    try:
        installed = importlib.metadata.version(PINNED_PACKAGE)
    except importlib.metadata.PackageNotFoundError:
        return {"status": "DEPENDENCY_NOT_INSTALLED", "synthesized": False}
    if installed != PINNED_VERSION:
        return {
            "status": "PINNED_VERSION_MISMATCH",
            "installed_version": installed,
            "synthesized": False,
        }
    try:
        import numpy as np
        from qsppack import solve

        phases, info = solve(
            np.asarray(ODD_CHEBYSHEV_COEFFICIENTS, dtype=float),
            1,
            {
                "method": PINNED_METHOD,
                "criteria": PINNED_CRITERIA,
                "targetPre": True,
                "typePhi": "full",
                "print": False,
                "maxiter": 1000,
            },
        )
    except Exception as exc:
        return {
            "status": "SYNTHESIS_EXCEPTION",
            "exception_type": type(exc).__name__,
            "exception_message": str(exc),
            "synthesized": False,
        }
    frozen = tuple(float(value) for value in phases)
    solver_converged = bool(info.get("converged", False))
    residual = float(info.get("value", math.inf))
    accepted = (
        solver_converged
        and residual <= PINNED_CRITERIA
        and len(frozen) == EXPECTED_PHASE_COUNT
        and all(math.isfinite(value) for value in frozen)
    )
    reconstruction = reconstruct_on_grid(phases=frozen) if accepted else None
    accepted = accepted and reconstruction is not None and reconstruction.passed
    return {
        "status": "SYNTHESIS_CONVERGED" if accepted else "SYNTHESIS_NOT_ACCEPTED",
        "package": PINNED_PACKAGE,
        "version": PINNED_VERSION,
        "method": PINNED_METHOD,
        "criteria": PINNED_CRITERIA,
        "coefficient_fingerprint": EXPECTED_FINGERPRINT,
        "phase_fingerprint": phase_fingerprint(frozen),
        "matches_frozen_phase_fingerprint": phase_fingerprint(frozen) == EXPECTED_PHASE_FINGERPRINT,
        "phase_count": len(frozen),
        "solver_info": {
            "iter": int(info.get("iter", -1)),
            "value": residual,
            "converged": solver_converged,
            "typePhi": str(info.get("typePhi", "")),
        },
        "synthesized": accepted,
        "independent_reconstruction": asdict(reconstruction) if reconstruction is not None else None,
    }
