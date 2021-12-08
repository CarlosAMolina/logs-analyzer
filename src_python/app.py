import flask

from . import analyzer
from . import parser
from . import vt


app = flask.Flask(__name__, template_folder="templates")


class LogsData:
    def __init__(self):
        get_file_as_df = parser.PandasParser("../logs-parser-results/access.log")
        logs = get_file_as_df()
        self._ips_count_html = (
            analyzer.LogsAnalyzer(logs).get_remote_addr_count().to_html()
        )
        get_logs_summarized = analyzer.LogsSummarize()
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


@app.route("/logs")
def show_logs():
    logs_data = LogsData()
    return flask.render_template(
        "logs.html",
        ips_count=logs_data.ips_count_html,
        ips_suspicious=logs_data.ips_suspicious,
        logs=logs_data.logs_suspicious_html,
    )


@app.route("/logs", methods=["POST"])
def analyze_ip():
    ips = flask.request.form["ips"].split("\r\n")
    get_ip_analysis = vt.IpAnalyzer()
    # get_ip_analysis = lambda x: "bad"
    vt_results_html = "<br>".join([f"{ip} {get_ip_analysis(ip)}" for ip in ips])
    logs_data = LogsData()
    return flask.render_template(
        "logs.html",
        ips_count=logs_data.ips_count_html,
        ips_suspicious=logs_data.ips_suspicious,
        logs=logs_data.logs_suspicious_html,
        vt_results=vt_results_html,
    )
