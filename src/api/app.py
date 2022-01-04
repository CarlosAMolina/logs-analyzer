import flask
import flask_restful

from .resources import log as log_resources

app = flask.Flask(__name__)
api = flask_restful.Api(app)

api.add_resource(log_resources.LogListResource, "/logs-all")
