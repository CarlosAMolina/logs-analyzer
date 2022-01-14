import { Component, OnInit } from '@angular/core';

import { LogFile } from '../log-file';
import { LogFileService } from '../log-file.service';
import { LogFileStorageService } from '../log-file-storage.service';

@Component({
  selector: 'app-logs-file',
  templateUrl: './logs-file.component.html',
  styleUrls: ['./logs-file.component.css']
})
export class LogsFileComponent implements OnInit {
  logsPathInput = '/tmp/access.log';
  errorMsg = '';

  constructor(private logFileService: LogFileService, public logFileStorageService: LogFileStorageService) { }

  ngOnInit(): void {
    this.setLogPathInput();
  }

  setLogPathInput(): void {
    if ( this.logFileStorageService.hasPath() ) {
      this.logsPathInput = this.logFileStorageService.logFile.path;
    }
  };

  setLogsFile(logFileInput: string): void {
    logFileInput = logFileInput.trim();
    this.logFileService.isFile(logFileInput)
          .subscribe(logFileResult => {
              this.setErrorMsg(logFileResult);
              if (logFileResult.isFile) {
                this.logFileStorageService.logFile=logFileResult;
              }
          }
    );
  }

  setErrorMsg(logFile: LogFile): void {
    if (!logFile.path.length) {
        this.errorMsg = 'ERROR. Empty path provided';
    } else if (!logFile.isFile) {
        this.errorMsg = `ERROR. File not found: ${logFile.path}`;
    } else {
        this.errorMsg = '';
    }
  }

}
