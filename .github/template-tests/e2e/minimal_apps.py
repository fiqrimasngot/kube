#!/usr/bin/env python3
"""Publish only the core Flux apps for the small QEMU bootstrap cluster.

This edits the temporary Git mirror, never the rendered working tree. Keep the
real Helm/bootstrap inputs in place; only limit what cluster-apps reconciles.
"""

from pathlib import Path
import sys


APPS = {
    "default": (),
    "flux-system": ("flux-operator", "flux-instance"),
    "kube-system": ("cilium", "coredns"),
}


def main(kubernetes: Path) -> None:
    apps = kubernetes / "apps"
    for namespace, workloads in APPS.items():
        resources = ["./namespace.yaml", *(f"./{name}/ks.yaml" for name in workloads)]
        components = "components:\n  - ../../components/sops\n" if workloads else ""
        (apps / namespace / "kustomization.yaml").write_text(
            "---\napiVersion: kustomize.config.k8s.io/v1beta1\n"
            f"kind: Kustomization\nnamespace: {namespace}\n{components}resources:\n"
            + "".join(f"  - {resource}\n" for resource in resources)
        )
    (apps / "kustomization.yaml").write_text(
        "---\napiVersion: kustomize.config.k8s.io/v1beta1\n"
        "kind: Kustomization\nresources:\n"
        + "".join(f"  - ./{namespace}\n" for namespace in APPS)
    )


if __name__ == "__main__":
    main(Path(sys.argv[1]))
