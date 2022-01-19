import flask

from ...backend.logs_file_parser import manager as logs_file_parser_manager
from ...backend.logs_file_analyzer import manager as logs_file_analyzer_manager
from . import response



class LogFileResource(response.ResponseParent):
    def post(self):
        data = logs_file_analyzer_manager.get_is_file(get_logs_path()).data
        return self.cors.build_actual_response(data)


class LogListResource(response.ResponseParent):
    def post(self):
        data = [
            log.data
            for log in logs_file_parser_manager.get_logs_from_file(get_logs_path())
        ]
        return self.cors.build_actual_response(data)


def get_logs_path() -> str:
    request_data = flask.request.get_json()
    return request_data["logs-file"]


class RemoteAddrCountListResource(response.ResponseParent):
    def post(self):
        get_remote_addrs_count = (
            logs_file_analyzer_manager.get_remote_addrs_count_from_file
        )
        data = [
            remote_addr_count.data
            for remote_addr_count in get_remote_addrs_count(get_logs_path())
        ]
        return self.cors.build_actual_response(data)

