from typing import List
import json

import flask
import flask_restful
import requests

from ..api import config as config_api
from ..backend.logs_etl import transformer as logs_transformer
from ..backend.vt import transformer as vt_transformer

app = flask.Flask(__name__, template_folder="templates")
app.secret_key = b"foo"
api = flask_restful.Api(app)


class LogsData:
    def __init__(self, logs_path: str):
        self._logs_path = logs_path
        get_file_as_df = logs_transformer.PandasParser(logs_path)
        logs = get_file_as_df()
        get_logs_summarized = logs_transformer.LogsSummarize()
        logs_summarized = get_logs_summarized(logs)
        self._logs_suspicious_html = logs_summarized.to_html()
        self._ips_suspicious = logs_summarized.index.drop_duplicates().tolist()

    @property
    def ips_suspicious(self):
        return self._ips_suspicious

    @property
    def logs_suspicious_html(self):
        return self._logs_suspicious_html

    @property
    def logs_all(self) -> List[dict]:
        url = f"http://localhost:{config_api.PORT}/logs-all"
        return self._get_post_request_results(url)

    def _get_post_request_results(self, url) -> List[dict]:
        data = {"logs-path": self._logs_path}
        headers = {"Content-type": "application/json", "Accept": "text/plain"}
        response = requests.post(
            url,
            data=json.dumps(data),
            headers=headers,
        )
        return response.json()["data"]

    @property
    def remote_addrs_count(self) -> List[dict]:
        url = f"http://localhost:{config_api.PORT}/remote-addrs-count"
        return self._get_post_request_results(url)


@app.route("/")
def main_path():
    return flask.redirect("/logs-path")


@app.route("/logs-path")
def logs_file_get():
    return flask.render_template("logs-path.html")


@app.route("/logs-path", methods=["POST"])
def logs_file_post():
    logs_path = flask.request.form["logs-path"].split("\r\n")[0]
    flask.session["logs-path"] = logs_path
    return flask.redirect("/logs")


@app.route("/logs", methods=["GET", "POST"])
def show_logs():
    logs_path = flask.session["logs-path"]
    logs_data = LogsData(logs_path)
    if flask.request.method == "GET":
        vt_results_html = None
    else:
        ips = flask.request.form["ips"].split("\r\n")
        ips = [ip for ip in ips if len(ip)]
        get_vt_analysis_as_df_of_ips = vt_transformer.IPsAnalyzerAsDf()
        vt_results = get_vt_analysis_as_df_of_ips(ips)
        vt_results_html = vt_results.to_html()
    return flask.render_template(
        "logs.html",
        ips_suspicious=logs_data.ips_suspicious,
        logs_suspicious=logs_data.logs_suspicious_html,
        vt_results=vt_results_html,
        logs_all=logs_data.logs_all,
        remote_addrs_count=logs_data.remote_addrs_count,
    )
