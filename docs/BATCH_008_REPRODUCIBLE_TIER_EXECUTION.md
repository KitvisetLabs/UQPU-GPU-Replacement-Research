# Eight-Lane Batch 008 — Reproducible Tier Execution

## Purpose
Batch 008 connects the versioned benchmark tiers to executable runner functions and the common benchmark-artifact schema.

## What is now executable
- deterministic generation of small/medium/large MaxCut QUBO contracts;
- measured local greedy baseline execution;
- optional OR-Tools execution when the benchmark dependency is installed;
- stable contract IDs across repeated runs;
- common artifact fields for later CPU/GPU/QPU comparisons.

## Important evidence correction
A heuristic objective is **not automatically accepted as meeting benchmark quality** merely because the runner completed. Its objective must be compared with an established reference or bounded solution. The current artifact note makes this explicit; later evidence gates must compute acceptance from the benchmark contract rather than execution success.

## Next gate
1. install the optional optimized solver in a controlled benchmark environment;
2. execute tier contracts with hardware and solver-version provenance;
3. establish reference/bound objectives;
4. calculate acceptance using the same contract;
5. only then compare GPU, simulator and real-QPU routes.

No quantum advantage or >=100x economic claim follows from this batch.
