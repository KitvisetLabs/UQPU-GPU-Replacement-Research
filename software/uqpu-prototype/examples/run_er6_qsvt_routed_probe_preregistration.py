#!/usr/bin/env python3
"""Emit the frozen ER6 routed-semantics probe preregistration."""

from __future__ import annotations

import json

from uqpu.er6_qsvt_routed_probe_preregistration import build_preregistration


if __name__ == "__main__":
    print(json.dumps(build_preregistration(), indent=2, sort_keys=True))
