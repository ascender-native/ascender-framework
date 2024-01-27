import click
import subprocess
from core.main import cli
from click.core import Context, Option

def flag_with_value(ctx: Context, param: Option, value):
    param.name = param.opts[0]
    return value

@cli.command("serve")
@click.option('--reload', is_flag=True)
@click.option('--port', callback=flag_with_value)
def serve(**args):
    flags = []
    params = []
    for arg,value in args.items():
        if isinstance(value, bool):
            if value == True:
                flags.append('--'+arg)
        elif value != None:
            params.append(arg)
            params.append(value)

    subprocess.run(['uvicorn', 'core.bootstrap:serve']+flags+params)