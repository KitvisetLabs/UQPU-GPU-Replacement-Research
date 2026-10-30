# Lane B contract — Mamba neural QEC decoder transfer

**Date:** 2026-10-30 · **Primary owner:** Lane B · **Work item:** QEC-MAMBA-001  
**Interfaces:** A logical-output workload; C syndrome/state bytes; D device/noise provenance; F evidence/economics; G controller/accelerator; H publication.  
**Status:** LITERATURE_ONLY / GATE 0 NOT RUN.

## Source identity

Lee, Hur & Park, *npj Quantum Information* (2026-10-28), DOI 10.1038/s41534-026-01403-y; preprint arXiv:2510.22724v1. Keep publisher and preprint result scopes separate until full-text reconciliation.

## Input/output contract

Each frozen shot record binds source/data hash, device, patch, distance, X/Z basis, cycles, syndrome/detection events, detector-error model, logical-label rule, raw shot/group identity, split and calibration provenance. Output is the experiment-specific logical observable/error prediction with explicit invalid/abstention state. Memory, modeled real-time and controller deadline outcomes are separate metrics.

## Baselines

1. Source-faithful Mamba and Transformer.
2. MWPM on identical shots and detector-error model.
3. Tensor-network comparison where labels/data are source-compatible.
4. Separate source-specific injected decoder-noise simulation.
5. Separate measured target/controller arm using actual latency; never substitute modeled p_dec for measured latency.

## Resource/cost record

Record training/fine-tuning iterations and accelerator hours; inference CPU/GPU/FPGA/NPU time; model/checkpoint and hidden-state bytes; syndrome/buffer bytes; peak RAM/VRAM; host-device transfer; p50/p95/p99/worst latency; sustained throughput; deadline misses; retries; reconstruction; measured energy boundary; and cost per accepted logical correction. Unknown values are NOT_MEASURED, never zero.

## Acceptance/falsification

Require source-version reconciliation, asset/license/hash verification, exact baseline reproduction, same-shot baselines, no split leakage, group-disjoint tests, uncertainty intervals, actual target deadline and full resource accounting. Reject if latency tails miss cadence, logical quality fails, or all-in cost erases the gain.

Public-data/local reproduction first. No provider call or paid QPU job is needed or authorized.
