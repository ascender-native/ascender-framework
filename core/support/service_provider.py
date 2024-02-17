from abc import ABC
from core.contracts.foundation.application import Application

class ServiceProvider(ABC):
    app: Application

    _booting_callbacks: list = []
    _booted_callbacks: list = []

    def __init__(self, app: Application):
        self.app = app

    def register(self) -> None:
        pass

    def add_booting(self, callback: callable):
        self._booting_callbacks.append(callback)

    def add_booted(self, callback: callable):
        self._booted_callbacks.append(callback)

    def call_booting_callbacks(self):
        for callback in self._booting_callbacks:
            self.app.call(callback)

    def call_booted_callbacks(self):
        for callback in self._booted_callbacks:
            self.app.call(callback)

    @staticmethod
    def default_list() -> list:
        return DefaultServiceProviders().get_providers()
    

class DefaultServiceProviders():
    _providers: []

    def __init__(self) -> None:
        from core.database.providers.db_service import DatabaseServiceProvider
        
        self._providers = [
            DatabaseServiceProvider,
        ]

    def get_providers(self) -> list:
        return self._providers
    

