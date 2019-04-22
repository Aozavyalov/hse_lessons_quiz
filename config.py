import logging
import os


DB_CONFIG = (
    ('cache_size', -1024 * 64),  # 64MB page-cache.
    ('journal_mode', 'wal'),  # Use WAL-mode (you should always use this!).
    ('foreign_keys', 1)
)

TOKEN = "fuck"

DIMA = 42928638
ALEX = None
ANDREY = None

ADMINS = (DIMA, ALEX, ANDREY)
