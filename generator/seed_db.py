#!/usr/bin/env python3
import csv
import os
import random
import sys

import requests


def main(number_of_rows):
    addr = get_env_fallback("API_ADDR", "http://localhost")
    port = get_env_fallback("API_PORT", "5001")

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
    r = requests.post(
        f"{addr}:{port}/astronauts/create",
        json=astronauts,
        headers={"Content-type": "application/json", "Accept": "text/plain"},
    )
    print(f"STATUS: {r.status_code}")
    print(f"RESPONSE: {r.text}")


def file_to_rows(name):
    with open(name) as names:
        csv_names = csv.DictReader(names, delimiter=",")
        return list(csv_names)


def get_env_fallback(name, fallback):
    return os.getenv(name) if name in os.environ else fallback


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    elif "ROWS" in os.environ:
        main(int(os.getenv("ROWS")))
    else:
        main(1000)
