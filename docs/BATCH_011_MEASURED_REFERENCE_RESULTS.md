# Batch 011 Measured Reference Benchmark Results

**GitHub Actions run:** 34374036120  
**Benchmark job:** reference-benchmark  
**Conclusion:** SUCCESS

## Environment
- Python: 3.12.14
- OR-Tools: 9.14.6206
- Machine: x86_64
- Platform: Linux-6.17.0-1022-azure-x86_64-with-glibc2.39

## Results

| Tier | Contract ID | Objective | Solver status | Runtime | Proven optimal | Certificate |
|---|---|---:|---|---:|---|---|
| small | 8e478d5edde63daa | -65.0 | FEASIBLE | 30.002208606 s | false | d0d77e3eaa0c7f268b74 |
| medium | 2ec80fa696739a17 | -433.0 | FEASIBLE | 45.003255759 s | false | cf2ff748d97c17d5520d |

## Evidence interpretation

Both results are **MEASURED_LOCAL / BEST_KNOWN_FEASIBLE** references generated on a GitHub-hosted CPU runner.

Neither result is an exact optimum certificate because OR-Tools did not report `OPTIMAL` within the configured time limits.

Therefore:
- these objectives may be used as best-known feasible comparison values;
- they must **not** be used as proof of the true optimality gap;
- they do not close RG-024;
- they provide the first controlled hosted execution evidence for RG-025.

## Next experiments
1. increase/parameterize time limits in a dedicated non-default benchmark run;
2. test stronger formulations or symmetry breaking;
3. extract or add rigorous lower bounds where available;
4. consider specialized MaxCut/MIP/branch-and-bound solvers for reference generation;
5. preserve the same contract IDs while comparing improvements.

No GPU/QPU advantage claim follows from these results.
