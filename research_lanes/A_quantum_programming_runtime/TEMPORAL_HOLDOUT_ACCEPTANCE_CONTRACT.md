# Lane A contract — chronological and group-disjoint temporal holdouts

**Contract ID:** A-TEMPORAL-HOLDOUT-001  
**Primary owner:** Lane A — workloads, model-evaluation and benchmark contracts  
**Evidence owner:** Lane F — reproducibility, uncertainty and resource accounting  
**Publication owner:** Lane H — literature provenance  
**Cross-lane consumers:** C (state/data movement), D/G (process drift), E (thermal/fluid/material/energy models)  
**Evidence class:** SOFTWARE_CONTRACT + SYNTHETIC_UNIT_FIXTURES  
**Status:** IMPLEMENTED CONTRACT / EXACT-HEAD CI PENDING  
**Related:** INV-034/035, FND-006, EQN-001–010, RG-045, RG-A-TEMPORAL-HOLDOUT-ORDERING-001

## Purpose

The existing split-disjointness manifest supports `TIME_BLOCK` as a holdout unit, but group disjointness alone does not prove chronological separation. This contract adds strict timestamp ordering and a caller-declared embargo between train, validation and test windows.

## Interface

- Implementation: `software/uqpu-prototype/uqpu/temporal_holdout.py`
- Tests: `software/uqpu-prototype/tests/test_temporal_holdout.py`
- Public function: `validate_temporal_holdout(records, timestamp_field="timestamp", embargo_seconds=0.0)`

Each raw record contains exactly `record_id`, `group_id`, `split`, and `payload`. The timestamp field must be an ISO-8601 string with an explicit UTC offset. The helper uses the canonical `split_disjointness.py` manifest builder/verifier, requires nonempty partitions, binds record IDs/groups/payloads into hashes, and rejects group leakage across partitions. It then requires:

- `max(train time) < min(validation time)`
- `max(validation time) < min(test time)`
- each gap is at least the declared nonnegative embargo

Timestamps are normalized to UTC before comparisons and certificate generation. The manifest is deterministic under record reordering.

## Acceptance gates

1. **Synthetic contract:** test ordered windows, timezone normalization, malformed/naive timestamps, group leakage, empty partitions, overlaps and embargo failures.
2. **Source-pinned dataset:** freeze data revision, acquisition procedure, license and raw-record hashes; the helper alone does not authenticate these.
3. **Blind temporal holdout:** freeze future-time blocks before tuning. Add parameter/geometry/law-family holdouts when the scientific question requires them.
4. **Physical validity:** pair with an independent numerical reference, PDE residual, initial/boundary errors, conservation/bounds, stability and uncertainty scoring as applicable.
5. **Matched resources:** compare methods under identical data, split, hardware, time, CPU/GPU hours, peak memory and energy-measurement boundary; retain all failed seeds.
6. **Independent reproduction:** do not promote a model or equation until independent reproduction and the physical interpretation gate pass.

## Non-claims

A PASS establishes only timestamp ordering and manifest/group-disjointness for supplied records. It does not prove generalization, a correct PDE, a new physical law, quantum advantage, material substitution, accepted bio-oil, low-cost fusion electricity or Data-Center-to-One-Phone compression.
