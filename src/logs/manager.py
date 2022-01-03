from typing import List

from ..models.log import Log
from . import exception
from . import extractor
from . import transformer


def get_logs_from_file(file: str) -> List[Log]:
    result = []
    for line in extractor.FileExtractor(file).get_lines_in_file():
        try:
            line_parsed = transformer.FileLineParser(line)
        except exception.LogInFileNotParsedError:
            continue
        log = Log(
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
