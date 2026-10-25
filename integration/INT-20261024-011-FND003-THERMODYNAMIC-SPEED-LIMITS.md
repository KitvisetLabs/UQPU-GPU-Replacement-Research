# INT-20261024-011 — thermodynamic speed-limit literature to FND-003

**Status:** PROPOSED / OFFLINE VALIDATION NOT EXECUTED  
**Date:** 2026-10-24  
**Primary literature artifact:** `research_lanes/H_strategy_finance_future_industries/LITERATURE_WATCH_2026-10-24_THERMODYNAMIC_SPEED_LIMITS.md`  
**Primary research owner:** Lane H  
**Integration/evidence owner:** Lane F  
**Stable follow-up ID:** `FND-003-TSL-001`  
**Canonical start SHA:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`  
**Source:** Kobashi, *Thermodynamic speed limits in isolated quantum systems*, PR Research accepted 2026-10-06, DOI 10.1103/k16k-nx74; arXiv:2609.12520  
**Evidence class:** THIRD_PARTY_ACCEPTED_THEORY / LITERATURE_ONLY  
**Project evidence promotion:** none

## Hypothesis

For a subset of exactly specified unitary state-transformation tasks, a thermodynamic speed limit based on the paper's entropy-production inequality and Vu–Saito quantum Wasserstein pseudo-distance may produce a more restrictive lower bound on protocol time than the incumbent Margolus–Levitin or Mandelstam–Tamm bound when all assumptions and energy conventions are matched.

This is a hypothesis about bound usefulness, not a claim that a physical process can attain the bound. The competing outcome—no tighter bound on any relevant contract—is an acceptable negative result.

## Typed inputs and contract

The offline fixture must freeze:

- finite Hilbert-space dimension and Hamiltonian family `H(t)`;
- initial state, final state, exact protocol duration and energy convention;
- initial/final coarse-graining projectors and selected entropy functional;
- the exact theorem assumptions, including passivity/macroscopic-state conditions where applicable;
- eigenvalue ordering/tolerance and the computation of `W_q`;
- entropy production and average entropy-production rate with explicit units;
- numeric precision, solver/version, seed and artifact hashes.

The core inequality must be checked using the paper's own definitions. `W_q` is a pseudo-metric dependent on spectra; `W_q=0` is not equivalent to equality of density operators. A zero or ill-conditioned entropy-production rate must be handled explicitly, never silently converted into infinite time or a passing result.

## Evaluation and falsifiers

1. Use analytically solvable two- and three-level cases plus independently computed small-matrix checks.
2. Test passive in-domain cases and negative controls for non-passive states, changed coarse-grainings, degeneracies, rank/support changes, zero entropy production and unitarily equivalent states.
3. Verify dimensional consistency and every in-domain inequality. Retain counterexamples, numerical failures and assumption violations.
4. Compare against Margolus–Levitin and Mandelstam–Tamm bounds under identical state-transition and energy conventions.
5. Freeze held-out Hamiltonian families before evaluation; any fitted estimator must not tune against held-out cases.
6. Require independent derivation and an independently implemented calculation before using the bound to change FND-003 experiment selection.

**Fail conditions:** any valid in-domain counterexample; an untracked assumption change; non-reproducible numerical results; or no tightening of an incumbent bound for the declared relevant cases. A pass only validates a finite mathematical fixture, not a new physical law, device speedup or commercial advantage.

## Cross-lane interfaces

| Lane | Interface / disposition |
|---|---|
| A | May consume a validated time lower bound only inside an identical useful-output workload contract; no compiler/runtime change now. |
| B | No provider access or QPU execution; target-specific use would require a separate authorized preflight. |
| C | Keep spectral distance and coarse-grained information distinct from readable classical output, RAM/VRAM/HBM and storage capacity. |
| D | No device specification until a validated bound changes a concrete control/readout requirement. |
| E | No material, bio-oil, fusion-electricity, cooling or infrastructure evidence. |
| F | Record uncertainty, wall time, memory, measured energy if available, and cost per accepted discriminating result; model bounds are not measured economics. |
| G | D/G co-design remains conditional on a validated device requirement; no manufacturing claim. |
| H | Maintains source traceability and the literature-to-test rationale. |

## Mission and invariant boundary

- INV-029: no physical Data-Center-to-One-Phone compression claim.
- INV-030: no Pangola/critical-material substitution claim.
- INV-031: no accepted liquid-fuel or commercial-cost claim.
- INV-032: no net reliable delivered fusion-electricity claim.
- INV-033: no financed-principal, interest or WACC effect.
- INV-034: a precise foundational-physics hypothesis is added to the falsifiable search queue.
- INV-035: current physics remains binding; the candidate must pass units, assumptions, limiting cases, counterexample, held-out and independent-validation gates.
- INV-025/026/027: the 100-million-unit and broad open-frontier goals remain unproven.

## Current state and next action

The literature review is complete; the FND-003-TSL-001 implementation and numerical tests are **NOT EXECUTED**. Next action: implement the deterministic small-system fixture, record analytic expected values and hashes, compare bounds under matched conventions, and publish both positive and negative cases. No credentials, provider service, QPU jobs, shots, instruments, purchases or funding actions were used.
