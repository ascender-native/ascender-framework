
from core.support.service_provider import ServiceProvider
from core.database.manager import DatabaseManager
import os 
import itertools

class DatabaseServiceProvider(ServiceProvider):
    async def boot(self):
        db: DatabaseManager = self.app.make('db')
        await db.connection()

    async def register(self):
        await self.register_connection_services()
        await self.register_models()

    async def register_connection_services(self):
        self.app.singleton('db', DatabaseManager)
        db: DatabaseManager = self.app.make('db')

    async def register_models(self):
        config: dict = self.app.make("config")
        model_directory = config.get("database", {}).get("models").get("path")
        models = []
        for directory in model_directory:
            models.append(self.get_filenames(directory))
        models = list(itertools.chain(*models))

        db: DatabaseManager = self.app.make('db')
        db._models.extend(models)

    def get_filenames(self, directory) -> list:
        try:
            filenames = os.listdir(directory)
            if "__pycache__" in filenames:
                filenames.remove("__pycache__")
            if not directory.endswith('/'):
                directory += "/"
            directory = directory.replace("/", ".")
            listmodules = [directory + filename.rstrip('.py') for filename in filenames]
            return listmodules
        except FileNotFoundError:
            print(f"Directory {directory} not found for models")
            return []