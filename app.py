import re

from flask import Flask
from http import HTTPStatus

app = Flask(__name__)

@app.route("/")
def design():
    design_file = open('./design', 'r')
    body = design_file.read()
    design_file.close()

    split = body.split('\n')
    formatted = [f'<p>{line}</p>' for line in split]
    joined = ''.join(formatted)
    wrapped = f'<html><body>{joined}</body></html>'

    return wrapped, HTTPStatus.OK
