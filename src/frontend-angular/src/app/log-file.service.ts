import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

import { HttpRequestPost } from './http-request';
import { HttpRequestService } from './http-request.service';
import { LogFile } from './log-file';

@Injectable({
  providedIn: 'root'
})
export class LogFileService {
  private isFileUrl = 'http://127.0.0.1:5000/log-file-is-file';

  constructor(
    private httpRequestService: HttpRequestService
  ) { }

  isFile(logPath: string): Observable<LogFile> {
    const httpRequestPost: HttpRequestPost<LogFile> = {
      bodyObject: { "logs-file": logPath },
      operation: 'isFile',
      responseDefault: { isFile: false, path: logPath },
      service: 'LogFileService',
      url: this.isFileUrl,
    }
    return this.httpRequestService.getPostResults<LogFile>(httpRequestPost);
  }

}
