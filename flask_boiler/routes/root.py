#!/usr/bin/env python3

import json

import flask
from flask import current_app as app

v1_root = flask.Blueprint('home', __name__)

@v1_root.route('/', methods=['GET'])
def landing_page():
    return flask.render_template('home.html')
