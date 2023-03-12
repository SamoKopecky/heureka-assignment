# About
Assignment for a position at heureka.

<a href="https://github.com/psf/black" alt="Code style: black">
        <img src="https://img.shields.io/badge/code%20style-black-000000.svg" /></a>

## How to run
To run this app use `docker-compose`:
```shell
docker-compose up -d --build
```

For development, you can run the API server locally, however make sure you have a postgres db running on `localhost:5432`, with credentials `postgres:secret`. If you have different setup create an `.env` file from the `.env.example` file.
```shell
pip install -r requirements.txt && \
python3 main.py
```

## REST API
The REST API provides server endpoints:
- `/astronauts` -- Get all astronauts
  - `/astronauts?limit=20` -- Optionally you can provide the parameter `limit` to limit the number of astronauts, in this case the astronauts are sorted in descending order by their year of birth, example:
- `/astronauts/{id}` -- Get a single astronaut by id
- `/astronauts/create` -- Create one or multiple astronauts by providing a json object with the proper content type `application/json`
- `/astronauts/{id}/delete` -- Delete a single astronaut by id
- `/astronauts/delete` -- Delete all astronauts
- `/astronauts/{id}/update` -- Update a single astronaut by id and by providing a json object

## Seeding the database

## Exporting/Importing the database

## TODO:
- docs in code, types
- setup script
- test deployment
- finish TODO
- clean up manager
