package config

import (
	"net"
)

#Config: {
	node_cidr: net.IPCIDR & !=cluster_pod_cidr & !=cluster_svc_cidr
	node_dns_servers?: [...net.IPv4]
	node_ntp_servers?: [...net.IPv4]
	node_default_gateway?: net.IPv4 & !=""
	node_vlan_tag?: string & !=""
	cluster_pod_cidr: *"10.42.0.0/16" | net.IPCIDR & !=node_cidr & !=cluster_svc_cidr
	cluster_svc_cidr: *"10.43.0.0/16" | net.IPCIDR & !=node_cidr & !=cluster_pod_cidr
	cluster_api_addr: net.IPv4
	cluster_api_tls_sans?: [...net.FQDN]
	cluster_gateway_addr: net.IPv4 & !=cluster_api_addr & !=cluster_dns_gateway_addr & !=cloudflare_gateway_addr
	cluster_dns_gateway_addr: net.IPv4 & !=cluster_api_addr & !=cluster_gateway_addr & !=cloudflare_gateway_addr
	repository_name: string
	repository_branch?: string & !=""
	repository_visibility?: *"public" | "private"
	cloudflare_domain: net.FQDN
	cloudflare_token: string
	cloudflare_gateway_addr: net.IPv4 & !=cluster_api_addr & !=cluster_gateway_addr & !=cluster_dns_gateway_addr
	cilium_bgp_router_addr?: net.IPv4 & !=""
	cilium_bgp_router_asn?: string & !=""
	cilium_bgp_node_asn?: string & !=""
	cilium_loadbalancer_mode?: *"dsr" | "snat"
	minio_root_user: string & !=""
	minio_root_password: string & !=""
	minio_openid_config_url: string & !=""
	minio_openid_config_client_id: string & !=""
	minio_openid_config_client_secret: string & !=""
	minio_openid_config_dcallback_uri: string & !=""
	aws_access_id: string & !=""
	aws_secret_access_key: string & !=""
	cloudnative_user: string & !=""
	cloudnative_password: string & !=""
	couchdb_user: string & !=""
	couchdb_password: string & !=""
	couchdb_password: string & !=""
	postgres_svc: net.IPv4
	pihole_svc: net.IPv4
	pihole_password: string & !=""
	pihole_api: string & !=""
	authentik_secret_key: string & !=""
	authentik_email_host: string & !=""
	authentik_email_username: string & !=""
	discord_bot_token: string & !=""
	mailgun_authentik_smtp_password: string & !=""
	authentik_email_from: string & !=""
	authentik_POSTGRES_USER: string & !=""
	authentik_POSTGRES_PASS: string & !=""
	authentik_redis_password: string & !=""
	paperless_admin_user: string & !=""
	paperless_admin_password: string & !=""
	paperless_api_token: string & !=""
	mealie_secret: string & !=""
	paperless_secret_key: string & !=""
	paperless_client_id: string & !=""
	paperless_client_secret: string & !=""
	ha_api: string & !=""
	n8n_encryption_key: string & !=""
	nextcloud_user: string & !=""
	nextcloud_password: string & !=""
	nextcloud_client_id: string & !=""
	nextcloud_client_secret: string & !=""
	nextcloud_redis_password: string & !=""
	smtp_relay_server: string & !=""
	smtp_relay_username: string & !=""
	smtp_relay_password: string & !=""
	nfs_svc: net.IPv4
	immich_jwt_secret: string & !=""
	grafana_client_id: string & !=""
	grafana_client_secret: string & !=""
	tailscale_client_id: string & !=""
	tailscale_client_secret: string & !=""
	smtp_relay_server: string & !=""
	smtp_relay_username: string & !=""
	smtp_relay_password: string & !=""
	searxng_secret: string & !=""
	action_runner_controller_github_app_id: string & !=""
	action_runner_controller_github_client_id: string & !=""
	action_runner_controller_github_installation_id: string & !=""
	action_runner_controller_github_client_secret: string & !=""
	action_runner_controller_github_runner_token: string & !=""
	action_runner_controller_github_webhook_secret_token: string & !=""
	action_runner_controller_github_private_key: string & !=""
	open_webui_client_id: string & !=""
	open_webui_client_secret: string & !=""
	open_webui_redirect: string & !=""
	nextcloud_db_user: string & !=""
	nextcloud_db_password: string & !=""
	shlink_api_key: string & !=""
	sonarr_api: string & !=""
	radarr_api: string & !=""
	sabnzbd_api: string & !=""
	mealie_api: string & !=""
	nextcloud_api: string & !=""
	paperless_api: string & !=""
	bazarr_api: string & !=""
	immich_api: string & !=""
	jellyfin_api: string & !=""
	jellyseerr_api: string & !=""
	lidarr_api: string & !=""
	sabnzbd_api: string & !=""
	prowlarr_api: string & !=""
	radarr_api: string & !=""
	lat: string & !=""
	long: string & !=""
	smb_pass: string & !=""
	samba_lb_ip: net.IPv4 & !=""
	secret_smtp_svc: net.IPv4 & !=""
	secret_sunshine_svc: net.IPv4 & !=""
	alert_manager_discord_webhook: string & !=""
	alert_manager_slack_webhook: string & !=""
}

#Config
