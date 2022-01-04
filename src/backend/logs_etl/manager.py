from typing import List

from ...api.models import log as log_model
from . import exception
from . import extractor
from . import transformer


def get_logs_from_file(logs_path: str) -> List[log_model.Log]:
    result = []
    for line in extractor.FileExtractor(logs_path).get_lines_in_file():
        try:
            line_parsed = transformer.FileLineParser(line)
        except exception.LogInFileNotParsedError:
            continue
        log = log_model.Log(
            remote_addr=line_parsed.remote_addr,
            remote_user=line_parsed.remote_user,
            time_local=line_parsed.time_local,
            request=line_parsed.request,
            status=line_parsed.status,
            body_bytes_sent=line_parsed.body_bytes_sent,
            http_referer=line_parsed.http_referer,
            http_user_agent=line_parsed.http_user_agent,
        )
        result.append(log)
    return result


def get_remote_addrs_count_from_file(logs_path: str) -> List[log_model.RemoteAddrCount]:
    get_file_as_df = transformer.PandasParser(logs_path)
    logs_df = get_file_as_df()
    result = []
    remote_addrs_count_df = transformer.LogsAnalyzer(logs_df).get_remote_addr_count()
    for row in remote_addrs_count_df.iterrows():
        remote_addr_count_df = row[1]
        remote_addr_count = log_model.RemoteAddrCount(
            remote_addr=remote_addr_count_df["remote_addr"],
            count=remote_addr_count_df["count"],
        )
        result.append(remote_addr_count)
    return result
