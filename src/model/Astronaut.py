import os

from dotenv import load_dotenv
from peewee import PostgresqlDatabase, Model, CharField, IntegerField


def get_db() -> PostgresqlDatabase:
    load_dotenv()
    return PostgresqlDatabase(
        "astronaut",
        user="postgres",
        password=os.getenv("PASSWD"),
        host=os.getenv("DB_ADDR"),
        port=os.getenv("DB_PORT"),
    )


class BaseModel(Model):
    class Meta:
        database = get_db()


class Astronaut(BaseModel):
    last_name = CharField()
    first_name = CharField()
    sex = CharField()
    year_of_birth = IntegerField()
    nationality = CharField()
