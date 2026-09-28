# Cycle 021 Primary Source Review

**Review date:** 2026-09-28  
**Evidence class:** primary format/runtime documentation; design inputs only.

## ZIP64 extra fields

[PKWARE APPNOTE v6.3.10 FINAL](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT), revised 2022-11-01, §§4.3.7, 4.3.9 and 4.3.12, accessed 2026-09-28, defines local/central ZIP fields and ZIP64 descriptor layouts. The Cycle 021 gate validates unrelated extra-field ordering and rejects duplicate ZIP64 extended-information fields before payload access. Archive bytes are synthetic and no producer corpus is tested.

## Process replacement

[Python `os.replace`](https://docs.python.org/3/library/os.html#os.replace), official documentation, accessed 2026-09-28, documents cross-filesystem replacement failure and successful atomic rename on POSIX. This cycle observes process exits only; it does not establish crash consistency, cache/flush behavior or power-loss durability.

## Assumptions and limits

- Graph, receipt, custody, covariance, ranking, lineage and QOS inputs are fixtures/models/fiction.
- No hardware, provider, physical-sample, calibration or commercial evidence is introduced.
