"""Executable evidence gate for INV-037 discovery articles.

Research Attribution:
- Research Owner / Principal Investigator / Research Direction: Kanutsanan Pongpanna
- Facebook: https://www.facebook.com/LoveMoneyTH
- YouTube: https://www.youtube.com/@LoveMoneyTHOfficial
- AI Research Agent: OpenAI GPT-5.6 Sol
- AI-assisted contribution: evidence-state model, validation logic, domain-specific
  promotion rules, non-claim preservation, tests and documentation.

The presence of an article never establishes a discovery by itself.
"""

from __future__ import annotations

from dataclasses import dataclass


DOMAINS = {"PHYSICS", "SCIENCE", "MATHEMATICS"}
STATUSES = {
    "HYPOTHESIS_OR_PROPOSAL",
    "PROJECT_REPRODUCED_RESULT",
    "INDEPENDENTLY_REPRODUCED_CANDIDATE",
    "VERIFIED_DISCOVERY",
    "ESTABLISHED_EXTERNAL_DISCOVERY",
}


@dataclass(frozen=True)
class DiscoveryArticleRecord:
    title: str
    domain: str
    status: str
    novelty_statement: str
    prior_art_search: str
    reproducibility_artifact: str
    falsifier_or_counterexample: str
    limitations: str
    attribution: str
    independent_validation: str = ""
    complete_proof_or_formal_artifact: str = ""
    uncertainty_or_error_analysis: str = ""
    external_discoverer_attribution: str = ""

    def validate(self) -> None:
        if self.domain not in DOMAINS:
            raise ValueError(f"unknown domain: {self.domain}")
        if self.status not in STATUSES:
            raise ValueError(f"unknown status: {self.status}")
        required = (
            self.title,
            self.novelty_statement,
            self.prior_art_search,
            self.reproducibility_artifact,
            self.falsifier_or_counterexample,
            self.limitations,
            self.attribution,
        )
        if any(not field.strip() for field in required):
            raise ValueError("all core discovery-article fields must be non-empty")

        if self.status == "ESTABLISHED_EXTERNAL_DISCOVERY":
            if not self.external_discoverer_attribution.strip():
                raise ValueError(
                    "external discoveries require explicit discoverer/source attribution"
                )

        if self.status == "VERIFIED_DISCOVERY":
            self._validate_verified_discovery()

    def _validate_verified_discovery(self) -> None:
        if not self.independent_validation.strip():
            raise ValueError("verified discovery requires independent validation")

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


def can_use_verified_discovery_label(record: DiscoveryArticleRecord) -> bool:
    """Return True only if the record validates as VERIFIED_DISCOVERY."""

    if record.status != "VERIFIED_DISCOVERY":
        return False
    try:
        record.validate()
    except ValueError:
        return False
    return True


def article_directory(domain: str) -> str:
    """Return canonical INV-037 directory for a supported domain."""

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
        "classification": "NEW_DISCOVERY_ARTICLE_REGISTRY_AND_PROMOTION_GATE",
        "evidence_level": "RESEARCH_GOVERNANCE_EXECUTABLE",
        "canonical_root": "articles/",
        "domains": sorted(DOMAINS),
        "statuses": sorted(STATUSES),
        "verified_discovery_requires_independent_validation": True,
        "mathematics_requires_proof_or_formal_artifact": True,
        "physics_science_require_uncertainty_or_error_analysis": True,
        "non_claims": {
            "article_presence_implies_discovery": False,
            "simulation_implies_experimental_discovery": False,
            "ai_generated_equation_implies_new_law": False,
            "project_only_reproduction_implies_verified_discovery": False,
            "quantum_advantage": False,
            "subsystem_replacement": False,
            "hundred_x": False,
            "hundred_million_x": False,
        },
    }
