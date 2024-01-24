from core.support.service_provider import ServiceProvider
from core.contracts.http.kernel import Kernel as KernelContract
from core.routing.router import Route, RouteList, Router

class RoutingServiceProvider(ServiceProvider):   

    async def register(self) -> None:
        await self._register_router()
    
    async def _register_router(self):
        self.app.bind(Route, RouteList)
        self.app.singleton(Router, Router)
        pass