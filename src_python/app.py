import flask

from . import analyzer
from . import parser
from . import vt


app = flask.Flask(__name__, template_folder="templates")


@app.route("/logs")
def show_logs():
    get_file_as_df = parser.PandasParser("../logs-parser-results/access.log")
    logs = get_file_as_df()
    get_logs_summarized = analyzer.LogsSummarize()
    logs_summarized = get_logs_summarized(logs)
    logs_html = logs_summarized.to_html(classes="logs")
    ips_html = (
        logs_summarized[[]]
        .reset_index()
        .drop_duplicates()
        .to_html(header=False, index=False)
    )
    return flask.render_template("logs.html", tables=[logs_html, ips_html])


@app.route("/logs", methods=["POST"])
def analyze_ip():
    ips = flask.request.form["ips"].split("\r\n")
    get_ip_analysis = vt.IpAnalyzer()
    return "<br>".join([f"{ip} {get_ip_analysis(ip)}" for ip in ips])
