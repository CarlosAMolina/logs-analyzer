import { Injectable } from '@angular/core';

import { Log } from './log';
import { LOGS } from './mock-logs';


@Injectable({
  providedIn: 'root'
})
export class LogService {

  constructor() { }

  getLogs(): Log[] {
    return LOGS;
  }

}
