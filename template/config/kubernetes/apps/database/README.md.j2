# Database

Created database namespace for the following helm
couchdb for obsidian
cloudnative-pg
dragonfly is a redis database for authentik
pgadmin for management

## Couchdb
Will depend on longhorn
Build it own init db

```yaml
        initContainers:
          init-config:
            image:
              repository: public.ecr.aws/docker/library/busybox
              tag: latest
            command:
              - "sh"
              - "-c"
              - "cp /tmp/config/*.ini /opt/couchdb/etc/default.d/; ls -lrt /opt/couchdb/etc/default.d;"

```
With the following config map

```yaml
      config:
        type: configMap
        name: obsidian-couchdb-configmap
        advancedMounts:
          main:
            init-config:
              - path: /tmp/config
```

## cloudnative-pg

Need to init-db first by adding the following line in the helm

```yaml
    initdb:
      database: immich
      owner: immich
      postInitApplicationSQL:
        - CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
        - CREATE EXTENSION IF NOT EXISTS cube;
        - CREATE EXTENSION IF NOT EXISTS earthdistance;
        - CREATE EXTENSION IF NOT EXISTS vectors;
      secret:
        name: cloudnative-pg
```

Then you should able to just recover the cluster on next deployment

```yaml
  bootstrap:
    recovery:
      source: &previousCluster postgres16-immich-v2
  # Note: externalClusters is needed when recovering from an existing cnpg cluster
  externalClusters:
    - name: *previousCluster
      barmanObjectStore:
        <<: *barmanObjectStore
        serverName: *previousCluster

```

cloudanative-pg are really useful when booting up on each db by only using initdb as a init for creating the db
should able to use the following hostname postgres-rw.database.svc.cluster.local

the following will ensure the db is backup into the minio via s3
```
  backup:
    retentionPolicy: 30d
    barmanObjectStore: &barmanObjectStore
      data:
        compression: bzip2
      wal:
        compression: bzip2
        maxParallel: 8
      destinationPath: s3://cloudnative-pg/
      endpointURL: http://minio.storage.svc.cluster.local:9000
      # Note: serverName version needs to be incremented
      # when recovering from an existing cnpg cluster
      serverName: &currentCluster postgres-immich-v1
      s3Credentials:
        accessKeyId:
          name: cloudnative-pg
          key: aws-access-key-id
        secretAccessKey:
          name: cloudnative-pg
          key: aws-secret-access-key

```

the following setup will ensure the db using recovery from the s3 restoration

```
  bootstrap:
    # initdb:
    #   database: immich
    #   owner: immich
    #   postInitApplicationSQL:
    #     - CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
    #     - CREATE EXTENSION IF NOT EXISTS cube;
    #     - CREATE EXTENSION IF NOT EXISTS earthdistance;
    #     - CREATE EXTENSION IF NOT EXISTS vectors;
    #   secret:
    #     name: cloudnative-pg
    recovery:
      source: &previousCluster postgres-immich-v10
  # # Note: externalClusters is needed when recovering from an existing cnpg cluster
  externalClusters:
    - name: *previousCluster
      barmanObjectStore:
        <<: *barmanObjectStore
        serverName: *previousCluster

```

should able to use dragonfly as redis databse by using the following hostname dragonfly.database.svc.cluster.local
password should not needed for this as is only use it for caching server



mariadb is the worst, hoping it gonna be work like cloudnative-pg
current workaround is to always find a way to create db initdb itself

```
    initdbScripts:
      create-pterodactyl.sql: |
        CREATE DATABASE IF NOT EXISTS panel;
        CREATE USER IF NOT EXISTS 'pterodactyl'@'%' IDENTIFIED BY '${PTERODACTYL_MARIADB_PASSWORD}';
        GRANT ALL PRIVILEGES ON panel.* to 'pterodactyl'@'%';
      # create-bookstack.sql: |
      #   CREATE DATABASE IF NOT EXISTS bookstackapp;
      #   CREATE USER IF NOT EXISTS 'bookstack'@'%' IDENTIFIED BY '${BOOKSTACK_MARIADB_PASSWORD}';
      #   GRANT ALL PRIVILEGES ON bookstackapp.* to 'bookstack'@'%';

```

only using couchdb soully for the obsidian, it got an option for s3 though, but i;m more comfortable using database to sync things around


pgadmin
is for managing or loooking what happen on it, shoukd able access the DB just fine when using pgadmin4 apps, on local

