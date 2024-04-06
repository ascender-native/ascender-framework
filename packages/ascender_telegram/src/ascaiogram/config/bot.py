import os

config = {
    "telegram": {
        "token": os.getenv("TELEGRAM_BOT_TOKEN"),
        "url": os.getenv("TELEGRAM_BOT_URL", os.getenv("APP_URL")),
    }
}