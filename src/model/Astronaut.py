import os

from dotenv import load_dotenv
from peewee import PostgresqlDatabase, Model, CharField, IntegerField


def get_db(db: str) -> PostgresqlDatabase:
    load_dotenv(override=False)
    return PostgresqlDatabase(
        db,
        user="postgres",
        password=os.getenv("DB_PASSWD"),
        host=os.getenv("DB_ADDR"),
        port=os.getenv("DB_PORT"),
    )


class BaseModel(Model):
    class Meta:
        database = get_db("astronaut")


class Astronaut(BaseModel):
    last_name = CharField()
    first_name = CharField()
    sex = CharField()
    year_of_birth = IntegerField()
    nationality = CharField()
