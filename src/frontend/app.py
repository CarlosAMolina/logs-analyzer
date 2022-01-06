from os.path import exists
from typing import List
import json

import flask
import flask_restful
import requests

from . import config as config_frontend
from ..api import config as config_api

app = flask.Flask(__name__, template_folder="templates")
app.secret_key = b"foo"
api = flask_restful.Api(app)


@app.route("/")
def root():
    return flask.redirect("/logs-path")


@app.route("/logs-path", methods=["GET", "POST"])
def logs_path():
    error_msg = None
    logs_path = "/tmp/access.log"
    if flask.request.method == "POST":
        logs_path = flask.request.form["logs-path"].split("\r\n")[0].strip()
        if exists(logs_path):
            flask.session["logs-path"] = logs_path
            return flask.redirect("/logs")
        else:
            error_msg = f"ERROR. File not found: {logs_path}"
    return flask.render_template(
        "logs-path.html",
        error_msg=error_msg,
        logs_path=logs_path,
    )


@app.route("/logs", methods=["GET", "POST"])
def logs():
    vt_results = None
    if flask.request.method == "POST":
        ips = flask.request.form["ips"].replace(" ", "").split("\r\n")
        ips = [ip for ip in set(ips) if len(ip)]
        vt_results = ApiRequests.get_ips_vt(ips)
    logs_path = flask.session["logs-path"]
    return flask.render_template(
        "logs.html",
        logs_all=ApiRequests.get_logs_path(logs_path),
        remote_addrs_count=ApiRequests.get_remote_addrs_count(logs_path),
        url_logs_path=f"http://127.0.0.1:{config_frontend.PORT}/logs-path",
        vt_results=vt_results,
    )


class ApiRequests:
    API_URL = f"http://localhost:{config_api.PORT}"

    @classmethod
    def get_logs_path(cls, logs_path: str) -> List[dict]:
        return cls._get_post_request_results(
            data={"logs-path": logs_path},
            url=f"{cls.API_URL}/logs-all",
        )

    @classmethod
    def _get_post_request_results(cls, data: dict, url: str) -> List[dict]:
        headers = {"Content-type": "application/json", "Accept": "text/plain"}
        response = requests.post(
            url,
            data=json.dumps(data),
            headers=headers,
        )
        return response.json()["data"]

    @classmethod
    def get_remote_addrs_count(cls, logs_path: str) -> List[dict]:
        return cls._get_post_request_results(
            data={"logs-path": logs_path},
            url=f"{cls.API_URL}/remote-addrs-count",
        )

    @classmethod
    def get_ips_vt(cls, ips: List[str]) -> List[dict]:
        return cls._get_post_request_results(
            data={"ips": ips},
            url=f"{cls.API_URL}/ips-vt",
        )
