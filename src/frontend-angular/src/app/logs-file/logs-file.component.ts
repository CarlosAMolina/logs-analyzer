import { Component, OnInit } from '@angular/core';

import { LogFile } from '../log-file';
import { LogFileService } from '../log-file.service';

@Component({
  selector: 'app-logs-file',
  templateUrl: './logs-file.component.html',
  styleUrls: ['./logs-file.component.css']
})
export class LogsFileComponent implements OnInit {
  logFile: LogFile = {isFile: false, path: ''};

  constructor(private logFileService: LogFileService) { }

  ngOnInit(): void {
  }

  setLogsFile(logFileInput: string): void {
    this.logFileService.isFile(logFileInput)
          .subscribe(isFileResult => {
                this.logFile = isFileResult;
          }
    );
  }

}
