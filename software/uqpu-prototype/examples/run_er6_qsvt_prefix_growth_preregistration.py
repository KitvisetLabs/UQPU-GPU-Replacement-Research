"""Write the frozen eight-query resource-growth preregistration artifact."""

from __future__ import annotations

import json

from uqpu.er6_qsvt_prefix_growth_falsifier import build_preregistration, validate_preregistration


def main() -> int:
    contract = build_preregistration()
    errors = validate_preregistration(contract)
    print(json.dumps(contract, indent=2, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
