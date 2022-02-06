import flask
import flask_migrate
import flask_restful

from . import config
from .extensions import db

# TODO uncomment
# from .models.log import User  # Required to create it's table in the database.
from .resources import log as log_resources
from .resources import vt as vt_resources


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
