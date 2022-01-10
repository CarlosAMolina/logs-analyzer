import { Injectable } from '@angular/core';

import { LogFile } from './log-file';
import { MessageService } from './message.service';

@Injectable({
  providedIn: 'root'
})
export class LogFileService {

  constructor(private messageService: MessageService) { }

  isFile(logFile: string): boolean {
    // TODO not mock
    const result = true;
    this.messageService.add(`LogsFileService: isFile ${JSON.stringify(logFile)} ${result}`);
    return result;
  }

}
