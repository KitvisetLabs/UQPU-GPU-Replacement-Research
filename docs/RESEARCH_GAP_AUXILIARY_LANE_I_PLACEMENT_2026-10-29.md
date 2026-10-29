# Research gap — auxiliary root-level Lane I placement and A–H architecture integrity

**Date opened:** 2026-10-29  
**Primary owner:** Lane F — integration/governance  
**Interfaces:** A/C controls and state; D/G devices and manufacturing; E energy/materials; H strategic provenance  
**Status:** OPEN / PATH INVENTORY AND CONTROLLED MIGRATION REQUIRED  
**Evidence class:** repository-architecture observation, not a physical or technology result

## Finding

The canonical directory policy defines exactly eight permanent top-level research lanes A–H and allows special programs to live beneath an owning lane or under `integration/`. The current tree also contains `research_lanes/I_FIELD_AGNOSTIC_CONTACTLESS_VEHICLE_LEVITATION/`. Its README describes a distinct contactless lift/propulsion research track. This is an architecture-placement mismatch; it must not be silently treated as a ninth permanent lane or allowed to replace any A–H lane.

## Preservation rule

Do not delete or move the auxiliary track as a quick fix. Its research artifacts, safety boundaries, provenance, links and tests must be inventoried first. Current descriptions classify its outputs as MODEL_ONLY or research plans; no antigravity, arbitrary-terrain levitation, occupied vehicle, onboard fusion or propulsion performance is demonstrated.

## Unlock criteria

1. Enumerate every file, import, relative link, CI path filter and external reference under the auxiliary directory.
2. Assign each artifact one primary A–H owner. Candidate destination is a nested special-program folder under the most appropriate owning lane, or `integration/` only for genuinely cross-lane system artifacts.
3. Preserve stable IDs and provide migration/redirect notes where old paths are public or referenced.
4. Update imports, links, depth checks and CI filters in one controlled change; verify no artifact was lost.
5. Keep high-voltage, high-field, outdoor, occupied or hazardous experiments behind explicit human authorization and safety review.

## Non-claims

This is a repository-governance gap only. It establishes no levitation/propulsion feasibility, new physics, fusion-to-propulsion capability, economic advantage or mission milestone.
