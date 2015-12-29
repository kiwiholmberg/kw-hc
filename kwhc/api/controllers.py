#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, current_app, jsonify
# from kwhc import telldus_core
from kwhc.common.telldus import get_device_by_name
bp = Blueprint('api', __name__)


@bp.route('/ping', methods=['GET'])
def pingpong():
    return jsonify({
        'data': 'pong'
    })

@bp.route('/control/device/<device_name>/<state>', methods=['POST', 'GET'])
def control_node(device_name, state):
    r = { 'status': 'ok'}

    d = get_device_by_name(device_name)
    if state == 'on':
        d.turn_on()
    elif state == 'off':
        d.turn_off()
    else:
        r['status'] = 'Invalid state'

    return jsonify(r)
