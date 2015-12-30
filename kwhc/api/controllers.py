#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, current_app, jsonify
from kwhc import telldus_core
from kwhc.common.telldus import get_device_by_name
from .models import Scene, SceneDevice

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

@bp.route('/control/scene/<scene_name>/activate', methods=['POST', 'GET'])
def control_scene(scene_name):
    r = { 'status': 'ok'}

    # The scene and its configured devices.
    scene = Scene.query.filter(Scene.name == scene_name).first()
    # Make a dict of all devices in the scene.
    scene_devices_by_name = { sd.device_name: sd for sd in scene.devices }

    for d in telldus_core.devices():
        if d.name in scene_devices_by_name:
            state = scene_devices_by_name[d.name].state
            if state == 'on':
                # print 'Turn on %s' % d.name
                d.turn_on()
            elif state == 'off':
                # print 'Turn off %s' % d.name
                d.turn_off()
            else:
                print 'Unhandled state: %s' % str(state)

    return jsonify(r)
