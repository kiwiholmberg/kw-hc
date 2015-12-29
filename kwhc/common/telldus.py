#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kwhc import telldus_core


def get_device_by_name(name):
    # Get a list of all devices and groups.
    for d in telldus_core.devices():
        if d.name == name:
            return d
    raise Exception('Device not found.')
