import logging
import os

DB_CONFIG = (
        ('cache_size', -1024 * 64),  # 64MB page-cache.
        ('journal_mode', 'wal'),  # Use WAL-mode (you should always use this!).
        ('foreign_keys', 1)
        )

TOKENS = {
    'TEST': os.environ.get("API_KEY_HSE_QUIZ_BOT")
}

LOGGING_LEVEL = logging.INFO
