from .utils import get_connection


def send_commands(export, file_path):
    connection = get_connection()
    channel = connection.channel()
    channel.queue_declare(queue="commands")

    if export:
        channel.basic_publish(
            exchange="",
            routing_key="commands",
            body="export",
        )
        channel.queue_declare(queue="export")

        def callback(ch, method, properties, body):
            save_to_file(body, file_path)
            ch.stop_consuming()

        channel.basic_consume(
            queue="export", on_message_callback=callback, auto_ack=True
        )
        channel.start_consuming()
    else:
        channel.basic_publish(
            exchange="",
            routing_key="commands",
            body="import",
        )
        channel.queue_declare(queue="import")
        channel.basic_publish(
            exchange="",
            routing_key="import",
            body=load_from_file(file_path),
        )


def load_from_file(file_path):
    with open(file_path, "rb") as file:
        return file.read()


def save_to_file(data, file_path):
    with open(file_path, "wb") as file:
        file.write(data)
