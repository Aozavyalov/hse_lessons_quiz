from peewee import (BooleanField, CharField, DateTimeField, ForeignKeyField,
                    IntegerField, Model, PrimaryKeyField, TextField)
from playhouse.pool import SqliteExtDatabase
from collections import Collection
from database import TABLES


def create_tables(tables: Collection) -> None:
    for table in tables:
        if not table.table_exists():
            print("create table: {}".format(table))
            table.create_table()


def drop_tables(tables: Collection) -> None:
    for table in reversed(tables):
        if table.table_exists():
            print("drop table: {}".format(table))
            table.drop_table()


def init_db() -> None:
    """ (re)Create tables in database """

    drop_tables(TABLES)
    create_tables(TABLES)
