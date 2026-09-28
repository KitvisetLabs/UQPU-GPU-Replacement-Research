"""Generate the Cycle 007 UMRL/SCM machine-unit coverage audit."""

import hashlib
import json
from pathlib import Path

from uqpu.cycle007_delta01 import audit_dimension_contracts


ROOT = Path(__file__).resolve().parents[3]
UMRL_PATH = ROOT / "benchmarks/experiments/cycle006-delta01-unified-math-goal-registry.json"
SCM_PATH = ROOT / "benchmarks/experiments/cycle006-delta01-scm-lokathibodi-math-registry.json"
OUTPUT = ROOT / "benchmarks/results/cycle007-delta01-umrl-dimension-audit.json"


def main() -> int:
    umrl = json.loads(UMRL_PATH.read_text(encoding="utf-8"))
    scm = json.loads(SCM_PATH.read_text(encoding="utf-8"))
    audit = audit_dimension_contracts(umrl, scm)
    audit["source_registries"] = {
        str(UMRL_PATH.relative_to(ROOT)): hashlib.sha256(UMRL_PATH.read_bytes()).hexdigest(),
        str(SCM_PATH.relative_to(ROOT)): hashlib.sha256(SCM_PATH.read_bytes()).hexdigest(),
    }
    OUTPUT.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(OUTPUT.relative_to(ROOT)),
        "variable_declarations": audit["variable_declaration_count"],
        "unit_or_type_coverage": audit["unit_or_type_coverage"],
        "machine_dimension_vector_coverage": audit["machine_dimension_vector_coverage"],
        "dimensional_consistency_claim": audit["dimensional_consistency_claim"],
        "errors": audit["errors"],
    }, indent=2, sort_keys=True))
    return 0 if audit["valid_registry_structure"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
