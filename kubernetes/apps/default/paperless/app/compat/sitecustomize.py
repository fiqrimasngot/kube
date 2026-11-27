"""Temporary Paperless 3.5.1 / gotenberg-client 1.0.0 compatibility for Gotenberg 9.

Loaded only in the app container through PYTHONPATH. No package files are
modified. Remove the mount and PYTHONPATH when upstream supports Gotenberg 9.
This deliberately covers Paperless's sync mail and Office conversion paths,
not the complete Gotenberg 8 API. Other routes/options retain upstream errors.
"""
import json
from functools import wraps
from importlib.metadata import version

from gotenberg_client._base.routes import SyncBaseRoute


def translate_request(url, data):
    """Translate only the conversion operations used by Paperless."""
    supported = {
        "/forms/pdfengines/merge",
        "/forms/chromium/convert/html",
        "/forms/libreoffice/convert",
    }
    if url not in supported:
        return url, data
    form = dict(data)
    stages = json.loads(form.pop("stages", "[]"))
    if url == "/forms/pdfengines/merge":
        # The dedicated v9 merge endpoint rejects stages; pipe supports both
        # merge and final PDF/A remediation in a single request.
        url = "/forms/pdf/pipe"
        stages.insert(0, {"op": "merge"})
    pdfa = form.pop("pdfa", None)
    if pdfa:
        stages.append({"op": "remediate", "profile": pdfa})
    if stages:
        form["stages"] = json.dumps(stages)
    return url, form


def install():
    if getattr(SyncBaseRoute._post_data, "_paperless_gotenberg9", False):
        return
    original = SyncBaseRoute._post_data

    @wraps(original)
    def post_data(self):
        # Python logs and ignores exceptions during sitecustomize import.
        # Check here instead so a dependency upgrade cannot silently bypass it.
        if version("gotenberg-client") != "1.0.0":
            raise RuntimeError("Revalidate the Gotenberg 9 compatibility shim before upgrading gotenberg-client")
        old_url, old_data = self._route_url, self._form_data
        self._route_url, self._form_data = translate_request(old_url, old_data)
        try:
            return original(self)
        finally:
            # Do not accumulate stages on retry or mutate caller-owned options.
            self._route_url, self._form_data = old_url, old_data

    post_data._paperless_gotenberg9 = True
    SyncBaseRoute._post_data = post_data


install()
