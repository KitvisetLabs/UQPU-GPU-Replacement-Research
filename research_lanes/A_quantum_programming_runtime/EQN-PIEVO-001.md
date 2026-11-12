# EQN-PIEVO-001 — matched-budget test of principle-space evolution

**Date:** 2026-10-26  
**Primary owner:** Lane A — quantum programming, workloads, compiler/runtime and equation-discovery harness  
**Cross-lane owners:** Lane F — benchmark/evidence/economics; Lane H — source and publication  
**Status:** READY_FOR_PREREGISTRATION / NOT_EXECUTED  
**Evidence class:** LITERATURE_ONLY + SOFTWARE_HELPER + FOCUSED_UNIT_TESTS

## Objective

Test whether allowing a scientific discovery system to expand its candidate-principle space improves accepted equation recovery or held-out generalization compared with a static-principle baseline under matched information and compute budgets. The PiEvo paper motivates this comparison; UQPU has not reproduced it.

## Hypotheses

- **H1:** on a preregistered set of synthetic known-law tasks, principle expansion improves a declared held-out recovery/generalization metric at equal total search resources without increasing the false-discovery rate beyond a frozen tolerance.
- **H0:** the improvement disappears under matched budgets, sealed held-out data, independent scoring or complete cost accounting.
- **H2 (physical, separate):** a candidate equation can support a physical-model claim only after domain-specific constraint checks and independent evidence. H1 cannot imply H2.

## Preregistered comparison contract

- Freeze source/code/data/dependency hashes and model configuration.
- Use identical task sets, initial observations, evaluator, seeds and stopping rules.
- Compare static-principle and principle-expanding modes; only training/validation anomalies may trigger an expansion.
- Seal held-out and extrapolation splits; prohibit post-test principle updates.
- Match wall-clock, model/API-token, CPU/GPU and candidate-evaluation budgets; if exact matching is impossible, mark the run INCOMPARABLE.
- Keep every candidate, failed run, retry, rejected formula, counterexample and false discovery.
- Report exact recovery, held-out/extrapolation errors and uncertainty, formula complexity, constraint violations, memory, latency, compute, token/API use, energy when measured, and cost per independently accepted formula under one named cost basis.
- Start with synthetic ground-truth equations. Do not treat synthetic fit as physical evidence.

## Fail-closed physical-equation metadata helper

The module equation_claim_gate.py requires the incumbent assumption/model, alternative equation, variables and units, domain, explicit dimensional/symmetry/conservation/causality checks, limiting cases, falsifier, discriminating observable, held-out prediction, counterexample plan, proof/simulation and experiment plans, independent validation, system consequence, economic consequence, source provenance and failure-recording plan.

The helper checks metadata completeness only. It cannot validate the correctness of a check, certify a proof, establish a physical law or promote a hypothesis. A complete record remains HYPOTHESIS_ONLY_PENDING_INDEPENDENT_EVIDENCE.

## Acceptance and falsification

Accept a computational-method improvement only if a frozen independent evaluator confirms a preregistered effect size and uncertainty criterion on held-out data, no split leakage occurs, all failures remain in the accounting, and the result reproduces from pinned artifacts. Reject the claimed benefit if it depends on unequal resources, test leakage, excluded failures, poor extrapolation, constraint violations or unstable independent replication.

A later physical claim additionally requires proof/simulation as appropriate, a discriminating experiment, independent replication, a concrete device/system consequence and separate economics. Current physical limits remain binding unless discriminating evidence establishes a better model.

## Mission boundaries

This work does not establish a quantum advantage or change the status of INV-029 through INV-033. It supports the research process for INV-034/INV-035 only. INV-025/026/027 and the 100,000,000-unit moonshots remain falsifiable goals. No provider, QPU, physical experiment, material purchase or paid model/API action is authorized by this artifact.
