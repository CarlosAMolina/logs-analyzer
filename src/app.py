from typing import List
import json

import flask
import flask_restful
import requests

from .logs import transformer as logs_transformer
from .resources import log as log_resources
from .vt import transformer as vt_transformer


app = flask.Flask(__name__, template_folder="templates")
app.secret_key = b"foo"
api = flask_restful.Api(app)

api.add_resource(log_resources.LogListResource, "/logs-all")


class LogsData:
    def __init__(self, logs_path: str):
        self._logs_path = logs_path
        get_file_as_df = logs_transformer.PandasParser(logs_path)
        logs = get_file_as_df()
        self._ips_count_html = (
            logs_transformer.LogsAnalyzer(logs).get_remote_addr_count().to_html()
        )
        get_logs_summarized = logs_transformer.LogsSummarize()
        logs_summarized = get_logs_summarized(logs)
        self._logs_suspicious_html = logs_summarized.to_html()
        self._ips_suspicious = logs_summarized.index.drop_duplicates().tolist()

    @property
    def ips_count_html(self):
        return self._ips_count_html

    @property
    def ips_suspicious(self):
        return self._ips_suspicious

    @property
    def logs_suspicious_html(self):
        return self._logs_suspicious_html

    @property
    def logs_all(self) -> List[dict]:
        url = "http://localhost:5000/logs-all"
        data = {"file": self._logs_path}
        headers = {"Content-type": "application/json", "Accept": "text/plain"}
        response = requests.post(
            url,
            data=json.dumps(data),
            headers=headers,
        )
        return response.json()["data"]

    @property
    def logs_all_keys(self) -> List[str]:
        return list(self.logs_all[0].keys())


@app.route("/")
def main_path():
    return flask.redirect("/logs-path")


@app.route("/logs-path")
def logs_file_get():
    return flask.render_template("logs-path.html")


@app.route("/logs-path", methods=["POST"])
def logs_file_post():
    logs_path = flask.request.form["logs-path"].split("\r\n")[0]
    flask.session["logs_path"] = logs_path
    return flask.redirect("/logs")


@app.route("/logs")
def show_logs():
    logs_path = flask.session["logs_path"]
    logs_data = LogsData(logs_path)
    return flask.render_template(
        "logs.html",
        ips_count=logs_data.ips_count_html,
        ips_suspicious=logs_data.ips_suspicious,
        logs_suspicious=logs_data.logs_suspicious_html,
        logs_all_keys=logs_data.logs_all_keys,
        logs_all=logs_data.logs_all,
    )


@app.route("/logs", methods=["POST"])
def analyze_ip():
    ips = flask.request.form["ips"].split("\r\n")
    ips = [ip for ip in ips if len(ip)]
    get_vt_analysis_as_df_of_ips = vt_transformer.IPsAnalyzerAsDf()
    vt_results = get_vt_analysis_as_df_of_ips(ips)
    vt_results_html = vt_results.to_html()
    logs_path = flask.session["logs_path"]
    logs_data = LogsData(logs_path)
    return flask.render_template(
        "logs.html",
        ips_count=logs_data.ips_count_html,
        ips_suspicious=logs_data.ips_suspicious,
        logs_suspicious=logs_data.logs_suspicious_html,
        vt_results=vt_results_html,
        logs_all_keys=logs_data.logs_all_keys,
        logs_all=logs_data.logs_all,
    )
