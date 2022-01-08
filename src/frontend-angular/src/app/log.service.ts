import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

import { Log } from './log';
import { LOGS } from './mock-logs';
import { MessageService } from './message.service';

@Injectable({
  providedIn: 'root'
})
export class LogService {

  constructor(private messageService: MessageService) { }

  getLogs(): Observable<Log[]> {
    const logs = of(LOGS);
    this.messageService.add('LogsService: fetched logs');
    return logs;
  }

}
