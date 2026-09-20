from __future__ import annotations

import hashlib
import importlib.metadata
import json
import math
from dataclasses import dataclass

from .qos_d23_explicit_polynomial_candidate import DEGREE, ODD_CHEBYSHEV_COEFFICIENTS

EXPECTED_FINGERPRINT = "4364297169fe219da396c1d663680f474508a03afed93e321dc8e9d8f0bad13a"
PINNED_PACKAGE = "qsppack"
PINNED_VERSION = "0.3.0"
PINNED_METHOD = "Newton"
PINNED_PARITY = 1
PINNED_TARGET_PRE = True
PINNED_PHASE_TYPE = "full"
PINNED_CRITERIA = 1e-12
EXPECTED_PHASE_COUNT = DEGREE + 1


def _dependency_versions() -> dict[str, str | None]:
    """Return exact package provenance without importing heavy dependencies."""
    versions: dict[str, str | None] = {}
    for package in ("qsppack", "numpy", "scipy", "sympy"):
        try:
            versions[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            versions[package] = None
    return versions


def coefficient_fingerprint() -> str:
    payload = json.dumps(
        {
            "degree": DEGREE,
            "odd_chebyshev_coefficients": [float.hex(x) for x in ODD_CHEBYSHEV_COEFFICIENTS],
        },
        sort_keys=True,
        separators=(",", ":"),
    ).encode()
    return hashlib.sha256(payload).hexdigest()


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
    dependency_versions = _dependency_versions()
    installed = dependency_versions[PINNED_PACKAGE]
    if installed is None:
        return {
            "status": "DEPENDENCY_NOT_INSTALLED",
            "contract": contract.__dict__,
            "dependency_versions": dependency_versions,
            "qsp_phase_sequence_synthesized": False,
            "independent_reconstruction_passed": False,
        }
    if installed != PINNED_VERSION:
        return {
            "status": "PINNED_VERSION_MISMATCH",
            "installed_version": installed,
            "contract": contract.__dict__,
            "dependency_versions": dependency_versions,
            "qsp_phase_sequence_synthesized": False,
            "independent_reconstruction_passed": False,
        }

    try:
        import numpy as np
        from qsppack import solve
    except Exception as exc:
        return {
            "status": "DEPENDENCY_IMPORT_EXCEPTION",
            "exception_type": type(exc).__name__,
            "exception_message": str(exc),
            "contract": contract.__dict__,
            "dependency_versions": dependency_versions,
            "qsp_phase_sequence_synthesized": False,
            "independent_reconstruction_passed": False,
        }

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
    except Exception as exc:  # preserve solver failure as research evidence
        return {
            "status": "SYNTHESIS_EXCEPTION",
            "exception_type": type(exc).__name__,
            "exception_message": str(exc),
            "contract": contract.__dict__,
            "dependency_versions": dependency_versions,
            "qsp_phase_sequence_synthesized": False,
            "independent_reconstruction_passed": False,
        }

    # QSPPACK 0.3.0 documents and returns ``value`` but no ``converged`` key.
    # Therefore convergence must be derived from the pinned numeric criterion,
    # while also requiring the degree+1 full phase count and finite phases.
    value = float(info.get("value", float("nan")))
    phase_count = int(len(phases))
    finite_phases = all(math.isfinite(float(x)) for x in phases)
    criterion_met = math.isfinite(value) and value <= PINNED_CRITERIA
    converged = criterion_met and phase_count == EXPECTED_PHASE_COUNT and finite_phases
    return {
        "status": "SYNTHESIS_CONVERGED" if converged else "SYNTHESIS_NOT_CONVERGED",
        "contract": contract.__dict__,
        "dependency_versions": dependency_versions,
        "solver_info": {
            "converged": converged,
            "criterion_met": criterion_met,
            "finite_phases": finite_phases,
            "value": value,
            "iter": int(info.get("iter", -1)),
            "method": str(info.get("method", PINNED_METHOD)),
            "parity": int(info.get("parity", PINNED_PARITY)),
            "targetPre": bool(info.get("targetPre", PINNED_TARGET_PRE)),
            "typePhi": str(info.get("typePhi", PINNED_PHASE_TYPE)),
        },
        "phase_count": phase_count,
        "phases": [float(x) for x in phases] if converged else [],
        "qsp_phase_sequence_synthesized": converged,
        "independent_reconstruction_passed": False,
    }
