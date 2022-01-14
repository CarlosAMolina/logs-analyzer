import { Injectable } from '@angular/core';

import { LogFile } from './log-file';

@Injectable({
  providedIn: 'root'
})
export class LogFileStorageService {
  logFile: LogFile = {isFile: false, path: ''};

  constructor() { }
}
