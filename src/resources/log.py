from flask import request
from flask_restful import Resource
from http import HTTPStatus

from ..logs import manager


class LogListResource(Resource):
    def get(self):
        data = [log.data for log in manager.get_logs_from_file()]
        return {"data": data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()
        file = data["file"]
        data = [log.data for log in manager.get_logs_from_file(file)]
        return {"data": data}, HTTPStatus.OK
