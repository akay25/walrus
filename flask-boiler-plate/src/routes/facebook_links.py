import sys, os

sys.path.insert(1, os.path.join(sys.path[0], ".."))

from utils import return_json
from __main__ import app


@app.route("/facebook-links", methods=["GET"])
def getLinks():
    data = [
        {
            "link": "some facebbok link",
            "type": "GROUP",
            "last_checked": 1582199578,
            "status": 1,
            "enabled": True,
            "total_scraps": 10
        },
        {
            "link": "some facebbok link",
            "type": "GROUP",
            "last_checked": 1582199578,
            "status": 1,
            "enabled": True,
            "total_scraps": 10
        },
        {
            "link": "some facebbok link",
            "type": "GROUP",
            "last_checked": 1582199578,
            "status": 1,
            "enabled": True,
            "total_scraps": 10
        },
        {
            "link": "some facebbok link",
            "type": "GROUP",
            "last_checked": 1582199578,
            "status": 1,
            "enabled": True,
            "total_scraps": 10
        },
        {
            "link": "some facebbok link",
            "type": "GROUP",
            "last_checked": 1582199578,
            "status": 1,
            "enabled": True,
            "total_scraps": 10
        },
        {
            "link": "some facebbok link",
            "type": "GROUP",
            "last_checked": 1582199578,
            "status": 0,
            "enabled": True,
            "total_scraps": 10
        },
        {
            "link": "some facebbok link",
            "type": "GROUP",
            "last_checked": 1582199578,
            "status": 1,
            "enabled": True,
            "total_scraps": 10
        },
        {
            "link": "some facebbok link",
            "type": "GROUP",
            "last_checked": 1582199578,
            "status": 2,
            "enabled": True,
            "total_scraps": 10
        },
        {
            "link": "some facebbok link",
            "type": "GROUP",
            "last_checked": 1582199578,
            "status": 2,
            "enabled": True,
            "total_scraps": 10
        }
    ]
    response = {
        "data": {
            "items": data,
            "total": len(data),
        },
        "code": 20000
    }
    return return_json(response)
