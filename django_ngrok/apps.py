import os

from django.apps import AppConfig
from django.conf import settings

NGROK_ALLOWED_HOSTS = [".ngrok.io", ".ngrok-free.app"]
NGROK_CONFIG = {
    "authtoken": None,
    "authtoken_from_env": True,
    "app_protocol": None,
    "session_metadata": None,
    "server_addr": None,
    "root_cas": None,
    "session_ca_cert": None,
    "metadata": None,
    "domain": None,
    "schemes": None,
    "proto": None,
    "proxy_proto": None,
    "labels": None,
    "basic_auth": None,
    "circuit_breaker": None,
    "compression": None,
    "allow_user_agent": None,
    "deny_user_agent": None,
    "allow_cidr": None,
    "deny_cidr": None,
    "crt": None,
    "key": None,
    "mutual_tls_cas": None,
    "oauth_provider": None,
    "oauth_allow_domains": None,
    "oauth_allow_emails": None,
    "oauth_scopes": None,
    "oauth_client_id": None,
    "oauth_client_secret": None,
    "oidc_issuer_url": None,
    "oidc_client_id": None,
    "oidc_client_secret": None,
    "oidc_allow_domains": None,
    "oidc_allow_emails": None,
    "oidc_scopes": None,
    "policy": None,
    "request_header_remove": None,
    "response_header_remove": None,
    "request_header_add": None,
    "response_header_add": None,
    "verify_upstream_tls": None,
    "verify_webhook_provider": None,
    "verify_webhook_secret": None,
    "websocket_tcp_converter": None,
}


class DjangoNgrokConfig(AppConfig):
    name = "django_ngrok"
    verbose_name = "Django ngrok"

    def ready(self):
        settings.NGROK_CONFIG = getattr(settings, "NGROK_CONFIG", NGROK_CONFIG)
        settings.NGROK_ALLOWED_HOSTS = getattr(
            settings, "NGROK_ALLOWED_HOSTS", NGROK_ALLOWED_HOSTS
        )
        settings.ALLOWED_HOSTS = list(
            set(getattr(settings, "ALLOWED_HOSTS", "") + settings.NGROK_ALLOWED_HOSTS)
        )
