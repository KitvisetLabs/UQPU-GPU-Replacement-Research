# NEW DISCOVERY ARTICLES

**Permanent discovery-article registry — INV-037**

This root-level folder is the canonical publication area for UQPU articles about potentially new findings in **physics, broader science, and mathematics**.

## Research Attribution

- Research Owner / Principal Investigator / Research Direction: **Kanutsanan Pongpanna**
- Facebook: https://www.facebook.com/LoveMoneyTH
- YouTube: https://www.youtube.com/@LoveMoneyTHOfficial
- AI Research Agent: **OpenAI GPT-5.6 Sol**
- AI-assisted contribution in establishing this registry: evidence-status design, article promotion rules, reproducibility contract, directory architecture, executable validation and documentation.

Attribution in every future article must reflect the actual contributors and roles for that article. Do not copy an AI/model name into an article unless that model/agent actually contributed.

# Permanent rule

Whenever this project develops, reproduces, validates, or identifies a materially new result in physics, science, or mathematics, create or update an article in this folder.

The folder is deliberately prominent and permanent. New work must not be hidden only in chat history, an issue comment, a benchmark JSON, or a code commit when it materially changes the scientific/mathematical understanding of the project.

## Directory map

- `physics/` — physics results, hypotheses, new mechanisms, physical laws/effective laws, particle/field/spacetime/material-physics findings.
- `science/` — non-physics scientific findings, including chemistry, materials, energy, biology or other scientific domains relevant to UQPU.
- `mathematics/` — theorems, proofs, counterexamples, bounds, algorithms or mathematical structures.
- `ARTICLE_TEMPLATE.md` — mandatory minimum structure for new articles.

## Evidence-status ladder

Every article must declare exactly one current status:

1. `HYPOTHESIS_OR_PROPOSAL` — a novel idea, equation, mechanism or conjecture; not a discovery claim.
2. `PROJECT_REPRODUCED_RESULT` — reproducible inside this repository/project, but not yet independently validated as a new discovery.
3. `INDEPENDENTLY_REPRODUCED_CANDIDATE` — independent validation/reproduction exists, but novelty and broader discovery status still require careful review.
4. `VERIFIED_DISCOVERY` — reserved for a result with a documented novelty search plus domain-appropriate independent validation. This is the only status that permits the repository to call the project result a verified new discovery.
5. `ESTABLISHED_EXTERNAL_DISCOVERY` — an article explains or extends a discovery made elsewhere; the repository must attribute the external discoverers and must not claim ownership.

## Domain-specific promotion rules

### Physics / empirical science

`VERIFIED_DISCOVERY` requires, at minimum:

- explicit prior-art/literature search;
- reproducible methods and raw/derived evidence provenance;
- uncertainty/error analysis;
- a falsifier or discriminating alternative explanation;
- independent reproduction or independent evidence capable of discriminating the claim;
- no promotion from simulation/theory/model alone to experimental fact;
- exact separation between project evidence and external evidence.

### Mathematics

`VERIFIED_DISCOVERY` requires, at minimum:

- explicit novelty/prior-art search;
- complete theorem statement and assumptions;
- complete proof or machine-checkable/formally checkable proof artifact where applicable;
- independent proof review/check or an equivalently strong verification route;
- counterexample search and boundary/degenerate-case analysis;
- no claim that numerical examples or symbolic fitting constitute a proof.

## Required article metadata

Every substantive article must identify:

- title and date;
- domain;
- evidence status;
- novelty statement;
- relationship to prior work;
- methods/proof;
- reproducibility instructions;
- evidence and uncertainty;
- falsifiers/counterexamples;
- limitations;
- implications;
- non-claims;
- human and AI contribution attribution according to actual roles;
- links to code/tests/results/PR/commit/issue where applicable.

## Naming convention

Recommended filename:

`YYYY-MM-DD_<DOMAIN>_<SHORT_DISCOVERY_NAME>.md`

Examples:

- `2026-09-14_PHYSICS_candidate_spin_transport_effect.md`
- `2026-09-14_MATHEMATICS_new_operator_bound.md`
- `2026-09-14_SCIENCE_new_material_conversion_result.md`

A filename may contain the word `candidate`; filenames should avoid `verified_discovery` until the promotion gate passes.

## Discovery article workflow

```text
new observation / theorem / hypothesis
-> prior-art search
-> article at correct evidence status
-> code/proof/data + tests
-> internal reproduction
-> adversarial review / counterexample search
-> independent validation when required
-> promotion or demotion of evidence status
-> permanent article + provenance links
```

Negative results, refutations and failed candidate discoveries may also be published because they prevent repeated dead ends and improve the research record.

## Non-claims

Creating an article does not make an idea a discovery. A model, simulation, AI-generated equation, numerical fit, internal reproduction, or unreviewed proof is not automatically a new physical law, scientific discovery, mathematical theorem, quantum advantage, subsystem replacement, `>=100x`, or `>=100,000,000x` result.
