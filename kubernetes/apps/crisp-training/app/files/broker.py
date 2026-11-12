"""Narrow GitHub OIDC -> fixed Kubernetes training Job broker."""
import json
import os
import re
import ssl
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import jwt
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey
from jwt.algorithms import RSAAlgorithm

ISSUER = "https://token.actions.githubusercontent.com"
JWKS_URL = "https://token.actions.githubusercontent.com/.well-known/jwks"
AUDIENCE = "crisp-gpu-training-broker"
REPO = "fiqrimasngot/crisp"
OWNER_ID = "39836635"
REPO_ID = "1445010308"
REF = "refs/heads/main"
WORKFLOW = "fiqrimasngot/crisp/.github/workflows/train-gpu.yaml@refs/heads/main"
UPSTREAM_SHA = "0f250620df338351ac7be42330672379d5360818"
IMAGE = "tensorflow/tensorflow:2.21.0-gpu@sha256:61fe1ce25bd26b0a38e310463a5588d4067d2d01b6bdb058a3ca4f5cf2e18f15"
NAMESPACE = "crisp-training"


class Unauthorized(Exception):
    pass


def fetch_jwks():
    with urlopen(JWKS_URL, timeout=5) as response:
        return json.load(response)


def authorize(token):
    try:
        header = jwt.get_unverified_header(token)
        if header.get("alg") != "RS256" or not isinstance(header.get("kid"), str):
            raise Unauthorized("unsupported token header")
        keys = fetch_jwks().get("keys", [])
        match = [key for key in keys if key.get("kid") == header["kid"] and key.get("kty") == "RSA" and key.get("use", "sig") == "sig"]
        if len(match) != 1:
            raise Unauthorized("unknown signing key")
        public_key = RSAAlgorithm.from_jwk(match[0])
        if not isinstance(public_key, RSAPublicKey):
            raise Unauthorized("signing key must be public")
        claims = jwt.decode(token, public_key, algorithms=["RS256"], audience=AUDIENCE,
                            issuer=ISSUER, options={"require": ["exp", "iat", "nbf", "iss", "aud", "sub"]})
        expected = {
            # The organization configures GitHub's ID-bound OIDC subject template.
            "iss": ISSUER, "aud": AUDIENCE,
            "sub": f"repo:fiqrimasngot@{OWNER_ID}/crisp@{REPO_ID}:ref:{REF}",
            "repository": REPO, "repository_id": REPO_ID, "ref": REF,
            "workflow_ref": WORKFLOW, "event_name": "workflow_dispatch",
        }
        if not isinstance(claims.get("aud"), str):
            raise Unauthorized("audience must be exact")
        if any(claims.get(key) != value for key, value in expected.items()):
            raise Unauthorized("workflow identity mismatch")
        if not isinstance(claims.get("sha"), str) or not re.fullmatch(r"[0-9a-f]{40}", claims["sha"]):
            raise Unauthorized("invalid source sha")
        if any(not isinstance(claims.get(key), str) or not re.fullmatch(r"[1-9][0-9]{0,11}", claims[key])
               for key in ("run_id", "run_attempt")):
            raise Unauthorized("invalid run identity")
        return claims
    except (jwt.PyJWTError, ValueError, KeyError, TypeError) as exc:
        raise Unauthorized("invalid OIDC token") from exc


def job_name(claims):
    return f"crisp-train-{claims['run_id']}-{claims['run_attempt']}"


def owns_job(claims, name):
    return name == job_name(claims)


def build_job(claims):
    name = job_name(claims)
    sha = claims["sha"]
    # The caller can only select its own signed run/commit. It cannot supply commands,
    # PVC names, images, namespace, resource requests or arbitrary Job names.
    bootstrap = '''import io,tarfile,urllib.request
from pathlib import Path
sha = "''' + sha + '''"
url = "https://codeload.github.com/fiqrimasngot/crisp/tar.gz/" + sha
with urllib.request.urlopen(url, timeout=90) as response:
    archive = tarfile.open(fileobj=io.BytesIO(response.read()), mode="r:gz")
    root = "crisp-" + sha + "/"
    for member in archive:
        if member.name not in (root + "scripts/run_training_job.py", root + "scripts/prepare_training_source.py", root + "scripts/validate_training_dataset.py"):
            continue
        target = Path("/work") / member.name.removeprefix(root)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(archive.extractfile(member).read())
for name in ("run_training_job.py", "prepare_training_source.py", "validate_training_dataset.py"):
    if not (Path("/work/scripts") / name).is_file():
        raise RuntimeError("missing pinned trainer script: " + name)
'''
    command = ["/bin/sh", "-ec", "python -m pip install --user --no-cache-dir 'tensorflow[and-cuda]==2.21.0' && "
               "python -c \"$BOOTSTRAP\" && python /work/scripts/run_training_job.py " + name]
    return {
        "apiVersion": "batch/v1", "kind": "Job",
        "metadata": {"name": name, "namespace": NAMESPACE,
                     "annotations": {"crisp.nousresearch.com/source-sha": sha,
                                     "crisp.nousresearch.com/run-id": claims["run_id"],
                                     "crisp.nousresearch.com/run-attempt": claims["run_attempt"]}},
        "spec": {"activeDeadlineSeconds": 14400, "ttlSecondsAfterFinished": 86400,
                 "backoffLimit": 0, "parallelism": 1, "completions": 1,
                 "template": {"metadata": {"labels": {"app.kubernetes.io/name": "crisp-training-job"}},
                              "spec": {"restartPolicy": "Never", "runtimeClassName": "nvidia",
                                       "serviceAccountName": "crisp-training-job", "automountServiceAccountToken": False,
                                       "securityContext": {"runAsNonRoot": True, "runAsUser": 1000, "runAsGroup": 1000, "fsGroup": 1000,
                                                           "seccompProfile": {"type": "RuntimeDefault"}},
                                       "containers": [{"name": "trainer", "image": IMAGE, "imagePullPolicy": "IfNotPresent",
                                                       "command": command,
                                                       "env": [{"name": "BOOTSTRAP", "value": bootstrap},
                                                               {"name": "HOME", "value": "/work"},
                                                               {"name": "PYTHONUNBUFFERED", "value": "1"}],
                                                       "workingDir": "/work", "resources": {
                                                           "requests": {"nvidia.com/gpu": "1", "memory": "8Gi", "cpu": "2"},
                                                           "limits": {"nvidia.com/gpu": "1", "memory": "16Gi", "cpu": "8"}},
                                                       "securityContext": {"allowPrivilegeEscalation": False,
                                                                           "capabilities": {"drop": ["ALL"]}},
                                                       "volumeMounts": [{"name": "dataset", "mountPath": "/dataset", "readOnly": True},
                                                                        {"name": "output", "mountPath": "/models", "subPath": name},
                                                                        {"name": "work", "mountPath": "/work"}]}],
                                       "volumes": [{"name": "dataset", "persistentVolumeClaim": {"claimName": "crisp-public-dataset", "readOnly": True}},
                                                   {"name": "output", "persistentVolumeClaim": {"claimName": "crisp-model-output"}},
                                                   {"name": "work", "emptyDir": {}}]}}}}


def same_job(existing, expected):
    def contains(actual, wanted):
        if isinstance(wanted, dict):
            return isinstance(actual, dict) and all(
                key in actual and contains(actual[key], value) for key, value in wanted.items())
        if isinstance(wanted, list):
            return (isinstance(actual, list) and len(actual) == len(wanted)
                    and all(contains(a, w) for a, w in zip(actual, wanted)))
        return actual == wanted

    return (existing.get("metadata", {}).get("name") == expected["metadata"]["name"]
            and existing.get("metadata", {}).get("namespace") == NAMESPACE
            and contains(existing.get("metadata", {}).get("annotations"), expected["metadata"]["annotations"])
            and contains(existing.get("spec"), expected["spec"]))


def kube(method, path, payload=None):
    token = open("/var/run/secrets/kubernetes.io/serviceaccount/token", encoding="utf-8").read().strip()
    context = ssl.create_default_context(cafile="/var/run/secrets/kubernetes.io/serviceaccount/ca.crt")
    host = os.environ.get("KUBERNETES_SERVICE_HOST", "kubernetes.default.svc")
    port = os.environ.get("KUBERNETES_SERVICE_PORT", "443")
    request = Request(f"https://{host}:{port}/apis/batch/v1/namespaces/{NAMESPACE}/jobs{path}",
                      data=json.dumps(payload).encode() if payload is not None else None,
                      headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"}, method=method)
    with urlopen(request, context=context, timeout=10) as response:
        return json.load(response)


def status(job):
    state = job.get("status", {})
    conditions = {c.get("type"): c.get("status") for c in state.get("conditions", [])}
    phase = "succeeded" if conditions.get("Complete") == "True" else (
        "failed" if conditions.get("Failed") == "True" else "running" if state.get("active") else "pending")
    return {"name": job["metadata"]["name"], "phase": phase,
            "active": state.get("active", 0), "succeeded": state.get("succeeded", 0), "failed": state.get("failed", 0)}


class Handler(BaseHTTPRequestHandler):
    def respond(self, code, body):
        data = json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def handle_request(self):
        if self.path == "/healthz" and self.command == "GET":
            return self.respond(200, {"ok": True})
        try:
            auth = self.headers.get("Authorization", "")
            if not auth.startswith("Bearer "):
                raise Unauthorized("missing bearer token")
            claims = authorize(auth[7:])
            name = job_name(claims)
            if self.command == "POST" and self.path == "/jobs":
                if self.headers.get("Content-Length", "0") != "0":
                    return self.respond(400, {"error": "request body forbidden"})
                expected = build_job(claims)
                try:
                    job = kube("POST", "", expected)
                except HTTPError as exc:
                    if exc.code != 409:
                        raise
                    exc.close()
                    job = kube("GET", "/" + name)
                    if not same_job(job, expected):
                        return self.respond(409, {"error": "job identity conflict"})
                return self.respond(200, status(job))
            if self.command == "GET" and self.path == "/jobs/" + name:
                job = kube("GET", "/" + name)
                if not same_job(job, build_job(claims)):
                    return self.respond(404, {"error": "job not found"})
                return self.respond(200, status(job))
            return self.respond(404, {"error": "not found"})
        except Unauthorized:
            return self.respond(401, {"error": "unauthorized"})
        except HTTPError as exc:
            return self.respond(502, {"error": "kubernetes API error", "code": exc.code})
        except (OSError, ValueError) as exc:
            print(f"broker dependency error: {type(exc).__name__}", flush=True)
            return self.respond(503, {"error": "broker dependency unavailable"})

    do_GET = handle_request
    do_POST = handle_request


if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
