import flask

from backend.vt import manager
from api.resources import response


class IPVTAnalysisListResource(response.ResponseParent):
    def post(self):
        request_data = flask.request.get_json()
        ips = request_data["ips"]
        data = [manager.get_analysis_of_ip(ip).data for ip in ips]
        return self.cors.build_actual_response(data)
