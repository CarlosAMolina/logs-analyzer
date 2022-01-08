import { Injectable } from '@angular/core';

import { RemoteAddrRequestsCount } from './remote-addr-requests-count';
import { REMOTE_ADDRS_REQUESTS_COUNT } from './mock-remote-addrs-requests-count';

@Injectable({
  providedIn: 'root'
})
export class RemoteAddrRequestsCountService {

  constructor() { }

  getRemoteAddrsRequestsCountService(): RemoteAddrRequestsCount[] {
    return REMOTE_ADDRS_REQUESTS_COUNT;
  }

}
