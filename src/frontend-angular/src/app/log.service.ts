import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

import { HttpRequestPost } from './http-request';
import { HttpRequestService } from './http-request.service';
import { Log } from './log';

@Injectable({
  providedIn: 'root'
})
export class LogService {

  constructor(
    private httpRequestService: HttpRequestService
  ) { }

  getLogs(logPath: string): Observable<Log[]> {
    const httpRequestPost: HttpRequestPost<Log[]> = {
      bodyObject: { "logs-file": logPath },
      operation: 'getLogs',
      responseDefault: [],
      service: 'LogService',
      url: 'http://127.0.0.1:5000/logs',
    }
    return this.httpRequestService.getPostResults<Log[]>(httpRequestPost);
  }

}
