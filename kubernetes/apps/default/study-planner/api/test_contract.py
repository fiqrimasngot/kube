from pathlib import Path

API = Path(__file__).with_name("app.py").read_text()
MIGRATION = Path(__file__).parent.joinpath("migrations/001_reminders.sql").read_text()
FRONTEND = Path(__file__).parents[1].joinpath("app/configmap.yaml").read_text()

assert '"/api/healthz"' in API
for route in ('/api/reminders', '/api/reminders/due'):
    assert route in API
for field in ('title', 'details', 'remind_at', 'completed', 'created_at', 'updated_at'):
    assert field in API
assert 'pg_advisory_xact_lock' in API
assert 'schema_migrations' in API
assert 'ORDER BY remind_at ASC NULLS LAST, id ASC' in API
assert 'BIGSERIAL PRIMARY KEY' in MIGRATION
assert 'location /api/' in FRONTEND
assert 'proxy_pass http://127.0.0.1:8081;' in FRONTEND
assert "taskKey='study-planner-tasks'" in FRONTEND
assert 'localStorage.setItem(taskKey' in FRONTEND
assert 'length < 0' in API
for action in ('POST', 'PATCH', 'DELETE'):
    assert f'do_{action}' in API or action == 'POST'
for marker in ('loadReminders', 'editReminder', 'toggleReminder', 'deleteReminder'):
    assert marker in FRONTEND
WORKFLOW = Path(__file__).parents[5].joinpath('.github/workflows/study-planner-api.yaml').read_text()
assert 'docker/build-push-action' in WORKFLOW
assert 'org.opencontainers.image.revision=${{ github.sha }}' in WORKFLOW
assert 'steps.image.outputs.digest' in WORKFLOW
print("study-planner reminder contract checks passed")
