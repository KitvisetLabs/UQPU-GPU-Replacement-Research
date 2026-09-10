# Lane Directory and Depth Policy

1. The project has eight permanent lane folders under `research_lanes/`, A through H.
2. Every substantive research artifact should have one primary lane owner, even when it integrates multiple lanes.
3. Special future programs may create nested subfolders under the owning lane, or under `integration/` for genuinely cross-lane system work.
4. **Maximum directory nesting is 16 levels from repository root.** A file that would exceed the limit must be reorganized before merge.
5. Prefer semantic folder names over dates alone. Batch/date folders may be used below a subject area when useful.
6. Avoid duplicate sources of truth. Cross-reference canonical artifacts instead.
7. Existing canonical paths remain valid during migration. Move executable artifacts only with corresponding import/link/test/CI updates or compatibility shims.
8. Every integrated research batch explicitly inspects all A-H lanes and uses the interface contract under `integration/`.
9. Lane A remains Priority #1, but folder ownership never suspends parallel A-H research.
10. Cross-lane integration is a design requirement: work packages should expose machine-readable identifiers and measurable interfaces wherever practical.
