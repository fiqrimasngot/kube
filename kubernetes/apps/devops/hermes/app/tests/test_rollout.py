import shutil
import subprocess
import tempfile
import unittest
import os
from pathlib import Path
import yaml

APP = Path(__file__).resolve().parents[1]

class RolloutTest(unittest.TestCase):
    def test_patch_change_updates_helmrelease_reference(self):
        with tempfile.TemporaryDirectory() as tmp:
            app = Path(tmp) / 'app'
            shutil.copytree(APP, app)
            def render():
                out = subprocess.check_output(['kubectl', 'kustomize', str(app)], text=True)
                out = subprocess.check_output(['flux', 'envsubst'], input=out, text=True)
                objects = list(yaml.safe_load_all(out))
                release = next(o for o in objects if o['kind'] == 'HelmRelease')
                name = release['spec']['values']['persistence']['skill-patch-script']['name']
                config = next(o for o in objects if o['kind'] == 'ConfigMap' and o['metadata']['name'] == name)
                chart = os.environ.get('APP_TEMPLATE_CHART')
                if chart:
                    values = Path(tmp) / 'values.yaml'
                    values.write_text(yaml.safe_dump(release['spec']['values']))
                    helm = subprocess.check_output(['helm', 'template', 'hermes', chart, '--namespace', 'devops', '-f', str(values)], text=True)
                    deployment = next(o for o in yaml.safe_load_all(helm) if o and o['kind'] == 'Deployment' and o['metadata']['name'] == 'hermes')
                    pod = deployment['spec']['template']['spec']
                    names = [v['configMap']['name'] for v in pod['volumes'] if 'configMap' in v]
                    self.assertIn(name, names)
                    init = next(c for c in pod['initContainers'] if c['name'] == 'patch-kanban-skill-check')
                    self.assertTrue(any(m.get('subPath') == 'patch-skill-resolver.py' for m in init['volumeMounts']))
                return name, config
            before, _ = render()
            script = app / 'resources/patch-skill-resolver.py'
            script.write_text(script.read_text() + '\n# changed patch\n')
            after, _ = render()
            self.assertNotEqual(before, after)
