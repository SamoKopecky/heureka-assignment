#!/usr/bin/env python3
import csv
import logging
import os
import random
import sys

from dotenv import load_dotenv
from requests import ConnectTimeout, post


def main(number_of_rows):
    load_dotenv(override=False)
    print(f"Creating {number_of_rows} astronauts...")
    names_rows = file_to_rows("./names.csv")
    nationalities_rows = file_to_rows("./nationalities.csv")

    firstnames = []
    surnames = []
    nationalities = []
    sexes = ["male", "female"]

    for row in names_rows:
        firstnames.append(row["firstname"])
        surnames.append(row["surname"])
    for nationality in nationalities_rows:
        nationalities.append(nationality["nationality"])

    astronauts = []
    for i in range(number_of_rows):
        astronauts.append(
            {
                "first_name": random.choice(firstnames),
                "last_name": random.choice(surnames),
                "sex": random.choice(sexes),
                "year_of_birth": random.randint(1900, 1999),
                "nationality": random.choice(nationalities),
            }
        )
    r = None
    try:
        r = post(
            f"{os.getenv('API_ADDR')}:{os.getenv('API_PORT')}/astronauts/create",
            json=astronauts,
            headers={"Content-type": "application/json", "Accept": "text/plain"},
            timeout=5,
        )
    except ConnectTimeout:
        logging.error("Connection timeout")
        exit(1)
    print(f"STATUS: {r.status_code}")
    print(f"RESPONSE: {r.text}")


def file_to_rows(name):
    with open(name) as names:
        csv_names = csv.DictReader(names, delimiter=",")
        return list(csv_names)


def get_env_fallback(name, fallback):
    return os.getenv(name) if name in os.environ else fallback


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(1000)
