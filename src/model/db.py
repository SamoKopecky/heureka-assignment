import logging
from time import sleep

from peewee import PostgresqlDatabase, OperationalError
from psycopg2.errors import DuplicateDatabase

from ..model.Astronaut import get_db, Astronaut


class Db:
    def __init__(self):
        self.create_db()
        self.pgdb: PostgresqlDatabase = get_db("astronaut")

    def __enter__(self):
        self.pgdb.connect()
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.pgdb.close()

    @staticmethod
    def create_db():
        retry = 1
        max_retry = 5
        for i in range(max_retry + 1):
            try:
                get_db("postgres").cursor().execute("CREATE DATABASE astronaut")
            except OperationalError:
                logging.warning(f"db not accessible, trying again in {retry} seconds")
                sleep(retry)
                retry *= 2
            except DuplicateDatabase:
                logging.info("DB already exists")
                return

    def create_tables(self):
        if not Astronaut.table_exists():
            self.pgdb.create_tables([Astronaut])
            return
