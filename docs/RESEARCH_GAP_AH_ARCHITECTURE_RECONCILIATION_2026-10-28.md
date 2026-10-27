# Research gap — reconcile canonical A–H architecture with legacy A–I manifest

**Opened:** 2026-10-28  
**Owner:** Lane F — evidence/integration/release gate; all A–H lanes reviewed  
**Status:** OPEN / GOVERNANCE_AND_SYNC_DEBT / NO SCIENTIFIC CLAIM  
**Related:** INV-024, INV-028, INV-029–035, RESEARCH OPERATING SYSTEM, lane directory policy, PR #144/#145

## Finding from the current main tree

The canonical Research Operating System, research_lanes/README.md, research_lanes/LANE_DIRECTORY_POLICY.md and integration/LANE_INTERFACE_CONTRACT.md define exactly eight permanent operational lanes, A–H. However, integration/eight_lane_manifest.json still declares schema uqpu-nine-lane-manifest-v2, enumerates A–I and all 36 lane pairs, and includes Lane I for field-agnostic contactless vehicle lift/propulsion. The main tree also contains multiple legacy/alias lane folders for some B–G areas, plus research_lanes/I_FIELD_AGNOSTIC_CONTACTLESS_VEHICLE_LEVITATION. docs/NINE_LANE_SCOREBOARD_2026-10-16.md retains an active-sounding nine-lane title. Open PR #144 updates that scoreboard; PR #145 carries a pending-main summary.

This is a real documentation/governance inconsistency. It is not evidence that the Lane I workstream is invalid, and it is not permission to delete or silently forget that work.

## Required resolution

1. Preserve all existing Lane I files, source references, tests, and evidence as history or an explicitly named supplemental workstream until the owner chooses its operational home.
2. Make A–H the only permanent operational lane map, consistent with INV-024 and the current Research Operating System.
3. Replace the nine-lane manifest with a versioned eight-lane schema and the 28 unordered A–H pairs. Keep any Lane I/vehicle/levitation scope in a separate supplemental-workstream field or a separately named cross-cutting program, not as lane I.
4. Identify the canonical B/C/D/E/F/G folders and mark legacy aliases explicitly. Do not bulk-delete or move folders until imports, references, ownership, reproducibility hashes and CI have been checked.
5. Retitle the legacy nine-lane scoreboard as historical/superseded, or add a clear banner that it is not the current operational scoreboard.
6. Update the manifest validator and cold-start audit together; require exact A–H coverage, no missing lane, no duplicate primary ownership, and depth <=16.
7. Reconcile PR #144/#145 and all append-only changes without dropping any prefix, failed run, Lane I result, multilingual strategic reference or funding/AI-agent reference.

## Acceptance criteria

- One machine-readable canonical manifest lists exactly A–H and 28 unordered pair interfaces.
- Lane I work is still discoverable but explicitly not represented as a ninth permanent lane.
- CI proves A–H folder and manifest agreement and allows declared legacy aliases only through an explicit compatibility map.
- README and cold-start handoff point to the same canonical architecture.
- All permanent root directives 00/00A/01–06, INV-025–035, FND-001–006, EQN-001–006, BIO-001, FUS-001 and FIN-001 remain present.
- No historical evidence, research result, or multilingual master-plan link is deleted during reconciliation.

## Current decision boundary

This cycle did not rewrite the manifest, lane directories, legacy scoreboard, WORKLOG.md or RESEARCH_GAPS.md. Those changes require a coordinated migration and regression tests, not a broad text replacement. The dated Batch 088 and integration report record the sync debt; this gap is the canonical governance task.

**Next gate:** resolve this discrepancy before merging any PR that changes the operational lane scoreboard or cold-start manifest. Do not silently upgrade A–H to A–I.
