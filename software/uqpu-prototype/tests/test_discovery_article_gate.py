import unittest

from uqpu.discovery_article_gate import (
    DiscoveryArticleRecord,
    article_directory,
    batch046_certificate,
    can_create_discovery_article,
)


class DiscoveryArticleGateTests(unittest.TestCase):
    def verified_base(self, **overrides):
        fields = {
            "title": "Verified new result",
            "domain": "PHYSICS",
            "status": "VERIFIED_DISCOVERY",
            "discovery_statement": "Precise verified discovery statement",
            "novelty_statement": "Novel relative to documented closest prior work",
            "prior_art_search": "Search date, sources, terms and closest prior work recorded",
            "reproducibility_artifact": "code/tests/data/results/commit",
            "falsifier_or_counterexample": "specific discriminating falsifier tested",
            "limitations": "scope and evidence limitations",
            "attribution": "actual human and AI roles recorded",
            "independent_validation": "independent reproduction/check reference",
            "uncertainty_or_error_analysis": "uncertainty quantified",
        }
        fields.update(overrides)
        return DiscoveryArticleRecord(**fields)

    def test_hypothesis_is_rejected_from_articles(self):
        record = self.verified_base(status="HYPOTHESIS_OR_PROPOSAL")
        self.assertFalse(can_create_discovery_article(record))
        with self.assertRaises(ValueError):
            record.validate_for_article()

    def test_project_reproduction_is_rejected_from_articles(self):
        record = self.verified_base(status="PROJECT_REPRODUCED_RESULT")
        self.assertFalse(can_create_discovery_article(record))

    def test_independent_candidate_is_still_rejected_until_verified(self):
        record = self.verified_base(status="INDEPENDENTLY_REPRODUCED_CANDIDATE")
        self.assertFalse(can_create_discovery_article(record))

    def test_external_literature_result_is_not_a_project_discovery_article(self):
        record = self.verified_base(status="EXTERNAL_LITERATURE_RESULT")
        self.assertFalse(can_create_discovery_article(record))

    def test_verified_empirical_discovery_requires_independent_validation(self):
        record = self.verified_base(independent_validation="")
        with self.assertRaises(ValueError):
            record.validate_for_article()

    def test_verified_empirical_discovery_requires_error_analysis(self):
        record = self.verified_base(uncertainty_or_error_analysis="")
        with self.assertRaises(ValueError):
            record.validate_for_article()

    def test_verified_empirical_discovery_can_enter_articles(self):
        record = self.verified_base()
        record.validate_for_article()
        self.assertTrue(can_create_discovery_article(record))

    def test_mathematical_discovery_requires_complete_proof(self):
        record = self.verified_base(
            domain="MATHEMATICS",
            uncertainty_or_error_analysis="",
            complete_proof_or_formal_artifact="",
        )
        with self.assertRaises(ValueError):
            record.validate_for_article()

    def test_mathematical_verified_discovery_can_enter_articles(self):
        record = self.verified_base(
            domain="MATHEMATICS",
            uncertainty_or_error_analysis="",
            complete_proof_or_formal_artifact="complete proof artifact",
        )
        record.validate_for_article()
        self.assertTrue(can_create_discovery_article(record))

    def test_domain_directory_mapping(self):
        self.assertEqual(article_directory("PHYSICS"), "articles/physics")
        self.assertEqual(article_directory("SCIENCE"), "articles/science")
        self.assertEqual(article_directory("MATHEMATICS"), "articles/mathematics")

    def test_certificate_enforces_verified_only_boundary(self):
        cert = batch046_certificate()
        self.assertEqual(cert["canonical_root"], "articles/")
        self.assertEqual(cert["allowed_article_statuses"], ["VERIFIED_DISCOVERY"])
        self.assertTrue(cert["articles_are_verified_discovery_only"])
        self.assertTrue(cert["hypotheses_forbidden_in_articles"])
        self.assertTrue(cert["project_only_reproductions_forbidden_in_articles"])
        self.assertFalse(cert["non_claims"]["registry_creation_implies_current_discovery"])
        self.assertFalse(cert["non_claims"]["ai_generated_equation_implies_new_law"])


if __name__ == "__main__":
    unittest.main()
