from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

# TODO: Переделать. Этот вариант не подходит
class SimpleMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Выполнение действий перед обработкой запроса
        print("Middleware: Перед обработкой запроса")

        # Передача запроса дальше по цепочке обработки
        response = await call_next(request)

        # Выполнение действий после обработки запроса
        print("Middleware: После обработки запроса")

        return response
