#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from kwhc import db


class Scene(db.Model):
    __tablename__ = 'scene'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    devices = db.relationship('SceneDevice', lazy='joined')

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow,
                                        onupdate=datetime.datetime.utcnow)


class SceneDevice(db.Model):
    __tablename__ = 'scene_device'

    id = db.Column(db.Integer, primary_key=True)
    scene_id = db.Column(db.Integer, db.ForeignKey('scene.id'))
    device_name = db.Column(db.String(255))
    state = db.Column(db.String(255))

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow,
                                        onupdate=datetime.datetime.utcnow)
