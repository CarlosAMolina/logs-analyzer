from flask import request
from flask_restful import Resource
from http import HTTPStatus

from ...backend.vt import manager


class IPVTAnalysisListResource(Resource):
    def post(self):
        request_data = request.get_json()
        ips = request_data["ips"]
        data = [manager.get_analysis_of_ip(ip).data for ip in ips]
        return {"data": data}, HTTPStatus.OK
