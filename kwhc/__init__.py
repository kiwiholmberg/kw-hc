#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from config import kwhc_appconfig
from flask.ext.sqlalchemy import SQLAlchemy
from tellcore.telldus import TelldusCore


app = Flask(__name__)
app.config.from_object('config.kwhc_appconfig')

# Init telstick interface.
telldus_core = TelldusCore()

# Init database.
db = SQLAlchemy(app)

# Init blueprints
import nodes.controllers  # noqa
app.register_blueprint(nodes.controllers.bp)


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        'error': str(error),
        'status': 'error'
    })
