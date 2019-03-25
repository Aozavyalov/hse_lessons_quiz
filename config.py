import logging
import os

USERDATA_PATH = r"backup/userdata"
CONVERSATIONS_PATH = r"backup/conversations"

PG_CONN = {
    'host': 'localhost',
    'port': 5432,
    'user': os.environ.get("POSTGRES_USER"),
    'password': os.environ.get("POSTGRES_PASSWORD"),
    'autorollback': True
}

TOKENS = {
    'TEST': os.environ.get("API_KEY_HSE_QUIZ_BOT")
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOGGING_LEVEL = logging.INFO