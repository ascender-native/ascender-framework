from ascaiogram.provider import TelegramBotProvider as BaseTelegramBotProvider

from app.http.controllers.bot_controller import TelegramBotController

class TelegramBotProvider(BaseTelegramBotProvider):
    def boot_router_controller(self):
        return TelegramBotController.handle