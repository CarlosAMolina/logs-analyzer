import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

import { Log } from './log';
import { LOGS } from './mock-logs';


@Injectable({
  providedIn: 'root'
})
export class LogService {

  constructor() { }

  getLogs(): Observable<Log[]> {
    const logs = of(LOGS);
    return logs;
  }

}
