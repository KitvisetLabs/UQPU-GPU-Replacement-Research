# Literature watch — Planckian bound on quantum dynamical entropy

**Date checked:** 2026-10-28  
**Primary owner:** Lane H — literature surveillance  
**Cross-lane interfaces:** FND-001 thermodynamic/information accounting, FND-003 speed-limit interpretation, Lane A accepted-task boundaries, Lane E thermal systems, Lane F evidence/economics  
**Evidence class:** PEER-REVIEWED THEORY + AUTHOR-REPORTED NUMERICAL SUPPORT / LITERATURE_ONLY FOR UQPU  
**Related gap:** RG-FND001-PLANCKIAN-ENTROPY-RATE-REPRO-001

## Primary source and date

Xiangyu Cao, “Planckian Bound on Quantum Dynamical Entropy,” *Physical Review Letters* 137, 030402, published 2026-07-13, DOI https://doi.org/10.1103/wd91-v58h. The author’s arXiv record is version 5, arXiv:2507.20914, dated 2026-07-13: https://arxiv.org/abs/2507.20914

## Genuine result and scope

The paper defines a simplified Connes–Narnhofer–Thirring (CNT) dynamical entropy for a quantum many-body system under continuous monitoring. It quantifies information gained about the initial condition while measurements back-react on subsequent observations. In a thermodynamic and long-time limit, the paper derives an entropy-growth-rate expression in terms of two-point correlation functions (Keldysh and retarded Green functions). It reports numerical comparison with a non-integrable mixed-field Ising chain at finite sizes and discusses local versus mesoscopic observables.

The broad statement \(s_{\mathrm{CNT}}\leq cT\) (in natural units) is explicitly presented as a **conjecture** for a general class of many-body systems and monitoring schemes away from thermal criticality. For the particular rescaled extensive observable and Gaussian measurement scheme analyzed, the paper derives a specific bound \(\beta s_{\mathrm{CNT}}\lesssim 0.57\) while maximizing the integral without imposing the fluctuation-dissipation constraint; the paper says a tighter bound follows when that constraint is included. This restricted derivation and its numerical support should not be conflated with a proven universal theorem for every quantum system.

## Limitations and evidence class

- UQPU has not independently reproduced the rate integral, numerical curves, finite-size scaling or any experimental protocol from this paper.
- The general extension beyond the analyzed measurement/operator class is conjectural. The authors identify thermal criticality, local-observable behavior, monitoring choices and the order of thermodynamic/long-time limits as relevant scope conditions.
- The entropy rate is an information-gain observable under a specified monitoring protocol. It is not automatically a bound on algorithm runtime, QAOA convergence, quantum speedup, Landauer heat, total wall-plug energy, or cost per accepted useful task.
- The paper’s use of natural units must be preserved when interpreting dimensions. No SI conversion or engineering-energy implication is claimed here.
- Numerical agreement in a finite spin chain is not proof of the universal conjecture or evidence that UQPU has validated it.

## Exact UQPU relevance

- **FND-001:** offers a candidate information/thermodynamic quantity to audit alongside, but not substitute for, accepted-task heat, reset, feedback, measurement, cooling and wall-plug energy accounting.
- **FND-003:** this is not a generic quantum-speed-limit theorem. It must not be used as a gate-time lower bound or a claim that a quantum algorithm is faster than a classical baseline.
- **Lane A / INV-029:** no inference follows about signed-Max-Cut output quality, workload latency, provider billing, local physical compression or Data-Center-to-Phone capability.
- **Lane E / FUS-001:** a thermal many-body information rate is not a fusion plant net-electricity model. Recirculating power, availability, materials damage and lifecycle economics remain separate.
- **Lane F / FIN-001:** no CAPEX, OPEX, project WACC, principal, interest or time-to-evidence saving is reported.
- **INV-034–035:** the result is a testable theoretical lead; present physics remains binding and the universal extension remains a hypothesis until discriminating evidence supports it.

## Falsifiable follow-up

1. Reconstruct the published rate formula and conventions from the versioned paper, including the normalization of the observable and measurement strength.
2. Independently reproduce the reported mixed-field Ising-chain calculations for the stated Hamiltonian and finite sizes \(L=6,8,10\), then quantify time-step and finite-size errors rather than treating the thermodynamic limit as directly measured.
3. Test the derived bound first under the exact Gaussian mesoscopic-measurement assumptions, then test extensions across operator classes and temperatures away from criticality with the fluctuation-dissipation relation enforced.
4. Predeclare a counterexample criterion: a reproducible, unit-consistent rate above the stated bound within the exact claimed domain falsifies that version of the bound; an example outside the assumptions only narrows the domain.
5. Keep the CNT rate, purification rate, entropy production, heat, device energy and accepted-task economics as distinct measurements.

## Decision

**LITERATURE_ONLY FOR UQPU.** The paper is a peer-reviewed theoretical lead with an explicitly conjectural universal extension. No new physical law, general computation limit, QPU advantage, lower energy/cost, commercial fusion result or mission-level milestone is claimed.
