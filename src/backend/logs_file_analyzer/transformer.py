from typing import List
import collections

from ...api.models import log as log_model


def get_remote_addrs_count(
    logs: List[log_model.Log],
) -> List[log_model.RemoteAddrCount]:
    remote_addrs = [log.remote_addr for log in logs]
    remote_addrs_count = dict(collections.Counter(remote_addrs))
    remote_addrs_count_sorted = dict(
        sorted(remote_addrs_count.items(), key=lambda item: item[1], reverse=True)
    )
    return [
        log_model.RemoteAddrCount(
            remote_addr=remote_addr,
            count=count,
        )
        for remote_addr, count in remote_addrs_count_sorted.items()
    ]
