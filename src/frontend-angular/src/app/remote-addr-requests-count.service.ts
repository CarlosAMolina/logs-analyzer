import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

import { RemoteAddrRequestsCount } from './remote-addr-requests-count';
import { REMOTE_ADDRS_REQUESTS_COUNT } from './mock-remote-addrs-requests-count';
import { MessageService } from './message.service';

@Injectable({
  providedIn: 'root'
})
export class RemoteAddrRequestsCountService {

  constructor(private messageService: MessageService) { }

  getRemoteAddrsRequestsCount(): Observable<RemoteAddrRequestsCount[]> {
    const remoteAddrRequestsCount = of(REMOTE_ADDRS_REQUESTS_COUNT);
    this.messageService.add('RemoteAddrRequestsCountService: fetched remoteAddrRequestsCount');
    return remoteAddrRequestsCount;
  }

}
