from core.support.service_provider import ServiceProvider
from core.foundation.support.providers.route_service import RouteServiceProvider as BaseRouteServiceProvider
from app.http.kernel import Kernel
from core.contracts.http.kernel import Kernel
from core.contracts.http.kernel import Kernel as KernelContract
from core.routing.router import Route, HttpRoute, Router

class RouteServiceProvider(BaseRouteServiceProvider):
    def boot(self):
        router: Router = self.app.make(Router)
        self.routers(routers=[
            router.group('routes/api.py', prefix="/api"),
            router.group('routes/web.py', prefix="/web"),
        ])