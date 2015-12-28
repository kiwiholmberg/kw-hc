#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Run migrations and other administrative tasks.
"""

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from kwhc import db, app

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
# manager.add_command('seed', SeedCommand)

if __name__ == "__main__":
    manager.run()
