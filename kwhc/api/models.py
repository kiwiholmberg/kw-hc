#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kwhc import db


class Node(db.Model):
    __tablename__ = 'nodes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
