# PERMANENT VERIFIED-DISCOVERY ARTICLE DIRECTIVE

**Permanent invariant:** INV-037  
**Canonical folder:** `articles/`  
**Domains:** Physics / Science / Mathematics  
**Date established:** 2026-09-14

## Research Attribution

- Research Owner / Principal Investigator / Research Direction: **Kanutsanan Pongpanna**
- Facebook: https://www.facebook.com/LoveMoneyTH
- YouTube: https://www.youtube.com/@LoveMoneyTHOfficial
- AI Research Agent: **OpenAI GPT-5.6 Sol**
- AI-assisted contribution: verified-discovery publication governance, novelty/validation contract, executable gate/tests and documentation.

Attribution in each future article must reflect the actual contributors and AI agents used for that discovery.

# Permanent rule

The root-level `articles/` folder is reserved **only for genuinely new discoveries that have already passed the project's verified-discovery gate** in physics, science or mathematics.

Do **not** create an article in `articles/` merely because a result is an interesting idea, hypothesis, conjecture, candidate equation, simulation, model, symbolic-regression output, numerical fit, internally reproduced result, preliminary experiment, unpublished interpretation, or literature finding.

Those earlier-stage materials belong in ordinary research locations such as `docs/`, the owning research lane, benchmark/result folders, issues or other research notes. They may be researched indefinitely there. An `articles/` file is created only after the result qualifies as a verified new discovery.

Canonical verified-discovery folders:

- `articles/physics/`
- `articles/science/`
- `articles/mathematics/`

The canonical article template is `articles/ARTICLE_TEMPLATE.md`.

# Entry gate — no candidate statuses inside `articles/`

A project result may enter `articles/` only when all common requirements are satisfied:

1. **Precise new-result statement** — the discovery is narrowly and unambiguously stated.
2. **Prior-art / novelty search** — closest known literature, theorem, dataset, experiment or public result has been searched and documented; novelty is not merely assumed.
3. **Reproducible primary evidence** — code/data/experiment/proof artifacts and provenance are sufficient for checking the result.
4. **Falsification / counterexample analysis** — credible alternatives and failure conditions have been tested.
5. **Independent validation appropriate to the domain** — validation cannot consist only of the same project pipeline repeating itself.
6. **Limitations and scope** — the claim is no broader than the evidence.
7. **Attribution** — actual human and AI contributions are recorded without overclaiming.

Additional domain gates apply below.

# Physics / empirical science

Before an article may be created under `articles/physics/` or `articles/science/`, the discovery must additionally include:

- domain-appropriate measurement or empirical evidence where the claim is empirical;
- uncertainty/error analysis;
- a discriminating falsifier or alternative-explanation check;
- independent reproduction or comparably strong independent evidence;
- separation of theory/simulation from experimental observation;
- evidence that the result is genuinely new relative to prior art.

A theory, simulation, AI-generated equation or project-only reproduction is **not sufficient** for entry into `articles/` as a physics/science discovery.

# Mathematics

Before an article may be created under `articles/mathematics/`, the discovery must include:

- a precise theorem/result statement and assumptions;
- a complete proof or equivalently strong formal/machine-checkable proof artifact where applicable;
- counterexample, boundary and degenerate-case analysis;
- explicit prior-art/novelty review;
- an independent proof check/review or comparably strong verification route.

Numerical examples, symbolic fitting or finite test cases alone are **not sufficient** for entry into `articles/` as a mathematical discovery.

# External discoveries and literature

Existing discoveries made by other researchers remain essential inputs, but ordinary literature reviews or explanations of external discoveries do **not** belong in this project's `articles/` verified-new-discovery registry. They belong in literature/research notes and must credit their original discoverers.

If UQPU later makes a genuinely new extension beyond prior work and that extension passes the full gate above, the new extension may receive its own article with precise prior-work attribution.

# Article trigger

The trigger is therefore simple:

```text
research idea / hypothesis / candidate / internal result
-> continue research OUTSIDE articles/
-> novelty search
-> reproducibility / proof
-> adversarial falsification / counterexample search
-> independent validation
-> verified genuinely new discovery
-> CREATE article in articles/ for the first time
```

Demotion is also mandatory: if later evidence invalidates the discovery claim, the article must be clearly retracted/corrected with provenance rather than silently left as verified.

# Non-claims

INV-037 does not retroactively classify any existing UQPU theory, model, simulation, symbolic-regression output, internal reproduction or AI-generated equation as a discovery. It does not weaken existing non-claim boundaries for real-QPU performance, quantum advantage, GPU/NPU/RAM/DRAM/HBM replacement, `>=100x`, `>=100,000,000x`, Data-Center-to-One-Phone, or new-law claims.
