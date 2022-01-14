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

  constructor(private logFileService: LogFileService, public logFileStorageService: LogFileStorageService) { }

  ngOnInit(): void {
    this.setLogPathForInput();
  }

  // TODO rename to setLogPathInput
  setLogPathForInput(): void {
    if ( this.logFileStorageService.hasPath() ) {
      this.logsPathInput = this.logFileStorageService.logFile.path;
    }
  };

  setLogsFile(logFileInput: string): void {
    this.logFileService.isFile(logFileInput)
          .subscribe(isFileResult => {
              this.logFileStorageService.logFile=isFileResult;
          }
    );
  }

}
