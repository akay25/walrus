from aux_functions import *
from flask import Flask, render_template, request, Response, session, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Importing routes
from routes import user, common

if __name__ == "__main__":
    WEB_HOST = env("WEB_IP")
    WEB_PORT = env("WEB_PORT")

    app.run(host=WEB_HOST, port=WEB_PORT)
