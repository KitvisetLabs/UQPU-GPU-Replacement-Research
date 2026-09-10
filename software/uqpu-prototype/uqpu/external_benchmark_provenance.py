"""Public-metadata provenance gates for external scientific benchmarks.

These helpers deliberately separate public metadata reconciliation from direct
execution of gated benchmark bytes. A metadata certificate is not an executed
benchmark result.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BenchmarkCountCertificate:
    declared_total: int
    split_counts: dict[str, int]

    @property
    def observed_total(self) -> int:
        return sum(self.split_counts.values())

    @property
    def delta(self) -> int:
        return self.observed_total - self.declared_total

    @property
    def consistent(self) -> bool:
        return self.delta == 0


def reconcile_benchmark_counts(*, declared_total: int, split_counts: dict[str, int]) -> dict[str, object]:
    """Compare a prose-declared problem count with machine-readable/public split counts."""
    if declared_total <= 0:
        raise ValueError("declared_total must be positive")
    if not split_counts or any((not name) or count < 0 for name, count in split_counts.items()):
        raise ValueError("split_counts must contain named nonnegative counts")
    certificate = BenchmarkCountCertificate(declared_total=declared_total, split_counts=dict(split_counts))
    return {
        "declared_total": certificate.declared_total,
        "split_counts": certificate.split_counts,
        "observed_total": certificate.observed_total,
        "delta": certificate.delta,
        "consistent": certificate.consistent,
    }


def llm_srbench_public_count_certificate() -> dict[str, object]:
    """Return the 2026-09-10 public-metadata count reconciliation for LLM-SRBench.

    The ICML 2025 paper/dataset prose says 239 problems. The current public
    Hugging Face README metadata exposes 24+36+25+44+111 = 240 examples.
    No gated numerical benchmark bytes are accessed by this function.
    """
    split_counts = {
        "lsr_synth_bio_pop_growth": 24,
        "lsr_synth_chem_react": 36,
        "lsr_synth_matsci": 25,
        "lsr_synth_phys_osc": 44,
        "lsr_transform": 111,
    }
    result = reconcile_benchmark_counts(declared_total=239, split_counts=split_counts)
    result.update(
        {
            "benchmark": "LLM-SRBench",
            "evidence_level": "PUBLIC_METADATA_ONLY",
            "official_dataset_bytes_accessed": False,
            "released_snapshot_denominator_indicated_by_public_metadata": 240,
            "fabricate_239_task_slice": False,
            "external_execution_completed": False,
            "interpretation": (
                "Public metadata is internally inconsistent with the prose total. "
                "Use 240 as the released-snapshot count for provenance discussions, "
                "but do not claim an official-byte benchmark run until gated data are "
                "accessed and pinned directly."
            ),
        }
    )
    return result
