from peewee import PostgresqlDatabase, Model, CharField, IntegerField


def get_db() -> PostgresqlDatabase:
    return PostgresqlDatabase(
        "astronaut", user="postgres", password="secret", host="127.0.0.1", port=5432
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
