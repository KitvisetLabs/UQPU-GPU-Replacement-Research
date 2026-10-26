# Research gap RG-046 — raw-record binding and external dataset provenance

**Date opened:** 2026-10-26  
**Status:** OPEN — raw-record manifest builder/verifier implemented; no public benchmark dataset pinned or independently audited  
**Primary owner:** Lane A — quantum programming/runtime and equation-discovery tooling  
**Cross-lane owners:** Lane F — evidence, benchmarks and cost accounting; Lane H — source provenance and publication  
**Related:** RG-045, RG-EQN-007, RG-EQN-008, FND-006, EQN-001–006, INV-034/035

## Observed gap

The split-disjointness validator can establish internal consistency of a declared manifest, including unique record IDs/content digests, nonempty partitions, group disjointness, canonical split hashes and binding to the matched-comparison contract. That alone cannot establish that the declared record digests were computed from the actual source records. A caller could supply arbitrary well-formed SHA-256 strings.

## Change made

The Lane A implementation now provides a builder that accepts canonical JSON payloads with explicit record ID, group ID and split assignment, derives per-record and dataset hashes, and emits the manifest. A verifier rebuilds the normalized manifest from supplied raw records and rejects a changed payload, a forged digest, a changed group or split assignment, or a changed dataset digest. Regression tests cover deterministic order, payload tampering, forged hashes, duplicate IDs and invalid split labels.

This closes the code-level self-attestation gap only when the raw records are supplied to the verifier. It does not authenticate the source, licensing, acquisition path, or representativeness of the data.

## Remaining blockers

- No external dataset source, exact revision/commit, license and acquisition record has been pinned for this cycle.
- No source-to-record inclusion/exclusion audit was performed.
- No independent reviewer recomputed the manifest from the same source snapshot.
- No matched 30-seed equation-discovery comparison was run.
- No candidate equation was formally checked or physically validated as part of this work.

## Unlock criteria

1. Select a public benchmark with clear license and stable version or immutable commit.
2. Record source URL, revision/commit, license, acquisition date, file names, raw file digests, schema, row count and deterministic preprocessing.
3. Freeze record IDs, group IDs, split policy, train/validation/test membership and group-holdout unit before method tuning.
4. Independently rebuild and compare the dataset and split digests from the pinned raw source.
5. Run the matched-comparison contract with the same dataset, group manifest, preprocessing, grammar, units, acceptance rules, >=30 preregistered seeds, resource ceilings and cost basis across methods.
6. Preserve failures, counterexamples, false discoveries and null outcomes; require held-out generalization and physics constraints before discussing physical relevance.

## Falsification and stop rules

Reject the benchmark run if any raw record or group assignment cannot be reconstructed, if any group crosses partitions, if the immutable source cannot be fetched under its license, or if method budgets differ. A reproducible hash of the wrong or biased dataset does not validate a scientific conclusion. No benchmark score alone establishes a physical law, QPU advantage, material substitution, commercial fuel/electricity, or lower financing rate.

## Sync debt

This standalone gap remains canonical until an append-only reconciliation can safely update RESEARCH_GAPS.md and WORKLOG.md without truncation. Keep the root directives, VERSION_INVARIANTS.md, multilingual strategic references and existing gap history intact.


## Provenance preflight implementation — 2026-10-26

A companion contract now exists at software/uqpu-prototype/uqpu/dataset_provenance.py with regression coverage in software/uqpu-prototype/tests/test_dataset_provenance.py. It binds source URL, source revision, license identifier, acquisition date, raw-file path/digests, dataset row count and dataset digest to the existing split manifest, and hashes the schema, preprocessing, inclusion/exclusion and group-holdout policies. Its benchmark-bundle preflight composes this with raw-record binding and split-disjointness verification.

This reduces provenance-schema drift but does not close RG-046. The verifier does not fetch or authenticate external bytes, decide legal license compliance, establish dataset representativeness, or validate scientific conclusions. No public benchmark source is pinned yet, and no independent audit or matched >=30-seed comparison has run. Keep RG-046 OPEN until all source, license, raw-file, split, held-out and resource-parity criteria above pass.
