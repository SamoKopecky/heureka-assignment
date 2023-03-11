FROM python:3.10
WORKDIR generator

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["./seed_db.py"]
