from flask import request
from flask_restful import Resource
from http import HTTPStatus

from ..logs import manager


class LogListResource(Resource):
    def post(self):
        request_data = request.get_json()
        logs_path = request_data["logs-path"]
        data = [log.data for log in manager.get_logs_from_file(logs_path)]
        return {"data": data}, HTTPStatus.OK
