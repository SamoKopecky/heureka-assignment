import json
import logging

from .utils import get_connection
from ..controller.astronaut import read_all
from ..controller.astronaut import create


def import_callback(ch, method, properties, body):
    create(json.loads(body))


def command_callback(ch, method, properties, body):
    if body == b"export":
        logging.info("Exporting db...")
        data = read_all()
        ch.queue_declare(queue="export")
        ch.basic_publish(
            exchange="",
            routing_key="export",
            body=json.dumps(data),
        )
    # Maybe these are not even required?
    elif body == b"import":
        logging.info("Importing db...")
        ch.queue_declare(queue="import")
        ch.basic_consume(
            queue="import", on_message_callback=import_callback, auto_ack=True
        )


def receive_commands():
    channel = get_connection().channel()
    channel.queue_declare(queue="commands")
    channel.basic_consume(
        queue="commands", on_message_callback=command_callback, auto_ack=True
    )
    logging.info(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()
