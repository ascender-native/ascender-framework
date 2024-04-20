from asccore.support.service_provider import ServiceProvider
from fastapi import APIRouter
from asccore.contracts.routing.http_router import HttpRouter

class AppServiceProvider(ServiceProvider):
    def register(self):
        self.app.bind(HttpRouter, APIRouter)
        pass

    def boot(self):
        pass