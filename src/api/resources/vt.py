from flask import request
from flask_restful import Resource
from http import HTTPStatus

from ...backend.vt.manager import manager


class IPVTAnalysisListResource(Resource):
    def post(self):
        request_data = request.get_json()
        ips = request_data["ips"]
        data = [manager.get_ip_analysis(ip).data for ip in ips]
        return {"data": data}, HTTPStatus.OK
