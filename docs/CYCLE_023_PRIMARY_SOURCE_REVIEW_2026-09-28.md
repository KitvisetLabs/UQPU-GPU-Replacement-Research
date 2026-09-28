# Cycle 023 Primary Source Review

**Review date:** 2026-09-28  
**Evidence class:** primary format/runtime documentation; design inputs only.

## ZIP64 descriptor interpretation

[PKWARE APPNOTE v6.3.10 FINAL](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT), revised 2022-11-01, §§4.3.7, 4.3.9 and 4.3.12, accessed 2026-09-28, defines ZIP64 metadata and descriptor fields. Synthetic size mutations are rejected before payload access; no real archive producer compatibility claim is made.

## Filesystem replacement limits

[Python `os.replace`](https://docs.python.org/3/library/os.html#os.replace), official runtime documentation, accessed 2026-09-28, describes cross-filesystem replacement behavior and POSIX atomic rename. The fixture tests process exits only, not crash consistency, cache/flush semantics or power loss.

## Assumptions and limits

- All graph, receipt, custody, covariance, ranking, lineage and operator data are fixture/model/fiction.
- Exact unit conversions are not calibration.
- No hardware, provider invoice, physical sample or empirical SCM evidence is present.
