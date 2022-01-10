from os.path import exists

from flask import request, Response, json, make_response
from flask_restful import Resource
from http import HTTPStatus

from ...backend.logs_file_parser import manager as logs_file_parser_manager
from ...backend.logs_file_analyzer import manager as logs_file_analyzer_manager


class LogFileResource(Resource):
    def post(self):
        data = exists(get_logs_path())
        return {"data": data}, HTTPStatus.OK


class LogListResource(Resource):
    def post(self):
        data = [
            log.data
            for log in logs_file_parser_manager.get_logs_from_file(get_logs_path())
        ]
        return {"data": data}, HTTPStatus.OK


def get_logs_path() -> str:
    request_data = request.get_json()
    return request_data["logs-path"]


class RemoteAddrCountListResource(Resource):
    def post(self):
        get_remote_addrs_count = (
            logs_file_analyzer_manager.get_remote_addrs_count_from_file
        )
        data = [
            remote_addr_count.data
            for remote_addr_count in get_remote_addrs_count(get_logs_path())
        ]
        # Fix CORS errors with Angular
        # https://werkzeug.palletsprojects.com/en/2.0.x/wrappers/#werkzeug.wrappers.Response
        resp = Response(
            response=json.dumps(data),
            content_type="application/json",
            headers=[('Access-Control-Allow-Origin', '*')],
            )
        return resp

    def options(self):
        def build_preflight_response():
            """ Fix CORS errors with Angular
            https://medium.com/@eric.hung0404/deal-with-cors-without-flask-cors-an-example-of-react-and-flask-5832c44108a7
            """
            response = make_response()
            response.headers.add("Access-Control-Allow-Origin", "*")
            response.headers.add('Access-Control-Allow-Headers', "*")
            response.headers.add('Access-Control-Allow-Methods', "*")
            return response

        return build_preflight_response()

