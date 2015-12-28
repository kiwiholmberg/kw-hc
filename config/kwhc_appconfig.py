# Enable debug mode.
DEBUG = True

# Connect to the database
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost/kwhc'

SQLALCHEMY_TRACK_MODIFICATIONS = False

try:
    from kwhc_appconfig_local import *
except ImportError:
    pass
