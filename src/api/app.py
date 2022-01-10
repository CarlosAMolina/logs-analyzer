import flask
import flask_restful

from .resources import log as log_resources
from .resources import vt as vt_resources

app = flask.Flask(__name__)
api = flask_restful.Api(app)

api.add_resource(log_resources.LogFileResource, "/log-file-is-file")
api.add_resource(log_resources.LogListResource, "/logs-all")
api.add_resource(log_resources.RemoteAddrCountListResource, "/remote-addrs-count")
api.add_resource(vt_resources.IPVTAnalysisListResource, "/ips-vt")
