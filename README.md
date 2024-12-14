# django-ngrok
_Expose your local Django app to the internet with ngrok_

## Quick start

1. Install with pip:

```
pip install django-ngrok
```

2. Add django-ngrok to INSTALLED_APPS in your Django settings file:

```python
INSTALLED_APPS = [
    ...
    'django_ngrok',
]
```

3. Run `python manage.py runserver_ngrok` to start a django development server and an ngrok tunnel pointing to the server address.

## Configuration

django-ngrok uses the `forward` method from [`ngrok-python`](https://github.com/ngrok/ngrok-python) to create a tunnel to the Django development server. If you are using a simple setup, no configuration is necessary, and you can get up-and-running by setting the `NGROK_AUTHTOKEN` environment variable.

For a more explicit setup, you can add the `NGROK_CONFIG` setting to your Django settings file. All options below are documented [here](https://github.com/ngrok/ngrok-python#full-configuration). If you have any questions about how to use these options, please direct them to the `ngrok-python` maintainers.

```python
NGROK_CONFIG = {
    # session configuration
    "authtoken": str,
    "authtoken_from_env": True | False,  # Defaults to True
    "app_protocol": str,
    "session_metadata": str,
    # advanced session connection configuration
    "server_addr": str,
    "root_cas": str,
    "session_ca_cert": str,
    # listener configuration
    "metadata": str,
    "domain": str,
    "schemes": list[str],
    "proto": str,
    "proxy_proto": str,
    "labels": str,
    # module configuration
    "basic_auth": list[str],
    "circuit_breaker":0.1,
    "compression":True,
    "allow_user_agent": str,
    "deny_user_agent": str,
    "allow_cidr": str,
    "deny_cidr": str,
    "crt": bytes,  # I assume bytes, docs don't specify, haven't tested it.
    "key": bytes,
    "mutual_tls_cas": bytes,
    "oauth_provider": str,
    "oauth_allow_domains": list[str],
    "oauth_allow_emails": list[str],
    "oauth_scopes": list[str],
    "oauth_client_id": str,
    "oauth_client_secret": str,
    "oidc_issuer_url": str,
    "oidc_client_id": str,
    "oidc_client_secret": str,
    "oidc_allow_domains": list[str],
    "oidc_allow_emails": list[str],
    "oidc_scopes": list[str],
    "policy": str,
    "request_header_remove": str,
    "response_header_remove": str,
    "request_header_add": str,
    "response_header_add": str,
    "verify_upstream_tls": True | False,
    "verify_webhook_provider": str,
    "verify_webhook_secret": str,
    "websocket_tcp_converter": True | False,
}
```

## Contributing
Contributions and feedback are welcome! A contribution guide is upcoming, but if you have any questions, please feel free to open an issue or reach out directly.
