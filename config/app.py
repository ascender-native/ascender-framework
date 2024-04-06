from core.support.service_provider import ServiceProvider

from app.providers.app_service import AppServiceProvider
from app.providers.route_service import RouteServiceProvider
from app.providers.route_service import RouteServiceProvider
from app.providers.auth_service import AuthServiceProvider
from core.foundation.support.providers.middleware_service import MiddlewareServiceProvider

from core.support.auth.middleware import JWTAuthentication

from ascaiogram.provider import TelegramBotProvider

import os

if ":" in os.getenv("APP_URL"):
    __host,__port = os.getenv("APP_URL").split(':')
else:
    __host = os.getenv("APP_URL", 'localhost')
    __port = '8000'


config = {
    "providers": ServiceProvider.default_list() + [
        MiddlewareServiceProvider,
        AppServiceProvider,
        RouteServiceProvider,
        TelegramBotProvider,
        AuthServiceProvider,
    ],

    "middlewares": {
        'api:auth': JWTAuthentication
    },

    "env": os.getenv("APP_ENV", 'local'),
    "url": os.getenv("APP_URL", 'localhost:8000'),
    "host": __host,
    "port": __port
}