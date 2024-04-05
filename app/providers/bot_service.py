from core.support.service_provider import ServiceProvider
from fastapi import APIRouter
from core.contracts.routing.http_router import HttpRouter

class BotServiceProvider(ServiceProvider):
    def register(self):
        self.app.bind(HttpRouter, APIRouter)
        pass

    def boot(self):
        pass