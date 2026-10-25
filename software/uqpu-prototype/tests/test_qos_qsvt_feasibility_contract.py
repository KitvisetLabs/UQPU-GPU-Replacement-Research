import unittest

from uqpu.qos_qsvt_feasibility_contract import (
    QSVTFeasibilityFixture,
    QSVTFeasibilityRunRecord,
    classify_feasibility_record,
)


HASH = "a" * 64


def univariate_fixture(**overrides):
    values = dict(
        fixture_id="QOS-QSVT-FEAS-001-U1",
        model_class="UNIVARIATE_QSP",
        source_reference="pinned theorem reference and local fixture manifest",
        statement_sha256=HASH,
        specification="Frozen univariate polynomial-pair fixture",
        expected_decision="FEASIBLE",
        scope_note="The theorem applies only to this declared univariate QSP class.",
        signal_variables=("x",),
        signal_operator_count=3,
    )
    values.update(overrides)
    return QSVTFeasibilityFixture(**values)


def record_for(fixture, **overrides):
    values = dict(
        fixture_id=fixture.fixture_id,
        statement_sha256=fixture.statement_sha256,
        status="THEOREM_CHECKED",
        decision="FEASIBLE",
        theorem_scope="Declared univariate QSP theorem scope",
        certificate_reference="artifacts/certificate.json",
    )
    values.update(overrides)
    return QSVTFeasibilityRunRecord(**values)


class QSVTFeasibilityContractTests(unittest.TestCase):
    def test_valid_univariate_fixture_passes_metadata_validation(self):
        fixture = univariate_fixture()
        fixture.validate()

    def test_multivariate_fixture_requires_two_named_variables(self):
        fixture = univariate_fixture(
            model_class="MULTIVARIATE_QSP",
            signal_variables=("x", "y"),
        )
        fixture.validate()
        with self.assertRaises(ValueError):
            univariate_fixture(
                model_class="MULTIVARIATE_QSP",
                signal_variables=("x",),
            )

    def test_univariate_fixture_rejects_extra_signal_variable(self):
        with self.assertRaises(ValueError):
            univariate_fixture(signal_variables=("x", "y"))

    def test_unknown_channel_requires_dimension_error_metric_and_oracle_model(self):
        fixture = QSVTFeasibilityFixture(
            fixture_id="QOS-QSVT-FEAS-001-CH1",
            model_class="UNKNOWN_CHANNEL_QSVT",
            source_reference="pinned unknown-channel QSVT theorem",
            statement_sha256=HASH,
            specification="Approximate channel block-encoding request",
            expected_decision="UNKNOWN",
            scope_note="Bound is limited to the declared oracle model.",
            channel_dimension=4,
            delta=1e-3,
            error_metric="diamond_norm",
            oracle_access_model="black-box channel access as stated by the source theorem",
            query_count_bound_reference="source theorem and its exact upper/lower-bound statements",
        )
        fixture.validate()
        with self.assertRaises(ValueError):
            QSVTFeasibilityFixture(
                fixture_id="bad",
                model_class="UNKNOWN_CHANNEL_QSVT",
                source_reference="source",
                statement_sha256=HASH,
                specification="spec",
                expected_decision="UNKNOWN",
                scope_note="scope",
                channel_dimension=4,
                delta=1e-3,
                error_metric="trace_distance",
                oracle_access_model="black-box",
                query_count_bound_reference="source theorem",
            ).validate()

    def test_hash_mismatch_fails_closed(self):
        fixture = univariate_fixture()
        decision = classify_feasibility_record(
            fixture, record_for(fixture, statement_sha256="b" * 64)
        )
        self.assertEqual(decision.status, "PROVENANCE_INVALID")
        self.assertFalse(decision.may_skip_synthesis)
        self.assertFalse(decision.may_claim_hardware_advantage)

    def test_tool_error_is_not_mathematical_infeasibility(self):
        fixture = univariate_fixture()
        decision = classify_feasibility_record(
            fixture,
            record_for(fixture, status="TOOL_ERROR", decision="INFEASIBLE"),
        )
        self.assertEqual(decision.status, "TOOL_BLOCKED")
        self.assertFalse(decision.may_claim_mathematical_infeasibility)
        self.assertFalse(decision.may_skip_synthesis)

    def test_theorem_result_requires_external_audit_before_any_promotion(self):
        fixture = univariate_fixture()
        decision = classify_feasibility_record(fixture, record_for(fixture))
        self.assertEqual(decision.status, "READY_FOR_INDEPENDENT_AUDIT")
        self.assertTrue(decision.independent_audit_required)
        self.assertFalse(decision.may_skip_synthesis)
        self.assertFalse(decision.may_claim_mathematical_infeasibility)
        self.assertFalse(decision.may_claim_hardware_advantage)

    def test_missing_certificate_or_scope_is_incomplete(self):
        fixture = univariate_fixture()
        decision = classify_feasibility_record(
            fixture,
            record_for(fixture, certificate_reference="", theorem_scope=""),
        )
        self.assertEqual(decision.status, "RESULT_INCOMPLETE")
        self.assertFalse(decision.independent_audit_required)

    def test_unresolved_or_mismatched_decision_is_not_promoted(self):
        fixture = univariate_fixture()
        unknown = classify_feasibility_record(
            fixture, record_for(fixture, decision="UNKNOWN")
        )
        mismatch = classify_feasibility_record(
            fixture, record_for(fixture, decision="INFEASIBLE")
        )
        self.assertEqual(unknown.status, "UNRESOLVED")
        self.assertEqual(mismatch.status, "EXPECTED_DECISION_MISMATCH")
        self.assertFalse(unknown.may_skip_synthesis)
        self.assertFalse(mismatch.may_claim_mathematical_infeasibility)


if __name__ == "__main__":
    unittest.main()
