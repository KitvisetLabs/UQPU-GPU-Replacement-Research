from __future__ import annotations
import json
from pathlib import Path

from .reference_generation import ReferenceGenerationResult


def reference_record(result: ReferenceGenerationResult) -> dict:
    r=result.reference
    return {
        "certificate_id":r.certificate_id,
        "contract_id":r.contract_id,
        "kind":r.kind.value,
        "objective":r.objective,
        "method":r.method,
        "evidence_level":r.evidence_level,
        "source":r.source,
        "notes":r.notes,
        "runtime_seconds":result.runtime_seconds,
        "solver_status":result.solver_status,
        "proven_optimal":result.proven_optimal,
    }


def write_reference_manifest(path: str | Path, results: list[ReferenceGenerationResult]) -> None:
    payload={
        "schema":"uqpu-reference-manifest-v1",
        "references":[reference_record(r) for r in results],
    }
    Path(path).write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n",encoding="utf-8")
