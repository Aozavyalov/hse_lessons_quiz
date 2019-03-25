from peewee import Model

from config import DB_CREDENTIALS

from playhouse.pool import SqliteDatabase
from playhouse.shortcuts import RetryOperationalError


db = SqliteDatabase('hse_quiz.db', **DB_CREDENTIALS)

class BaseModel(Model):
    id = PrimaryKeyField()

    class Meta:
        database = db

class User(BaseModel):
    telegram_id = IntegerField(unique=1)
    name = CharField()
    group = ForeignKeyField(
        Group,
        to_field='id',
        on_update='CASCADE',
        db_column='group_id'
    )

class Group(BaseModel):
    name = CharField()

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
