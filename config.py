import logging
import os

DB_CREDENTIALS = {
    'host': 'localhost',
    'port': 5432,
    'user': os.environ.get("POSTGRES_USER"),
    'password': os.environ.get("POSTGRES_PASSWORD"),
    'autorollback': True
}

TOKENS = {
    'TEST': os.environ.get("API_KEY_HSE_QUIZ_BOT")
}

LOGGING_LEVEL = logging.INFO