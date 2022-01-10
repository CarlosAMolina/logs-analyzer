import { Injectable } from '@angular/core';

import { LogFile } from './log-file';
import { LOG_FILE } from './mock-log-file';
import { MessageService } from './message.service';

@Injectable({
  providedIn: 'root'
})
export class LogFileService {

  constructor(private messageService: MessageService) { }

  getLogsFile(): LogFile {
    // TODO not mock
    const logsFile = LOG_FILE;
    this.messageService.add(`LogsFileService: fetched logs-file ${JSON.stringify(logsFile)}`);
    return logsFile;
  }

}
