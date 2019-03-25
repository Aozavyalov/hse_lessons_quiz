from peewee import Model
from peewee import (BooleanField, CharField, DateTimeField, ForeignKeyField,
                    IntegerField, Model, PrimaryKeyField, TextField)
from config import DB_CONFIG
from datetime import datetime as dt

from playhouse.pool import SqliteExtDatabase


db = SqliteExtDatabase('lesson_quiz.db', pragmas=DB_CONFIG)


class BaseModel(Model):
    id = PrimaryKeyField()

    class Meta:
        database = db


class Group(BaseModel):
    name = CharField()


class User(BaseModel):
    telegram_id = IntegerField(unique=1)
    name = CharField()
    group = ForeignKeyField(
        Group,
        to_field='id',
        on_update='CASCADE',
        db_column='group_id'
    )


class Event(BaseModel):
    name = CharField()
    link = CharField()
    poll = CharField()
    datetime = DateTimeField(default=dt.now())


class Materials(BaseModel):
    link = CharField()
    content = CharField()


class Notification(BaseModel):
    user = ForeignKeyField(
        User,
        to_field='id',
        on_update='CASCADE',
        db_column='user_id'
    )
    datetime = DateTimeField(default=dt.now())


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
