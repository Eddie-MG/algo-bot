import os
import requests
import json


def login():
    hdr = {
        'Content-Type': 'application/json; charset=UTF-8',
        "Accept": "application/json; charset=UTF-8",
        "VERSION": "2",
        "X-IG-API-KEY": os.environ["API_KEY"]
    }

    bdy = {
        "identifier": os.environ["UNAME"],
        "password": os.environ["PWORD"],
        "encryptedPassword": None,
    }

    resp = requests.post("https://demo-api.ig.com/gateway/deal/session", headers=hdr, json=bdy)

    resp_dict = json.loads(resp.content.decode('utf-8'))
    print(resp_dict["accountInfo"])

    return {"CST": resp.headers["CST"], "TOKEN": resp.headers["X-SECURITY-TOKEN"]}
