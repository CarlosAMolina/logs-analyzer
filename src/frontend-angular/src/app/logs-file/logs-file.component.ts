import { Component, OnInit } from '@angular/core';

import { LogFile } from '../log-file';
import { LogFileService } from '../log-file.service';
import { LOG_FILE } from '../mock-log-file';

@Component({
  selector: 'app-logs-file',
  templateUrl: './logs-file.component.html',
  styleUrls: ['./logs-file.component.css']
})
export class LogsFileComponent implements OnInit {
  errorMsg = '';
  logFile: LogFile = LOG_FILE;

  constructor(private logFileService: LogFileService) { }

  ngOnInit(): void {
  }

  setLogsFile(logFileNew: string): void {
    const exists = this.logFileService.isFile(logFileNew);
    if (exists) {
      this.logFile = { path: logFileNew };
    }
    else {
      this.errorMsg = `ERROR. File not found: ${logFileNew}`;
    }
  }

}
