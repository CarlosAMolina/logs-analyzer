import { Component, OnInit } from '@angular/core';

import { LogsPath } from '../logs-path';

@Component({
  selector: 'app-logs-path',
  templateUrl: './logs-path.component.html',
  styleUrls: ['./logs-path.component.css']
})
export class LogsPathComponent implements OnInit {
  errorMsg = 'Foo';
  logsPath: LogsPath = {value: '/tmp/access.log'};

  constructor() { }

  ngOnInit(): void {
  }

}
