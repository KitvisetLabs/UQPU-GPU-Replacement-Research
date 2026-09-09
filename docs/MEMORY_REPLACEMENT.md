# UQPU Memory-System Replacement Research

## Expanded mission

The UQPU project now treats the conventional accelerator memory hierarchy as part of the replacement target.

The long-term system objective is not merely:

```text
GPU -> UQPU
```

but:

```text
GPU + VRAM/HBM + accelerator-local memory traffic
        |
        v
UQPU + quantum/native memory architecture
```

with additional research into reducing dependence on large conventional system RAM where workload semantics permit it.

## Why memory is a first-class target

Modern data-center AI/HPC systems spend substantial silicon area, power, packaging complexity and cost on memory capacity and bandwidth.

Current AI data-center architectures rely on combinations of:
- HBM close to accelerators;
- DDR/RDIMM/MRDIMM system memory;
- LPDDR-derived server memory in emerging designs;
- SSD/storage tiers.

The UQPU project therefore measures **compute + memory + movement** as one economic system.

## Replacement scope

### VRAM/HBM functional role

UQPU must investigate alternatives for:
- model/tensor working sets;
- high-bandwidth accelerator-local data;
- temporary activations;
- KV cache;
- framebuffer and graphics working sets;
- scientific arrays;
- simulation state;
- queues and intermediate buffers.

### System RAM role

UQPU research should reduce system-RAM demand when semantic compression, quantum state reuse, generative loading or alternate representations make this possible.

The project does **not** assume that all classical RAM can disappear. Classical host control, input/output and exact data storage may still require RAM.

## Proposed memory hierarchy

```text
Persistent storage / dataset
          |
          v
Classical staging memory
          |
          v
State preparation / semantic encoder
          |
          +----------------------+
          |                      |
          v                      v
Quantum working memory       Compact classical cache
          |
          v
Long-lived logical state
          |
          v
Measurement / decode
          |
          v
Classical output buffer
```

## QVRAM / QMEM research concepts

The project uses the terms:

- **QMEM** — generic quantum/native working-memory subsystem.
- **QVRAM** — functional replacement target for accelerator-local VRAM/HBM.
- **QHBM** — hypothetical high-bandwidth quantum/native memory interface.

These are research abstractions, not claims that present-day QPUs possess drop-in VRAM equivalents.

## Cost model

GPU baseline should increasingly be measured as a **system stack**:

[
C_{GPU-stack/task}
=
C_{GPU}
+
C_{VRAM/HBM}
+
C_{host-RAM}
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
A_C =
C_{GPU-stack/task}/C_{UQPU-stack/task}
]

Research targets remain:

- at least **100×** lower total cost/task;
- up to **100,000,000×** lower total cost/task as a workload-specific moonshot.

## Memory-specific benchmark metrics

Every serious benchmark should report:

- input bytes;
- output bytes;
- peak accelerator-local memory;
- peak host RAM;
- memory bandwidth used;
- bytes moved between tiers;
- state-preparation bytes;
- quantum-state reuse factor;
- classical-materialization bytes avoided;
- memory energy;
- memory cost/task;
- memory share of total cost.

## Key research hypothesis

The largest advantage may not come from replacing a memory chip one-for-one.

It may come from **changing the computation so that large intermediate classical representations never need to exist**.

Example:

```text
Conventional:
RAM -> HBM -> tensor A -> tensor B -> tensor C -> output

UQPU semantic path:
encoded input -> quantum/native state evolution -> selected observable -> output
```

If intermediate tensor materialization is avoided, both compute and memory traffic can fall simultaneously.

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
- energy;
- physical footprint.

## Research direction

1. model VRAM/HBM + RAM as explicit GPU baseline costs;
2. add memory pressure to semantic IR;
3. estimate classical intermediate materialization;
4. reward whole-graph plans that avoid materialization;
5. investigate state reuse and quantum-native compressed representations;
6. build cloud-QPU benchmark cases where input/output is small relative to internal computation;
7. identify workloads where memory replacement is impossible or uneconomic;
8. preserve all negative results.
