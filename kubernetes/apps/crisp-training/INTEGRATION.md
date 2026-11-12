# Run Crisp GPU training

This setup lets a manual `fiqrimasngot/crisp` workflow ask a broker to start one GPU Job. The `gha-crisp` runner has no Kubernetes token, GPU, or dataset mount. The broker checks GitHub's signed OIDC identity, then creates a fixed Job in `crisp-training`. The Job reads `crisp-public-dataset` and writes the checkpoint to the separate, private `crisp-model-output` claim. Never mount `devops/hermes` here.

## Publish and verify the manifests

The `app/files/broker.py` copy must match `fiqrimasngot/crisp/training_broker/broker.py`. The app Kustomization packages that file into a hash-named ConfigMap and rewrites the broker Deployment reference. The Python base image is pinned by digest; startup installs PyJWT 2.15.0 and cryptography 46.0.3. For an offline/reproducible deployment, replace startup installation with a tested, digest-pinned broker image.

Run these checks from the kube repository before publishing:

```sh
kubectl kustomize kubernetes/apps/crisp-training
kubectl kustomize kubernetes/apps/crisp-training/app
kubectl apply --dry-run=server -k kubernetes/apps/crisp-training/app
```

The admission policy must accept only the broker's fixed Job shape; a dry-run does **not** prove live admission. The Job image is pinned to `tensorflow/tensorflow:2.21.0-gpu` by digest. It checks TensorFlow GPU visibility before training. The dataset is read-only in the trainer; its working directory is ephemeral. The model claim is not mounted in ARC. Each trainer sees only its own Job-named `subPath` of the claim. The trainer needs public HTTPS to download pinned source and CUDA dependencies, so review both sources before dispatch. NetworkPolicy does not prevent exfiltration to public HTTPS; do not put private data in this dataset claim.

After Flux reconciles, check the namespace, both PVCs, broker rollout, service endpoints, quota, policy and binding, and the updated ARC NetworkPolicy. Cilium translates the Kubernetes Service address before enforcing policy here, so `apiserver-network.yaml` grants the broker the `kube-apiserver` entity instead of relying on a node IP. Confirm a broker API request returns an authenticated 404 for a nonexistent Job, then test the broker from an assigned `gha-crisp` runner. A healthy Deployment alone does not prove API access, GitHub OIDC, or runner connectivity.

## Seed the public dataset once

`manual/seed-job.yaml` and `manual/seed-networkpolicy.yaml` are intentionally outside Flux. Apply the temporary NetworkPolicy and seed Job only after the namespace and PVC are ready. The Job downloads public Drive file `1tc9MGn5bpyVe63k2uDb-ABx8KC2yRpqP`, checks the 14,918,553,729-byte ZIP and SHA-256 `12593cb29b693db7d14cd145afd2293720be3ed9fa1a6e3f6aaae492def6ae74`, then verifies 16,519,380,466 extracted bytes and the file count. The archive has 75 missing DeepFashion image references; preprocessing skips these records. Once the Job succeeds, confirm its checksum marker and dataset validation, then remove the temporary seed NetworkPolicy. A marker alone is not proof of the files if someone changed the claim later.

Dispatch `.github/workflows/train-gpu.yaml` on `main` after seeding. Watch the workflow **and** the Job and its logs. Only report a successful model after checking the new `<job-name>/project_model_best.keras` in the private claim and loading it to verify output shapes. The workflow reports Job completion, not model quality or inference deployment. The existing inference app is unchanged.
