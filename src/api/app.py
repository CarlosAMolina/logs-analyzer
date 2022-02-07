import sys
import os

PROJECT_PATH = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_PATH)

import flask
import flask_migrate
import flask_restful

# Required to create it's table in the database
# TODO use correct class
# from api.models.log import LogB
from api import config
from api.extensions import db
from api.resources import log as log_resources
from api.resources import vt as vt_resources


def get_app():
    app = flask.Flask(__name__)
    app.config.from_object(config.Config)

    register_extensions(app)
    register_resources(app)

    return app


def register_extensions(app):
    db.init_app(app)
    # migrate = flask_migrate.Migrate(app, db) # TODO delte if not required
    flask_migrate.Migrate(app, db)


def register_resources(app):
    api = flask_restful.Api(app)

    api.add_resource(log_resources.LogFileResource, "/log-file-is-file")
    api.add_resource(log_resources.LogListResource, "/logs")
    api.add_resource(log_resources.RemoteAddrCountListResource, "/remote-addrs-count")
    api.add_resource(vt_resources.IPVTAnalysisListResource, "/ips-vt")


app = get_app()

if __name__ == "__main__":
    app.run()
