from __future__ import annotations

import uuid
from http import HTTPStatus
from typing import TYPE_CHECKING

import pytest
import requests

if TYPE_CHECKING:
    from pytest_django.fixtures import SettingsWrapper


@pytest.fixture
def domain(settings: SettingsWrapper) -> str:
    return settings.NGROK_CONFIG["domain"]


@pytest.mark.usefixtures("runserver_ngrok")
def test_runserver_ngrok(domain: str) -> None:
    ping = uuid.uuid4().hex
    response = requests.get("http://127.0.0.1:8000", params={"ping": ping})
    assert response.status_code == HTTPStatus.OK
    assert response.json()["pong"] == ping

    response = requests.get(f"http://{domain}", params={"ping": ping})
    assert response.status_code == HTTPStatus.OK
    assert response.json()["pong"] == ping
