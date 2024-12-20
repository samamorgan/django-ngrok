from __future__ import annotations

import asyncio
import os
from urllib.parse import ParseResult, urlunparse

import ngrok
from django.conf import settings
from django.core.management.commands.runserver import Command as RunServerCommand


class Command(RunServerCommand):
    help = f'{RunServerCommand.help.rstrip(".")} with ngrok.'

    def on_bind(self, server_port: int) -> None:
        super().on_bind(server_port)

        asyncio.run(self.setup_ngrok(server_port))
        self.stdout.write(
            f"ngrok forwarding to {self.listener_addr} from ingress url: "
            f"{self.listener.url()}"
        )

    async def setup_ngrok(self, server_port: int) -> None:
        parts = ParseResult(
            scheme=self.protocol,
            netloc=f"{self.addr}:{server_port}",
            path="",
            params="",
            query="",
            fragment="",
        )
        self.listener_addr = urlunparse(parts)

        try:
            self.listener = await ngrok.forward(
                addr=self.listener_addr,
                **settings.NGROK_CONFIG,
            )
        except ValueError as e:
            self.stderr.write(f"Error setting up ngrok: {e}")
            await self.listener.close()
            os._exit(1)
