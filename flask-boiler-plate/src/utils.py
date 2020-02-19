from __main__ import app
from flask import json
import requests


def return_json(data):
    return app.response_class(response=json.dumps(data), mimetype="application/json")


def getVPNServersList():
    vpn_servers = []
    response = requests.get("https://vpn.hidemyass.com/vpn-config/l2tp/")
    if response.status_code == 200:
        data = [x for x in response.text.split("\n")]

        for row in data:
            if len(row.strip()):
                row = row.split("\t")
                vpn_servers.append({"server": row[0], "region": row[1]})

    return vpn_servers
