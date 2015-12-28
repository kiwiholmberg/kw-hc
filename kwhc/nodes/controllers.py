#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, current_app, jsonify

bp = Blueprint('node', __name__)


@bp.route('/helloworld', methods=['GET'])
def helloworld():
    return jsonify({
        'data': 'Hello world.'
    })
