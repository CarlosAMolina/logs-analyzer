import { Component, OnInit } from '@angular/core';

import { Log } from '../log';
import { LogFileStorageService } from '../log-file-storage.service';
import { LogService } from '../log.service';

@Component({
  selector: 'app-logs',
  templateUrl: './logs.component.html',
  styleUrls: ['./logs.component.css']
})
export class LogsComponent implements OnInit {
  logs: Log[] = [];

  constructor(private logService: LogService, public logFileStorageService: LogFileStorageService) { }

  ngOnInit(): void {
    this.getLogs();
  }

  getLogs(): void {
    this.logService.getLogs(this.logFileStorageService.logFile.path)
        .subscribe(logs => this.logs = logs);
  }

}
