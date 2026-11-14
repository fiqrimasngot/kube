"""Run with: uv run --with pyyaml python3 -m unittest discover -s kubernetes/apps/network/pihole/tests -v"""
import pathlib
import sqlite3
import unittest
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[5]
MANIFEST = ROOT / 'kubernetes/apps/network/pihole/app/helmrelease.yaml'
TEMPLATE = ROOT / 'template/config/kubernetes/apps/network/pihole/app/helmrelease.yaml.j2'


def values(path):
    return list(yaml.safe_load_all(path.read_text()))[1]['spec']['values']


class RefreshTests(unittest.TestCase):
    def test_daily_stateless_refresh_and_startup_labels(self):
        v = values(MANIFEST)
        self.assertEqual(v, values(TEMPLATE))
        self.assertEqual(len(v['adlists']), len(set(v['adlists'])))
        self.assertEqual(v.get('persistentVolumeClaim'), {'enabled': False})
        spec = list(yaml.safe_load_all(MANIFEST.read_text()))[1]['spec']
        patch = spec['postRenderers'][0]['kustomize']['patches'][0]['patch']
        self.assertIn('cp /etc/pihole/crontab.txt /crontab.txt', patch)
        self.assertIn('exec /usr/bin/start.sh', patch)
        self.assertNotIn('extraVolumeMounts', v)
        script = v['extraInitContainers'][0]['args'][0]
        self.assertIn('17 3 * * *', script)
        self.assertIn('pihole updateGravity', script)
        self.assertIn('pihole -g', script)
        sql = script.split("<<'SQL'\n", 1)[1].split('\nSQL', 1)[0]
        db = sqlite3.connect(':memory:')
        db.executescript(MANIFEST.parent.parent.joinpath('tests/gravity-schema.sql').read_text())
        feeds = [u for u in v['adlists'] if any(s in u for s in ('kboghdady/', 'pawan418/', 't0mer-youtube'))]
        self.assertEqual(len(feeds), 3)
        for url in feeds + ['https://unrelated.example/list']:
            db.execute('INSERT INTO adlist (address,comment) VALUES (?, ?)', (url, 'old'))
        sql = '\n'.join(line for line in sql.splitlines() if not line.startswith('.'))
        db.executescript(sql)
        db.executescript(sql)
        for url, label in db.execute('SELECT address,comment FROM adlist'):
            if url in feeds:
                self.assertIn('Suspicious YouTube Ads', label)
            else:
                self.assertEqual(label, 'old')


HOST = 'rr3---sn-h5mpn-30ay.googlevideo.com'
PS5 = '10.32.1.59'
GROUP = 'PS5 exact-host trial'


class TrialTests(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(':memory:')
        self.addCleanup(self.db.close)
        self.db.executescript(pathlib.Path(__file__).with_name('gravity-schema.sql').read_text())
        self.script = values(MANIFEST)['extraInitContainers'][0]['args'][0]
        # Dot commands belong to the sqlite CLI, not the SQL engine.
        self.sql = '\n'.join(line for line in self.script.split("<<'SQL'\n", 1)[1].split('\nSQL', 1)[0].splitlines()
                             if not line.startswith('.'))

    def assert_scope(self):
        self.assertEqual(self.db.execute('SELECT type,enabled FROM domainlist WHERE domain=?', (HOST,)).fetchall(), [(1, 1)])
        self.assertEqual(self.db.execute('SELECT g.name,g.enabled FROM domainlist d JOIN domainlist_by_group m ON m.domainlist_id=d.id JOIN "group" g ON g.id=m.group_id WHERE d.domain=? AND d.type=1', (HOST,)).fetchall(), [(GROUP, 1)])
        self.assertEqual(self.db.execute('SELECT c.ip FROM client c JOIN client_by_group m ON m.client_id=c.id JOIN "group" g ON g.id=m.group_id WHERE g.name=?', (GROUP,)).fetchall(), [(PS5,)])
        self.assertEqual({r[0] for r in self.db.execute('SELECT g.name FROM client c JOIN client_by_group m ON m.client_id=c.id JOIN "group" g ON g.id=m.group_id WHERE c.ip=?', (PS5,))}, {'Default', GROUP})
        self.assertEqual(self.db.execute('SELECT domain FROM vw_denylist WHERE group_id=0 AND domain=?', (HOST,)).fetchall(), [])
        self.assertEqual(self.db.execute('PRAGMA foreign_key_check').fetchall(), [])

    def test_fresh_gravity_database_scopes_only_ps5(self):
        self.db.executescript(self.sql)
        self.assert_scope()

    def test_repeated_seed_keeps_ids_and_exact_membership(self):
        self.db.executescript(self.sql)
        tables = ('group', 'client', 'domainlist', 'client_by_group', 'domainlist_by_group', 'adlist_by_group')
        before = {t: self.db.execute(f'SELECT * FROM "{t}"').fetchall() for t in tables}
        self.db.executescript(self.sql)
        self.assertEqual(before, {t: self.db.execute(f'SELECT * FROM "{t}"').fetchall() for t in tables})
        self.assert_scope()

    def test_existing_mappings_and_unrelated_rows_survive(self):
        self.db.executescript('''
            INSERT INTO "group" (id,name) VALUES (7,'Existing group');
            INSERT INTO client (id,ip,comment) VALUES (20,'10.32.1.59','Keep PS5 comment'),(21,'192.0.2.42','Other client');
            INSERT INTO client_by_group VALUES (20,7),(21,7);
            INSERT INTO domainlist (id,type,domain,comment) VALUES (30,0,'allowed.example','Keep allow'),(31,1,'blocked.example','Keep deny');
            INSERT INTO domainlist_by_group VALUES (30,7),(31,7);
            INSERT INTO adlist (id,address,comment) VALUES (40,'https://unrelated.example/list','Keep feed');
            INSERT INTO adlist_by_group VALUES (40,7);
        ''')
        tables = ('group', 'client', 'domainlist', 'adlist', 'client_by_group', 'domainlist_by_group', 'adlist_by_group')
        before = {t: set(self.db.execute(f'SELECT * FROM "{t}"')) for t in tables}
        self.db.executescript(self.sql)
        self.db.executescript(self.sql)
        for table, rows in before.items():
            self.assertTrue(rows <= set(self.db.execute(f'SELECT * FROM "{table}"')), table)
        self.assertEqual(self.db.execute('SELECT group_id FROM client_by_group WHERE client_id=20 ORDER BY group_id').fetchall(), [(0,), (7,), (8,)])
        self.assertEqual(self.db.execute('PRAGMA foreign_key_check').fetchall(), [])

    def test_repairs_disabled_trial_and_unintended_scope(self):
        self.db.executescript(self.sql)
        self.db.executescript('''
            UPDATE "group" SET enabled=0 WHERE name='PS5 exact-host trial';
            UPDATE domainlist SET enabled=0;
            INSERT INTO "group" (id,name) VALUES (19,'Unrelated');
            INSERT INTO domainlist_by_group SELECT id,0 FROM domainlist;
            INSERT INTO domainlist_by_group SELECT id,19 FROM domainlist;
            INSERT INTO client (ip) VALUES ('192.0.2.42');
            INSERT INTO client_by_group SELECT c.id,g.id FROM client c CROSS JOIN "group" g
              WHERE c.ip='192.0.2.42' AND g.name='PS5 exact-host trial';
            DELETE FROM client_by_group WHERE group_id=0 AND client_id=(SELECT id FROM client WHERE ip='10.32.1.59');
        ''')
        self.db.executescript(self.sql)
        self.assert_scope()
        self.assertEqual(self.db.execute("SELECT group_id FROM client_by_group JOIN client ON client.id=client_id WHERE ip='192.0.2.42'").fetchall(), [(0,)])

    def test_seed_runs_after_gravity_before_main_without_global_blacklist(self):
        v = values(MANIFEST)
        self.assertEqual(v['blacklist'], {})
        self.assertEqual(len(v['extraInitContainers']), 1)
        self.assertLess(self.script.index('pihole -g\n'), self.script.index("<<'SQL'"))
        self.assertIn('.bail on\nPRAGMA foreign_keys = ON;\nBEGIN IMMEDIATE;', self.script)
        self.assertIn('COMMIT;\nSQL', self.script)
        self.assertEqual(v['extraInitContainers'][0]['command'], ['sh', '-c'])
        self.assertTrue(self.script.startswith('set -eu\n'))
        self.assertFalse(any(m['mountPath'].endswith('blacklist.txt') for m in v['extraInitContainers'][0]['volumeMounts']))


if __name__ == '__main__':
    unittest.main()
