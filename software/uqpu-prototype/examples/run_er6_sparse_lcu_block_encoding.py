"""Emit the workload-derived ER6 LCU block-encoding contract."""

import json
from pathlib import Path

from uqpu.er6_sparse_lcu_block_encoding import build_lcu_contract, validate_lcu_contract


ROOT = Path(__file__).resolve().parents[3]
source = json.loads((ROOT / "benchmarks/experiments/cycle002-delta01-er6-frozen-contract.json").read_text())
contract = build_lcu_contract(source)
errors = validate_lcu_contract(contract)
if errors:
    raise SystemExit(";".join(errors))
print(json.dumps(contract, indent=2, sort_keys=True))
