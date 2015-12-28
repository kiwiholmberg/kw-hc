#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from config import kwhc_appconfig
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config.kwhc_appconfig')

# Init database.
db = SQLAlchemy(app)

# Init blueprints
import nodes.controllers  # noqa
app.register_blueprint(nodes.controllers.bp)
