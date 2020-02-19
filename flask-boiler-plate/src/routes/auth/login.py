import sys, os

sys.path.insert(1, os.path.join(sys.path[0], ".."))

from utils import return_json
from __main__ import app
from flask import request


@app.route("/user/login", methods=["POST"])
def login():
    print(request.json)
    username = request.json["username"]
    password = request.json["password"]

    if username == "admin" and password == "111111":
        response = {"data": 20000}
    return return_json()
