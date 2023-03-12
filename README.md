# About
Assignment for a position at heureka.

<a href="https://github.com/psf/black" alt="Code style: black">
        <img src="https://img.shields.io/badge/code%20style-black-000000.svg" /></a>

## How to run
To run this app use `docker-compose`:
```shell
docker-compose up -d --build
```

For development, you can run the components locally. First make sure you install dependencies with:
```shell
pip install -r requirements.txt
```
If your components like the database are not hosted on `localhost` create an `.env` file from the `.env.example` file. For more help with running individual components, see
```shell
python3 main.py --help
```

## Database model

The database has one table named astronauts with rows:
- `first_name`
- `second_name`
- `gender` -- either female or male
- `year_of_birth`
- `nationality`

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

See `README.md` in the `generator` folder.

## Exporting/Importing the database

To export the database to a file
- with a docker container:
  ```shell
  docker build -t manager . && \
  docker run --network="host" --name="producer" manager -pe && \
  docker cp producer:/src/export.json . && \
  docker rm producer
  ```
  The exported file will be in the current directory with the name `export.json`. If you want to save the file to a different location, edit the 3rd line in the command above like this:
  ```shell
  docker cp producer:/src/export.json {file_path}
  ```
- without a docker container:
  ```shell
  python3 main.py -pe -fp {file_path}
  ```

To import a file to the database
- with a docker container:
  ```shell
  docker build -t manager . && \
  docker container create --rm --name producer --network="host" manager -pi && \
  docker cp export.json producer:/src/export.json && \
  docker start producer
  ```
  The import file needs to be in the current directory and be named `export.json`, if you want to specify a different file, edit the 2nd command like this:
  ```shell
  docker cp {file_path} producer:/src/export.json
  ```
- without a docker container:
  ```shell
  python3 main.py -pi -fp {file_path}
  ```

If the address of your db/rabbitmq containers are not localhost, change them using `env` variables. List of available `env` variables can be seen in `./Dockerfile`.
