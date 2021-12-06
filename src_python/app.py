import flask

from . import analyzer
from . import parser


app = flask.Flask(__name__, template_folder="templates")


@app.route("/logs")
def show_logs():
    get_file_as_df = parser.PandasParser("../logs-parser-results/access.log")
    logs = get_file_as_df()
    get_logs_summarized = analyzer.LogsSummarize()
    logs_summarized = get_logs_summarized(logs)
    return flask.render_template(
        "view.html", tables=[logs_summarized.to_html(justify="left")]
    )
