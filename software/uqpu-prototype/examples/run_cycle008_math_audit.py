#!/usr/bin/env python3
"""Regenerate the bounded Cycle 008 typed-math/SCM audit artifact."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "software" / "uqpu-prototype"))

from uqpu.cycle008_delta01 import build_cycle008_math_audit  # noqa: E402


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    registry = ROOT / "benchmarks/experiments/cycle008-delta01-typed-math-scm-registry.json"
    generator = Path(__file__).resolve()
    output = ROOT / "benchmarks/results/cycle008-delta01-typed-math-scm-audit.json"

    artifact = build_cycle008_math_audit(json.loads(registry.read_text(encoding="utf-8")))
    artifact["provenance"] = {
        "registry_sha256": sha256(registry),
        "generator_sha256": sha256(generator),
        "generator": "software/uqpu-prototype/examples/run_cycle008_math_audit.py",
        "implementation": "software/uqpu-prototype/uqpu/cycle008_delta01.py",
        "implementation_sha256": sha256(ROOT / "software/uqpu-prototype/uqpu/cycle008_delta01.py"),
        "source_umrl_document": "00E_UNIFIED_MATHEMATICAL_LANGUAGE_AND_DISCOVERY_LEDGER.md",
        "source_umrl_sha256": sha256(ROOT / "00E_UNIFIED_MATHEMATICAL_LANGUAGE_AND_DISCOVERY_LEDGER.md"),
        "source_scm_document": "docs/SCM_LOKATHIBODI_MIND_MENTAL_FACTORS_CONTROL_FORMALISM_V0_1_2026-09-28.md",
        "source_scm_sha256": sha256(ROOT / "docs/SCM_LOKATHIBODI_MIND_MENTAL_FACTORS_CONTROL_FORMALISM_V0_1_2026-09-28.md"),
        "checkpoint_document": "docs/CYCLE008_TYPED_MATH_AND_SCM_STATE_CONTRACT_2026-09-28.md",
        "checkpoint_document_sha256": sha256(ROOT / "docs/CYCLE008_TYPED_MATH_AND_SCM_STATE_CONTRACT_2026-09-28.md"),
        "test_file": "software/uqpu-prototype/tests/test_cycle008_delta01.py",
        "test_file_sha256": sha256(ROOT / "software/uqpu-prototype/tests/test_cycle008_delta01.py"),
    }
    output.write_text(
        json.dumps(artifact, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "output": str(output.relative_to(ROOT)),
        "status": artifact["status"],
        "equations_checked": artifact["dimension_equation_count"],
        "scm_equations": artifact["scm_equation_extensions"]["equation_ids"],
        "provenance": artifact["provenance"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
