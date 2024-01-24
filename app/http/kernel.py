from core.contracts.foundation.application import Application
from fastapi import FastAPI
from core.foundation.bootstrap import load_configuration, load_environment, register_providers, boot_providers, connection_database
from contextlib import asynccontextmanager
from core.foundation.http.http_kernel import HttpKernel

class Kernel(HttpKernel):
    _app: any
    _router: any
    server: any
    _routes: any

    __bootstrappers: dict = [
        load_environment.LoadEnvironment,
        load_configuration.LoadConfiguration,
        connection_database.ConnectionDatabase,
        register_providers.RegisterProviders,
        boot_providers.BootProviders
    ]

    def __init__(self, app: Application, router = None) -> None:
        self._app = app
        self._router = router
        self.sync_middleware_to_router()

    def get_bootstrappers(self):
        return self.__bootstrappers
    
    async def bootstrap(self):        
        await self._app.bootstrap_with(self.get_bootstrappers())

    @asynccontextmanager
    async def lifespan(self, app: FastAPI):
        await self.bootstrap()
        yield

    def sync_middleware_to_router(self):
        return

    def handle(self):
        dependencies = [
            # ....
        ]
        self.server = FastAPI(lifespan=self.lifespan, dependencies=dependencies)
        
    def send(self):
        return self.server