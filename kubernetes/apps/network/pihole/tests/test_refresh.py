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
        db.execute('CREATE TABLE adlist (address TEXT, comment TEXT)')
        feeds = [u for u in v['adlists'] if any(s in u for s in ('kboghdady/', 'pawan418/', 't0mer-youtube'))]
        self.assertEqual(len(feeds), 3)
        for url in feeds + ['https://unrelated.example/list']:
            db.execute('INSERT INTO adlist VALUES (?, ?)', (url, 'old'))
        db.executescript(sql)
        db.executescript(sql)
        for url, label in db.execute('SELECT address,comment FROM adlist'):
            if url in feeds:
                self.assertIn('Suspicious YouTube Ads', label)
            else:
                self.assertEqual(label, 'old')


if __name__ == '__main__':
    unittest.main()
