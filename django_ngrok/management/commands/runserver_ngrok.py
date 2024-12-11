from __future__ import annotations

import asyncio
import os
from typing import TYPE_CHECKING

import ngrok
from django.core.management.commands.runserver import Command as RunServerCommand

if TYPE_CHECKING:
    from django.core.management.base import CommandParser


class Command(RunServerCommand):
    help = f"{RunServerCommand.help[:-1]} with ngrok."

    def add_arguments(self, parser: CommandParser) -> None:
        super().add_arguments(parser)

        parser.add_argument(
            "--domain",
            help="host tunnel on a custom subdomain or hostname.",
        )

    def handle(self, *args, **options) -> None:
        self.domain = options.get("domain")
        print(self.domain)

        super().handle(*args, **options)

    def on_bind(self, server_port: int) -> None:
        super().on_bind(server_port)

        asyncio.run(self.setup_ngrok())
        self.stdout.write(
            f"ngrok forwarding to {self.addr} from ingress url: {self.listener.url()}"
        )

    async def setup_ngrok(self):
        try:
            self.listener = await ngrok.forward(
                addr=self.addr,
                authtoken_from_env=True,
                domain=self.domain,
            )
        except ValueError as e:
            self.stderr.write(f"Error setting up ngrok: {e}")
            os._exit(1)
