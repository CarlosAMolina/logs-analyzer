import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

import { RemoteAddrRequestsCount } from './remote-addr-requests-count';
import { REMOTE_ADDRS_REQUESTS_COUNT } from './mock-remote-addrs-requests-count';

@Injectable({
  providedIn: 'root'
})
export class RemoteAddrRequestsCountService {

  constructor() { }

  getRemoteAddrsRequestsCount(): Observable<RemoteAddrRequestsCount[]> {
    const remoteAddrRequestsCount = of(REMOTE_ADDRS_REQUESTS_COUNT);
    return remoteAddrRequestsCount;
  }

}
