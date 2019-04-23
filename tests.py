import pytest
from playhouse.pool import SqliteExtDatabase
from playhouse.test_utils import test_database

from bot.models import (TABLES, Event, Event_Group, Event_Materials, Group,
                        Materials, Notification, User, User_Group,
                        create_tables, drop_tables)
from config import DB_CONFIG


db_test = SqliteExtDatabase('test.db', pragmas=DB_CONFIG)


def setup_module(self):
    create_tables(TABLES)


def teardown_module(self):
    drop_tables(TABLES)


class TestUser:
    def setup_class(self):
        # TODO tests preparations here
        pass

    def test_create_user(self):
        with test_database(db_test, (User,)):
            assert len(User) == 0
            user = User.create(
                telegram_id=0,
                name="user",
                group=Group(name="group")
            )
            assert user
            assert len(User) == 1


class TestEvent:
    pass


class TestMaterial:
    pass

# TODO
