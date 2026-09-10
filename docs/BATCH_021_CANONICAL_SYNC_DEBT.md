# Batch 021 — Canonical Sync Debt

**Date:** 2026-09-10  
**Status:** EXPLICIT GOVERNANCE DEBT / NO SCIENTIFIC CLAIM

Batch 021 has been published in the root strategies, project charter, version invariants, goals, README, strategic master plan, lane-specific research tracks, executable software and CI tests.

Some long append-only canonical history files are currently behind the newest batch chronology:

- `docs/EIGHT_LANE_SCOREBOARD.md` currently ends at an older batch and requires safe reconciliation through Batch 021;
- `WORKLOG.md` requires a Batch 021 historical entry;
- `RESEARCH_GAPS.md` should formally add BIO-001, FUS-001 and FIN-001 plus the latest real-QPU gate state;
- `DECISIONS.md` should formalize the decisions that accepted liquid-fuel function, net delivered fusion electricity and the principal-vs-rate financing distinction are permanent evidence rules.

The connector updates these files by full replacement. They must **not** be overwritten from a truncated fetch merely to make the batch number look current. Until a safe full-content reconciliation is performed, this document records the debt explicitly rather than risking loss of project history.

Canonical scientific/strategic state for the new pillars is already preserved in:

- `02_ULTRA_LOW_COST_BIOMASS_BIO_OIL_STRATEGY.md` / INV-031;
- `03_FUSION_ELECTRICITY_COST_STRATEGY.md` / INV-032;
- `04_INTEREST_COST_AND_RND_FINANCE_STRATEGY.md` / INV-033;
- `docs/BATCH_021_BIO_OIL_FUSION_INTEREST_COST.md`;
- `research_lanes/E_materials_energy_cooling_infrastructure/ULTRA_LOW_COST_BIO_OIL_RESEARCH_TRACK.md`;
- `research_lanes/E_materials_energy_cooling_infrastructure/FUSION_ELECTRICITY_COST_RESEARCH_TRACK.md`;
- `research_lanes/F_economics_benchmark_evidence/INTEREST_COST_RND_FINANCE_CONTRACT.md`;
- `software/uqpu-prototype/uqpu/energy_finance.py`.

**Next governance action:** reconcile the large append-only history files from a complete, non-truncated source while preserving every earlier entry, then remove only the resolved debt statements—not the scientific history.