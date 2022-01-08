import { Injectable } from '@angular/core';

import { Log } from './log';
import { LOGS_ALL } from './mock-logs-all';


@Injectable({
  providedIn: 'root'
})
export class LogService {

  constructor() { }

  getLogs(): Log[] {
    return LOGS_ALL;
  }

}
