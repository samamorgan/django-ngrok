from __future__ import annotations

import asyncio
import sys
from typing import TYPE_CHECKING

import pytest
from ngrok import Listener

from django_ngrok.management.commands.runserver_ngrok import Command

if TYPE_CHECKING:
    from faker import Faker
    from pytest_django.fixtures import SettingsWrapper


class TestCommand:
    @pytest.fixture
    def command(self) -> Command:
        command = Command()
        command.addr = command.default_addr
        command._raw_ipv6 = False

        return command

    @pytest.fixture
    def listener_url(self, faker: Faker) -> str:
        return f'https://{"-".join(faker.words(nb=3, unique=True))}.ngrok-free.app'

    @pytest.fixture
    def _monkeypatch_setup_ngrok(
        self, monkeypatch: pytest.MonkeyPatch, listener_url: str
    ) -> None:
        class MockListener:
            def url(self) -> str:
                return listener_url

        async def setup_ngrok(self, server_port: int) -> None:
            self.listener_addr = (
                f"{Command.protocol}://{Command.default_addr}:{server_port}"
            )
            self.listener = MockListener()

        monkeypatch.setattr(Command, "setup_ngrok", setup_ngrok)

    @pytest.fixture
    def _monkeypatch__exit(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr("os._exit", sys.exit)

    @pytest.mark.usefixtures("_monkeypatch_setup_ngrok")
    def test_on_bind(self, command: Command, capfd: pytest.CaptureFixture) -> None:
        command.on_bind(command.default_port)

        out = capfd.readouterr().out
        assert (
            f"ngrok forwarding to {command.listener_addr} from ingress url: "
            f"{command.listener.url()}"
        ) in out

    @pytest.mark.usefixtures("_monkeypatch__exit")
    def test_setup_ngrok(
        self, command: Command, settings: SettingsWrapper, capfd: pytest.CaptureFixture
    ) -> None:
        asyncio.run(command.setup_ngrok(command.default_port))

        assert (
            command.listener_addr
            == f"{Command.protocol}://{Command.default_addr}:{command.default_port}"
        )
        assert isinstance(command.listener, Listener)

        settings.NGROK_CONFIG = {"proto": "not_a_valid_proto"}
        with pytest.raises(SystemExit, match="1"):
            asyncio.run(command.setup_ngrok(command.default_port))

        err = capfd.readouterr().err
        assert "Error setting up ngrok: " in err
