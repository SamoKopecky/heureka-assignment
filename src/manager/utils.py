import logging
import os
from time import sleep

from dotenv import load_dotenv
from pika import PlainCredentials, BlockingConnection, ConnectionParameters
from pika.exceptions import AMQPConnectionError


def get_connection():
    load_dotenv(override=False)
    creds = PlainCredentials(os.getenv("RABBITMQ_USER"), os.getenv("RABBITMQ_PASSWD"))
    retry = 1
    max_retry = 5
    for i in range(max_retry + 1):
        try:
            return BlockingConnection(
                ConnectionParameters(
                    os.getenv("RABBITMQ_ADDR"),
                    int(os.getenv("RABBITMQ_PORT")),
                    "/",
                    creds,
                )
            )
        except AMQPConnectionError:
            logging.warning(f"rabbitmq not accessible, trying again in {retry} seconds")
            sleep(retry)
            retry *= 2
