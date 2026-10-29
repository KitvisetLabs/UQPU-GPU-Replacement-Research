# Daily integration — 2026-10-29 — equation-stability source audit and known-law fixture

**Starting main:** 268a423add2a5960aa4b7efa9711c1311aeaa318  
**Primary artifact owner:** Lane A  
**Integration owner:** Lane F  
**Publication/provenance owner:** Lane H  
**Evidence class:** MODEL_ONLY synthetic numeric fixture + external source-provenance audit

## What changed

- Added a deterministic floating-point fixture for two algebraically equivalent expressions, using an 80-digit Decimal intermediate as the numerical reference.
- Added regression tests requiring the cancellation-prone expression to have larger held-out numerical error and normalized perturbation amplification than the rationalized expression.
- Audited the official EIC code repository at pinned commit 6e3abfcc308f2c71292abfa683ffb404412d022a. Repository license metadata is null and there is no root-level license file; nested licenses are scoped to named third-party subprojects/data. No EIC code was copied or executed.
- Added a preregistration for a future grouped known-law benchmark. The fit-plus-complexity baseline and UQPU proxy are to be compared under equal budgets; the official EIC arm remains blocked until reuse rights and environment/data provenance are resolved.

## A–H integration map

| Lane | Shared interface / current disposition |
|---|---|
| A | Owns the fixture, numerical metric and known-law benchmark contract. This does not replace the Priority-1 exact-QUBO/QAOA accepted-output path. |
| B | Provider-neutral cloud paths unchanged; no paid QPU jobs or target execution. |
| C | Readable output, memory, transfer and reconstruction remain separate metrics; no Hilbert-space-to-classical-storage inference. |
| D | Molecular spin–photon reproduction gate from Batch 126 remains open; no device evidence added here. |
| E | BIO-001 accepted liquid, INV-030 material function and FUS-001 net electricity remain open; no commercial evidence. |
| F | Owns matched budgets, evidence class, false-discovery accounting and cost-per-accepted-candidate boundaries. |
| G | D/G process-window, repeatability, yield and cost-per-good-device work remains active but unmeasured. |
| H | Owns source provenance and strategic continuity; GOLLuM/EIC sources were already indexed, so no duplicate literature article was added. |

All 28 unordered A–H lane pairs were reviewed for a concrete interface or an explicit no-change/open-gate disposition; see the machine-readable record INT-20261029-EIC-REPRODUCTION-PREFLIGHT.json.

## Foundational and mission gates

FND-006 advances only at synthetic diagnostic level. FND-001–005, EQN-001–006, BIO-001, FUS-001 and FIN-001 remain evidence-gated. INV-029–035 and INV-025/026/027 remain preserved. No physical law, QPU advantage, critical-material substitution, accepted bio-oil, net fusion electricity, lower WACC or phone-class physical-compression result is claimed.

## Validation and next gate

Starting-head core/invariant and cold-start workflows both passed. Exact-head CI for this new commit is pending. No local full-suite result is claimed and no paid QPU job was submitted. Next gate: exact-head Actions, then a frozen grouped known-law comparison under equal budgets. Do not enable the official EIC arm until its code-reuse rights and source/data/environment pinning are resolved.

Research-Sync: main
