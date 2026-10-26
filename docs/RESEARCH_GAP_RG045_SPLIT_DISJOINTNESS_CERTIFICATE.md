# Research gap RG-045 — actual split-disjointness certificate for equation discovery

**Date:** 2026-10-26  
**Primary owner:** Lane A — equation-discovery contract/tooling  
**Evidence owner:** Lane F — benchmarks, uncertainty and reproducibility  
**Cross-lane consumers:** B, C, D, E, G, H  
**Status:** IMPLEMENTED MANIFEST VALIDATOR; REAL-DATA CERTIFICATION OPEN  
**Related:** EQN-001–006, FND-006, INV-034/035, RG-EQN-008

## Problem

The matched equation-discovery comparator rejects mismatched split hashes and declared holdout units, but metadata agreement alone does not establish that train, validation and test records or scientific groups are actually disjoint. A method can otherwise claim a law-family or material-family holdout while leaking records or groups across partitions.

## Implemented contract

The new `software/uqpu-prototype/uqpu/split_disjointness.py` defines a strict `uqpu-split-manifest-v1` manifest and computes a reproducible certificate. It:

1. requires nonempty train, validation and test partitions;
2. requires a nonempty record ID, group ID and SHA-256 record-content digest for each record;
3. rejects duplicate record IDs and duplicate content hashes across partitions;
4. rejects group IDs appearing in more than one partition;
5. canonicalizes each partition by record ID and computes split digests plus a held-out-group digest;
6. binds the manifest to a matched comparison's dataset hash, split hashes, holdout unit and declared test-group count.

The validator is deliberately stricter than a random-row split. It supports law-family, material-family, fluid-pair, scale, geometry, time-block, device-family and composite-group holdout units.

## Evidence and limits

- Local smoke checks passed for a valid certificate, group-leakage rejection and record-overlap rejection before publication.
- Regression tests cover valid/canonicalized manifests, duplicate record IDs, duplicate content hashes, group leakage, empty partitions, invalid hashes, group-count mismatch, and binding the certificate to matched-comparison records.
- A PASS certifies only the supplied manifest declarations and digests. It does not independently fetch or hash the raw source dataset, prove provenance, establish scientific representativeness, or prove a physical law.
- No actual scientific dataset, cross-method benchmark, QPU, material, fuel, fusion-electricity or financing experiment was run in this cycle.

## Unlock criteria

1. Pin a real dataset revision and source license; publish the raw-data acquisition/provenance procedure.
2. Produce the canonical manifest from the dataset loader, with deterministic record-content hashes and group labels.
3. Independently audit the manifest against the loaded records and verify split/group disjointness before any model selection.
4. Run at least 30 preregistered seeds for at least two methods with identical total-resource ceilings, law-family-disjoint and held-out-scale tests, and all failed searches retained.
5. Keep symbolic fit, formal proof, physical validation and economic advantage as separate evidence gates.

This record is standalone. The large append-heavy `RESEARCH_GAPS.md` remains unchanged to avoid unsafe partial-history replacement; synchronization is explicit debt.
