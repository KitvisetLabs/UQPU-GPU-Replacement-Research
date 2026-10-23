# INT-20261023-001 — FND-QFI-001 analytic audit interface

**Status:** TESTED_LOCALLY / PR_PENDING  
**Primary owner:** Lane A  
**Participants:** Lane B (no-submit boundary), Lane C (information/storage semantics), Lane F (evidence and cost accounting), Lane H (literature provenance); cross-cutting FND-002/FND-003/FND-006 and EQN-001/004/005.

## Inputs and stable contract

- Source preprint: arXiv:2610.29146v1, submitted 2026-10-21.
- Implementation: software/uqpu-prototype/uqpu/qfi_ancilla_transfer_audit.py.
- Frozen model result: benchmarks/results/fnd-qfi-001-ghz-analytic-audit.json.
- Detailed primary-owner report: docs/FND_QFI_001_GHZ_ANALYTIC_AUDIT_2026-10-23.md.
- Contract ID: FND-QFI-001.
- Evidence class: MODEL_ONLY.

## Interface and nonclaims

The audit emits system size, ancilla dimension, phase, theoretical system QFI, direct-measurement CFI, distinct nonzero score-class count m, the boolean precondition m > n, formula-check status, and explicit zero provider jobs/shots with null energy/cost. It does not emit an “advantage” flag and does not infer readable classical memory from a Hilbert-space dimension.

## Lane handoff

- A owns the implementation and exact small-state follow-up.
- B keeps all provider execution disabled; no credentials or target calls are required for this audit.
- C treats this as parameter-information accounting, not RAM/VRAM/HBM/storage capacity.
- D/G receive no device/fabrication requirement until a physical target and measured resource contract exist.
- E receives no biomass/material/fuel/fusion claim.
- F preserves evidence labels and leaves measured energy, cost, shots and provider usage null.
- H preserves source provenance and the staged-finance/publication discipline.
- INV-034/035 feed every lane; the current physical model remains binding and generated equations are not laws by declaration.

## Acceptance gate

Local focused tests passed 6/6 on CPython 3.13.5. Hosted CI, the broader suite, independent density-matrix reproduction, counterexample search and independent review remain pending. No paid QPU job or funding action is authorized.
