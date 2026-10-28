# Literature watch — Planckian bound on quantum dynamical entropy

**Reviewed:** 2026-10-28  
**Primary source:** Xiangyu Cao, “Planckian Bound on Quantum Dynamical Entropy,” *Physical Review Letters* 137, 030402 (published 2026-07-13).  
**Official record:** https://journals.aps.org/prl/abstract/10.1103/wd91-v58h  
**DOI:** https://doi.org/10.1103/wd91-v58h  
**Evidence class:** PEER_REVIEWED_THEORY / ABSTRACT-LEVEL SOURCE REVIEW; the proposed universal bound is explicitly a conjecture. No UQPU reproduction.

## What is new and what the source actually says

The APS abstract introduces a simplified version of Connes–Narnhofer–Thirring quantum dynamical entropy for continuously monitoring an observable. It states that a nonzero entropy-growth rate can arise when monitoring thermal fluctuations of an extensive observable in a generic many-body system away from classical or large-\( N \) limits. The author computes the rate in the thermodynamic and long-time limit in terms of two-point correlation functions, and **conjectures** a universal Planckian bound for that rate; related purification-rate results are also reported. The APS record gives publication date 13 July 2026, acceptance date 26 May 2026, and DOI 10.1103/wd91-v58h.

The genuine project-relevant delta is a potentially useful *observable-specific information-acquisition-rate model* for the foundational accounting of continuous monitoring. It is distinct from the September 2026 *Nature Physics* paper on a proved Planckian timescale for a universal thermalization machine. The two results have different objects and assumptions and must not be merged into one universal quantum-speed-limit formula.

## Limitations and evidence boundary

- The accessible official source in this review is the APS abstract; the full article and supplemental derivation were not available for independent reconstruction in this run. Formula-level details, constants, assumptions, and theorem/conjecture boundaries therefore remain unverified here.
- A conjectured entropy-rate bound is not a proved universal law. The article abstract does not establish a lower bound on arbitrary gate time, QAOA runtime, fault-tolerant computation, accepted-useful-task latency, or total wall-plug energy.
- Monitoring-induced information gain is not automatically useful classical output. Readout, controller computation, memory, measurement back-action, reset, error correction, data transfer, and output reconstruction remain in the end-to-end ledger.
- The paper is external literature, not a UQPU reproduction, physical experiment by this project, or evidence of a quantum advantage.

## Exact relevance to UQPU

- **FND-001:** informs the separation of intrinsic entropy/information quantities from controller, reset, cooling, and wall-plug energy; it does not replace Landauer accounting.
- **FND-002:** may help characterize the information acquired by a continuous measurement channel, but it does not by itself bound the readable bits or accepted output of a workload.
- **FND-003:** provides a candidate theory lead for matched measurement/control experiments. The observable, Hamiltonian, state, temperature, monitoring protocol, time window, and classical baseline must be identical before comparison.
- **Lane A/B/C:** any eventual use in runtime or provider comparisons must include measurement bandwidth, shots, readout error, state preparation, memory/I/O, host compute, and output-quality acceptance.
- **INV-029:** only a future validated relation with a demonstrated device/system consequence could inform physical compression; this paper alone does not change the Data-Center-to-One-Phone status.
- **INV-031/032/033:** no direct accepted-liquid fuel, net fusion-electricity, or financing result follows from this paper.

## Falsifiable follow-up proposal

1. Obtain the full paper/supplement and transcribe the exact entropy definition, correlation-function expression, units, limits, and assumptions before coding a formula.
2. Independently derive the expression for one exactly solvable finite many-body model with a declared extensive observable and thermal state. Check units, positivity, finite-size and finite-time corrections, and the classical/large-\( N \) limits.
3. Pre-register the conjectured dimensionless comparison and a null model; sweep temperature, system size, observation bandwidth, and time-window length. Reserve held-out parameter regimes and adversarial cases.
4. Report estimator uncertainty and whether the bound is theorem-derived, conjectured, or merely fitted. Search counterexamples before proposing an experiment.
5. Only if a robust discriminating prediction survives should a low-cost controlled experiment be designed. Any future physical test must report detector/controller/reset energy separately from the inferred system quantity and be independently replicated.

**Disposition:** literature lead retained; full-text/theorem reconstruction and independent reproduction remain open. No equation or physical limit is promoted.
