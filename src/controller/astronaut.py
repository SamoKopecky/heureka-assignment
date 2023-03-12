from typing import List, Dict

from playhouse.shortcuts import model_to_dict

import src.model.Astronaut
from ..model.Astronaut import Astronaut
from ..model.db import Db


def create(data: Dict) -> int:
    bulk_size = 100
    with Db() as db:
        with db.pgdb.atomic():
            for idx in range(0, len(data), bulk_size):
                Astronaut.insert_many(data[idx : idx + bulk_size]).execute()
    return len(data)


def read_all() -> List[Dict]:
    return [astronaut for astronaut in Astronaut.select().dicts()]


def read_by_id(read_id: int) -> Dict:
    try:
        return model_to_dict(Astronaut.get_by_id(read_id))
    except Exception as e:
        if "does not exist" in e.args[0]:
            return {}


def read_with_limit(records: str) -> List[Dict]:
    return [
        author
        for author in Astronaut.select()
        .order_by(Astronaut.year_of_birth.desc())
        .limit(records)
        .dicts()
    ]


def delete_by_id(to_delete_id: int) -> bool:
    query = Astronaut.delete().where(Astronaut.id == to_delete_id)
    if query.execute() != 0:
        return True
    return False


def delete_all() -> int:
    query = Astronaut.delete()
    return query.execute()


def update_by_id(update_id: int, data: Dict):
    query = Astronaut.update(data).where(Astronaut.id == update_id)
    query.execute()
