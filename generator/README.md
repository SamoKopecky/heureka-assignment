# Generator

Generate random astronauts from data in `names.csv` and `nationalities.csv`.

## How to run

By default, 1000 rows are generated:
```shell
docker build -t generator . && \
docker run --network="host" --rm generator
```

To specify `n` rows, use:
```shell
docker build -t generator . && \
docker run --network="host" --rm generator 2000
```

To a different location for the API change `env` variables:
```shell
docker build -t generator . && \
docker run --network="host" --rm -e API_ADDR=https://myapi.com -e API_PORT=1234 generator
```

If running locally, specify `n` rows with:
```shell
./seed_db.py n
```
Also create an `.env` file from the template in `.env.example` to change API location.
