from abc import ABCMeta
from core.foundation.support.providers.route_service import RouteServiceProvider as BaseRouteServiceProvider
from core.routing.router import Router
from core.main import config

from .controller import WebhookController
from .console import ngork

import ngrok

from asyncio import Task

from aiogram import Bot, Dispatcher

class TelegramBotProvider(BaseRouteServiceProvider):
    WEBHOOK_PATH = 'webhook/telegram/bot/{token}'

    async def register(self):
        self.publish({'ascaiogram.config.bot': 'config.bot'}, 'config')

        token = config('bot.telegram.token')
        if token:
            self.register_bot(token)
            await self.register_webhook(token)

    def register_bot(self, token: str):
        self.app.bind(Bot, lambda: Bot(
            token=token
        ))
        self.app.bind(Dispatcher, lambda: Dispatcher(
            self.app.make(Bot)
        ))

    async def register_webhook(self, token: str):
        bot: Bot = self.app.make(Bot)
        webhook_info = await bot.get_webhook_info()

        telegram_url = config('bot.telegram.url') 
        webhook_url = f"{telegram_url}/{self.WEBHOOK_PATH.replace('{token}', token)}"
        if webhook_info.url != webhook_url:
            await bot.set_webhook(url=webhook_url)

    def boot(self):
        self.boot_router(self.app.make(Router))
        
    def boot_router(self, router: Router):
        self.routers(routers=[
            router.post(f"/{self.WEBHOOK_PATH}", WebhookController.bot).tags('webhooks'),
        ])