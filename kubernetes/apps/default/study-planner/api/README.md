# Study Planner reminder API

This is the checked-in build context for the same-Pod reminder API. It binds to
`127.0.0.1:8081` by default and uses the runtime-only `DB_HOST`, `DB_PORT`,
`DB_NAME`, `DB_USER`, and `DB_PASSWORD` environment variables. Startup applies
versioned migrations under a PostgreSQL advisory transaction lock.

Build and publish this image to an approved immutable registry reference before
adding it to the HelmRelease. The deployment intentionally does not invent a
registry coordinate or credentials.
