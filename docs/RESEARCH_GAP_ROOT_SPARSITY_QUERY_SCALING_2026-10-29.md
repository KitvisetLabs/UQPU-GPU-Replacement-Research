# Research gap RG-A-ROOT-SPARSITY-REPRO-001 — sparse-oracle complexity to accepted-workload resources

**Opened:** 2026-10-29  
**Primary owner:** Lane A — algorithm and workload resource contracts  
**Interfaces:** B (provider-neutral execution), C (state/data movement), D/G (target implementation), F (evidence/economics), H (literature provenance)  
**Status:** OPEN / OFFICIAL-PREPRINT-CLAIM / UQPU REPRODUCTION NOT STARTED  
**Source:** https://arxiv.org/abs/2610.02939  
**Related:** INV-025–027, INV-029, INV-034/035, FND-002/004, EQN-001–EQN-006

## Objective

Determine whether the reported root-sparsity query scaling can be reproduced on a small, explicit sparse-matrix workload and then mapped to a complete accepted-useful-task contract without confusing asymptotic query complexity with measured gates, latency, energy or cost.

## Source claim and applicability contract

For an (s)-sparse Hermitian matrix whose row/column Euclidean norms are bounded by η, with τ = η|t|, the official preprint reports a query-complexity expression of the form

`O(√s τ + √(s τ log(1/ε)) + log(1/ε))`.

The theorem is tied to its sparse-access and norm assumptions. Time-dependent use requires the stated coherent time-indexed access and certified discretisation. Gate-efficient implementation adds assumptions about efficient entry decoding, arithmetic and source preparation. These assumptions must be recorded separately from the expression itself.

## Current implementation delta — 2026-10-29

Added `root_sparsity_hamiltonian_query_proxy` to `software/uqpu-prototype/uqpu/fundamental_limits.py`. It evaluates the dimensionless expression with positive finite sparsity/norm/time checks and (0<ε<1), returning its terms and an explicit MODEL_ONLY boundary. Regression tests cover the hand-calculated expression, monotonic scaling and invalid inputs.

This helper is a reproducible arithmetic proxy only. It does not check a matrix's sparsity/norm promise, construct an oracle, prove the source theorem, count gates, or estimate physical/economic performance.

## Acceptance contract

- Freeze matrix entries, sparse-access semantics, row/column norm certificate, evolution time and target trace-distance error.
- Use exact small-instance evolution as reference; publish seeds and held-out sparsity/time/precision profiles.
- Record query count separately from oracle construction, input-state preparation, synthesis, host compute, peak memory, transfers, output reconstruction, retries and verification.
- Compare against a matched classical numerical baseline for the same accepted output and accuracy.
- Preserve failed profiles and counterexamples; require independent reproduction before stronger evidence labels.

## Falsifiers and stop conditions

The claim is not transferable to a workload if its oracle/access model or norm assumptions are unmet, if held-out error fails the accepted predicate, or if omitted state-preparation/data costs remove the proposed advantage. A numerical scaling fit alone does not validate the theorem.

## Non-claims

No new physical law, real-QPU advantage, GPU/CPU/NPU/RAM/VRAM/storage replacement, Data-Center-to-One-Phone milestone, Pangola-carbon substitution, accepted bio-oil, net fusion electricity, lower WACC or commercial economics is established. Current physical limits remain binding.
