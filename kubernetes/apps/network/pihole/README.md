# Stateless list refresh

Pi-hole uses `emptyDir` for `/etc/pihole`. It does not create a PVC. A new pod downloads the declared lists, builds Gravity, and labels the three existing YouTube subscriptions by exact URL. IDs can change when the database is rebuilt.

The init container also prepares the image's crontab. A Flux Helm post-render patch makes the main container copy it into `/crontab.txt` before running the normal image entrypoint. Do not bind-mount that file: the image uses `sed -i`, which needs to replace it by rename. The wrapper runs again on a main-container restart.

Native `crond` runs `pihole updateGravity` every day at **03:17 Asia/Kuala_Lumpur**, using the existing `${TIMEZONE}` cluster setting. This replaces the weekly Gravity entry, not the other maintenance jobs. All subscribed feeds refresh together; upstream HTTP cache validation can report “No changes detected”. The log is `/var/log/pihole/pihole_updateGravity.log`.

- `kboghdady/youTube_ads_4_pi-hole` and `pawan418/yt-ad-blocker` follow the remote published feeds. Their comment is `Suspicious YouTube Ads (daily upstream refresh)`.
- `fiqrimasngot/kube/.../t0mer-youtube.txt` remains the existing static snapshot. Its comment explicitly says it is not upstream-synced. Downloading it daily does not automate conversion from t0mer. This change does not add a converter or run upstream scripts.

Comments are labels, not new Pi-hole groups. Startup imports assign these lists to the default group. Subscription refresh does not infer new domains from query timing. DNS blocking of shared YouTube hosts can break playback and does not prove ads are removed.

## Temporary PS5 exact-host trial

The init container seeds an enabled exact deny rule (type `1`, not allow type `0`) for `rr3---sn-h5mpn-30ay.googlevideo.com` **after** `pihole -g` creates the database. It runs in a transaction with SQLite errors stopping init. Main Pi-hole startup follows only after init succeeds.

The rule belongs only to `PS5 exact-host trial`. Pi-hole's insert trigger initially assigns new rules to Default, so the SQL explicitly removes that assignment and any other non-trial assignment for this rule. There is no global `blacklist.txt` entry. The only client in the trial group is the exact IPv4 address `10.32.1.59`. That client also keeps Default and any other existing group mappings; other clients, groups, rules and subscriptions stay unchanged outside this dedicated trial scope. Unknown clients still use Default. Keep the PS5's address reserved; this does not cover a different IPv4 address or IPv6 source.

This is a user-authorized experiment, not a proven ad-only hostname. It appeared in labelled ad-related DNS evidence, but cached DNS and shared video delivery limit what that proves. Normal PS5 playback may break. No other lists or regex rules were added. Private query evidence stays outside Git.

After deployment, fully close and reopen the PS5 app, then check both ads and normal videos. Check real query logs for this exact host **from `10.32.1.59` after activation**. A rule that the PS5 has not queried is not an effectiveness test. Never spoof that source address for a probe. An ordinary non-PS5 DNS probe must still resolve this host.

### Check the scope

```sh
kubectl -n network exec deploy/pihole -c pihole -- pihole-FTL sqlite3 /etc/pihole/gravity.db "SELECT d.domain,d.type,d.enabled,g.name,g.enabled FROM domainlist d JOIN domainlist_by_group m ON m.domainlist_id=d.id JOIN \"group\" g ON g.id=m.group_id WHERE d.domain='rr3---sn-h5mpn-30ay.googlevideo.com';"
kubectl -n network exec deploy/pihole -c pihole -- pihole-FTL sqlite3 /etc/pihole/gravity.db "SELECT c.ip,g.name FROM client c JOIN client_by_group m ON m.client_id=c.id JOIN \"group\" g ON g.id=m.group_id ORDER BY c.ip,g.id;"
kubectl -n network exec deploy/pihole -c pihole -- nslookup rr3---sn-h5mpn-30ay.googlevideo.com 127.0.0.1
```

Expect one domain row: type `1`, enabled `1`, group `PS5 exact-host trial`, group enabled `1`. The PS5 must have Default plus the trial group, and no other client may belong to the trial group. The loopback DNS probe is a Default-group check, **not** a PS5 test; it must return real upstream addresses rather than a blocked answer.

### Roll back the trial

For a durable rollback, revert the trial commit and push to `main`, or remove only the temporary trial SQL from both HelmRelease files (keep the surrounding transaction, `COMMIT`, existing subscription labels and daily refresh). Reconcile the Git source, `network/pihole` Kustomization and HelmRelease. The changed init script rolls out a fresh pod and emptyDir without the trial rule, group or explicit client. Read back the applied Git revision, healthy new pod and absence of the rule; verify DNS resolves. A main-container-only restart does not clear emptyDir.

For urgent playback recovery before Git reconciliation, run `pihole deny remove rr3---sn-h5mpn-30ay.googlevideo.com` inside the Pi-hole container and reload lists with `pihole reloaddns`. Read back the rule's removal. Publish the rollback too: a new pod otherwise restores it. Do not add an allow rule as a removal shortcut.

## Verify

Run from the repository root:

```sh
uv run --with pyyaml python3 -m unittest discover -s kubernetes/apps/network/pihole/tests -v
kustomize build kubernetes/apps/network/pihole/app
kubectl -n network get helmrelease pihole
kubectl -n network exec deploy/pihole -c pihole -- crontab -l
kubectl -n network exec deploy/pihole -c pihole -- pihole-FTL sqlite3 /etc/pihole/gravity.db "SELECT id,address,enabled,comment,number,invalid_domains,status FROM adlist WHERE comment LIKE 'Suspicious YouTube%';"
```

The tests use the image's Gravity schema, including Default-assignment triggers. They check manifest/template values match, unique subscriptions, no PVC, startup ordering, daily schedule, idempotent SQL, exact trial scope, repair of unintended trial mappings, and preservation of unrelated rows and mappings. Render the pinned Helm chart **with the post-render patch** when validating the workload; `helm template` alone does not apply Flux post-renderers.

## Deployment status and rollback

Flux's `network/pihole` Kustomization follows `main` and manages this configuration. After publication, reconcile the Git source, this Kustomization, and the HelmRelease. Verify the applied Git revision and live crontab before treating the rollout as complete. Keep Flux unsuspended.

Live verification exercised a fresh emptyDir rollout and an actual native-cron Gravity run using a temporary accelerated schedule, then restored and read back the daily schedule. Both remote feeds were checked successfully; no upstream change was available during that run. The original duplicate Disconnect URL caused a first-init database constraint error and was deduplicated without removing a subscription.

For playback problems, disable the affected subscription by its exact URL in Pi-hole and run Gravity. Such UI changes disappear with a new emptyDir. For a durable rollback, remove the affected URL from both manifests before the next authorized publication. To restore the stock weekly schedule, remove the post-renderer and cron-generation portion of the init script; keep `pihole -g` if startup downloads are still wanted.
