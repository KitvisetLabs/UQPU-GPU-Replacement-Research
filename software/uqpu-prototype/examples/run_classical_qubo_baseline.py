from uqpu.baseline_provenance import capture_baseline
from uqpu.optimization_baseline import demo_maxcut_triangle, exact_qubo_baseline


if __name__=="__main__":
    result=exact_qubo_baseline(demo_maxcut_triangle())
    evidence=capture_baseline(
        "combinatorial_optimization",
        result,
        notes="Tiny correctness fixture only; not a competitive CPU/GPU performance baseline.",
    )
    print(evidence.to_json())
