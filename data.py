#!/usr/bin/python3
import sys

import requests as requests


def insert():
    r = requests.post(
        "http://localhost:5001/astronauts/create",
        json=[
            {
                "last_name": "foo",
                "first_name": "bar",
                "sex": "male",
                "year_of_birth": "1987",
                "nationality": "slovakia",
            },
            {
                "last_name": "zoo",
                "first_name": "tag",
                "sex": "female",
                "year_of_birth": "1989",
                "nationality": "russia",
            },
        ],
        headers={"Content-type": "application/json", "Accept": "text/plain"},
    )
    print(r.status_code)
    print(r.text)


def update():
    r = requests.patch(
        "http://localhost:5001/astronauts/44/update",
        json={
            "first_name": "ccc",
        },
        headers={"Content-type": "application/json", "Accept": "text/plain"},
    )
    print(r.status_code)
    print(r.text)


if __name__ == "__main__":
    if len(sys.argv) > 0 and sys.argv[1] == "-i":
        insert()
    else:
        update()
