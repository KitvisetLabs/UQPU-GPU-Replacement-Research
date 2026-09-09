from __future__ import annotations
import json
import os
import platform
import sys
from importlib.metadata import version

from uqpu.benchmark_tiers import representative_tiers
from uqpu.reference_generation import generate_ortools_reference
from uqpu.reference_manifest import reference_record


def main() -> int:
    tiers={t.name:t for t in representative_tiers()}
    specs=(("small",30.0),("medium",45.0))
    records=[]
    for name,limit in specs:
        result=generate_ortools_reference(tiers[name],time_limit_seconds=limit,workers=1)
        records.append(reference_record(result))
    payload={
        "schema":"uqpu-reference-benchmark-run-v1",
        "environment":{
            "python":sys.version.split()[0],
            "ortools":version("ortools"),
            "platform":platform.platform(),
            "machine":platform.machine(),
            "processor":platform.processor() or "unknown",
            "github_runner_os":os.getenv("RUNNER_OS"),
            "github_run_id":os.getenv("GITHUB_RUN_ID"),
            "github_sha":os.getenv("GITHUB_SHA"),
        },
        "references":records,
    }
    print(json.dumps(payload,indent=2,sort_keys=True))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
