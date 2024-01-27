from core.contracts.foundation.application import Application
from core.foundation.bootstrap import (
    load_configuration, 
    load_environment, 
    register_providers, 
    boot_providers, 
    connection_database
)
from core.console.cli_ascender import AscernderCLI
import asyncio
import importlib.util
from core.main import cli
import click
import os
import glob

class ConsoleKernel():
    _app: any
    _router: any
    server: any
    _routes: list = []
    routes: list = []
    cli: any
    _commands: dict = {}

    __bootstrappers: dict = [
        load_environment.LoadEnvironment,
        load_configuration.LoadConfiguration,
        connection_database.ConnectionDatabase,
        register_providers.RegisterProviders,
        boot_providers.BootProviders
    ]

    def __init__(self, app: Application) -> None:
        self._app: Application = app
        self.routes: list = []
        self._router = None

    async def bootstrap(self):
        await self._app.bootstrap_with(self.get_bootstrappers())
        self.load_base_commands()
        self.commands()

    def get_bootstrappers(self):
        return self.__bootstrappers
    
    def commands(self) -> None:
        pass

    def load_base_commands(self) -> None:
        self.load('core.foundation.console.commands.*')

    def handle(self):
        asyncio.run(self.bootstrap())
        cli()

    def getCLI(self) -> AscernderCLI:
        if not hasattr(self, 'cli'):
            self.cli = AscernderCLI()
            self.cli.commands |= self._commands
            # self.cli.resolve_commands(self._commands)
            # self.cli.refresh_comand_loader()
        return self.cli
    
    def load(self, cmd_name:str, cmd_object_name="cli"):
        split_method = cmd_name.split(":", 1)
        if len(split_method) == 2:
            cmd_object_name = split_method[1]
            cmd_name = split_method[0]

        directory = cmd_name.split(".*", 1)
        if len(directory) == 2:
            dir_path = directory[0]
            modules = self.get_modules(dir_path)
            for module in modules:
                self.load(module, cmd_object_name)
            return

        mod = importlib.import_module(cmd_name)
        cmd_object = getattr(mod, cmd_object_name)
        if not isinstance(cmd_object, click.BaseCommand):
            raise ValueError(
                f"Lazy loading of {cmd_name} failed by returning "
                "a non-command object"
            )
        return cmd_object
    
    def get_modules(self, module_dir: str):
        module_dir = module_dir.replace('.', '/')
        module_files_path = glob.glob(os.path.join(module_dir, '*.py'))
        modules_path = [file_path.replace('/', '.').replace('.py', '') for file_path in module_files_path]

        return modules_path