#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, current_app, jsonify, render_template
from kwhc import telldus_core

bp = Blueprint('ui', __name__)


@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html',
                           devices=telldus_core.devices()
    )
