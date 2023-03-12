import argparse
import logging

from src.api.routes import app

from src.model.db import Db
from src.manager.consumer import receive_commands
from src.manager.producer import send_commands


def parse_args():
    default_file = "./export.json"
    parser = argparse.ArgumentParser()
    options = parser.add_mutually_exclusive_group()
    options.add_argument(
        "-c",
        "--consumer",
        action="store_true",
        help="run as consumer for db management",
    )
    options.add_argument(
        "-pi",
        "--producer-import",
        action="store_true",
        help="run as a producer, send the command to import the db",
    )
    options.add_argument(
        "-pe",
        "--producer-export",
        action="store_true",
        help="run as a producer, send the command to export the db",
    )
    options.add_argument("-a", "--api", action="store_true", help="run the rest api")
    parser.add_argument(
        "-fp",
        "--file-path",
        action="store",
        default=default_file,
        help=f"full path name to a file (default '{default_file}')",
    )
    parsed = parser.parse_args()
    return parsed, parser.print_help


def api():
    db = Db()
    db.create_tables()
    app.run(port=5001, host="0.0.0.0", debug=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    args, help_fun = parse_args()
    if args.api:
        api()
    elif args.consumer:
        receive_commands()
    elif args.producer_export or args.producer_import:
        send_commands(args.producer_export, args.file_path)
    else:
        help_fun()
