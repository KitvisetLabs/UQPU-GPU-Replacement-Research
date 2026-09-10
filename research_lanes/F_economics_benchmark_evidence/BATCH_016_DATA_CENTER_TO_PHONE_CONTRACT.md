# Batch 016 — Data-Center-to-One-Phone Measurable Contract

**Date:** 2026-09-10  
**Owner lane:** F — Economics / Benchmark / Evidence / Integration  
**Strategic invariant:** INV-029  
**Status:** EXECUTABLE EVIDENCE CONTRACT / TARGET NOT DEMONSTRATED.

## Problem

The owner's US$10T-US$100T ambition envelope is a strategic scale proxy, not a unit of computation. A dollar number cannot be converted directly into FLOPS, tokens/s, RAM bytes, storage IOPS or useful service quality.

Therefore the project now uses an executable `uqpu.north_star_contract` gate that requires explicit service metrics and an explicit physical device envelope.

## Contract layers

### 1. Service portfolio
Each target data-center service must have explicit metrics with units and direction. Examples include:

- accepted AI outputs/s or tokens/s at fixed model/quality contract;
- accepted optimization tasks/s at fixed solution-quality threshold;
- graphics/media frames/s at fixed quality/resolution;
- scientific/HPC useful outputs/s under validated numerical tolerance;
- application-visible memory/state capacity, bandwidth and latency;
- persistent-storage capacity, read/write throughput, latency, retention and durability;
- network ingress/egress bandwidth and latency;
- reliability/availability/recovery requirements.

Peak FLOPS/TOPS alone cannot establish service equivalence.

### 2. Device envelope
The phone-class end state must state its own thresholds rather than relying on a vague label. The executable contract therefore accepts scenario-defined maximum:

- end-user price in THB;
- device mass;
- physical volume;
- sustained power.

The research program does **not** hard-code arbitrary final mass/volume/power numbers as scientific facts. Each scenario must declare them and preserve provenance.

### 3. Physical-boundary rule
`requires_external_compute=True` automatically prevents the final North-Star claim. A phone may use networking for ordinary service I/O, but required external QPU/server compute cannot be hidden outside the claimed physical-compression boundary.

### 4. Evidence rule
A metric can numerically satisfy its threshold while still failing the final claim if it is simulation/model evidence. `demonstrated=True` requires every service metric and the device result to be measured end-to-end.

## New executable artifact

`software/uqpu-prototype/uqpu/north_star_contract.py`

The module separates:

- numerical threshold satisfaction;
- complete service coverage;
- phone-envelope compliance;
- independence from external compute;
- end-to-end evidence completeness;
- final demonstrated status.

This prevents an attractive modeled number from silently becoming a claim of a US$10T-US$100T-data-center-to-phone achievement.

## NPU integration repair

During this research audit we found two older executable economic artifacts that still reflected the pre-NPU subsystem set:

- `uqpu.moonshot_contract.SUBSYSTEMS` lacked `npu`;
- `ConventionalSystemCost` lacked a dedicated NPU cost component.

Batch 016 corrects both. The 100M-unit executable moonshot now covers GPU, CPU, **NPU**, RAM, VRAM and storage, and full-stack conventional economics can account for NPU cost separately.

## Next measurable gates

1. define a small real data-center **service portfolio**, not a dollar proxy;
2. ingest competitive CPU/GPU/NPU measured baselines for those services;
3. add memory/storage/network service contracts;
4. run the identical useful-output contracts through UQPU simulation and authorized real-QPU paths;
5. progressively measure physical support burden and eliminate hidden external infrastructure;
6. only after broad service equivalence exists, evaluate device-level integration scenarios.

## Evidence boundary

The existence of an executable contract does not demonstrate the North Star. It makes the claim harder to fake and converts the mission into a sequence of falsifiable measurements.
