# RG-045 implementation note — split-membership certificate

**Date:** 2026-10-24  
**Primary owner:** Lane A — quantum programming, workloads, compiler/runtime and equation-discovery software  
**Cross-lane consumers:** Lane F — evidence/leakage/accounting; Lane H — research publication  
**Status:** CODE IMPLEMENTED / HOSTED CI PENDING / RAW-DATA-LOADER VALIDATION PENDING  
**Canonical main at cycle start:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`  
**Implementation branch:** `research/2026-10-24-cosr-progressive-discovery`  
**Related:** RG-042, RG-045, EQN-COSR-001, FND-006, INV-034, INV-035

## Finding addressed

Three distinct serialized-file hashes do not establish that the train, validation and held-out partitions contain disjoint records. Distinct files can share sample, trajectory, experiment or source-row identifiers. The progressive equation-discovery plan therefore needs an explicit membership-level certificate, not hash inequality alone.

## Implementation

`DataSplits` now carries:
- the SHA-256 digest of the frozen source dataset;
- a declared sample-ID namespace;
- stable train, validation and held-out record IDs;
- pinned schema and canonicalization versions;
- deterministic per-split manifest digests; and
- a full certificate digest.

Canonicalization is sorted-key compact JSON encoded as UTF-8, with each split's sample IDs sorted before hashing. The validator fails closed on pairwise overlap, duplicate identifiers within a split, empty splits, non-string or non-normalized identifiers, malformed source or manifest digests, unsupported schema/canonicalization versions, and a manifest/data digest mismatch.

Tests cover the overlapping-ID adversary, duplicate and empty splits, invalid identifier types, invalid source digest, schema/canonicalization drift, deterministic order-independent hashes, source-digest binding, and digest mismatch. The original equal-budget, stage-dependency, physics-constraint-audit, held-out-sealing, failed-candidate-retention and zero-provider/QPU rules remain in force.

## Evidence boundary

**Evidence class: SOFTWARE_PROTOCOL_TEST / MODEL_ONLY.** The validator establishes structural identifier disjointness for the IDs supplied to it. It does not authenticate that a loader honestly derived those IDs from the raw dataset bytes. Before a benchmark consumes the certificate, its data loader must independently hash the exact source bytes, derive stable IDs from those same bytes, and verify the manifest against that extraction.

No quantum provider was called and no QPU job or paid execution was submitted. No equation-discovery performance result is claimed. No AI-generated equation is promoted to a physical law.

## Acceptance gate

1. Hosted CI must pass the exact implementation commit on all configured Python versions.
2. The dataset loader must independently verify source-byte digest and identifier extraction.
3. A loader-level adversarial fixture must prove that altered bytes or altered IDs fail closed.
4. Only then may the RG-042 synthetic comparison use this certificate; its matched-budget execution, held-out/OOD metrics, counterexample search and independent replay remain separate gates.

## A–H and invariant impact

| Lane | Status for this change |
|---|---|
| A — workloads/compiler/runtime | Implemented a fail-closed split-membership contract and tests; no method-performance conclusion. |
| B — cloud/QPU integration | No provider calls, credentials, target assumptions, jobs or billable usage. |
| C — memory/storage/data movement | Manifest storage is explicit in the contract but not yet measured; no Hilbert-space/classical-memory equivalence claim. |
| D — device/chip/process | No device or fabrication implication. |
| E — biomass/materials/bio-oil/fusion/cooling | No material, accepted-fuel, net-electricity, cooling or commercial-cost evidence. |
| F — economics/evidence/integration | Reduces one identifiable leakage/selection-bias failure mode; no energy/cost value is imputed. |
| G — manufacturing equipment/factory | No factory or manufacturing claim. |
| H — strategy/publication | Preserves the distinction between literature context, software protocol evidence and physical evidence. |

- **INV-029:** no phone-class compression or end-to-end capability claim; the change only protects the integrity of future evidence.
- **INV-030/031/032:** no Pangola-material, accepted bio-oil or net fusion-electricity result.
- **INV-033:** a better evidence gate may avoid wasted R&D principal/time, but no realized financing or interest reduction is measured.
- **INV-034/035:** preserves mathematics-first exploration while requiring reproducible provenance and evidence before any physical-law claim.

The canonical multilingual strategic references, permanent root directives and large append-only `RESEARCH_GAPS.md` were not overwritten. RG-045 remains open until the exact-commit and raw-data-loader gates pass.
