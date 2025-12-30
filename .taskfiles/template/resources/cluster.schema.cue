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
	mailgun_authentik_smtp_password: string & !=""
	authentik_email_from: string & !=""
	authentik_POSTGRES_USER: string & !=""
	authentik_POSTGRES_PASS: string & !=""
	authentik_redis_password: string & !=""
}

#Config
