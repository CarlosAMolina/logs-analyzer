import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

import { HttpRequestPost } from './http-request';
import { HttpRequestService } from './http-request.service';
import { IpVtAnalysis } from './ip-vt-analysis';
import { MessageService } from './message.service';

@Injectable({
  providedIn: 'root'
})
export class IpVtAnalysisService {
  constructor(
    private httpRequestService: HttpRequestService
  ) { }

  getIpsVtAnalysis(ips: string[]): Observable<IpVtAnalysis[]> {
    const httpRequestPost: HttpRequestPost<IpVtAnalysis[]> = {
      bodyObject: { "ips": ips },
      operation: 'getIpsVtAnalysis',
      responseDefault: [],
      service: 'IpVtAnalysisService',
      url: 'http://127.0.0.1:5000/ips-vt',
    }
    return this.httpRequestService.getPostResults<IpVtAnalysis[]>(httpRequestPost);
  }
}
