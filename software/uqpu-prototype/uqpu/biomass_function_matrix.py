from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class BiomassSubstitutionCandidate:
    incumbent: str
    required_function: str
    biomass_route: str
    evidence_level: str
    principal_risk: str


def baseline_candidates() -> tuple[BiomassSubstitutionCandidate, ...]:
    return (
        BiomassSubstitutionCandidate("graphite/carbon additives","electrochemical conduction/storage","hard carbon / activated carbon from lignocellulosic residues","PUBLISHED_EXPERIMENT","purity and performance consistency"),
        BiomassSubstitutionCandidate("polymer packaging/insulation","structural/electrical insulation","cellulose/lignin-derived polymers and composites","PUBLISHED_EXPERIMENT","moisture/thermal/reliability limits"),
        BiomassSubstitutionCandidate("activated carbon adsorbents","gas/liquid adsorption and purification","biochar/activated carbon","PUBLISHED_EXPERIMENT","contaminant-specific selectivity"),
        BiomassSubstitutionCandidate("part of EMI/thermal composite filler","shielding/thermal management","carbonized biomass composite filler","MODEL_ONLY","conductivity and interface resistance"),
        BiomassSubstitutionCandidate("critical-metal recovery sorbents","selective capture/recovery","functionalized cellulose/biochar/biopolymer sorbents","PUBLISHED_EXPERIMENT","selectivity/regeneration/economics"),
    )
