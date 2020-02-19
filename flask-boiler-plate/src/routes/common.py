import sys, os

sys.path.insert(1, os.path.join(sys.path[0], ".."))

import requests
from utils import return_json, getVPNServersList
from __main__ import app


@app.route("/vpn-servers", methods=["GET"])
def getVPNServers():
    data = getVPNServersList()
    return return_json(data)
