# Lane A — First Verified Win Workload Program

Priority #1 is to obtain the first reproducible workload where a current cloud-QPU/hybrid path satisfies the same useful output contract as a competitive classical baseline and can be measured end-to-end.

Initial candidate classes:
1. combinatorial optimization;
2. Monte-Carlo-like estimation;
3. structured linear-algebra subroutines where only observables are required;
4. stateful workflows where large classical materialization can be avoided.

The project MUST NOT count a speedup on an internal kernel as success unless input preparation, output reconstruction, retries/error mitigation, host orchestration and provider billing are included.

Acceptance sequence:
```text
contract -> classical baseline -> quantum/hybrid formulation
-> simulator/dry-run -> cloud execution when authorized
-> output-quality validation -> total cost/useful-task
-> reproducibility artifact -> evidence label
```

The first verified win is expected to be narrow. Expansion to broader CPU/GPU/RAM/VRAM/storage coverage follows workload by workload.
