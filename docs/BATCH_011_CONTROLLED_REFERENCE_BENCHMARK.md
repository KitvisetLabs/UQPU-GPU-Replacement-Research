# Eight-Lane Batch 011 — Controlled Reference Benchmark

## Priority #1 advance
Batch 011 creates a dedicated GitHub Actions benchmark job that is separate from the dependency-light core test matrix.

The benchmark job:
- uses Python 3.12;
- installs the prototype normally;
- installs a pinned optional benchmark dependency: `ortools==9.14.6206`;
- executes the current small and medium MaxCut/QUBO contracts;
- emits environment provenance including Python, OR-Tools, platform, machine, GitHub run ID and commit SHA;
- emits certificate records containing contract ID, objective, runtime, solver status and proof strength.

## Evidence rule
A solver result marked `OPTIMAL` may generate an `EXACT_OPTIMUM` certificate. A merely feasible result remains `BEST_KNOWN_FEASIBLE`.

The benchmark is still a CPU reference-generation experiment, not a GPU baseline and not quantum evidence.

## Integration
A/F: closes part of RG-025 with a reproducible hosted benchmark path.
B: the same contract IDs remain available for simulator/cloud-QPU routing.
C: state/memory/transfer measurements remain required for later end-to-end comparison.
D/G: process-window research continues in parallel.
E: functional-unit material economics continues in parallel.
H: strategic stage-gating continues in parallel.

No paid QPU execution occurs in this job.
