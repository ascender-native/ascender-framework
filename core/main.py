from core.foundation.application import Application
import click
from core.console.cli_ascender import AscernderCLI 

app = Application()

@click.group(cls=AscernderCLI, help="main CLI command for lazy example",)
def cli():
    pass