import flask
import flask_restful


class ResponseParent(flask_restful.Resource):
    def __init__(self):
        self.cors = Cors()

    def options(self):
        return self.cors.build_preflight_response()


class Cors:
    """
    Fix CORS errors with Angular
    https://medium.com/@eric.hung0404/deal-with-cors-without-flask-cors-an-example-of-react-and-flask-5832c44108a7
    https://werkzeug.palletsprojects.com/en/2.0.x/wrappers/#werkzeug.wrappers.Response
    """

    def build_actual_response(self, response_data):
        return flask.Response(
                response=flask.json.dumps(response_data),
                content_type="application/json",
                headers=[('Access-Control-Allow-Origin', '*')],
                )
    
    
    def build_preflight_response(self):
        response = flask.make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add('Access-Control-Allow-Headers', "*")
        response.headers.add('Access-Control-Allow-Methods', "*")
        return response

