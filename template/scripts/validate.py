"""Validate cluster.toml, apply defaults, and emit the config as JSON.

Standalone usage (doctor, CI): uv run --locked --no-dev template/scripts/validate.py [cluster.toml]
Schema export (just template schema): uv run --locked --no-dev template/scripts/validate.py --schema
In-process usage (makejinja plugin): from validate import load

Exits non-zero with one human-readable error per line on stderr when the
config is invalid.
"""

import json
import re
import sys
import tomllib
from ipaddress import IPv4Address, IPv4Network
from pathlib import Path
from typing import Annotated, Any, Literal, Self

from pydantic import (AfterValidator, BaseModel, BeforeValidator, ConfigDict,
                      Field, ValidationError, computed_field, model_validator)

# Git hosts whose SSH host keys are bundled with the template; ssh:// URLs
# pointing anywhere else must provide repository.known_hosts.
KNOWN_SSH_HOSTS = ["github.com", "gitlab.com", "codeberg.org"]

REPO_URL_PATTERN = r"^(https?://|ssh://git@)[^/]+/.+$"
FQDN_PATTERN = r"^([a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,}$"


def _network(value: Any) -> Any:
    """Parse a CIDR, requiring network-address form (no host bits set)."""
    if not isinstance(value, str):
        return value
    try:
        return IPv4Network(value)
    except ValueError:
        try:
            fixed = IPv4Network(value, strict=False)
        except ValueError:
            raise ValueError(f"{value!r} is not a valid IPv4 CIDR") from None
        raise ValueError(
            f"{value!r} has host bits set; did you mean {fixed}?"
        ) from None


def _asn(value: str) -> str:
    if value == "":
        return value
    if not re.fullmatch(r"[0-9]+", value):
        raise ValueError(f"{value!r} must be a decimal ASN")
    if not 1 <= int(value) <= 4294967295:
        raise ValueError(f"{value!r} must be in the range 1-4294967295")
    return value


type Cidr = Annotated[IPv4Network, BeforeValidator(_network)]
type Asn = Annotated[str, AfterValidator(_asn)]
type Fqdn = Annotated[str, Field(pattern=FQDN_PATTERN)]


class Model(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Network(Model):
    node_cidr: Cidr
    dns_servers: list[IPv4Address] = [IPv4Address("1.1.1.1"), IPv4Address("1.0.0.1")]
    ntp_servers: list[IPv4Address] = [IPv4Address("162.159.200.1"), IPv4Address("162.159.200.123")]
    # The first IP in node_cidr unless set explicitly.
    default_gateway: IPv4Address = Field(
        default_factory=lambda data: data["node_cidr"].network_address + 1
    )
    vlan_tag: str | None = Field(default=None, pattern=r"^[0-9]+$")

    @model_validator(mode="after")
    def check(self) -> Self:
        if self.default_gateway not in self.node_cidr:
            raise ValueError(
                f"default_gateway {self.default_gateway} is not inside node_cidr {self.node_cidr}"
            )
        if self.vlan_tag is not None and not 1 <= int(self.vlan_tag) <= 4094:
            raise ValueError(f"vlan_tag {self.vlan_tag} must be in the range 1-4094")
        return self


class Api(Model):
    addr: IPv4Address
    tls_sans: list[Fqdn] | None = None


class Kubernetes(Model):
    pod_cidr: Cidr = IPv4Network("10.42.0.0/16")
    svc_cidr: Cidr = IPv4Network("10.43.0.0/16")
    # The 10th IP in svc_cidr unless set explicitly.
    coredns_addr: IPv4Address = Field(
        default_factory=lambda data: data["svc_cidr"].network_address + 10
    )
    api: Api

    @model_validator(mode="after")
    def check(self) -> Self:
        if self.coredns_addr not in self.svc_cidr:
            raise ValueError(
                f"coredns_addr {self.coredns_addr} is not inside svc_cidr {self.svc_cidr}"
            )
        return self


class Gateways(Model):
    internal: IPv4Address
    dns: IPv4Address
    # Required when ingress.mode is not "none".
    external: IPv4Address | None = None


class Repository(Model):
    url: str = Field(pattern=REPO_URL_PATTERN)
    branch: str = Field(default="main", min_length=1)
    webhook_provider: Literal["github", "gitlab", "generic-hmac", "none"] = "github"
    known_hosts: str = ""

    @model_validator(mode="after")
    def check(self) -> Self:
        if self.url.startswith("ssh://"):
            host = self.url.removeprefix("ssh://git@").split("/", 1)[0].split(":", 1)[0]
            if host not in KNOWN_SSH_HOSTS and not self.known_hosts:
                raise ValueError(
                    f"known_hosts is required for ssh:// URLs to {host!r} "
                    f"(host keys are only bundled for {', '.join(KNOWN_SSH_HOSTS)})"
                )
        return self


class Domain(Model):
    name: Fqdn


class Dns(Model):
    provider: Literal["cloudflare", "none"] = "cloudflare"
    token: str = ""

    @model_validator(mode="after")
    def check(self) -> Self:
        if self.provider == "cloudflare" and not self.token:
            raise ValueError("token is required when dns.provider is 'cloudflare'")
        if self.provider == "none" and self.token:
            raise ValueError("token must be empty when dns.provider is 'none'")
        return self


class Ingress(Model):
    mode: Literal["cloudflare-tunnel", "direct", "none"] = "cloudflare-tunnel"


class Bgp(Model):
    router_addr: IPv4Address | Literal[""] = ""
    router_asn: Asn = ""
    node_asn: Asn = ""

    @model_validator(mode="after")
    def check(self) -> Self:
        unset = [name for name in ("router_addr", "router_asn", "node_asn") if getattr(self, name) == ""]
        if unset and len(unset) < 3:
            raise ValueError(
                "bgp is partially configured: set router_addr, router_asn and "
                f"node_asn together (missing: {', '.join(unset)})"
            )
        return self


class Talos(Model):
    # Default Image Factory schematic for nodes that don't set their own.
    schematic_id: str | None = Field(default=None, pattern=r"^[a-z0-9]{64}$")


class Spegel(Model):
    # True when the cluster has more than one node, unless set explicitly.
    enabled: bool | None = None


class Cilium(Model):
    loadbalancer_mode: Literal["dsr", "snat"] = "dsr"
    bgp: Bgp = Bgp()

class Couchdb(Model):
    user: str = ""
    password: str = ""


class S3(Model):
    aws_access_id: str = ""
    aws_secret_access_key: str = ""


class Cloudnative(Model):
    username: str = ""
    password: str = ""
    email: str = ""
    internal: str = ""


class Jwt(Model):
    secret_key: str = ""


class Paperless(Model):
    admin_user: str = ""
    api_token: str = ""
    admin_password: str = ""
    client_id: str = ""
    client_secret: str = ""
    secret_key: str = ""
    api: str = ""


class Minio(Model):
    root_user: str = ""
    root_password: str = ""
    openid_config_url: str = ""
    openid_config_client_id: str = ""
    openid_config_client_secret: str = ""
    openid_config_callback_uri: str = ""


class Tailscale(Model):
    client_id: str = ""
    client_secret: str = ""
    client_authkey: str = ""


class Pihole(Model):
    internal: str = ""
    api: str = ""
    password: str = ""


class Samba(Model):
    loadbalance: str = ""
    internal: str = ""
    password: str = ""


class Smtp(Model):
    internal: str = ""
    server: str = ""
    username: str = ""
    password: str = ""


class Authentik(Model):
    secret_key: str = ""
    postgres_password: str = ""
    email_host: str = ""
    email_username: str = ""
    email_password: str = ""
    email_from: str = ""
    postgres_user: str = ""
    redis_password: str = ""


class Sunshine(Model):
    internal: str = ""


class Discord(Model):
    bot_token: str = ""


class Mealie(Model):
    secret: str = ""
    api: str = ""


class Homeassistant(Model):
    api: str = ""


class N8n(Model):
    encryption_key: str = ""


class Nextcloud(Model):
    user: str = ""
    password: str = ""
    client_id: str = ""
    client_secret: str = ""
    redis_password: str = ""
    api: str = ""
    db_user: str = ""
    db_password: str = ""


class Immich(Model):
    jwt_secret: str = ""
    api: str = ""


class Grafana(Model):
    client_id: str = ""
    client_secret: str = ""


class Location(Model):
    latitude: str = ""
    longitude: str = ""


class Searxng(Model):
    secret: str = ""


class GithubRunner(Model):
    app_id: str = ""
    client_id: str = ""
    installation_id: str = ""
    client_secret: str = ""
    runner_token: str = ""
    webhook_secret_token: str = ""
    private_key: str = ""


class OpenWebui(Model):
    client_id: str = ""
    client_secret: str = ""
    redirect: str = ""


class Shlink(Model):
    geolite_license_key: str = ""
    api_key: str = ""


class Sonarr(Model):
    api: str = ""


class Radarr(Model):
    api: str = ""


class Bazarr(Model):
    api: str = ""


class Jellyfin(Model):
    api: str = ""


class Jellyseerr(Model):
    api: str = ""


class Lidarr(Model):
    api: str = ""


class Sabnzbd(Model):
    api: str = ""


class Prowlarr(Model):
    api: str = ""


class AlertManager(Model):
    discord_webhook: str = ""
    slack_webhook: str = ""


class Hermes(Model):
    api: str = ""
    username: str = ""
    password: str = ""
    secret: str = ""

class Garage(Model):
    rpc_secret: str = ""
    admin_token: str = ""
    metrics_token: str = ""

class Node(Model):
    name: str = Field(pattern=r"^[a-z0-9][a-z0-9\-]{0,61}[a-z0-9]$|^[a-z0-9]$")
    address: IPv4Address
    controller: bool
    disk: str
    mac_addr: str = Field(pattern=r"^([0-9a-f]{2}:){5}[0-9a-f]{2}$")
    # Falls back to talos.schematic_id when unset.
    schematic_id: str | None = Field(default=None, pattern=r"^[a-z0-9]{64}$")
    mtu: int = Field(default=1500, ge=1450, le=9000)
    secureboot: bool = False
    encrypt_disk: bool = False
    kernel_modules: list[str] = []

    @model_validator(mode="after")
    def check(self) -> Self:
        if self.name in ("global", "controller", "worker"):
            raise ValueError(f"node name {self.name!r} is reserved")
        return self


class Config(Model):
    model_config = ConfigDict(extra="forbid", title="cluster.toml")

    network: Network
    kubernetes: Kubernetes
    gateways: Gateways
    repository: Repository
    domain: Domain
    dns: Dns
    # Defaults to "cloudflare-tunnel" when dns.provider is "cloudflare",
    # otherwise "none".
    ingress: Ingress = Field(
        default_factory=lambda data: Ingress(
            mode="cloudflare-tunnel" if data["dns"].provider == "cloudflare" else "none"
        )
    )
    cilium: Cilium = Cilium()
    couchdb: Couchdb = Couchdb()
    s3: S3 = S3()
    cloudnative: Cloudnative = Cloudnative()
    talos: Talos = Talos()
    spegel: Spegel = Spegel()
    jwt: Jwt = Jwt()
    paperless: Paperless = Paperless()
    minio: Minio = Minio()
    tailscale: Tailscale = Tailscale()
    pihole: Pihole = Pihole()
    samba: Samba = Samba()
    smtp: Smtp = Smtp()
    authentik: Authentik = Authentik()
    sunshine: Sunshine = Sunshine()
    discord: Discord = Discord()
    mealie: Mealie = Mealie()
    homeassistant: Homeassistant = Homeassistant()
    n8n: N8n = N8n()
    nextcloud: Nextcloud = Nextcloud()
    immich: Immich = Immich()
    grafana: Grafana = Grafana()
    location: Location = Location()
    searxng: Searxng = Searxng()
    github_runner: GithubRunner = GithubRunner()
    open_webui: OpenWebui = OpenWebui()
    shlink: Shlink = Shlink()
    sonarr: Sonarr = Sonarr()
    radarr: Radarr = Radarr()
    bazarr: Bazarr = Bazarr()
    jellyfin: Jellyfin = Jellyfin()
    jellyseerr: Jellyseerr = Jellyseerr()
    lidarr: Lidarr = Lidarr()
    sabnzbd: Sabnzbd = Sabnzbd()
    prowlarr: Prowlarr = Prowlarr()
    alert_manager: AlertManager = AlertManager()
    hermes: Hermes = Hermes()
    garage: Garage = Garage()
    nodes: list[Node]

    @computed_field
    @property
    def cilium_bgp_enabled(self) -> bool:
        bgp = self.cilium.bgp
        return bgp.router_addr != "" and bgp.router_asn != "" and bgp.node_asn != ""

    # Replica counts for control-plane-only workloads key off this rather
    # than len(nodes); a cluster can have many workers but one controller.
    @computed_field
    @property
    def controller_count(self) -> int:
        return sum(1 for node in self.nodes if node.controller)

    @computed_field
    @property
    def cluster_issuer(self) -> str:
        if self.dns.provider == "cloudflare":
            return "letsencrypt-production"
        return "internal-ca"

    # Single source for the machine and apiServer certificate SAN lists,
    # which live in separate patch files.
    @computed_field
    @property
    def cert_sans(self) -> list[str]:
        return ["127.0.0.1", str(self.kubernetes.api.addr), *(self.kubernetes.api.tls_sans or [])]

    @model_validator(mode="after")
    def check(self) -> Self:
        if self.spegel.enabled is None:
            self.spegel.enabled = len(self.nodes) > 1
        for i, node in enumerate(self.nodes):
            if node.schematic_id is None:
                node.schematic_id = self.talos.schematic_id
            if node.schematic_id is None:
                raise ValueError(
                    f"nodes[{i}].schematic_id is required: set it on the node "
                    "or set a cluster-wide default in [talos]"
                )
        if self.ingress.mode != "none" and self.dns.provider != "cloudflare":
            raise ValueError(
                f"ingress.mode {self.ingress.mode!r} requires dns.provider 'cloudflare'"
            )
        if self.ingress.mode != "none" and self.gateways.external is None:
            raise ValueError(
                f"gateways.external is required when ingress.mode is {self.ingress.mode!r}"
            )

        cidrs = {
            "network.node_cidr": self.network.node_cidr,
            "kubernetes.pod_cidr": self.kubernetes.pod_cidr,
            "kubernetes.svc_cidr": self.kubernetes.svc_cidr,
        }
        names = list(cidrs)
        for i, a in enumerate(names):
            for b in names[i + 1:]:
                if cidrs[a].overlaps(cidrs[b]):
                    raise ValueError(f"{a} {cidrs[a]} overlaps {b} {cidrs[b]}")

        addresses = {
            "kubernetes.api.addr": self.kubernetes.api.addr,
            "gateways.internal": self.gateways.internal,
            "gateways.dns": self.gateways.dns,
            "network.default_gateway": self.network.default_gateway,
        } | {f"nodes[{i}].address": n.address for i, n in enumerate(self.nodes)}
        if self.gateways.external is not None:
            addresses["gateways.external"] = self.gateways.external
        seen: dict[IPv4Address, str] = {}
        for owner, addr in addresses.items():
            if addr in seen:
                raise ValueError(f"address {addr} is used by both {seen[addr]} and {owner}")
            seen[addr] = owner

        node_cidr = self.network.node_cidr
        for i, node in enumerate(self.nodes):
            if node.address not in node_cidr:
                raise ValueError(
                    f"nodes[{i}].address {node.address} is not inside node_cidr {node_cidr}"
                )
        if self.kubernetes.api.addr not in node_cidr:
            raise ValueError(
                f"kubernetes.api.addr {self.kubernetes.api.addr} is not inside node_cidr {node_cidr}"
            )
        # Without BGP the gateway VIPs are announced over L2 and must live in
        # the node network.
        if not self.cilium_bgp_enabled:
            for name in ("internal", "dns", "external"):
                addr = getattr(self.gateways, name)
                if addr is not None and addr not in node_cidr:
                    raise ValueError(
                        f"gateways.{name} {addr} is not inside node_cidr {node_cidr} "
                        "(required unless BGP is enabled)"
                    )

        for field, label in (("name", "name"), ("mac_addr", "MAC address")):
            values: dict[str, int] = {}
            for i, node in enumerate(self.nodes):
                value = getattr(node, field)
                if value in values:
                    raise ValueError(
                        f"duplicate node {label} {value!r} on nodes[{values[value]}] and nodes[{i}]"
                    )
                values[value] = i
        return self


def format_errors(error: ValidationError) -> str:
    lines = []
    for err in error.errors():
        loc = ".".join(str(part) for part in err["loc"])
        msg = err["msg"].removeprefix("Value error, ")
        lines.append(f"{loc}: {msg}" if loc else msg)
    return "\n".join(lines)


class ConfigError(Exception):
    pass


# Validate config_file and return the defaulted config as a plain dict.
# Raises ConfigError with a human-readable message.
def load(config_file: str = "cluster.toml") -> dict[str, Any]:
    path = Path(config_file)
    try:
        raw = tomllib.loads(path.read_text())
    except FileNotFoundError:
        raise ConfigError(f"{path}: file not found") from None
    except tomllib.TOMLDecodeError as e:
        raise ConfigError(f"{path}: invalid TOML: {e}") from None

    try:
        config = Config.model_validate(raw)
    except ValidationError as e:
        raise ConfigError(format_errors(e)) from None

    # Unset optionals stay in the dump as None rather than being dropped:
    # makejinja renders with StrictUndefined, so a template testing
    # network.vlan_tag needs the key to exist.
    return config.model_dump(mode="json")


# JSON Schema for editor completion and validation of cluster.toml (taplo's
# #:schema directive). Cross-field rules and data-aware defaults only exist in
# the model validators, so the schema is an editing aid, not the gate.
def schema() -> dict[str, Any]:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        **Config.model_json_schema(),
    }


def main() -> int:
    if sys.argv[1:] == ["--schema"]:
        json.dump(schema(), sys.stdout, indent=2)
        sys.stdout.write("\n")
        return 0
    try:
        data = load(sys.argv[1] if len(sys.argv) > 1 else "cluster.toml")
    except ConfigError as e:
        print(e, file=sys.stderr)
        return 1
    json.dump(data, sys.stdout, indent=2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
