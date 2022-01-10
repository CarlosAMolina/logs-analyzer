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
  errorMsg = 'ERROR. File not found: foo.log';
  logFileDefault: LogFile = LOG_FILE;
  logFile: string = '';

  constructor(private logFileService: LogFileService) { }

  ngOnInit(): void {
    this.getLogsFile();
  }

  getLogsFile(): void {
    this.logFileService.getLogsFile();
  }

}
