from collections import Collection
from datetime import datetime as dt
from typing import NoReturn

from peewee import (CharField, DateTimeField, ForeignKeyField, IntegerField,
                    Model, PrimaryKeyField, TextField)
from playhouse.pool import SqliteExtDatabase

from config import DB_CONFIG


db = SqliteExtDatabase('lesson_quiz.db', pragmas=DB_CONFIG)


class BaseModel(Model):
    id = PrimaryKeyField()

    class Meta:
        database = db


class Group(BaseModel):
    name = CharField(unique=True, max_length=64)


class User(BaseModel):
    telegram_id = IntegerField(unique=True)
    name = CharField()
    group = ForeignKeyField(
        Group,
        to_field='id',
        on_update='CASCADE',
        db_column='group_id'
    )


class Event(BaseModel):
    name = CharField()
    link = CharField(unique=True, max_length=512)
    poll = CharField(max_length=512)
    datetime = DateTimeField(default=dt.now)


class Materials(BaseModel):
    link = CharField(unique=True, max_length=512)
    content = TextField()


class Notification(BaseModel):
    user = ForeignKeyField(
        User,
        to_field='id',
        on_update='CASCADE',
        db_column='user_id'
    )
    datetime = DateTimeField(default=dt.now)


class User_Group(BaseModel):
    user = ForeignKeyField(
        User,
        to_field='id',
        on_update='CASCADE',
        db_column='user_id'
    )
    group = ForeignKeyField(
        Group,
        to_field='id',
        on_update='CASCADE',
        db_column='group_id'
    )


class Event_Materials(BaseModel):
    event = ForeignKeyField(
        Event,
        to_field='id',
        on_update='CASCADE',
        db_column='event_id'
    )
    materials = ForeignKeyField(
        Materials,
        to_field='id',
        on_update='CASCADE',
        db_column='materials_id'
    )


class Event_Group(BaseModel):
    event = ForeignKeyField(
        Event,
        to_field='id',
        on_update='CASCADE',
        db_column='event_id'
    )
    group = ForeignKeyField(
        Group,
        to_field='id',
        on_update='CASCADE',
        db_column='group_id'
    )


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


TABLES = (User, Group, Event, Materials, Notification,
          User_Group, Event_Materials, Event_Group)
