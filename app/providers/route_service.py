from asccore.foundation.support.providers.route_service import RouteServiceProvider as BaseRouteServiceProvider
from asccore.routing.router import Router

class RouteServiceProvider(BaseRouteServiceProvider):
    def boot(self):
        router: Router = self.app.make(Router)

        # Определение групп маршрутов
        auth_routes = router.group('routes/auth.py', prefix="/auth").tags('auth')
        api_routes = router.group('routes/api.py', prefix="/api").tags('api')
        web_routes = router.group('routes/web.py', prefix="/web").tags('web')

        # Добавление всех групп маршрутов
        self.routers(routers=[auth_routes, api_routes, web_routes])