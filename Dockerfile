FROM python:3.10
WORKDIR src

ENV DB_PASSWD=secret
ENV DB_ADDR=127.0.0.1
ENV DB_PORT=5432
ENV RABBITMQ_PASSWD=guest
ENV RABBITMQ_USER=guest
ENV RABBITMQ_ADDR=127.0.0.1
ENV RABBITMQ_PORT=5672

COPY requirements.txt .

RUN apt install -y libpq-dev
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "main.py"]
