# Literature watch — 2026-10-24: proof- and witness-gated scientific discovery

**Accessed:** 2026-10-24  
**Primary owner:** Lane H — strategy, finance and future-industry research  
**Feeds:** A–H; FND-001–006; EQN-001–006; BIO-001; FUS-001; FIN-001  
**Evidence class:** `LITERATURE_ONLY / THIRD_PARTY_RESEARCH`  
**Project evidence promotion:** none  
**Canonical starting main SHA:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`

## Why this surveillance delta matters

The 2026-10-23 watch already covered optimization-law discovery and an assumption-scoped ancilla-QFI boundary. This follow-up addresses a complementary bottleneck: how to keep AI-generated mathematical, physical-model and engineering candidates from being accepted merely because they fit data or look plausible. The useful new connection is the explicit proof-/witness-gated workflow demonstrated in recent formal-verification research, combined with feedback-trained equation generation.

These papers do not establish a new physical law, UQPU advantage, new quantum capability, material substitution, cheap fuel, fusion economics or lower financing rate. Their transferable contribution is a validation architecture.

## Sources reviewed

1. Romy Peled, Daniel Kroening, Michael Tautschnig and Yakir Vizel, **“Large Lemma Miners: Can LLMs Do Induction Proofs for Hardware?”**, IJCAI 2026, pp. 3988–3998, DOI: 10.24963/ijcai.2026/444. Official proceedings: https://www.ijcai.org/proceedings/2026/444. The paper reports LLM-generated candidate inductive arguments checked by a symbolic tool; at least one prompting setup succeeded on 90% of its problem set after sufficient reprompting.
2. Mingkai Miao, Guangyu Hu, Ziyi Yang and Hongce Zhang, **“IC3-Evolve: Proof-/Witness-Gated Offline LLM-Driven Heuristic Evolution for IC3 Hardware Model Checking”**, IJCAI 2026, pp. 271–278, DOI: 10.24963/ijcai.2026/31. Official proceedings: https://ijcai.org/proceedings/2026/31. The workflow accepts a SAFE result only with an independently checked certificate and requires replayable counterexample traces for UNSAFE results; proposed heuristic patches are offline and slot-restricted.
3. Boxiao Wang et al., **“LLM-Based Scientific Equation Discovery via Physics-Informed Token-Regularized Policy Optimization”**, arXiv:2602.10576, submitted 2026-02-11. Official preprint: https://arxiv.org/abs/2602.10576. PiT-PO combines physics-informed constraints with token-level penalties and feedback-based policy optimization for candidate equation generation; reported results include benchmark tasks and turbulence-model discovery.
4. Eric Jiang et al., **“From Solvers to Research: Large Language Model-Driven Formal Mathematics at the Research Frontier”**, arXiv:2607.07779, submitted 2026-07-08. Official preprint: https://arxiv.org/abs/2607.07779. This position paper distinguishes success on well-defined formal problems from the much harder, open-ended task of discovering new mathematics.

## Genuine novelty and limits

The material synthesis is **not** that AI can declare equations true. It is that candidate generation and candidate acceptance can be separated operationally:

- generate candidate equation, lemma, algorithm or implementation change;
- encode applicable dimensional, domain, symmetry, conservation and causality constraints;
- use the right checker for the claim: algebra/proof checker for formal identities, counterexample witness for violated properties, and reference solver/experiment for empirical models;
- freeze held-out regimes before ranking candidates;
- retain rejected candidates, counterexamples and failed proofs;
- promote only the specific claim that passed its own gate.

The formal-verification papers concern hardware transition systems and discrete properties, not general empirical physics. A proof of a model's internal property does not prove that the model describes nature. PiT-PO's reported equation fit and benchmark results are third-party results; they are not independent replication, not a UQPU result and not evidence that a discovered turbulence model generalizes to new materials, fusion plasmas or quantum devices. The research-frontier survey itself cautions that open-ended discovery is harder than solving preformalized problems.

## Proposed falsifiable UQPU follow-up

Create a small, offline equation-discovery audit suite before attempting a broader generator:

1. **Known-answer set:** generate synthetic data from a preregistered family of equations with known dimensions, symmetries and (where applicable) conserved quantities. Include degenerate, noisy and underdetermined cases.
2. **Hard constraints:** reject dimensionally inconsistent candidates and violations of explicitly required symmetries/conservation laws before predictive ranking. Do not impose a conservation law where the modeled system does not support it.
3. **Held-out tests:** reserve parameter ranges, initial conditions and boundary conditions that the generator never sees. Report interpolation and extrapolation separately.
4. **Counterexample gate:** search the declared domain for a counterexample to each claimed identity or invariant. Store the smallest found counterexample and its seed. A failed search is not a proof of absence.
5. **Claim-appropriate verification:** use symbolic or proof-assistant checks for mathematical identities; reference numerical solvers for approximate constitutive models; and identify a discriminating physical measurement for any claim that changes established physics.
6. **Baselines:** compare against a simple symbolic-regression baseline and a fixed-generator baseline under equal data, search budget and compute budget. Record false discoveries, rejected candidates, runtime and held-out error.
7. **Stop rule:** no candidate is promoted to a physical law or engineering input based on fit, internal consistency or AI confidence alone. A changed physical claim requires a distinct observable, uncertainty budget, preregistered falsifier and independent validation path.

**Acceptance condition:** every candidate marked “verified” must carry a machine-readable claim type, assumptions, constraint results, held-out metrics, counterexample-search status and artifact hashes. Any invalid candidate accepted by the hard gates is a test failure. Passing this suite would validate only the audit machinery on the tested cases, not establish a new physical law or a technology advantage.

## A–H relevance and status

- **A — Workloads/compiler/runtime (Priority #1):** make the same proof/witness pattern part of compiler-lowering and workload-contract validation. Next gate remains exact-commit hosted confirmation of the independently routed probes, then a stronger scalable equivalence verifier.
- **B — Cloud/QPU integration:** provider-neutral lowering and read-only target snapshots remain separate from paid execution. A provider snapshot or successful submission is not quality acceptance.
- **C — Memory/state/data movement:** record state size, serialization, host/device transfers and output reconstruction; a formal state-space count is not readable classical-memory capacity.
- **D — Devices/chips/process/packaging:** require device-model assumptions and measurable observables before turning a candidate relation into a process or device requirement.
- **E — Biomass/materials/bio-oil/fusion/cooling:** apply the same gate to mass/energy balances and constitutive models; keep Pangola/material hypotheses, bio-oil TEA and fusion envelopes as models until measured accepted-function evidence exists.
- **F — Economics/evidence/integration:** charge candidate search, validation, host compute, repeats and time-to-evidence to the total workflow. Do not label a faster search as lower WACC; shorter capital lock-up and reduced financed principal are separate, measurable channels.
- **G — Manufacturing equipment/factory systems:** use certificate/witness-gated process-window and yield-model changes, co-designed with Lane D; no manufacturing benefit follows from a mathematical fit alone.
- **H — Strategic/financial publication:** publish reproducible gates, negative results, uncertainty and capital-per-validated-milestone implications; preserve the multilingual Kanusanan Pongpanna Model references.

## Invariant contribution

- **INV-029:** improves the validation route toward a measurable useful-service contract; no physical compression result is claimed.
- **INV-030:** strengthens candidate screening for material-function models; no carbon-derived material substitution is demonstrated.
- **INV-031:** requires complete accepted-liquid mass/energy and upgrading boundaries; no commercial bio-oil cost result is claimed.
- **INV-032:** protects net-delivered-electricity models from being promoted on plasma-gain or fit alone; no commercial fusion claim is made.
- **INV-033:** makes time-to-evidence and validation cost auditable; no reduction in WACC is inferred.
- **INV-034:** links mathematics-first invention to explicit proof, counterexample and experiment gates.
- **INV-035:** permits broad equation generation while requiring physical constraints, held-out predictions, falsifiers and independent validation.

## Negative evidence and surveillance boundary

No new UQPU workload result, real-QPU run, independently reproduced physical anomaly, material characterization, accepted bio-oil/fuel measurement, net fusion-electricity measurement or project-finance outcome was obtained in this literature pass. No provider pricing or performance figures were mixed across targets. Paid QPU execution remains unauthorized absent credentials, an explicit bounded budget and user consent.

## Next highest-value gate

Implement and test the small known-answer/counterexample audit suite offline, then attach its machine-readable output to the existing EQN/FND ledger. In parallel, resolve the Lane A exact-commit hosted-CI/equivalence gate. Do not widen to physical experiments until the offline acceptance and provenance contract is reproducible.
