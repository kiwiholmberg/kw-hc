#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, current_app, jsonify
from kwhc import telldus_core
bp = Blueprint('node', __name__)


@bp.route('/helloworld', methods=['GET'])
def helloworld():
    return jsonify({
        'data': 'Hello world.'
    })

@bp.route('/control/device/<device_name>/<state>')
def control_node(device_name, state):
    r = { 'status': 'ok'}

    # Get a list of all devices and groups.
    for d in telldus_core.devices():
        print d.name
        if d.name == device_name:
            if state == 'on':
                d.turn_on()
            elif state == 'off':
                d.turn_off()
            else:
                r['status'] = 'Invalid state'

    return jsonify(r)
