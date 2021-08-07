from flask import Flask
from http import HTTPStatus

app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'boot', HTTPStatus.OK
