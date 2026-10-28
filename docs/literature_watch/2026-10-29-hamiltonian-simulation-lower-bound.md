# Literature watch — Hamiltonian-simulation lower bounds and equation-search discipline

**Date checked:** 2026-10-29  
**Primary owner:** Lane H — literature surveillance/publication  
**Interfaces:** A/B/C/D/G/F; INV-034/035; FND-002/003/004; EQN-001–EQN-006  
**Evidence class:** OFFICIAL ARXIV PREPRINT / MATHEMATICAL LOWER-BOUND CLAIM; not independently reproduced by UQPU

## Source and dated status

Zlokapa, Allen and Harrow, “Optimal Lower Bounds for Hamiltonian Simulation,” arXiv:2607.19852 v1, submitted 2026-07-22. Official record: https://arxiv.org/abs/2607.19852. Full text: https://arxiv.org/html/2607.19852v1. The checked arXiv record lists no journal reference, so this watch does not claim peer-reviewed publication.

The paper studies H(τ) = Σⱼ aⱼ hⱼ(τ), with ordered positive normalized coefficients a₁ ≥ … ≥ aL > 0, Σⱼ aⱼ = 1, and local bounded-degree terms of unit norm. For λK = Σⱼ>K aⱼ, it reports gate and classical-query lower bounds of the asymptotic form

\[
\Omega\!\left(\min_{0\le K\le L}\left(Kt+\frac{t^2\lambda_K^2}{\epsilon}\right)\right),
\]

for suitable hard instances and trace-distance error ε. The matching composite-qDRIFT construction treats large terms deterministically and samples the coefficient tail.

## Genuine novelty

The result makes the coefficient-profile trade-off explicit: how many large terms are handled directly versus how much of the small-term tail is sampled. It strengthens the lower-bound discussion beyond results that choose only worst-case coefficient profiles to encode a Boolean computation. For algorithms using generic access and coefficient magnitudes alone, it cautions against assuming that a more elaborate generic randomized formula automatically beats the composite trade-off.

## Limitations and evidence boundary

- This is a mathematical complexity theorem for specified hard-instance families and access models, not a measured hardware result.
- The gate lower bound is an existence result for suitable time-dependent Hamiltonians; it does not say every physical Hamiltonian saturates the bound.
- The query theorem uses a **classical** oracle that cannot be queried in superposition; it is not directly a lower bound for coherent block-encoding oracles.
- The authors state that additional Hamiltonian structure, spatial locality or special input-state properties may enable specialized algorithms outside the generic bound's direct scope.
- An asymptotic Ω expression does not itself give pulse time, fault-tolerant runtime, QEC overhead, energy, cost or a finite-instance numeric lower bound with known constants.
- UQPU has not independently checked the proof or reproduced the comparison.

## Exact UQPU relevance

- **A:** a candidate resource-bound certificate for Hamiltonian simulation/QSP-QSVT only when the Hamiltonian family, coefficient ordering, error metric, time dependence and access model match. It is not a direct result about the parity-QAOA prototype.
- **B:** count term/oracle construction and compiled gates; query count alone may omit the cost of constructing the oracle.
- **C:** record coefficient-list/state preparation, host/device memory, data movement and output reconstruction. Hilbert-space dimension is not readable classical memory.
- **D/G:** target-native gate synthesis, connectivity, control, packaging and yield require separate validated hardware/resource models.
- **E:** possible relevance to computational workloads for materials/fusion does not establish Pangola-carbon substitution, accepted bio-oil, net delivered fusion electricity or cooling benefit.
- **F/FIN-001:** gate/query bounds do not establish cost per accepted task, lower principal, lower WACC or reduced interest without complete cost/time accounting.
- **H:** retain this as a mathematical/algorithm research lead within the Kanusanan Pongpanna Model context, not as scientific or financial evidence.

## Cross-check of equation-discovery surveillance

The official APS accepted-paper record for CoSR still states “accepted 6 October 2026” (https://journals.aps.org/prresearch/accepted/10.1103/f2kp-pp4q), while the same-title arXiv record still says it was withdrawn by the author and cites methodological flaws in the Rayleigh–Bénard convection case (https://arxiv.org/abs/2603.13727; version 2 dated 2026-05-29). This conflict remains unresolved on 2026-10-29; the existing gap remains open and no CoSR benchmark result is adopted.

The official PiT-PO and LLM-controlled symbolic-search records were rechecked at https://arxiv.org/abs/2602.10576 and https://arxiv.org/abs/2607.04156. They reinforce the design rule that AI may guide candidate exploration while deterministic, physics-aware and held-out tests decide which candidates survive. Neither is a UQPU reproduction or proof of a new physical law.

## Falsifiable follow-up

1. Pin the preprint version and independently review theorem assumptions, coefficient profile, trace-distance definition and gate convention.
2. Freeze a small bounded-degree Hamiltonian suite with uniform, power-law and exponentially decaying coefficient profiles, source hashes, exact small-instance evolution and a declared ε metric.
3. Compute the minimizing cut K and compare direct product formulas, qDRIFT and composite qDRIFT under equal error targets. Treat this as a scaling/model check, not an exact finite-size gate bound.
4. Count term-oracle construction, state preparation, compilation, host work, memory/I/O, retries and output verification; hold out a coefficient profile and Hamiltonian structure.
5. Preserve failures/counterexamples. If a discrepancy appears, check theorem assumptions and access model before considering any anomaly.
6. Transfer results to device/material/fusion/finance only after a causal interface and independently measured system/economic consequence are specified.

**Non-claims:** no new law of nature, new physical primitive, QPU advantage, GPU replacement, readable-memory equivalence, material substitution, commercial bio-oil, net fusion electricity, lower financing rate or Data-Center-to-One-Phone milestone is established.
