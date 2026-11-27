# Repository Boundaries and Split Plan

**Date:** 2026-11-27  
**Status:** PROPOSED ARCHITECTURE — no repository has been created, transferred, or migrated by this document.  
**Purpose:** Separate genuinely independent projects into their own GitHub repositories while keeping the UQPU system research coherent and reproducible.

## Decision rule

Create a separate repository when a workstream has its own mission, deliverables, contributors, release cadence, safety/governance needs and can be understood without the parent project's full codebase. Keep a workstream inside UQPU when its primary output is an input to the UQPU system and it shares core workload, hardware, evidence, benchmark and integration contracts.

Do not split merely because a topic has a separate folder. Avoid duplicated sources of truth: each artifact must have one canonical home; other repositories link to a pinned commit/release or a stable integration contract.

## Proposed repository map

| Workstream | Canonical home recommendation | Decision | Rationale / boundary |
|---|---|---|---|
| UQPU core: quantum software/runtime, cloud QPU, memory/data movement, device/chip, materials/energy/cooling, benchmarks/economics, manufacturing, strategy | `KitvisetLabs/UQPU-GPU-Replacement-Research` | KEEP AS ONE REPOSITORY | The eight A–H lanes share a single system mission and explicit cross-lane interfaces. Splitting them now would multiply versioning, CI and evidence synchronization and could break end-to-end comparisons. Keep A–H integrated. |
| Quantum Gravity (QGR) | Proposed: `KitvisetLabs/Quantum-Gravity-Research` | SPLIT OUT — HIGH PRIORITY | Foundational physics has an independent research question, literature base, mathematical outputs and review community. It can proceed without UQPU hardware/software. Keep a small, explicit bridge only where quantum algorithms, simulation or computing resources materially intersect. |
| Contactless vehicle levitation / ionic propulsion / fusion-propulsion concepts | Proposed: `KitvisetLabs/Contactless-Propulsion-Research` | SPLIT OUT — AFTER INVENTORY | Its mission and safety controls differ from QPU/GPU replacement. Group the legacy contactless-levitation work with ionic-jet/fusion propulsion only if their shared deliverables and interfaces are documented. Do not imply antigravity, practical levitation, fusion propulsion or vehicle performance is demonstrated. |
| Pangola grass / biomass production and commercialization | Existing: `KitvisetLabs/Pangola-Grass` | ALREADY SEPARATE | Keep agronomy, product, supply, customer and biomass-industry records canonical there. UQPU Lane E may link to relevant biomass/material/energy evidence but should not duplicate the business or farm database. |
| Kitviset AI app | Existing: `KitvisetLabs/Kitviset-AI-App` | ALREADY SEPARATE | Keep application source and product-specific implementation there. Link only shared research or interfaces where needed. |

## What remains in UQPU

The eight permanent lanes A–H remain together:

- A — quantum programming, workloads, compiler and runtime
- B — cloud QPU and provider integration
- C — memory, state, storage and data movement
- D — devices, chips, fabrication and packaging
- E — materials, energy, cooling and infrastructure
- F — economics, benchmarks and evidence integration
- G — manufacturing equipment and factory software
- H — strategy, finance and future industries

Their existing lane/interface invariants are preserved. Do not create eight separate repositories for A–H unless future evidence shows a lane has become an independently releasable product with stable interfaces and independent governance.

## Migration sequence

### Stage 0 — establish canonical ownership (this document)
- Agree on repository boundaries and names.
- Keep current UQPU tree intact.
- Identify all paths, imports, links, workflows, CI filters, stable IDs and external references for each candidate split.
- Record which artifacts are shared inputs versus owned deliverables.

### Stage 1 — prepare independent repository foundations
For each approved new repository:
- Create the repository under the intended owner.
- Add a project-specific README, mission, scope/non-scope, evidence policy, license decision, contribution guide, security/safety policy and handoff instructions.
- Pin the initial source commit and provenance.
- Define how issues, releases, tests and citations are maintained.

### Stage 2 — migrate without breaking history or reproducibility
- Prefer a documented subtree/history-preserving migration where practical; otherwise preserve original commit/path provenance in a migration manifest.
- Move only artifacts whose primary ownership is assigned to the new repository.
- Keep compatibility links or stubs in UQPU for old public paths.
- Update relative links, imports, CI path filters, manifests and validators.
- Do not delete the source copy until destination content, history/provenance, links and tests are verified.

### Stage 3 — connect repositories through contracts
- UQPU remains the integration hub for UQPU-specific system interfaces.
- Each independent repository publishes versioned, stable outputs and a short integration contract.
- Cross-repository references must pin tags or commit SHAs, not mutable branch names where reproducibility matters.
- Record any cross-repository dependency and evidence boundary in both repositories.

### Stage 4 — verify and close
- Run all relevant tests and link/path checks.
- Verify every migrated artifact has one canonical owner and no missing history or provenance.
- Update UQPU root README, WORKLOG and research-gap/governance records.
- Mark migration complete only after exact commit references and verification results are recorded.

## Safety and authorization

No repository split permits paid services, external spending, credential changes, hazardous experiments, public announcements or destructive deletion without explicit authorization. High-voltage/high-field/vehicle experiments require separate professional safety review and explicit human approval.

## Current execution limitation

The available GitHub connection in this session can list repositories and read/write repository files and issues, but it does not expose a repository-creation or repository-transfer operation. Therefore this plan can be committed to the existing UQPU repository, but the proposed new repositories cannot truthfully be reported as created here. Once they exist, migration can proceed in controlled stages without deleting the original source prematurely.

## Next actions

1. Confirm the proposed repository boundaries and names.
2. Create `Quantum-Gravity-Research` and `Contactless-Propulsion-Research` under `KitvisetLabs` using GitHub's repository-creation interface.
3. Start with QGR because its initial canonical material is small and largely self-contained.
4. Inventory the full propulsion/levitation directory and all cross-references before moving anything.
5. Keep `UQPU-GPU-Replacement-Research`, `Pangola-Grass` and `Kitviset-AI-App` intact as their respective canonical homes.
