"""Unit tests with the real gotenberg-client; only HTTP is substituted."""
import importlib.util
import json
import unittest
from pathlib import Path
from unittest.mock import patch

from gotenberg_client import GotenbergClient
from gotenberg_client._base.routes import SyncBaseRoute
from gotenberg_client.options import PdfAFormat

spec = importlib.util.spec_from_file_location(
    "paperless_compat", Path(__file__).parents[1] / "compat/sitecustomize.py"
)
compat = importlib.util.module_from_spec(spec)
spec.loader.exec_module(compat)


class TranslationTests(unittest.TestCase):
    def test_merge_pdfa_keeps_input_unchanged(self):
        source = {"pdfa": "PDF/A-2b"}
        url, form = compat.translate_request("/forms/pdfengines/merge", source)
        self.assertEqual(url, "/forms/pdf/pipe")
        self.assertEqual(json.loads(form["stages"]), [
            {"op": "merge"}, {"op": "remediate", "profile": "PDF/A-2b"}
        ])
        self.assertEqual(source, {"pdfa": "PDF/A-2b"})
        self.assertNotIn("pdfa", form)

    def test_merge_plain_pdf(self):
        _, form = compat.translate_request("/forms/pdfengines/merge", {})
        self.assertEqual(json.loads(form["stages"]), [{"op": "merge"}])

    def test_conversion_preserves_other_options_and_all_pdfa_profiles(self):
        for route in ("/forms/chromium/convert/html", "/forms/libreoffice/convert"):
            for profile in ("PDF/A-1b", "PDF/A-2b", "PDF/A-3b"):
                url, form = compat.translate_request(route, {"pdfa": profile, "updateIndexes": "false"})
                self.assertEqual(url, route)
                self.assertEqual(form["updateIndexes"], "false")
                self.assertEqual(json.loads(form["stages"]), [{"op": "remediate", "profile": profile}])

    def test_unrelated_routes_unchanged(self):
        source = {"pdfa": "PDF/A-2b"}
        url, form = compat.translate_request("/health", source)
        self.assertEqual(url, "/health")
        self.assertIs(form, source)

    def test_install_idempotent(self):
        before = SyncBaseRoute._post_data
        compat.install()
        self.assertIs(before, SyncBaseRoute._post_data)

    def test_http_failure_preserves_route_for_retry(self):
        with GotenbergClient("http://localhost:3000") as client, client.merge.merge() as route:
            route.pdf_format(PdfAFormat.A2b)
            original = dict(route._form_data)
            with patch.object(route._client, "post", side_effect=RuntimeError("synthetic HTTP failure")) as post:
                for _ in range(2):
                    with self.assertRaisesRegex(RuntimeError, "synthetic HTTP failure"):
                        route.run()
                    sent = post.call_args.kwargs
                    self.assertEqual(sent["url"], "/forms/pdf/pipe")
                    self.assertEqual(len(json.loads(sent["data"]["stages"])), 2)
                    self.assertEqual(route._route_url, "/forms/pdfengines/merge")
                    self.assertEqual(route._form_data, original)

    def test_unsupported_client_fails_at_request_not_python_startup(self):
        with GotenbergClient("http://localhost:3000") as client, client.merge.merge() as route:
            with patch.object(compat, "version", return_value="2.0.0"):
                with self.assertRaisesRegex(RuntimeError, "Revalidate"):
                    route.run()


if __name__ == "__main__":
    unittest.main()
