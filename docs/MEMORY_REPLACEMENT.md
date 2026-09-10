# UQPU Memory-System Replacement Research

## Expanded mission

The UQPU project treats the conventional memory hierarchy as part of the replacement target, but uses a **role-based taxonomy** rather than treating DRAM as an independent peer subsystem.

The long-term system objective is not merely:

```text
GPU -> UQPU
```

but:

```text
CPU/GPU/NPU + volatile memory hierarchy + persistent storage + data movement
        |
        v
UQPU + quantum/native state architecture + only the classical memory/storage still required
```

with explicit research into reducing or replacing the functional/economic roles of system RAM, accelerator-local memory, cache/SRAM and persistent storage where workload semantics permit it.

## Memory taxonomy

### Role 1 — System / host volatile memory

Typical present-era technologies include:
- DDR-class DRAM;
- RDIMM/MRDIMM server memory;
- LPDDR-class system memory;
- other DRAM-derived host-memory implementations.

### Role 2 — Accelerator-local volatile memory

Typical technologies include:
- HBM;
- GDDR / graphics VRAM;
- other high-bandwidth accelerator-local DRAM implementations.

### Role 3 — On-chip volatile memory

Typical technologies/functions include:
- SRAM caches;
- scratchpads;
- register files;
- local buffering.

### Role 4 — Persistent storage

Typical technologies include:
- SSD / NAND flash tiers;
- HDD;
- other nonvolatile storage systems.

**Important taxonomy rule:** `DRAM` is a memory-technology family, not a separate peer role beside RAM, VRAM or HBM. HBM and GDDR are themselves DRAM-family technologies, while system RAM is commonly implemented with DDR/LPDDR-class DRAM. UQPU claims must therefore state both the conventional memory **role** being replaced/reduced and the baseline **technology** used for comparison.

## Why memory is a first-class target

Modern data-center AI/HPC systems spend substantial silicon area, power, packaging complexity and cost on memory capacity and bandwidth. DRAM-class systems also introduce refresh/standby energy, latency, data movement and memory-controller/interconnect costs that must be included when material to the workload.

Current AI data-center architectures rely on combinations of:
- HBM close to accelerators;
- DDR/RDIMM/MRDIMM system memory;
- LPDDR-derived server memory in emerging designs;
- SRAM/cache tiers;
- SSD/storage tiers.

The UQPU project therefore measures **compute + memory + movement + persistence** as one economic system.

## Replacement scope

### Accelerator-local VRAM/HBM/GDDR functional role

UQPU must investigate alternatives for:
- model/tensor working sets;
- high-bandwidth accelerator-local data;
- temporary activations;
- KV cache;
- framebuffer and graphics working sets;
- scientific arrays;
- simulation state;
- queues and intermediate buffers.

### System RAM / DRAM functional role

UQPU research should reduce system-memory demand when semantic compression, quantum state reuse, generative loading, sparse/implicit representations or alternate execution graphs make this possible.

A serious system-DRAM replacement claim must compare at least:
- required usable capacity;
- sustained/peak workload bandwidth;
- access latency or service time;
- refresh and idle/standby power where applicable;
- active-access/data-movement energy;
- reliability/ECC and recovery requirements where applicable;
- physical footprint and packaging;
- amortized memory-system cost per accepted useful task.

The project does **not** assume that all classical DRAM or RAM can disappear. Classical host control, input/output, exact data storage, buffering and fault recovery may still require conventional memory.

### SRAM/cache role

On-chip SRAM/cache is tracked separately because low-latency cache/register behavior is not equivalent to bulk DRAM capacity. A system that eliminates host DRAM but requires very large conventional SRAM must count that SRAM area, leakage/active power and cost honestly.

## Proposed memory hierarchy

```text
Persistent storage / dataset
          |
          v
Classical staging memory (DDR/LPDDR/HBM/GDDR/SRAM as required)
          |
          v
State preparation / semantic encoder
          |
          +----------------------+
          |                      |
          v                      v
Quantum/native working state  Compact classical cache
          |
          v
Long-lived logical state / reusable representation
          |
          v
Measurement / decode
          |
          v
Classical output buffer / persistence tier
```

## QVRAM / QMEM research concepts

The project uses the terms:

- **QMEM** — generic quantum/native working-memory or state-service subsystem.
- **QVRAM** — functional replacement target for accelerator-local VRAM/HBM/GDDR roles.
- **QHBM** — hypothetical high-bandwidth quantum/native memory interface.

These are research abstractions, not claims that present-day QPUs possess drop-in DRAM, HBM or VRAM equivalents.

## Cost model

The conventional baseline should increasingly be measured as a full system stack:

[
C_{baseline/task}
=
C_{compute}
+
C_{system-DRAM}
+
C_{HBM/GDDR}
+
C_{SRAM/cache}
+
C_{persistent-storage}
+
C_{memory-energy}
+
C_{data-movement}
+
C_{interconnect}
+
C_{cooling}
]

UQPU target:

[
A_C = C_{baseline/task}/C_{UQPU-stack/task}
]

Research targets remain:

- at least **100×** lower total cost/task;
- up to **100,000,000×** lower total cost/task as a workload-specific moonshot.

These are targets, not demonstrated capabilities.

## Memory-specific benchmark metrics

Every serious benchmark should report, when applicable:

- input bytes;
- output bytes;
- peak system DRAM/RAM capacity;
- peak accelerator-local HBM/GDDR/VRAM capacity;
- peak on-chip SRAM/cache footprint when material;
- memory technology and configuration used by the baseline;
- sustained and peak memory bandwidth relevant to the workload;
- access latency/service-time assumptions;
- bytes moved between tiers;
- state-preparation bytes;
- quantum-state reuse factor;
- classical-materialization bytes avoided;
- DRAM refresh/idle energy;
- active memory/data-movement energy;
- memory-system cost/task;
- memory share of total cost.

## Key research hypothesis

The largest advantage may not come from replacing a memory chip one-for-one.

It may come from **changing the computation so that large intermediate classical representations never need to exist**.

Example:

```text
Conventional:
DRAM/RAM -> HBM/GDDR -> tensor A -> tensor B -> tensor C -> output

UQPU semantic path:
encoded input -> quantum/native state evolution -> selected observable -> output
```

If intermediate tensor materialization is avoided, compute, DRAM footprint and memory traffic may fall simultaneously. This is a workload-specific hypothesis that must be measured rather than assumed.

## Hard limits

Quantum state dimension must not be confused with directly readable classical capacity.

An n-qubit state can mathematically occupy a 2^n-dimensional Hilbert space, but it does not provide free random access to 2^n classical values.

All QVRAM/QMEM proposals must state:
- loading mechanism;
- address/access model;
- coherence assumptions;
- read/write semantics;
- measurement requirements;
- error correction;
- lifetime;
- bandwidth;
- latency/service semantics;
- energy;
- physical footprint;
- classical DRAM/SRAM/storage still required around the quantum subsystem.

## Research direction

1. model system DRAM, HBM/GDDR, SRAM/cache and persistent storage as explicit baseline costs;
2. add memory role + technology tags to workload/economic contracts;
3. add memory pressure to semantic IR;
4. estimate classical intermediate materialization;
5. reward whole-graph plans that avoid materialization;
6. investigate state reuse and quantum-native compressed representations;
7. build cloud-QPU benchmark cases where input/output is small relative to internal computation;
8. identify workloads where DRAM/memory replacement is impossible or uneconomic;
9. preserve all negative results.
