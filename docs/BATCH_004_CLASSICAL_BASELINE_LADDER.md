# Eight-Lane Batch 004 — Classical Baseline Ladder

Batch 004 attacks RG-018 without pretending that a tiny Python exhaustive search is a competitive CPU/GPU baseline.

## Baseline ladder

Level 0 — correctness fixture
- deterministic tiny QUBO;
- exact optimum;
- provenance capture;
- guards against accidental exponential scaling.

Level 1 — optimized single-CPU baseline
- established optimization solver;
- repeated trials;
- wall-clock, CPU model, memory and energy/cost assumptions.

Level 2 — competitive multicore/GPU baseline
- tuned solver/implementation appropriate to the workload;
- identical instance set and quality contract;
- measured runtime, host/device memory, data movement and amortized cost.

Level 3 — cloud-QPU/hybrid comparison
- same workload contract;
- input preparation, queue/execution, retries, reconstruction and classical orchestration included;
- real provider billing evidence when authorized.

Only Levels 2–3 are suitable for serious economic-advantage claims.

## Batch 004 artifact
The repository now contains an executable Level-0 QUBO fixture and provenance schema. It establishes correctness plumbing while explicitly leaving RG-018 open for competitive measured baselines.
