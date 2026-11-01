# Study Planner release ownership

Edit `kubernetes/apps/default/study-planner/app/helmrelease.yaml` for Study Planner deployment changes. The Study Planner Release workflow updates only this file when it publishes API and web images. Keep both image references pinned by digest.

`makejinja.toml` excludes this HelmRelease from generation in both template input layers. The template copy is a historical bootstrap example, not the deployed source of truth. Do not copy its old image references over the live file. For a new checkout, use the tracked live HelmRelease. Other Study Planner templates still generate normally.

Run the regression test with:

    uv run --frozen python -m unittest discover -s template/scripts -p 'test_release_owned_manifest.py' -v

The test advances both live image references in a temporary fixture and runs the real generator with the configured exclusion rules. It checks that neither input layer overwrites the live manifest and that an unrelated template still renders. It does not load cluster credentials or regenerate the real cluster tree.

## Accepted review-policy exception

On November 1, 2026, the owner chose to retain zero required approvals on `fiqrimasngot/study-planner/main` because only one collaborator was available. This is an accepted exception to the rollout plan's pull-request review requirement, not evidence that the original requirement passed.

Keep the required `CI / test` and `CI / docker-build` checks and administrator enforcement. Do not change the approval count without a new owner decision. Read back protection settings after publishing changes; this document does not establish their current remote values.
