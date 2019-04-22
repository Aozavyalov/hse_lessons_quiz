from collections import Collection
from typing import NoReturn

from database.models import (Event, Event_Group, Event_Materials, Group,
                             Materials, Notification, User, User_Group)


TABLES = (User, Group, Event, Materials, Notification,
          User_Group, Event_Materials, Event_Group)


def create_tables(tables: Collection) -> NoReturn:
    for table in tables:
        if not table.table_exists():
            print("create table: {}".format(table))
            table.create_table()


def drop_tables(tables: Collection) -> NoReturn:
    for table in reversed(tables):
        if table.table_exists():
            print("drop table: {}".format(table))
            table.drop_table()


def init_db() -> NoReturn:
    """ (re)Create tables in database """
    drop_tables(TABLES)
    create_tables(TABLES)
