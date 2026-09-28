# Cycle 018 Primary Source Review

**Review date:** 2026-09-28  
**Review depth:** checked the official ZIP64 local/central/descriptor definitions and Python replacement documentation.  
**Evidence class:** primary format specification and runtime documentation; design inputs only.

## ZIP64 cross-binding

[PKWARE APPNOTE v6.3.10 FINAL](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT), revised 2022-11-01, §§4.3.7, 4.3.9 and 4.3.12, accessed 2026-09-28.

The specification defines matching local-file and central-directory records; the central entry carries the disk number and disk-relative local-header offset. ZIP64 descriptor sizes use 8-byte values. This cycle's fixture binds the name, flags, method, CRC/size metadata, offset, disk and descriptor, rejecting mutations before reading payload bytes. It does not cover complete archives or all producer variants.

## Process-level replacement

[Python `os.replace`](https://docs.python.org/3/library/os.html#os.replace), official Python documentation, accessed 2026-09-28.

Cross-filesystem replacement may fail and successful rename is atomic on POSIX. Cycle 018 checks stale-stage cleanup after subprocess exits and preserves active names during cleanup. This does not test crash consistency, cache persistence, device flush or power-loss durability.

## Assumptions and limits

- The ZIP vectors are synthetic and single-entry; payload bytes are not inspected.
- The filesystem test is local to this run's operating system and mounted filesystem.
- The model and schema fixtures do not establish provider, physical, commercial, AI-equivalence, or empirical SCM evidence.
