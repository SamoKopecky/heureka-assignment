from peewee import PostgresqlDatabase

from ..model.Astronaut import get_db, Astronaut


class Db:
    def __init__(self):
        self.pgdb: PostgresqlDatabase = get_db()

    def __enter__(self):
        self.pgdb.connect()
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.pgdb.close()

    def create_tables(self):
        if not Astronaut.table_exists():
            self.pgdb.create_tables([Astronaut])
            return
        # Check if all columns are the same
        columns = self.pgdb.get_columns("astronaut")
