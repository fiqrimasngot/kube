"""Run inside the Paperless app container against its Gotenberg sidecar.

Synthetic inputs only; no database writes or document imports.
"""
import io
import tempfile
from pathlib import Path

import pikepdf
from gotenberg_client import GotenbergClient
from gotenberg_client.options import PdfAFormat


def check(response, pages):
    assert response.status_code == 200
    assert response.content.startswith(b"%PDF-")
    with pikepdf.Pdf.open(io.BytesIO(response.content)) as pdf:
        assert len(pdf.pages) == pages, len(pdf.pages)
        with pdf.open_metadata() as metadata:
            assert str(metadata.get("pdfaid:part")) == "2", dict(metadata)
            assert str(metadata.get("pdfaid:conformance")).upper() == "B", dict(metadata)
    print(f"PASS: HTTP 200, {pages} page(s), PDF/A-2b metadata, {len(response.content)} bytes")


with tempfile.TemporaryDirectory(prefix="paperless-gotenberg-probe-") as directory:
    root = Path(directory)
    with GotenbergClient(host="http://localhost:3000", timeout=120) as client:
        with client.chromium.html_to_pdf() as route:
            first = route.string_index("<html><body><p>Synthetic compatibility test</p></body></html>").run()
            assert first.content.startswith(b"%PDF-")
            source = root / "source.pdf"
            source.write_bytes(first.content)
        print("Merge with PDF/A:")
        with client.merge.merge() as route:
            check(route.merge([source, source]).pdf_format(PdfAFormat.A2b).run(), 2)
        print("Single input merge (HTML_ONLY / TEXT_ONLY):")
        with client.merge.merge() as route:
            check(route.merge([source]).pdf_format(PdfAFormat.A2b).run(), 1)
        print("HTML directly to PDF/A (plain-text email path):")
        with client.chromium.html_to_pdf() as route:
            check(route.string_index("<html><body>Plain email test</body></html>").pdf_format(PdfAFormat.A2b).run(), 1)
        print("Office conversion with PDF/A:")
        office = root / "source.rtf"
        office.write_text(r"{\rtf1\ansi Synthetic office document}")
        with client.libre_office.to_pdf() as route:
            check(route.convert(office).update_indexes(update_indexes=False).pdf_format(PdfAFormat.A2b).run(), 1)
