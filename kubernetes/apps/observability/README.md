# Metrics

## grafana

configured oauth with authentik
```
      auth.generic_oauth:
        name: Authentik
        enabled: true
        client_id: $__env{openid-config-client-id}
        client_secret: $__env{openid-config-client-secret}
        scopes: "openid email profile"
        auth_url: "https://auth.${SECRET_DOMAIN}/application/o/authorize/"
        token_url: "https://auth.${SECRET_DOMAIN}/application/o/token/"
        api_url: "https://auth.${SECRET_DOMAIN}/application/o/userinfo/"
        role_attribute_path: |
          contains(groups[*], 'Grafana Admins') && 'Admin' || 'Viewer'

```

pending
[] to make loki working to scrape syslog
