from __future__ import annotations

import importlib.metadata
from dataclasses import dataclass

from .qos_d23_explicit_polynomial_candidate import ODD_CHEBYSHEV_COEFFICIENTS
from .qos_d23_exact_bernstein_certificate import coefficient_fingerprint

EXPECTED_FINGERPRINT = "4364297169fe219da396c1d663680f474508a03afed93e321dc8e9d8f0bad13a"
PINNED_PACKAGE = "qsppack"
PINNED_VERSION = "0.3.0"
PINNED_METHOD = "Newton"
PINNED_PARITY = 1
PINNED_TARGET_PRE = True
PINNED_PHASE_TYPE = "full"
PINNED_CRITERIA = 1e-12


@dataclass(frozen=True)
class PhaseSynthesisContract:
    package: str
    version: str
    method: str
    parity: int
    target_pre: bool
    phase_type: str
    criteria: float
    coefficient_fingerprint: str

    @property
    def fingerprint_matches_batch051(self) -> bool:
        return self.coefficient_fingerprint == EXPECTED_FINGERPRINT


def frozen_contract() -> PhaseSynthesisContract:
    return PhaseSynthesisContract(
        package=PINNED_PACKAGE,
        version=PINNED_VERSION,
        method=PINNED_METHOD,
        parity=PINNED_PARITY,
        target_pre=PINNED_TARGET_PRE,
        phase_type=PINNED_PHASE_TYPE,
        criteria=PINNED_CRITERIA,
        coefficient_fingerprint=EXPECTED_FINGERPRINT,
    )


def synthesize_with_pinned_qsppack() -> dict[str, object]:
    """Attempt the pinned external synthesis; preserve missing/version/failure states.

    This is deliberately separate from the independent reconstruction gate. A
    successful solver return is numerical synthesis evidence, not a theorem or
    hardware result.
    """
    contract = frozen_contract()
    runtime_fingerprint = coefficient_fingerprint()
    if runtime_fingerprint != EXPECTED_FINGERPRINT:
        return {
            "status": "COEFFICIENT_FINGERPRINT_MISMATCH",
            "runtime_coefficient_fingerprint": runtime_fingerprint,
            "contract": contract.__dict__,
            "qsp_phase_sequence_synthesized": False,
            "independent_reconstruction_passed": False,
        }
    try:
        installed = importlib.metadata.version(PINNED_PACKAGE)
    except importlib.metadata.PackageNotFoundError:
        return {
            "status": "DEPENDENCY_NOT_INSTALLED",
            "contract": contract.__dict__,
            "qsp_phase_sequence_synthesized": False,
            "independent_reconstruction_passed": False,
        }
    if installed != PINNED_VERSION:
        return {
            "status": "PINNED_VERSION_MISMATCH",
            "installed_version": installed,
            "contract": contract.__dict__,
            "qsp_phase_sequence_synthesized": False,
            "independent_reconstruction_passed": False,
        }

    import numpy as np
    from qsppack import solve

    coefficients = np.asarray(ODD_CHEBYSHEV_COEFFICIENTS, dtype=float)
    options = {
        "method": PINNED_METHOD,
        "criteria": PINNED_CRITERIA,
        "targetPre": PINNED_TARGET_PRE,
        "typePhi": PINNED_PHASE_TYPE,
        "print": False,
    }
    try:
        phases, info = solve(coefficients, PINNED_PARITY, options)
    except Exception as exc:
        return {
            "status": "SYNTHESIS_EXCEPTION",
            "exception_type": type(exc).__name__,
            "exception_message": str(exc),
            "contract": contract.__dict__,
            "qsp_phase_sequence_synthesized": False,
            "independent_reconstruction_passed": False,
        }

    converged = bool(info.get("converged", False))
    return {
        "status": "SYNTHESIS_CONVERGED" if converged else "SYNTHESIS_NOT_CONVERGED",
        "contract": contract.__dict__,
        "solver_info": {
            "converged": converged,
            "value": float(info.get("value", float("nan"))),
            "iter": int(info.get("iter", -1)),
            "method": str(info.get("method", PINNED_METHOD)),
            "parity": int(info.get("parity", PINNED_PARITY)),
            "targetPre": bool(info.get("targetPre", PINNED_TARGET_PRE)),
            "typePhi": str(info.get("typePhi", PINNED_PHASE_TYPE)),
        },
        "phase_count": int(len(phases)),
        "phases": [float(x) for x in phases] if converged else [],
        "qsp_phase_sequence_synthesized": converged,
        "independent_reconstruction_passed": False,
    }
