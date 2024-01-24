import os

config = {
    "default": os.getenv("DB_CONNECTION"),

    "connections": {
        "pgsql": {
            'url': os.getenv('DATABASE_URL'),
            'host': os.getenv('DB_HOST', '127.0.0.1'),
            'port': os.getenv('DB_PORT', '5432'),
            'database': os.getenv('DB_DATABASE', 'forge'),
            'username': os.getenv('DB_USERNAME', 'forge'),
            'password': os.getenv('DB_PASSWORD', ''),
            'charset': 'utf8',
            'prefix': '',
            'prefix_indexes': True,
            'search_path': 'public',
            'sslmode': 'prefer',
        }
    },

    "models": {
        "path": [
            "app/entity/"
        ]
    }
}