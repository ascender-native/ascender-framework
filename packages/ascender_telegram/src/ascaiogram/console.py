import ngrok

from core.main import cli
from core.main import click
from core.main import config

import asyncio

@cli.command("ngork")
@click.option('--port')
@click.option('--host')
def ngork(port, host):
    host = host if host is not None else config('app.host')
    port = port if port is not None else config('app.port')
    listener = ngrok.forward(f"{host}:{port}", authtoken_from_env=True)

    print("id: ", listener.id())
    print("metadata: ", listener.metadata())
    print("url: ", listener.url())
    asyncio.run(listener)

@cli.command("ngork.disconnect")
@click.option('--port')
@click.option('--host')
def disconnec2t(port, host):
    host = host if host is not None else config('app.host')
    port = port if port is not None else config('app.port')
    disconnect_task: asyncio.Task = ngrok.disconnect(f"{host}:{port}")