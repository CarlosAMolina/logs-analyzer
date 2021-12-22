from flask_restful import Resource
from http import HTTPStatus

from ..logs import manager


class LogListResource(Resource):
    def get(self):
        data = [log for log in manager.get_logs_from_file()]
        return {"data": data}, HTTPStatus.OK
