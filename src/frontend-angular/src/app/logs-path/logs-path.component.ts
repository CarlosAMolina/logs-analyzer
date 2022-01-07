import { Component, OnInit } from '@angular/core';

import { LogsFile } from '../logs-file';

@Component({
  selector: 'app-logs-path',
  templateUrl: './logs-path.component.html',
  styleUrls: ['./logs-path.component.css']
})
export class LogsPathComponent implements OnInit {
  errorMsg = 'ERROR. File not found: foo.log';
  logsFile: LogsFile = {path: '/tmp/access.log'};

  constructor() { }

  ngOnInit(): void {
  }

}
