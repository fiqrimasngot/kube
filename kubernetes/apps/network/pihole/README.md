# Stateless list refresh

Pi-hole uses `emptyDir` for `/etc/pihole`. It does not create a PVC. A new pod downloads the declared lists, builds Gravity, and labels the three existing YouTube subscriptions by exact URL. IDs can change when the database is rebuilt.

The init container also prepares the image's crontab. A Flux Helm post-render patch makes the main container copy it into `/crontab.txt` before running the normal image entrypoint. Do not bind-mount that file: the image uses `sed -i`, which needs to replace it by rename. The wrapper runs again on a main-container restart.

Native `crond` runs `pihole updateGravity` every day at **03:17 Asia/Kuala_Lumpur**, using the existing `${TIMEZONE}` cluster setting. This replaces the weekly Gravity entry, not the other maintenance jobs. All subscribed feeds refresh together; upstream HTTP cache validation can report “No changes detected”. The log is `/var/log/pihole/pihole_updateGravity.log`.

- `kboghdady/youTube_ads_4_pi-hole` and `pawan418/yt-ad-blocker` follow the remote published feeds. Their comment is `Suspicious YouTube Ads (daily upstream refresh)`.
- `fiqrimasngot/kube/.../t0mer-youtube.txt` remains the existing static snapshot. Its comment explicitly says it is not upstream-synced. Downloading it daily does not automate conversion from t0mer. This change does not add a converter or run upstream scripts.

Comments are labels, not new Pi-hole groups. Startup imports assign these lists to the default group. No domains are inferred from query timing. DNS blocking of shared YouTube hosts can break playback and does not prove ads are removed.

## Verify

Run from the repository root:

```sh
uv run --with pyyaml python3 -m unittest discover -s kubernetes/apps/network/pihole/tests -v
kustomize build kubernetes/apps/network/pihole/app
kubectl -n network get helmrelease pihole
kubectl -n network exec deploy/pihole -c pihole -- crontab -l
kubectl -n network exec deploy/pihole -c pihole -- pihole-FTL sqlite3 /etc/pihole/gravity.db "SELECT id,address,enabled,comment,number,invalid_domains,status FROM adlist WHERE comment LIKE 'Suspicious YouTube%';"
```

The unit test checks the manifest/template values match, unique subscriptions, no PVC, startup wrapper, daily schedule, and idempotent SQL labels that leave unrelated rows unchanged. Render the pinned Helm chart **with the post-render patch** when validating the workload; `helm template` alone does not apply Flux post-renderers.

## Deployment status and rollback

Flux's `network/pihole` Kustomization follows `main` and manages this configuration. After publication, reconcile the Git source, this Kustomization, and the HelmRelease. Verify the applied Git revision and live crontab before treating the rollout as complete. Keep Flux unsuspended.

Live verification exercised a fresh emptyDir rollout and an actual native-cron Gravity run using a temporary accelerated schedule, then restored and read back the daily schedule. Both remote feeds were checked successfully; no upstream change was available during that run. The original duplicate Disconnect URL caused a first-init database constraint error and was deduplicated without removing a subscription.

For playback problems, disable the affected subscription by its exact URL in Pi-hole and run Gravity. Such UI changes disappear with a new emptyDir. For a durable rollback, remove the affected URL from both manifests before the next authorized publication. To restore the stock weekly schedule, remove the post-renderer and cron-generation portion of the init script; keep `pihole -g` if startup downloads are still wanted.
