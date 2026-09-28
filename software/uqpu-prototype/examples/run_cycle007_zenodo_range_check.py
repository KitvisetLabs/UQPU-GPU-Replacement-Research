"""Fetch bounded official Zenodo ranges and verify ZIP metadata/README CRC.

This deliberately does not download the 145 MB archive or its Parquet payloads.
"""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.request

from uqpu.cycle006_delta01 import (
    parse_zip_central_directory_tail,
    recover_zip_member_from_range,
)
from uqpu.cycle007_delta01 import validate_content_range


ROOT = Path(__file__).resolve().parents[3]
API_URL = "https://zenodo.org/api/records/14257632"
RECORD_URL = "https://zenodo.org/records/14257632"
ARCHIVE_URL = "https://zenodo.org/records/14257632/files/data_upload.zip?download=1"
MAX_ZIP_TAIL_BYTES = 22 + 65535
MAX_README_RANGE_BYTES = 4096
MAX_API_BYTES = 2_000_000


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _open(request: urllib.request.Request, *, limit: int) -> tuple[int, dict, bytes]:
    with urllib.request.urlopen(request, timeout=45) as response:
        status = response.status
        headers = {key.lower(): value for key, value in response.headers.items()}
        # Never read an unbounded response, even if a source ignores Range.
        body = response.read(limit + 1)
        if len(body) > limit:
            raise ValueError(f"response exceeds bounded read limit ({limit} bytes)")
        return status, headers, body


def _get_exact_range(start: int, end: int, total: int, *, limit: int):
    if end - start + 1 > limit:
        raise ValueError("requested range exceeds configured byte limit")
    request = urllib.request.Request(
        ARCHIVE_URL,
        headers={"Range": f"bytes={start}-{end}", "Accept-Encoding": "identity"},
    )
    status, headers, body = _open(request, limit=limit)
    errors = validate_content_range(
        status=status,
        content_range=headers.get("content-range"),
        start=start,
        end=end,
        total=total,
        body_length=len(body),
    )
    if errors:
        raise ValueError(f"range response rejected: {errors}")
    return body, {
        "status": status,
        "content_range": headers.get("content-range"),
        "returned_bytes": len(body),
        "sha256": _sha256(body),
        "http_date": headers.get("date"),
    }


def capture() -> dict:
    request = urllib.request.Request(API_URL, headers={"Accept": "application/json"})
    status, api_headers, api_body = _open(request, limit=MAX_API_BYTES)
    if status != 200:
        raise ValueError(f"Zenodo API returned HTTP {status}, expected 200")
    record = json.loads(api_body)
    if record.get("id") != 14257632:
        raise ValueError("Zenodo record ID mismatch")
    files = record.get("files", [])
    if len(files) != 1 or files[0].get("key") != "data_upload.zip":
        raise ValueError("unexpected archive inventory")
    archive = files[0]
    size = archive.get("size")
    if not isinstance(size, int) or size <= 0:
        raise ValueError("archive size missing or invalid")

    tail_start = max(0, size - MAX_ZIP_TAIL_BYTES)
    tail, tail_observation = _get_exact_range(
        tail_start, size - 1, size, limit=MAX_ZIP_TAIL_BYTES
    )
    central = parse_zip_central_directory_tail(
        tail, range_start=tail_start, archive_size=size
    )
    readme_entry = next(
        (row for row in central["entries"] if row["path"] == "data_upload/README.md"),
        None,
    )
    if readme_entry is None:
        raise ValueError("README entry missing from central directory")
    readme_start = readme_entry["local_header_offset"]
    readme_end = min(readme_start + MAX_README_RANGE_BYTES - 1, size - 1)
    readme_range, readme_observation = _get_exact_range(
        readme_start, readme_end, size, limit=MAX_README_RANGE_BYTES
    )
    recovered = recover_zip_member_from_range(
        readme_range, "data_upload/README.md"
    )
    if recovered["crc32"] != readme_entry["crc32"]:
        raise ValueError("README local and central-directory CRC mismatch")
    readme_text = recovered.pop("content").decode("utf-8")
    anchors = [
        "pandas data frames",
        'pd.read_parquet("first_d3_bit_flip")',
        "nbar: storage mean photon number",
        "num_cycles: The number of cycles",
        "The logical state is the xor",
        "The syndromes take values of 0,1, and 2",
        "syndrome state 0 represents even, 1 represents an erasure, and 2 represents odd",
    ]
    missing = [anchor for anchor in anchors if anchor not in readme_text]
    if missing:
        raise ValueError(f"README semantic anchors missing: {missing}")

    metadata = record["metadata"]
    return {
        "schema": "uqpu-cycle007-primary-source-range-verification-v1",
        "cycle": "007",
        "delta": "01",
        "access_date_utc": datetime.now(timezone.utc).date().isoformat(),
        "source": {
            "record_url": RECORD_URL,
            "api_url": API_URL,
            "archive_url": ARCHIVE_URL,
            "record_id": record["id"],
            "title": metadata.get("title"),
            "publication_date": metadata.get("publication_date"),
            "license": metadata.get("license"),
            "api_http_status": status,
            "api_http_date": api_headers.get("date"),
            "api_response_bytes": len(api_body),
            "api_response_sha256": _sha256(api_body),
        },
        "archive": {
            "key": archive["key"],
            "bytes": size,
            "publisher_checksum_metadata": archive.get("checksum"),
            "full_archive_downloaded": False,
            "full_archive_checksum_recomputed": False,
            "tail_range": {
                "start": tail_start,
                "end": size - 1,
                **tail_observation,
            },
            "central_directory": {
                "eocd": central["eocd"],
                "inventory_summary": central["inventory_summary"],
                "readme_entry": readme_entry,
            },
        },
        "readme_range": {
            "start": readme_start,
            "end": readme_end,
            **readme_observation,
            "member_path": recovered["path"],
            "member_crc32": recovered["crc32"],
            "central_directory_crc32": readme_entry["crc32"],
            "member_sha256": recovered["sha256"],
            "member_bytes": recovered["uncompressed_size"],
            "semantic_anchors_checked": len(anchors),
            "semantic_anchors_missing": missing,
        },
        "analysis_state": {
            "parquet_payload_retrieved": False,
            "experimental_values_read": False,
            "full_archive_md5_recomputed": False,
            "project_reproduction": False,
        },
        "evidence_class": "PRIMARY_ZENODO_API_AND_HTTP_RANGE_VERIFIED_ARCHIVE_METADATA_AND_README_CRC",
        "nonclaims": [
            "The API publisher MD5 is recorded but was not recomputed across the full archive.",
            "No Parquet payload, experimental value, rate, fit, uncertainty, or reproduction was analyzed.",
            "Range integrity and README CRC do not authenticate every archive byte.",
        ],
    }


def main() -> int:
    result = capture()
    output = ROOT / "benchmarks/evidence/cycle007-delta01-zenodo-range-verification.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(output.relative_to(ROOT)),
        "archive_bytes": result["archive"]["bytes"],
        "tail_range": result["archive"]["tail_range"]["content_range"],
        "entries": result["archive"]["central_directory"]["inventory_summary"]["entries"],
        "readme_sha256": result["readme_range"]["member_sha256"],
        "full_archive_checksum_recomputed": result["archive"]["full_archive_checksum_recomputed"],
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
