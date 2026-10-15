"""Regenerate the deterministic Cycle 008 Delta 02 checkpoint."""
import json
from pathlib import Path

from uqpu.cycle008_delta02 import build_integrated_checkpoint


ROOT = Path(__file__).resolve().parents[3]
target = ROOT / "benchmarks/results/cycle008-delta02-integrated-gates.json"
target.write_text(json.dumps(build_integrated_checkpoint(), indent=2) + "\n", encoding="utf-8")
print(target)
