# Generator

Generate random astronauts from data in `names.csv` and `nationalities.csv`.

## How to run

By default, 1000 rows are generated:
```shell
docker build -t generator . && docker run --network="host" --rm generator
```

To specify `n` rows, use:
```shell
docker build -t generator . && docker run --network="host" --rm -e ROWS=n generator
```

If running locally, specify `n` rows with:
```shell
./seed_db.py n
```
