from core.contracts.foundation.application import Application
from core.support.service_provider import ServiceProvider
from core.contracts.http.kernel import Kernel as KernelContract
from fastapi import FastAPI, APIRouter, Request
from core.routing.router import HttpRoute, RouteList
from core.foundation.application import Application

class RouteServiceProvider(ServiceProvider):
    http_routes = []
    build_routes:list = []
    
    def __init__(self, app: Application):
        super().__init__(app)
        self.kernel = self.app.make(KernelContract)
        self.server: FastAPI = self.kernel.server

    def routers(self, routers, prefix=""):        
        for router in routers:
            if not isinstance(router, RouteList): continue
            http_routes = router.build()
            self.register_routes(http_routes)

    def register_routes(self, routes) -> None:            
        api_router = APIRouter()
        for route in routes:
            if not isinstance(route, HttpRoute): continue
            full_path = route.prefix + route.path
            api_router.add_api_route(
                path=full_path, 
                endpoint=route.enpoint, 
                methods=route.methods,
                )
            # TODO: Реализовать кастомный middleware
            # for middleware in route.middlewares:
            #     api_router.dependencies.append(middleware)
            # print(api_router.dependencies)
        self.server.include_router(api_router)