# Hermes Agent

Adapted from [blackjid/home-ops](https://github.com/blackjid/home-ops/blob/main/kubernetes/apps/ai/hermes/app/helmrelease.yaml).

The `devops/hermes` release runs the Hermes gateway and dashboard together, using
app-template 5.2.1 and the reference's pinned Hermes v2026.9.24 image. The dashboard
uses the internal Envoy gateway at **https://hermes.fiqriha.kim**. The API remains
cluster-internal at **http://hermes.devops.svc.cluster.local:8642/v1**.

A dedicated 10 GiB `ceph-block` PVC stores `/opt/data`, including configuration,
provider logins, sessions, skills, and the workspace. `Recreate` avoids simultaneous
writers during updates. The PVC is protected from Flux pruning; backups are not
configured. Initial config is copied only when no config exists, so UI/CLI changes
and provider login survive restarts. The Kubernetes service account has read-only
inspection permissions; it cannot change workloads or read Secrets.

## Dashboard login

Username: `fiqrim`. Retrieve the generated password locally:

```sh
kubectl -n devops get secret hermes-secret \
  -o jsonpath='{.data.HERMES_DASHBOARD_BASIC_AUTH_PASSWORD}' | base64 --decode
```

Credentials are SOPS-encrypted in `app/secret.sops.yaml`. The template copy is
also encrypted and preserves these credentials when configuration is regenerated.

## Connect your ChatGPT subscription

Once the pod is running:

```sh
kubectl -n devops exec -it deployment/hermes -c app -- hermes model
```

Select **ChatGPT or Codex Subscription**, complete the displayed device login in
your browser, and choose an available model. This is Hermes' `openai-codex`
provider; it does not turn a ChatGPT subscription into a general OpenAI API key.
Provider authentication requires your interaction and is not preconfigured.

Restart Hermes after changing provider settings:

```sh
kubectl -n devops rollout restart deployment/hermes
```

The login and selected model are persisted on the PVC. To use API billing instead,
select OpenAI in the same setup flow and provide your own API key there.

## Use your existing Ollama backend

In `hermes model`, select a custom OpenAI-compatible endpoint:

- Base URL: `http://ollama.devops.svc.cluster.local:11434/v1`
- API key: `ollama` (a placeholder for your unauthenticated local Ollama endpoint)
- Model: an exact tool-capable model name already installed in your Ollama server.

Hermes reuses Ollama over the network and requests no additional GPU.

## Add Hermes to Open WebUI

After connecting a provider, add an OpenAI-compatible connection in Open WebUI's
administrator settings. Keep the existing Ollama connection.

- URL: `http://hermes.devops.svc.cluster.local:8642/v1`
- Model: `hermes-agent`
- API key: retrieve the Hermes gateway token below (this is not an OpenAI key):

```sh
kubectl -n devops get secret hermes-secret \
  -o jsonpath='{.data.API_SERVER_KEY}' | base64 --decode
```

## GitOps and verification

`../kustomization.yaml` includes `hermes/ks.yaml`; the generated and template trees
are both updated. Push these files to the watched repository to make this release
managed by the cluster's normal Flux reconciliation.

```sh
kubectl -n devops get helmrelease hermes
kubectl -n devops get pods -l app.kubernetes.io/instance=hermes
kubectl -n devops logs deployment/hermes -c app --tail=50
kubectl -n devops logs deployment/hermes -c dashboard --tail=50
```

References: [Hermes providers](https://hermes-agent.nousresearch.com/docs/integrations/providers/),
[dashboard](https://hermes-agent.nousresearch.com/docs/user-guide/features/web-dashboard/),
[API server](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server/).
