# Check the postBuild values on a real HelmRelease from each affected namespace.
INDEX(.[]; .metadata.namespace + "/" + .metadata.name) as $releases
| [
    $releases["default/paperless"].spec.values.persistence.consume.server,
    $releases["media/sonarr"].spec.values.persistence.tv.server,
    $releases["storage/samba"].spec.values.persistence.camera.server,
    $releases["media/ghost"].spec.values.route.app.hostnames[0]
  ] == ["nfs.example.invalid", "nfs.example.invalid", "nfs.example.invalid", "ghost.example.invalid"]
