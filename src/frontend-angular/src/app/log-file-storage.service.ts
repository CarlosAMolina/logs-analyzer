import { Injectable } from '@angular/core';

import { LogFile } from './log-file';

@Injectable({
  providedIn: 'root'
})
export class LogFileStorageService {
  logFile: LogFile = {isFile: false, path: ''};

  constructor() { }

  hasDefaultValues(): boolean {
    return this.logFile.isFile === false && this.logFile.path !== '';
  }

  hasPath(): boolean {
    return this.logFile.path.length != 0;
  }

  // TODO create setPath(path: string) and remove blank spaces at beginning and end of the path
}
