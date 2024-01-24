from core.support.service_provider import ServiceProvider
from app.providers.app_service import AppServiceProvider
from app.providers.route_service import RouteServiceProvider

config = {
    "providers": ServiceProvider.default_list() + [
        AppServiceProvider,
        RouteServiceProvider
    ]
}