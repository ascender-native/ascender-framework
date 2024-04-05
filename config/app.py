from core.support.service_provider import ServiceProvider

from app.providers.app_service import AppServiceProvider
from app.providers.route_service import RouteServiceProvider
from app.providers.route_service import RouteServiceProvider
from app.providers.auth_service import AuthServiceProvider
from core.foundation.support.providers.middleware_service import MiddlewareServiceProvider

from core.support.auth.middleware import JWTAuthentication
from ascis.ascis_provider import AscisProvider

import os

if ":" in os.getenv("APP_URL"):
    __host,__port = os.getenv("APP_URL").split(':')
else:
    __host = os.getenv("APP_URL")
    __port = '8000'


config = {
    "providers": ServiceProvider.default_list() + [
        MiddlewareServiceProvider,
        AppServiceProvider,
        RouteServiceProvider,
        AuthServiceProvider,
        AscisProvider,
    ],

    "middlewares": {
        'api:auth': JWTAuthentication
    },

    "host": __host,
    "port": __port
}