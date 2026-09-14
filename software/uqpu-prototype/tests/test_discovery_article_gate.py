import unittest

from uqpu.discovery_article_gate import (
    DiscoveryArticleRecord,
    article_directory,
    batch046_certificate,
    can_use_verified_discovery_label,
)


class DiscoveryArticleGateTests(unittest.TestCase):
    def base(self, **overrides):
        fields = {
            "title": "Candidate result",
            "domain": "PHYSICS",
            "status": "HYPOTHESIS_OR_PROPOSAL",
            "novelty_statement": "Narrow novelty statement",
            "prior_art_search": "Search date, sources and closest prior work recorded",
            "reproducibility_artifact": "code/tests/results/commit",
            "falsifier_or_counterexample": "specific discriminating falsifier",
            "limitations": "scope and evidence limitations",
            "attribution": "human and AI roles recorded",
        }
        fields.update(overrides)
        return DiscoveryArticleRecord(**fields)

    def test_hypothesis_can_be_published_without_discovery_label(self):
        record = self.base()
        record.validate()
        self.assertFalse(can_use_verified_discovery_label(record))

    def test_project_reproduction_is_not_verified_discovery(self):
        record = self.base(status="PROJECT_REPRODUCED_RESULT")
        record.validate()
        self.assertFalse(can_use_verified_discovery_label(record))

    def test_empirical_verified_discovery_requires_independent_validation(self):
        record = self.base(
            status="VERIFIED_DISCOVERY",
            uncertainty_or_error_analysis="uncertainty quantified",
        )
        with self.assertRaises(ValueError):
            record.validate()

    def test_empirical_verified_discovery_requires_error_analysis(self):
        record = self.base(
            status="VERIFIED_DISCOVERY",
            independent_validation="independent reproduction reference",
        )
        with self.assertRaises(ValueError):
            record.validate()

    def test_empirical_verified_discovery_can_pass_full_contract(self):
        record = self.base(
            status="VERIFIED_DISCOVERY",
            independent_validation="independent reproduction reference",
            uncertainty_or_error_analysis="uncertainty quantified",
        )
        record.validate()
        self.assertTrue(can_use_verified_discovery_label(record))

    def test_mathematical_verified_discovery_requires_complete_proof(self):
        record = self.base(
            domain="MATHEMATICS",
            status="VERIFIED_DISCOVERY",
            independent_validation="independent proof review",
        )
        with self.assertRaises(ValueError):
            record.validate()

    def test_mathematical_verified_discovery_can_pass_full_contract(self):
        record = self.base(
            domain="MATHEMATICS",
            status="VERIFIED_DISCOVERY",
            independent_validation="independent proof review",
            complete_proof_or_formal_artifact="complete proof artifact",
        )
        record.validate()
        self.assertTrue(can_use_verified_discovery_label(record))

    def test_external_discovery_requires_external_attribution(self):
        record = self.base(status="ESTABLISHED_EXTERNAL_DISCOVERY")
        with self.assertRaises(ValueError):
            record.validate()

    def test_domain_directory_mapping(self):
        self.assertEqual(article_directory("PHYSICS"), "articles/physics")
        self.assertEqual(article_directory("SCIENCE"), "articles/science")
        self.assertEqual(article_directory("MATHEMATICS"), "articles/mathematics")

    def test_certificate_preserves_nonclaims(self):
        cert = batch046_certificate()
        self.assertEqual(cert["canonical_root"], "articles/")
        self.assertFalse(cert["non_claims"]["article_presence_implies_discovery"])
        self.assertFalse(cert["non_claims"]["simulation_implies_experimental_discovery"])
        self.assertFalse(cert["non_claims"]["ai_generated_equation_implies_new_law"])


if __name__ == "__main__":
    unittest.main()
