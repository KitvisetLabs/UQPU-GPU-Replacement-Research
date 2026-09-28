# Cycle 020 Primary Source Review

**Review date:** 2026-09-28  
**Evidence class:** primary format specification and runtime documentation; design inputs only.

## ZIP64 fields and descriptors

[PKWARE APPNOTE v6.3.10 FINAL](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT), revised 2022-11-01, §§4.3.7, 4.3.9 and 4.3.12, accessed 2026-09-28, defines local-file and central-directory metadata and ZIP64 data descriptors. The Cycle 020 gate cross-binds synthetic ZIP64 sizes and local-header offset and verifies descriptor variants. It does not establish compatibility with a real archive-producer corpus.

## Replacement limits

[Python `os.replace`](https://docs.python.org/3/library/os.html#os.replace), official Python runtime documentation, accessed 2026-09-28, describes cross-filesystem failure and POSIX atomic rename behavior. The subprocess fixture checks process termination only, not crash consistency, caches, flushes or power loss.

## Assumptions and limits

- Graph, receipt, custody, covariance, ranking, lineage and operator values are synthetic/model/fiction.
- Unit conversions are exact arithmetic fixtures and are not calibration.
- No physical samples, provider invoices or hardware measurements are observed.
