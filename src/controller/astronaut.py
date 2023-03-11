from playhouse.shortcuts import model_to_dict

from .db import Db
from ..model.Astronaut import Astronaut


def create(data):
    bulk_size = 100
    with Db() as db:
        with db.pgdb.atomic():
            for idx in range(0, len(data), bulk_size):
                Astronaut.insert_many(data[idx : idx + bulk_size]).execute()
    return len(data)


def read_all():
    return [astronaut for astronaut in Astronaut.select().dicts()]


def read_by_id(read_id):
    return model_to_dict(Astronaut.get_by_id(read_id))


def read_with_limit(records):
    return [
        author
        for author in Astronaut.select()
        .order_by(Astronaut.year_of_birth.desc())
        .limit(records)
        .dicts()
    ]


def delete_by_id(to_delete_id):
    query = Astronaut.delete().where(Astronaut.id == to_delete_id)
    if query.execute() != 0:
        return True
    return False


def delete_all():
    query = Astronaut.delete()
    return query.execute()


def update_by_id(update_id, data):
    query = Astronaut.update(data).where(Astronaut.id == update_id)
    return query.execute()
