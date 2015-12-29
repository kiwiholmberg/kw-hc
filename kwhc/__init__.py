#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
import jinja2
from config import kwhc_appconfig
from flask.ext.sqlalchemy import SQLAlchemy
from tellcore.telldus import TelldusCore


app = Flask(__name__)
app.config.from_object('config.kwhc_appconfig')

# Init Jinja2 templates.
new_jinja_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader('kwhc/ui/templates'),
])
app.jinja_loader = new_jinja_loader

# Init telstick interface.
telldus_core = TelldusCore()

# Init database.
db = SQLAlchemy(app)

# Init blueprints
import api.controllers  # noqa
import ui.controllers  # noqa
app.register_blueprint(api.controllers.bp)
app.register_blueprint(ui.controllers.bp)


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        'error': str(error),
        'status': 'error'
    })


@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
