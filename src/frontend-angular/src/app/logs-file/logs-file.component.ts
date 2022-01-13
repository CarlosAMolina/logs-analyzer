import { Component, OnInit } from '@angular/core';

import { LogFile } from '../log-file';
import { LogFileService } from '../log-file.service';

@Component({
  selector: 'app-logs-file',
  templateUrl: './logs-file.component.html',
  styleUrls: ['./logs-file.component.css']
})
export class LogsFileComponent implements OnInit {
  logsPathInput = '/tmp/access.log';

  constructor(public logFileService: LogFileService) { }

  ngOnInit(): void {
    this.setLogPathForInput();
  }

  setLogPathForInput(): void {
    if (this.logFileService.logFile.path.length != 0 ) {
      this.logsPathInput = this.logFileService.logFile.path;
    }
  };

  setLogsFile(logFileInput: string): void {
    this.logFileService.isFile(logFileInput)
          .subscribe(isFileResult => {
              this.logFileService.logFile=isFileResult;
          }
    );
  }

}
