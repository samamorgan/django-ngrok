from __future__ import annotations

import uuid
from http import HTTPStatus
from typing import TYPE_CHECKING

import pytest
import requests

if TYPE_CHECKING:
    from pytest_django.fixtures import SettingsWrapper


@pytest.fixture
def listener_url(settings: SettingsWrapper) -> str:
    return f'http://{settings.NGROK_CONFIG["domain"]}'


@pytest.mark.usefixtures("runserver_ngrok")
def test_runserver_ngrok(listener_url: str) -> None:
    ping = uuid.uuid4().hex
    response = requests.get("http://127.0.0.1:8000", params={"ping": ping})
    assert response.status_code == HTTPStatus.OK
    assert response.json()["pong"] == ping

    response = requests.get(listener_url, params={"ping": ping})
    assert response.status_code == HTTPStatus.OK
    assert response.json()["pong"] == ping
