# Eight-Lane Batch 007 — Optimized Baseline Adapter and CI Hardening

## CI repair
The GitHub Actions failure was traced to stale invariant tests, not Python 3.11/3.12.

The old test still expected:
- a legacy mission marker;
- invariants only through INV-018;
- the obsolete six-lane operating-system phrase.

The project is now A–H with INV-024. CI was hardened to:
- compare invariant IDs from the charter against VERSION_INVARIANTS instead of hard-coding a fragile numeric range;
- require the current eight-lane bootstrap;
- check Lane A through Lane H;
- update GitHub Actions to current Node-24-compatible major versions.

## Competitive-baseline path
Batch 007 adds an optional OR-Tools CP-SAT QUBO adapter.

This is not installed by default. The core remains lightweight. When OR-Tools is available, binary quadratic terms are linearized with auxiliary Boolean variables and solved under an explicit time limit.

## Benchmark artifact
A common artifact schema now records:
- benchmark contract ID;
- implementation/solver class;
- objective/acceptance;
- runtime;
- evidence level;
- provider/backend or hardware when applicable;
- memory/data-transfer/energy/cost measurements when actually known.

Missing values remain null.

## Evidence boundary
An optimized classical solver is a prerequisite for credible comparison, not evidence of quantum advantage. GPU and real-QPU measurements remain future gates.
