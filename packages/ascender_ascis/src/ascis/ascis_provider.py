from core.support.service_provider import ServiceProvider
from config.ascis import config

class AscisProvider(ServiceProvider):
    def register(self):
        self.publish({
           'config.ascis': 'config.ascis'
        }, 'config')
        pass

    def boot(self):
        pass