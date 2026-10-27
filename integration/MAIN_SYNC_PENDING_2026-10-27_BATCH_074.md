# Main-branch sync record — Batch 074 (pending review)

**Date:** 2026-10-27  
**Canonical main SHA at work start:** `3ffe242d25be42c5a4ac3c23fe5375bd3c8ac2df`  
**Research PR:** [#142 — Batch 074: independent parity references and symbolic-ensemble materials watch](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/pull/142)  
**Source branch:** `research/2026-10-27-gf2-parity-symbolic-ensemble`  
**Source head:** `67e41a885f27892b9d383956d8db40675293fd46`  
**Sync status:** `PENDING_REVIEW` — no claim that source work has merged to main.

## Source commits

The source branch contains these commits, all reachable from source head `b3fb93b7f8b1d6edfb4e24baecfd15825293862d`:

1. `ed1096d324ba35254e1c081e903917cb4fd68fcc` — add independent GF(2) and signed parity objective checks.
2. `5625039ec3d786220578fc34fcd8b9102f6c5e49` — record symbolic-ensemble interatomic-potential literature.
3. `5c8e1ad8ece1a88023758ce428d80e3644a8b8f6` — open falsifiable symbolic-potential reproduction/carbon-transfer gap.
4. `ef971dd5cea428b96dceaeb55628f11f149bff4f` — publish Batch 074.
5. `e176ef22c9d5792921c23c6590f06d15df0d15d6` — publish Eight-Lane integration record.
6. `ba311e3f4a88228f323ead5cb0f3b51d962b7129` — add stable cross-lane integration edge.
7. `4bec529b16cb5b8fad7ccfc7bcd65083de6b2539` — correct exhaustive graph-count comment.
8. `fce928f76421cfcac0a9ab2fc87296c782f725a6` — index Batch 074 in README.
9. `fb8cea2921d362b62ea90d9fb8cae6312e031484` — append Batch 074 to WORKLOG.
10. `4b5f659d8c7cf96d63bbc9eade743c88201b2151` — append material and parity gaps from complete fetched snapshot.
11. `b3fb93b7f8b1d6edfb4e24baecfd15825293862d` — refresh the cold-start handoff manifest.
12. `67e41a885f27892b9d383956d8db40675293fd46` — record the cold-start trailer correction; the commit message includes `Research-Sync: pending-main`.

## Files and substantive delta

- `software/uqpu-prototype/tests/test_parity_encoding_reference.py`: independent bit-packed GF(2) rank, all labelled simple graphs with 1–5 vertices, cycle-incidence and signed-edge objective checks.
- `docs/literature_watch/2026-10-27-symbolic-ensemble-interatomic-potentials.md` and `docs/RESEARCH_GAP_PANGOLA_SYMBOLIC_POTENTIAL_TRANSFER_2026-10-27.md`: peer-reviewed aluminum-potential method, source limits and falsifiable aluminum-first reproduction gate.
- `docs/BATCH_074_GF2_PARITY_AND_SYMBOLIC_ENSEMBLE.md`, `integration/DAILY_CYCLE_2026-10-27_GF2_PARITY_AND_SYMBOLIC_ENSEMBLE.md`, and `integration/INT-20261027-SYMBOLIC-ENSEMBLE-MATERIALS.json`: batch, cross-lane integration and stable ID.
- `README.md`, `WORKLOG.md`, `RESEARCH_GAPS.md`, `integration/COLD_START_HANDOFF_MANIFEST.json`: discoverability, gap ledger and next-agent handoff.

## CI and evidence boundary

At record creation, PR #142 exact-head Actions for source SHA `b3fb93b7f8b1d6edfb4e24baecfd15825293862d` were queued. Cold-start audit [40486846870](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40486846870) then failed closed because that commit message lacked the required `Research-Sync: pending-main` trailer; this was a handoff-governance failure, not a scientific test. Follow-up source head `67e41a885f27892b9d383956d8db40675293fd46` adds the required trailer and triggers new exact-head checks. Core workflow for the new head is still pending at this record update; inspect the new run before promoting test evidence. The literature item remains `LITERATURE_ONLY`; no parity-QAOA circuit, QPU execution, material substitution, new physical law, fuel/fusion/electricity/finance result, or Data-Center-to-Phone achievement is claimed.

This record is intentionally a separate PR so the canonical main branch can review and account for the source work without bypassing the project's synchronization policy. Once PR #142 is merged or closed, update this record with the exact disposition and reconcile any remaining sync debt.