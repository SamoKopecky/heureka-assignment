from src.api.routes import app

from src.controller.db import Db


def main():
    db = Db()
    db.create_tables()
    app.run(port=5001, host="0.0.0.0", debug=True)


if __name__ == "__main__":
    main()
