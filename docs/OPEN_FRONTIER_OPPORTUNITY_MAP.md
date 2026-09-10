# Open-Frontier Opportunity Map for the 100M-Unit Moonshot

Date: 2026-09-10  
Status: Living research map  
Evidence boundary: this document ranks research directions; it does not claim the 100,000,000-unit or 100,000,000x targets are achieved.

## Tier 1 — Established quantum-computing mechanisms worth aggressive testing

### Structured exponential/super-polynomial algorithmic advantage
Examples include period finding/factoring and selected hidden-structure problems. These routes are the strongest known conceptual path to replacing an enormous conventional compute fleet with one logical quantum system because the advantage can grow much faster than a constant-factor hardware improvement.

Constraint: advantage is workload-specific. It does not imply a universal 100M-GPU or 100M-CPU replacement.

Primary reference: P. W. Shor, “Algorithms for quantum computation: discrete logarithms and factoring,” FOCS 1994, DOI 10.1109/SFCS.1994.365700.

### Quantum simulation
Quantum systems can represent and evolve quantum states natively. This is a high-priority candidate where classical memory/compute requirements can scale exponentially with simulated system size.

Research question: identify useful outputs that are compact observables rather than requiring full classical reconstruction of the quantum state.

### Amplitude estimation / quadratic sampling advantage
Quantum amplitude-estimation families can reduce sample complexity for selected estimation problems. Quadratic speedups alone are unlikely to guarantee a 100M-unit replacement at arbitrary scale, but may combine with large workload size, expensive classical samples and favorable QPU economics.

### Quantum walks / search
Grover-type unstructured search gives a quadratic query advantage, O(sqrt(N)) rather than O(N). This is important but also a warning: quantum computing is not automatically exponentially faster for every search problem.

References: L. K. Grover, arXiv:quant-ph/9605043; Bennett, Bernstein, Brassard and Vazirani, SIAM J. Comput. 26 (1997), DOI 10.1137/S0097539796300933.

### Quantum linear algebra with compressed outputs
HHL-like algorithms can be powerful when matrices are suitably structured, state preparation is efficient and the desired answer is an observable rather than a full classical vector.

Constraint: loading arbitrary classical data and reading a complete N-dimensional answer can destroy the nominal asymptotic advantage.

Reference: Harrow, Hassidim and Lloyd, Phys. Rev. Lett. 103, 150502 (2009), DOI 10.1103/PhysRevLett.103.150502.

## Tier 2 — Architecture routes that may amplify useful advantage

- fault-tolerant logical qubits and lower-overhead QEC;
- bosonic/error-biased encodings;
- topological protection if experimentally scalable;
- photonic quantum computing and multiplexed photonic interconnects;
- neutral-atom and trapped-ion architectures with high connectivity;
- analog quantum simulation for physics/materials workloads;
- quantum-classical decomposition that keeps only the provably advantageous kernel on the QPU;
- circuit cutting, dynamic circuits and mid-circuit measurement where they reduce total cost rather than merely moving overhead;
- error mitigation only when the added shots/classical processing improve cost per accepted useful output;
- multi-QPU networking when communication cost is lower than duplicating classical accelerator fleets.

## Tier 3 — Memory/state routes

Literal replacement of classical RAM/VRAM/HDD by qubit count is not a valid equivalence argument. Stronger research routes are:

1. semantic elimination of large intermediate tensors/states;
2. recomputation instead of storage when cheaper;
3. succinct quantum-state preparation from structured generators;
4. quantum memory for quantum data that would otherwise require exponentially large classical descriptions;
5. hybrid cache/checkpoint architectures;
6. compressed classical summaries of quantum observables;
7. application-specific persistent-state services rather than byte-for-byte disk emulation.

Known constraints include measurement collapse, classical addressability, finite coherence, no-cloning and accessible-information bounds. Wootters and Zurek showed that an unknown arbitrary quantum state cannot be perfectly cloned (Nature 299, 802–803, 1982; DOI 10.1038/299802a0).

## Tier 4 — Device/material/manufacturing opportunity routes

- lower-control-overhead qubits;
- cryogenic CMOS/co-integrated control;
- photonic interconnects and optical control;
- 3D integration/chiplets;
- higher-yield fabrication processes;
- relaxed-lithography architectures where device physics permits;
- biomass-derived carbon/packaging/purification/thermal/EMI materials when they meet functional-unit requirements;
- recovery/minimization of scarce metals rather than assuming impossible chemical transmutation;
- improved metrology/process feedback to reduce cost per good quantum device.

These routes primarily improve economics and scale; by themselves they do not supply the algorithmic 100M-fold useful-work advantage.

## Tier 5 — Thermodynamics and reversible computing

Landauer-style energy bounds motivate reversible and low-dissipation computation. These are important for energy/cooling economics, especially at data-center scale, but an energy reduction alone is not equivalent to throughput replacement.

Research requirement: separate joules/op, operations/task, latency, capital cost and total accepted-task cost.

## Tier 6 — Fundamental-physics frontier

Research may examine condensed-matter phases, many-body phenomena, quantum optics, nuclear/particle phenomena and quantum field theory when a concrete computational mechanism can be stated.

For every frontier proposal, require:
- an explicit information-processing primitive;
- equations/scaling law;
- compatibility check against conservation laws, causality, thermodynamics and quantum-information limits;
- a reproducible experiment or mathematical bound;
- a path from effect -> device -> system -> useful task -> economics.

## Tier 7 — Speculative beyond-standard-model computation

Examples such as physically available postselection, nonlinear quantum mechanics, closed-timelike-curve computation, exotic spacetime resources or presently unknown interactions may have extreme theoretical computational power in mathematical models. They remain SPECULATIVE unless nature supplies the required resource.

For example, PostBQP = PP in the postselection model (Aaronson, Proc. R. Soc. A 461, 3473–3482, 2005, DOI 10.1098/rspa.2005.1546). This is a complexity-theory result, not evidence that arbitrary postselection is a free physical operation.

Such directions may be retained as clearly labeled theoretical research but must never be mixed with engineering roadmaps for current cloud QPUs.

## Hard constraints / early-kill tests

A proposed 100M-unit route should be downgraded quickly if any of the following dominates:
- Omega(N)-scale classical input loading for a claimed exponentially faster N-input task;
- output requires materializing an exponentially large classical object;
- QEC/mitigation shots overwhelm algorithmic savings;
- queue/network/state-preparation latency dominates useful compute;
- the comparison uses a weak CPU/GPU baseline;
- the quantum output solves a different/looser task than the conventional baseline;
- memory equivalence is argued only by Hilbert-space dimension;
- the physical mechanism violates established laws without a discriminating experiment;
- economics excludes required classical control, memory, cooling, maintenance or reconstruction.

## Highest-value current path

The strongest near-term path remains:

structured workload -> identical useful-output contract -> competitive CPU/GPU baseline -> quantum-native formulation -> target-aware simulation -> bounded real-QPU execution -> end-to-end cost/useful-task -> scale-law analysis.

In parallel, the open-frontier program searches for workload classes where the algorithmic scaling is strong enough that a 10^8-unit replacement hypothesis is not ruled out before engineering begins.
