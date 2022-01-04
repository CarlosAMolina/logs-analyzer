from ...api.models import vt as vt_model
from . import transformer
from . import extractor


def get_analysis_of_ip(ip: str) -> vt_model.IPVTAnalysis:
    ip_analyzer = extractor.RequestIp()
    response_analysis = ip_analyzer.get_analysis(ip)
    ip_results = transformer.IpResults(response_analysis)
    return vt_model.IPVTAnalysis(
        ip=ip,
        malicious=ip_results.malicious,
        suspicious=ip_results.suspicious,
        harmless=ip_results.harmless,
        last_modification_date=ip_results.last_modification_date,
    )
