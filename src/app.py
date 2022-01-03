from typing import List

import flask
import flask_restful

from .logs import transformer as logs_transformer
from .logs import extractor
from .resources import log as log_resources
from .vt import transformer as vt_transformer


app = flask.Flask(__name__, template_folder="templates")
app.secret_key = b"foo"
api = flask_restful.Api(app)


class LogsData:
    def __init__(self):
        get_file_as_df = logs_transformer.PandasParser(extractor.LOG_FILE)
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
    def logs_all(self) -> dict:
        return log_resources.LogListResource().get()[0]["data"]

    @property
    def logs_all_keys(self) -> List[str]:
        return list(self.logs_all[0].keys())


@app.route("/")
def main_path():
    return flask.redirect("/logs-file")


@app.route("/logs-file")
def logs_file_get():
    return flask.render_template("logs-file.html")


@app.route("/logs-file", methods=["POST"])
def logs_file_post():
    logs_file = flask.request.form["logs-file"].split("\r\n")[0]
    flask.session["logs_file"] = logs_file
    return flask.redirect("/logs")


@app.route("/logs")
def show_logs():
    logs_file = flask.session["logs_file"]
    print(logs_file)
    logs_data = LogsData()
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
    logs_data = LogsData()
    return flask.render_template(
        "logs.html",
        ips_count=logs_data.ips_count_html,
        ips_suspicious=logs_data.ips_suspicious,
        logs_suspicious=logs_data.logs_suspicious_html,
        vt_results=vt_results_html,
        logs_all_keys=logs_data.logs_all_keys,
        logs_all=logs_data.logs_all,
    )
