FROM python:3.10
WORKDIR heureka

COPY requirements.txt .

RUN apt install -y libpq-dev
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "main.py"]
