from flask import Flask
from flask import request

from ..controller.astronaut import (
    read_with_limit,
    read_all,
    create,
    delete_by_id,
    delete_all,
    update_by_id,
    read_by_id,
)

app = Flask(__name__)
astronauts = "astronauts"


@app.route(f"/{astronauts}")
def read_astronauts():
    if "limit" in request.args.keys():
        return read_with_limit(request.args["limit"])
    return read_all()


@app.route(f"/{astronauts}/<int:read_id>")
def read_astronaut(read_id):
    astronaut = read_by_id(read_id)
    if astronaut == {}:
        return {"error": "record not found"}, 404
    return astronaut


@app.route(f"/{astronauts}/create", methods=["POST"])
def create_astronaut():
    if request.content_type != "application/json":
        return {"error": "unsupported content type"}, 415
    data = request.json
    if type(data) != list:
        data = [data]
    return {"created": create(data)}, 201


@app.route(f"/{astronauts}/<int:delete_id>/delete", methods=["DELETE"])
def delete_astronaut(delete_id):
    if delete_by_id(delete_id):
        return {"deleted": delete_id}
    return {"error": "record not found"}, 404


@app.route(f"/{astronauts}/delete", methods=["DELETE"])
def delete_astronauts():
    count = delete_all()
    return {"deleted": f"{count}"}


@app.route(f"/{astronauts}/<int:update_id>/update", methods=["PATCH"])
def update_astronaut(update_id):
    update_by_id(update_id, request.json)
    return {"updated": update_id}
