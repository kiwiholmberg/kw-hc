#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, current_app, jsonify, render_template
from kwhc import telldus_core

bp = Blueprint('ui', __name__)


@bp.route('/', methods=['GET'])
def index():
    # Always put groups first in list.
    devices = sorted(
        telldus_core.devices(),
        key=lambda x: hasattr(x, 'devices_in_group'),
        reverse=True
    )

    return render_template('index.html',
                           devices=devices
    )
