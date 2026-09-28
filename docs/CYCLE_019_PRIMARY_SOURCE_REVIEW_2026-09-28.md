# Cycle 019 Primary Source Review

**Review date:** 2026-09-28  
**Evidence class:** primary format specification and runtime documentation; design inputs only.

## ZIP64 descriptor forms

[PKWARE APPNOTE v6.3.10 FINAL](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT), revised 2022-11-01, §§4.3.7, 4.3.9 and 4.3.12, accessed 2026-09-28, specifies local/central record fields and ZIP64 descriptor values; the descriptor signature is optional. Cycle 019 tests signed and unsigned synthetic forms and size mutation rejection before payload access. It does not establish compatibility with a real archive producer corpus.

## Process replacement limits

[Python `os.replace`](https://docs.python.org/3/library/os.html#os.replace), official runtime documentation, accessed 2026-09-28, describes cross-filesystem failures and atomic successful POSIX rename behavior. The subprocess controls capture process-exit boundaries only; they do not test crash consistency, flushes, caches or power loss.

## Assumptions and limits

- Receipt, custody, covariance, ranking, lineage and operator inputs are synthetic, model or fiction fixtures.
- The unit rescaling check is an algebraic matrix transform and is not a calibration.
- No payload bytes, physical sample, provider invoice or hardware result are observed.
