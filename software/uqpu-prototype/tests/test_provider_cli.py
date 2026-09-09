import io
import json
import unittest
from contextlib import redirect_stdout

from uqpu.provider_cli import health_payload, main


class ProviderCliTests(unittest.TestCase):
    def test_health_payload_contains_all_provider_adapters(self):
        payload = health_payload()
        self.assertGreaterEqual(len(payload), 12)
        self.assertTrue(all("readiness" in x for x in payload))

    def test_dry_run_cli(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = main(["dry-run", "ibm_quantum", "--target", "diagnostic", "--shots", "10"])
        self.assertEqual(code, 0)
        result = json.loads(buf.getvalue())
        self.assertEqual(result["status"], "DRY_RUN_ONLY")
        self.assertEqual(result["shots"], 10)


if __name__ == "__main__":
    unittest.main()
