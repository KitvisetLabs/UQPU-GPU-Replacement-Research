# Pending-main sync — FND-005 false-vacuum simulator literature watch

**Date:** 2026-10-26  
**Canonical main base SHA:** 5fbe3d295ad6ca5b7c701f05c64899829910cbe8  
**Source PR:** #114 — FND-005: watch cold-atom gauge-theory pair-production experiment  
**Source branch:** research/2026-10-26-fnd005-false-vacuum-watch  
**Source head at sync-record creation:** 05fd7a8f2dc2add43726af8187c1f5e9b7d0676f  
**Work item:** FND005-FVD-001  
**Integration record:** INT-FND005-FALSE-VACUUM-20261026-001  
**Status:** PENDING_MAIN_REVIEW; source article is not yet canonical main.

## Source and scope

Zhu et al., “Probing False Vacuum Decay on a Cold-Atom Gauge-Theory Quantum Simulator,” *Physical Review Letters* 137, 141601 (published 2026-10-01), DOI 10.1103/vhnm-j9bw. The article reports a cold-atom analog simulation of out-of-equilibrium pair-production dynamics in a 1+1D U(1) lattice-gauge quantum-link model. It is not a direct observation of cosmological false-vacuum decay or pair production in empty space.

## Source branch artifacts

- docs/literature_watch/2026-10-26-false-vacuum-decay-cold-atom-gauge-theory-simulator.md
- integration/INT-FND005-FALSE-VACUUM-20261026-001.json

## Evidence and CI boundary

The paper is a PUBLISHED_EXPERIMENT in an analog-simulator platform; for UQPU it remains LITERATURE_ONLY. No independent reproduction, real-QPU run, quantum advantage, new physical law, material/fuel/fusion economics or mission-level result is claimed. Exact-head CI is pending; do not promote queued workflows to pass.

## Invariants and next gate

INV-025/026/027 and INV-029–035 remain preserved. Next gate: source-exact small-lattice reproduction, independent exact-diagonalization/MPS references, held-out parameter/lattice checks and counterexample controls. No paid QPU job is authorized.

After review/merge, map all source SHAs to the resulting main SHA. This sync record does not claim the source article is already on main.
