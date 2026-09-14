# Batch 047 — Root-Level Articles Front-Page Visibility

**Status:** repository navigation / publication-governance hardening  
**Primary owner:** repository governance / cross-lane publication surface  
**Date:** 2026-09-14

## Objective

Make the canonical verified-discovery article registry structurally and visually prominent on the repository front page.

The project owner requires the **folder itself** to live at repository root, not as a subfolder under `docs/`, `research_lanes/`, `software/`, or another area.

Canonical location:

```text
/articles/
```

The root-level folder contains the INV-037 verified-discovery registry and its domain partitions:

- `articles/physics/`
- `articles/science/`
- `articles/mathematics/`
- `articles/ARTICLE_TEMPLATE.md`
- `articles/README.md`

## Front-page rule

The root `README.md` must include a high-visibility navigation block near the top linking directly to `articles/` and its three verified-discovery domains.

This is a navigation/governance rule. It does not relax the admission standard. Only results with `VERIFIED_DISCOVERY` status under INV-037 belong in `articles/`.

## Executable invariant

`test_project_invariants.py` now verifies that:

1. `ROOT / "articles"` exists and is a directory;
2. its parent is the repository root;
3. its physics/science/mathematics README files and article template exist;
4. `articles/README.md` explicitly declares the root-level canonical location;
5. the root README contains the high-visibility article-hub block and direct links;
6. that block appears before the first large permanent-principle section.

## Evidence classification

`ROOT_ARTICLES_PUBLICATION_HUB_GOVERNANCE`

Evidence level: `REPOSITORY_STRUCTURE_AND_CI_INVARIANT`.

## Non-claims

This batch does not create or promote a scientific discovery. It changes repository visibility and governance only. Existing hypotheses, simulations, reproductions and external discoveries remain outside the verified-discovery registry unless they independently satisfy INV-037.

## Research Attribution

- Research Owner / Principal Investigator / Research Direction: **Kanutsanan Pongpanna**
- Facebook: https://www.facebook.com/LoveMoneyTH
- YouTube: https://www.youtube.com/@LoveMoneyTHOfficial
- AI Research Agent: **OpenAI GPT-5.6 Sol**
- AI-assisted contribution: repository-structure audit, front-page navigation design, root-folder governance wording, executable invariant design, documentation, CI/PR preparation and merge verification.

Attribution reflects roles in this batch only.
