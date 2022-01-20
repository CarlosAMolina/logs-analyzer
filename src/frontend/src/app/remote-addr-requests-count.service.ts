import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

import { HttpRequestPost } from './http-request';
import { HttpRequestService } from './http-request.service';
import { RemoteAddrRequestsCount } from './remote-addr-requests-count';

@Injectable({
  providedIn: 'root'
})
export class RemoteAddrRequestsCountService {

  constructor(
    private httpRequestService: HttpRequestService
  ) { }

  getRemoteAddrsRequestsCount(logPath: string): Observable<RemoteAddrRequestsCount[]> {
    const httpRequestPost: HttpRequestPost<RemoteAddrRequestsCount[]> = {
      bodyObject: { "logs-file": logPath },
      operation: 'getRemoteAddrsRequestsCount',
      responseDefault: [],
      service: 'RemoteAddrRequestsCountService',
      url: 'http://127.0.0.1:5000/remote-addrs-count',
    }
    return this.httpRequestService.getPostResults<RemoteAddrRequestsCount[]>(httpRequestPost);
  }

}
