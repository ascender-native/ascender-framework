from aiogram import Bot, Dispatcher
from aiogram.types import Update

class TelegramBotController():
    async def handle(token: str, update: Update):
        dp = Dispatcher()
        bot: Bot = Bot(token)

        # dp.include_router(router)

        await dp.feed_webhook_update(bot, update)

        return True