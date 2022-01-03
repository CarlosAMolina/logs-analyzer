import os

import requests


API_KEY = os.environ["VT_KEY"]


class RequestIp:
    URL = "https://www.virustotal.com/api/v3/ip_addresses/{ip}"

    def get_analysis(self, ip: str) -> dict:
        response = requests.get(
            self.URL.format(ip=ip),
            headers={"x-apikey": API_KEY},
        )
        return response.json()
