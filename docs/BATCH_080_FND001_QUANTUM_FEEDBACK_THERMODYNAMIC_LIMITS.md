# Batch 080 — FND-001 quantum-feedback thermodynamic limits

**Date:** 2026-10-27  
**Starting main SHA:** `140f9d788aae2230b8c50c79ec2cdae8fdf8adeb`  
**Primary technical owner:** Lane A — equation reconstruction and reference contract  
**Evidence/accounting owner:** Lane F  
**Publication owner:** Lane H  
**Cross-lane review:** A–H explicitly; specialized Lane I checked and not materially coupled to this source  
**Evidence class:** PEER_REVIEWED_THEORY / OFFICIAL PREPRINT; not a UQPU reproduction

## Research question

How should UQPU represent thermodynamic work bounds when a controller has quantum side information, without treating information as free or confusing extractable work with whole-device energy and accepted-task cost?

## Fresh literature surveillance

Ji, Gour and Wilde, “Fundamental limits for thermodynamic control with quantum feedback,” was accepted by *Physical Review Letters* on 2026-10-06. The official APS record is [DOI 10.1103/x67n-33gr](https://doi.org/10.1103/x67n-33gr); the official preprint is [arXiv:2503.09012v4](https://arxiv.org/abs/2503.09012v4), posted 2026-10-09. The authors derive tight single-shot bounds on work of formation and extractable work conditioned on arbitrary quantum side information and an asymptotic conditional-free-energy formulation. The abstract states that acquisition, processing and reset of side information restore consistency with the traditional second law.

This is a material theoretical/accounting lead, not a new law of nature or an experimentally demonstrated technology advantage.

## Work completed

- Published a source-pinned literature watch with evidence class, actual novelty, limitations and cross-lane relevance.
- Opened RG-FND001-QUANTUM-FEEDBACK-WORK-BOUNDARY-001 with a pinned-source and small-system reproduction plan.
- Recorded why a guessed arithmetic implementation is deferred until theorem conventions and equations are independently reconstructed.
- Added a dated integration record and machine-readable integration edge.
- Updated README, WORKLOG and the cold-start handoff manifest in the same commit.
- Did not modify the large append-only `RESEARCH_GAPS.md`; the focused gap is canonical and aggregate sync debt remains visible.

## Lane A–H review

- **A — Quantum programming/workloads/compiler/runtime:** the next task is a finite-dimensional reference fixture with pinned assumptions, sign conventions and limiting cases. No guessed net-work helper was added.
- **B — Cloud/QPU/provider integration:** theorem variables are not provider measurements; no paid job or target claim.
- **C — RAM/VRAM/HBM/storage/data movement:** quantum side information is not automatically classical-readable memory. Controller storage, measurement records and transfer must be separate ledger entries.
- **D — Devices/chips/fabrication/packaging:** no device result; future mapping needs target-specific control/readout/reset data.
- **E — Biomass/materials/bio-oil/fusion/cooling:** only the general thermodynamic boundary discipline transfers; no material, fuel or fusion evidence.
- **F — Economics/evidence/integration:** keep work, heat, wall-plug energy and currency separate; require common boundary and non-double-counted terms.
- **G — Manufacturing equipment/factory systems:** no yield or cost-per-good-device implication; future control-electronics overhead requires measurements.
- **H — Strategy/publication:** official primary-source watch and gap are now available to a cold-start contributor.
- **Specialized Lane I:** inspected via the canonical lane manifest; no credible causal link to the current theorem was found, so no artificial integration is claimed.

## FND/EQN and permanent invariants

- **FND-001:** adds a new theorem-reconstruction target for conditional work bounds; no thermodynamic measurement or new lower bound from UQPU.
- **FND-002:** no output-information lower bound changed.
- **FND-003:** no matched speed-limit experiment changed.
- **FND-004/005/006:** no new physical primitive, particle mechanism or mathematics discovery promoted.
- **EQN-001–006 / INV-034–035:** theory is bound by its assumptions; no candidate equation is promoted to physical law.
- **INV-029:** no phone-boundary compression milestone.
- **INV-030/031:** no Pangola material or accepted-liquid result.
- **INV-032:** no net delivered fusion electricity result.
- **INV-033:** no measured interest or WACC reduction.
- **INV-025–027:** moonshots and open-frontier constraints remain unchanged.

## CI and evidence

At the start of this cycle, main was `140f9d788aae2230b8c50c79ec2cdae8fdf8adeb`. Prototype/invariant workflow [#1814](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40511317314) passed all 15 jobs, including Python 3.10/3.11/3.12 and extended QSP/QSVT/Qiskit/reference checks. Cold-start audit [#1022](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40511317225) passed. These checks validate the starting head, not this new commit; exact-head CI for Batch 080 remains a gate after publication.

## Highest-value next gate

Pin and independently reconstruct the paper's equations and operational conventions; freeze small-system test cases; compare against exact finite-dimensional references and known limiting cases; then implement only the validated reference contract. Keep ergotropy SDP reproduction, Helios QEC reproduction, EQN-008 matched comparison, BIO-001 and FUS-001 open.
