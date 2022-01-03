from ..logs_etl import extractor


class RuleGenerator:
    def get_drop_ip(str, ip: str) -> str:
        return f"-A ufw-before-input -s {ip} -j DROP"


class FileIpAnalyzer:
    def __init__(self, file: str):
        self._file_extractor = extractor.FileExtractor(file)
        self._generate_rule = RuleGenerator()

    def print_rule_drop_ip_addresses(self):
        for ip in self._file_extractor.get_lines_in_file():
            print(self._generate_rule.get_drop_ip(ip))
