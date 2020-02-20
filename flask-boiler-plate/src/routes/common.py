import sys, os

sys.path.insert(1, os.path.join(sys.path[0], ".."))

import requests
from utils import return_json, getVPNServersList
from __main__ import app


@app.route("/regions", methods=["GET"])
def getRegions():
    data = [
        {
            "server": "192.168.137.236",
            "region": "Local"
        },
        {
            "server": "192.168.137.23",
            "region": "Local"
        },
        {
            "server": "192.168.137.22",
            "region": "Local"
        },
        {
            "server": "192.168.137.256",
            "region": "Local"
        },
        {
            "server": "192.168.137.2",
            "region": "Local"
        }
    ]
    response = {
        "code": 20000,
        "data": data
    }
    return return_json(response)

@app.route("/facebook-users", methods=["GET"])
def getFacebookUsers():
    data = [
        {
            "username": "kalakaar.humara",
            "password": "Asafaf",
            "status": 1,
            "region": "192.168.137.236",
            "total_scraps": 10,
            "last_checked": 1578523941
        }
    ]
    response = {
        "data": data,
        "code": 20000
    }
    return return_json(response)



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

