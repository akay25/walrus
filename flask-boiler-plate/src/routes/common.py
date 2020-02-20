import sys, os

sys.path.insert(1, os.path.join(sys.path[0], ".."))

import requests
from utils import return_json, getVPNServersList
from __main__ import app


@app.route("/vpn-servers", methods=["GET"])
def getVPNServers():
    data = getVPNServersList()
    return return_json(data)

@app.route("/link-types", methods=["GET"])
def getFacebookLinkTypes():
    data = [
        "EVENT",
        "GROUP",
        "HASHTAG",
        "LIST",
        "PAGE",
        "USER",
    ]
    response = {
        "data": data,
        "code": 20000
    }
    return return_json(response)
