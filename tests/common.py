import pytest
from config import DB_CONFIG
from bot.models import TABLES, create_tables, drop_tables
from playhouse.pool import SqliteExtDatabase
from playhouse.test_utils import test_database

db_test = SqliteExtDatabase('test.db', pragmas=DB_CONFIG)


def setup_module(self):
    create_tables(TABLES)


def teardown_module(self):
    drop_tables(TABLES)


class TestEvents:
    pass


class TestUpdateDB:
    pass


class TestMaterials:
    pass


class TestUsers:
    pass
