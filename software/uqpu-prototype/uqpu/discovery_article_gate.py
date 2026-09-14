"""Executable admission gate for INV-037 verified-discovery articles.

Research Attribution:
- Research Owner / Principal Investigator / Research Direction: Kanutsanan Pongpanna
- Facebook: https://www.facebook.com/LoveMoneyTH
- YouTube: https://www.youtube.com/@LoveMoneyTHOfficial
- AI Research Agent: OpenAI GPT-5.6 Sol
- AI-assisted contribution: verified-discovery admission model, domain-specific
  validation rules, non-claim preservation, tests and documentation.

The `articles/` folder is reserved for genuinely new verified discoveries only.
Ideas, hypotheses, candidate results and project-only reproductions must remain
outside `articles/` until this gate passes.
"""

from __future__ import annotations

from dataclasses import dataclass


DOMAINS = {"PHYSICS", "SCIENCE", "MATHEMATICS"}
ARTICLE_STATUS = "VERIFIED_DISCOVERY"
NON_ARTICLE_RESEARCH_STATES = {
    "HYPOTHESIS_OR_PROPOSAL",
    "PROJECT_REPRODUCED_RESULT",
    "INDEPENDENTLY_REPRODUCED_CANDIDATE",
    "PRELIMINARY_RESULT",
    "EXTERNAL_LITERATURE_RESULT",
}


@dataclass(frozen=True)
class DiscoveryArticleRecord:
    title: str
    domain: str
    status: str
    discovery_statement: str
    novelty_statement: str
    prior_art_search: str
    reproducibility_artifact: str
    falsifier_or_counterexample: str
    limitations: str
    attribution: str
    independent_validation: str
    complete_proof_or_formal_artifact: str = ""
    uncertainty_or_error_analysis: str = ""

    def validate_for_article(self) -> None:
        """Validate that this record is eligible to exist inside `articles/`."""

        if self.domain not in DOMAINS:
            raise ValueError(f"unknown domain: {self.domain}")
        if self.status != ARTICLE_STATUS:
            raise ValueError(
                "articles/ accepts VERIFIED_DISCOVERY only; earlier-stage research "
                "must remain outside the articles registry"
            )

        required = (
            self.title,
            self.discovery_statement,
            self.novelty_statement,
            self.prior_art_search,
            self.reproducibility_artifact,
            self.falsifier_or_counterexample,
            self.limitations,
            self.attribution,
            self.independent_validation,
        )
        if any(not field.strip() for field in required):
            raise ValueError("all verified-discovery article fields must be non-empty")

        if self.domain in {"PHYSICS", "SCIENCE"}:
            if not self.uncertainty_or_error_analysis.strip():
                raise ValueError(
                    "verified empirical discovery requires uncertainty/error analysis"
                )

        if self.domain == "MATHEMATICS":
            if not self.complete_proof_or_formal_artifact.strip():
                raise ValueError(
                    "verified mathematical discovery requires a complete proof or formal artifact"
                )


def can_create_discovery_article(record: DiscoveryArticleRecord) -> bool:
    """Return True only when a result qualifies for entry into `articles/`."""

    try:
        record.validate_for_article()
    except ValueError:
        return False
    return True


def article_directory(domain: str) -> str:
    """Return canonical INV-037 directory for a supported verified discovery."""

    if domain not in DOMAINS:
        raise ValueError(f"unknown domain: {domain}")
    return {
        "PHYSICS": "articles/physics",
        "SCIENCE": "articles/science",
        "MATHEMATICS": "articles/mathematics",
    }[domain]


def batch046_certificate() -> dict[str, object]:
    return {
        "program": "INV-037/BATCH-046",
        "classification": "VERIFIED_NEW_DISCOVERY_ARTICLE_REGISTRY_AND_ADMISSION_GATE",
        "evidence_level": "RESEARCH_GOVERNANCE_EXECUTABLE",
        "canonical_root": "articles/",
        "domains": sorted(DOMAINS),
        "allowed_article_statuses": [ARTICLE_STATUS],
        "non_article_research_states": sorted(NON_ARTICLE_RESEARCH_STATES),
        "articles_are_verified_discovery_only": True,
        "hypotheses_forbidden_in_articles": True,
        "project_only_reproductions_forbidden_in_articles": True,
        "external_literature_summaries_forbidden_in_articles": True,
        "verified_discovery_requires_independent_validation": True,
        "mathematics_requires_proof_or_formal_artifact": True,
        "physics_science_require_uncertainty_or_error_analysis": True,
        "non_claims": {
            "registry_creation_implies_current_discovery": False,
            "simulation_implies_experimental_discovery": False,
            "ai_generated_equation_implies_new_law": False,
            "project_only_reproduction_implies_verified_discovery": False,
            "quantum_advantage": False,
            "subsystem_replacement": False,
            "hundred_x": False,
            "hundred_million_x": False,
        },
    }
