# Batch 024 — Governance Sync Note

**Date:** 2026-09-10  
**Purpose:** preserve new decisions/gaps without risking truncation of large append-only canonical files through the connector.

## Pending decision D096 — A gate duration alone cannot establish a quantum-speed-limit gap

A physical `observed duration / quantum speed limit` ratio requires matched quantities for the same evolution and a justified theorem. Saved instruction duration alone is insufficient. For the standard orthogonal-state Margolus–Levitin expression, the required mean energy above ground must be measured or defensibly derived for the same physical evolution. External pulse/control/cryo/wall-plug energy remains a separate economic quantity.

**Reason:** substituting a resonance frequency, drive power, instruction duration or wall-plug energy into the wrong theoretical quantity can create arbitrarily misleading speedup factors.

## Pending decision D097 — Output semantics, not Hilbert-space dimension, define the classical egress floor

For exact identification of one arbitrary outcome among `M` distinguishable possibilities, use the fixed-length counting floor `ceil(log2 M)` bits. For error-tolerant uniformly distributed identity tasks, Fano's inequality may provide a mutual-information lower bound when its assumptions are explicit.

**Reason:** this simultaneously prevents two errors: claiming exponentially many readable classical memory values from an n-qubit state, and unnecessarily requiring a quantum algorithm to materialize its entire internal state when the application only needs a compact result.

## Pending research gap RG-029 — Matched physical energy/timing for FND-003

**Status:** DATA_BLOCKED / NOT_YET_MEASURED  
**Objective:** obtain state/Hamiltonian/energy/timing evidence sufficient to compute a physically valid control-to-quantum-speed-limit ratio for one frozen evolution.  
**Blocker:** current saved target snapshot provides instruction durations but not the matched mean energy above ground or theorem applicability evidence.  
**Unlock:** one reproducible backend/device experiment satisfying `FND_003_CONTROL_ENERGY_MEASUREMENT_CONTRACT.md` with uncertainty and provenance.

## Pending research gap RG-030 — Measured output-information / reconstruction accounting

**Status:** SOFTWARE_CONTRACT_READY / MEASUREMENT_OPEN  
**Objective:** carry application-visible output-information requirements into classical and QPU benchmark artifacts, then measure actual output bytes, decoding/reconstruction time, network transfer and storage where applicable.  
**Current evidence:** executable zero-error counting and Fano-derived bounds only.  
**Unlock:** the same useful-output contract contains required information semantics and measured egress/reconstruction values for both the competitive conventional path and UQPU path.

## Canonical sync rule

Append D096/D097 to `DECISIONS.md` and RG-029/RG-030 to `RESEARCH_GAPS.md` only when the full current canonical file can be read and rewritten without truncation. Until then this note is the lossless source for later reconciliation. Do not overwrite canonical history with a partial connector read.
