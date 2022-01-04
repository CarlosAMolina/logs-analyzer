from typing import List
import json

import flask
import flask_restful
import requests

from ..api import config as config_api

app = flask.Flask(__name__, template_folder="templates")
app.secret_key = b"foo"
api = flask_restful.Api(app)


@app.route("/")
def main_path():
    return flask.redirect("/logs-path")


@app.route("/logs-path")
def logs_file_get():
    return flask.render_template("logs-path.html")


@app.route("/logs-path", methods=["POST"])
def logs_file_post():
    logs_path = flask.request.form["logs-path"].split("\r\n")[0].strip()
    flask.session["logs-path"] = logs_path
    return flask.redirect("/logs")


@app.route("/logs", methods=["GET", "POST"])
def show_logs():
    logs_path = flask.session["logs-path"]
    logs_data = LogsData(logs_path)
    vt_results = None
    if flask.request.method == "POST":
        ips = flask.request.form["ips"].replace(" ", "").split("\r\n")
        ips = [ip for ip in set(ips) if len(ip)]
        vt_results = logs_data.get_vt_analysis_of_ips(ips)
    return flask.render_template(
        "logs.html",
        vt_results=vt_results,
        logs_all=logs_data.logs_all,
        remote_addrs_count=logs_data.remote_addrs_count,
    )


class LogsData:
    def __init__(
        self,
        logs_path: str,
    ):
        self._logs_path = logs_path

    @property
    def logs_all(self) -> List[dict]:
        return self._get_post_request_results(
            data={"logs-path": self._logs_path},
            url=f"http://localhost:{config_api.PORT}/logs-all",
        )

    def _get_post_request_results(self, data: dict, url: str) -> List[dict]:
        headers = {"Content-type": "application/json", "Accept": "text/plain"}
        response = requests.post(
            url,
            data=json.dumps(data),
            headers=headers,
        )
        return response.json()["data"]

    @property
    def remote_addrs_count(self) -> List[dict]:
        return self._get_post_request_results(
            data={"logs-path": self._logs_path},
            url=f"http://localhost:{config_api.PORT}/remote-addrs-count",
        )

    def get_vt_analysis_of_ips(self, ips: List[str]) -> List[dict]:
        return self._get_post_request_results(
            data={"ips": ips},
            url=f"http://localhost:{config_api.PORT}/ips-vt",
        )
