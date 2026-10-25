# RG-045 — Certify actual split disjointness for progressive equation discovery

**Status:** `OPEN / PROTOCOL-INTEGRITY GAP / NOT IMPLEMENTED`  
**Date:** 2026-10-24  
**Primary owner:** Lane A — workload/equation-discovery software  
**Cross-lane owners:** Lane F — leakage/selection-bias and evidence accounting; Lane H — literature context/publication  
**Related:** Issue #68, pending PR #56, RG-042, INV-034, INV-035, FND-006, EQN-001–006  
**Canonical starting main SHA:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`  
**Evidence class:** `SOFTWARE_PROTOCOL_GAP`; no project scientific result is promoted

## Finding

The pending progressive-discovery contract in PR #56 defines train, validation and held-out data as non-overlapping and commits three distinct SHA-256 file digests. Its current `DataSplits.validate()` checks digest syntax and that the three file hashes differ. Distinct file hashes do **not** prove that the files contain disjoint records: sample, trajectory, experiment, source-row or near-duplicate IDs can overlap while the serialized files remain different.

This is a gap in the proposed protocol guard, not a claim that the external Chain of Symbolic Regression paper is wrong. PR #56 remains unmerged; this note does not represent its code as canonical main.

## Required contract

1. Each split has a versioned manifest bound to the exact dataset-byte digest and canonicalization/schema version.
2. The manifest identifies stable record units appropriate to the dataset (for example, sample, trajectory, experiment or source-row IDs). If stable IDs are unavailable, the alternative partition certificate and its assumptions must be stated explicitly.
3. Validation checks pairwise disjointness across train, validation and held-out identifiers; it also rejects duplicate IDs within a split, missing identifiers, invalid manifest schemas and digest/manifest mismatches.
4. Canonical ordering and serialization are deterministic so the manifest itself can be hashed and independently reproduced.
5. The held-out set remains sealed from model selection, prompt choice, pruning, repair and progressive-stage construction until the complete plan is frozen.
6. A negative test uses three different file hashes with at least one overlapping record ID and must fail closed. Positive and adversarial tests cover disjoint partitions, duplicate IDs, empty splits where forbidden, identifier-type collisions, canonicalization, and manifest/data digest mismatch.
7. The guard remains offline: zero provider calls, zero QPU jobs, and no paid execution.

## Acceptance gate

An exact-commit CI artifact must demonstrate that distinct file hashes with overlapping record IDs are rejected, genuinely disjoint manifests pass, and each manifest is bound to the exact committed dataset bytes. Only then may the RG-042 synthetic benchmark runner use the split as a leakage-controlled input. The matched-budget one-shot versus progressive comparison, counterexample controls, held-out/OOD metrics and independent replay still must execute before any method-performance conclusion.

## Cross-lane integration

- **A:** manifest schema, split validation and deterministic benchmark runner.
- **B:** no cloud/QPU adapter is invoked; provider neutrality is preserved.
- **C:** report manifest bytes, dataset materialization and any split-storage overhead separately from quantum state size.
- **D/G:** no device/fabrication implication until a physical constitutive model is independently validated.
- **E:** no Pangola material, saleable bio-oil, fusion-electricity or energy claim follows from synthetic equation-search validation.
- **F:** detect leakage/selection bias; retain false discoveries and failed candidates; never treat unknown energy/cost as zero.
- **H:** publish literature context without upgrading third-party claims to UQPU evidence.
- **INV-034/035:** current physical laws remain binding; generated relations remain hypotheses and must pass dimensional, symmetry, conservation, causality, scaling, falsifier, held-out, counterexample and independent-validation gates.

## Mission impact and non-claims

This gate can improve the credibility of future equation-search experiments and reduce the risk of spending R&D capital on a leakage-induced false discovery. It does not demonstrate improved equation recovery, a new physical law, quantum advantage, GPU/CPU/NPU/RAM/VRAM/storage replacement, Data-Center-to-Phone feasibility, Pangola-carbon substitution, commercial low-cost bio-oil, commercial low-cost fusion, or a lower financing rate/WACC.

## Next action

Implement the split manifest and pairwise disjointness validator in the progressive-discovery branch or a reviewed follow-up; add the adversarial tests above; run the pinned test suite and hosted CI; update RG-042 only through a separate, reviewable change. Keep this gap open until the exact artifact and CI provenance are available.
