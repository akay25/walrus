import sys, os

sys.path.insert(1, os.path.join(sys.path[0], ".."))

from utils import return_json
from __main__ import app
from flask import request

tokens = {"admin": {"token": "admin-token"}, "editor": {"token": "editor-token"}}

users = {
    "admin-token": {
        "roles": ["admin"],
        "introduction": "I am a super administrator",
        "avatar": "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif",
        "name": "Super Admin",
    },
    "editor-token": {
        "roles": ["editor"],
        "introduction": "I am an editor",
        "avatar": "https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif",
        "name": "Normal Editor",
    },
}


@app.route("/user/login", methods=["POST"])
def login():
    response = {}
    username = request.json["username"]
    password = request.json["password"]

    if username not in tokens:
        response = {"code": 60204, "message": "Account and password are incorrect."}
    else:
        token = tokens[username]
        response = {"code": 20000, "data": token}
    return return_json(response)


@app.route("/user/logout", methods=["GET"])
def logout():
    response = {"code": 20000, "data": "success"}
    return return_json(response)


@app.route("/user/info", methods=["GET"])
def user_info():
    token = request.headers["X-Token"]
    if token in users:
        # Valid user
        info = users[token]
        response = {"code": 20000, "data": info}
    else:
        response = {"code": 50008, "message": "Unauthorized"}
    return return_json(response)

