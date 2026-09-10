# Batch 031 — DRAM Memory-Scope Clarification

**Date:** 2026-09-10  
**Program:** Lane C / Memory-System Replacement  
**Evidence:** ARCHITECTURE_SCOPE_CLARIFICATION  
**REAL_QPU:** No  
**Quantum advantage:** Not demonstrated  
**UQPU memory replacement:** Not demonstrated

## Decision

DRAM is now explicit in UQPU memory research, but it is **not** modeled as a separate top-level peer subsystem beside RAM, VRAM and HBM.

The project instead adopts a role-based memory taxonomy with technology tags:

1. **System/host volatile memory** — RAM commonly implemented with DDR/LPDDR/RDIMM/MRDIMM-class DRAM.
2. **Accelerator-local volatile memory** — VRAM/HBM/GDDR; HBM and GDDR are themselves DRAM-family technologies.
3. **On-chip volatile memory** — SRAM/cache/register-file/scratchpad roles.
4. **Persistent storage** — SSD/HDD and other nonvolatile tiers.

This avoids double-counting DRAM while making its physical/economic costs explicit.

## Why this is preferable to adding `DRAM` as another sibling target

`RAM` describes a functional/storage role more broadly than one semiconductor implementation. `DRAM` describes a technology family. A conventional system can use multiple DRAM-family memories at different levels of the hierarchy, including system DDR-class memory and accelerator-local HBM/GDDR. Therefore a target list such as `RAM + DRAM + HBM` can overlap categories and create ambiguous economic accounting.

UQPU comparisons must state both:

- the **memory role** being replaced/reduced/avoided; and
- the **baseline physical technology** providing that role.

## DRAM-specific evidence contract

A claim that UQPU reduces or functionally replaces a DRAM-backed memory role must record, when applicable:

- required usable capacity;
- sustained and peak workload bandwidth;
- latency or service-time requirement;
- DRAM refresh and idle/standby energy;
- active-access and data-movement energy;
- ECC/reliability/recovery requirements;
- physical footprint and packaging;
- amortized memory cost per accepted useful task;
- remaining host/accelerator DRAM required by state preparation, control, decoding and output reconstruction.

Reducing materialized bytes is useful evidence, but it is not by itself a DRAM replacement demonstration.

## Architecture consequence

Lane C is expanded from a shorthand `RAM/VRAM/HBM/storage` description to an explicit volatile-memory hierarchy:

```text
system DRAM/RAM
+ accelerator-local HBM/GDDR/VRAM
+ SRAM/cache
+ persistent storage
+ data movement
        |
        v
semantic replacement / reduction / materialization avoidance
        |
        v
accepted useful workload result + full-stack cost
```

The preferred UQPU route remains semantic: avoid or compress unnecessary classical state where possible rather than assuming a quantum subsystem must reproduce DRAM cells, HBM interfaces or cache microarchitecture one-for-one.

## Non-claims

This clarification:

- does not demonstrate DRAM replacement;
- does not demonstrate RAM/HBM/VRAM/SRAM replacement;
- does not establish a capacity advantage from Hilbert-space dimension;
- does not demonstrate a quantum speedup or economic advantage;
- does not change the existing >=100x or >=100,000,000x targets into demonstrated results.

## Files updated

- `docs/MEMORY_REPLACEMENT.md`
- `docs/LANE_C_STATE_EVIDENCE_CHECKLIST.md`
- `research_lanes/README.md`

## Next research gate

Future memory experiments should report separate ratios for at least:

- `R_capacity`
- `R_bandwidth`
- `R_latency`
- `R_energy`
- `R_cost`
- `R_materialized_bytes`

and should not collapse these into one generic "memory advantage" number unless the workload contract justifies the aggregation.
