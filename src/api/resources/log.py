from flask import request
from flask_restful import Resource
from http import HTTPStatus

from ...backend.logs_etl import manager


class LogListResource(Resource):
    def post(self):
        data = [log.data for log in manager.get_logs_from_file(get_logs_path())]
        return {"data": data}, HTTPStatus.OK


def get_logs_path() -> str:
    request_data = request.get_json()
    return request_data["logs-path"]


class RemoteAddrCountListResource(Resource):
    def post(self):
        data = [
            remote_addr_count.data
            for remote_addr_count in manager.get_remote_addrs_count_from_file(
                get_logs_path()
            )
        ]
        return {"data": data}, HTTPStatus.OK
