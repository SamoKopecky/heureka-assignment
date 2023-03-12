FROM python:3.10
WORKDIR generator

ENV API_ADDR="http://localhost"
ENV API_PORT="5001"

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["./seed_db.py"]
