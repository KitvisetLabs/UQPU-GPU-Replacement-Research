from __future__ import annotations

import json

from uqpu.qos_d23_positive_margin_repair import batch034_certificate


if __name__ == "__main__":
    print(json.dumps(batch034_certificate(), indent=2, sort_keys=True))
