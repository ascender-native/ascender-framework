from core.foundation.support.providers.route_service import RouteServiceProvider as BaseRouteServiceProvider
from core.routing.router import Router

class RouteServiceProvider(BaseRouteServiceProvider):
    def boot(self):
        router: Router = self.app.make(Router)
        self.routers(routers=[
            router.group('routes/api.py', prefix="/api"),
            router.group('routes/web.py', prefix="/web"),
        ])