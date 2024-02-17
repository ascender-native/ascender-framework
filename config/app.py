from core.support.service_provider import ServiceProvider

from app.providers.app_service import AppServiceProvider
from app.providers.route_service import RouteServiceProvider
from app.providers.route_service import RouteServiceProvider
from app.providers.auth_service import AuthServiceProvider
from core.foundation.support.providers.middleware_service import MiddlewareServiceProvider

from core.support.auth.middleware import JWTAuthentication

config = {
    "providers": ServiceProvider.default_list() + [
        MiddlewareServiceProvider,
        AppServiceProvider,
        RouteServiceProvider,
        AuthServiceProvider,
    ],

    "middlewares": {
        'api:auth': JWTAuthentication
    } 
}