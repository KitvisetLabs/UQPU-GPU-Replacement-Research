# Cycle 022 Primary Source Review

**Review date:** 2026-09-28  
**Evidence class:** primary format/runtime documentation used as design inputs only.

## ZIP64 descriptors and record binding

[PKWARE APPNOTE v6.3.10 FINAL](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT), revised 2022-11-01, §§4.3.7, 4.3.9 and 4.3.12, accessed 2026-09-28, defines the ZIP64 local/central fields and data-descriptor layout. Cycle 022 mutates descriptor CRC and validates record cross-binding before payload reads. Its archives are synthetic and do not represent a producer corpus.

## Filesystem replacement

[Python `os.replace`](https://docs.python.org/3/library/os.html#os.replace), official documentation, accessed 2026-09-28, describes cross-filesystem replacement failures and successful atomic POSIX rename. These subprocess tests stop at process exit and do not measure crash consistency, flushes, caches or power loss.

## Assumptions and limits

- Graph, receipt, custody, covariance, ranking, lineage and operator evidence is local fixture/model/fiction only.
- Exact unit arithmetic is not calibration.
- No hardware execution, physical sample or provider record is observed.
