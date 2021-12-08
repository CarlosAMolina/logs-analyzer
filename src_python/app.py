import flask

from . import analyzer
from . import parser
from . import vt


app = flask.Flask(__name__, template_folder="templates")


@app.route("/logs")
def show_logs():
    get_file_as_df = parser.PandasParser("../logs-parser-results/access.log")
    logs = get_file_as_df()
    ips_count_html = analyzer.LogsAnalyzer(logs).get_remote_addr_count().to_html()
    get_logs_summarized = analyzer.LogsSummarize()
    logs_summarized = get_logs_summarized(logs)
    logs_html = logs_summarized.to_html()
    ips_suspicious = logs_summarized.index.drop_duplicates().tolist()
    return flask.render_template(
        "logs.html",
        ips_count=ips_count_html,
        ips_suspicious=ips_suspicious,
        logs=logs_html,
    )


@app.route("/logs", methods=["POST"])
def analyze_ip():
    ips = flask.request.form["ips"].split("\r\n")
    get_ip_analysis = vt.IpAnalyzer()
    return "<br>".join([f"{ip} {get_ip_analysis(ip)}" for ip in ips])
