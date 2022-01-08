import { Component, OnInit } from '@angular/core';

import { Log } from '../log';
import { LogService } from '../log.service';
import { LOGS } from '../mock-logs';

@Component({
  selector: 'app-logs',
  templateUrl: './logs.component.html',
  styleUrls: ['./logs.component.css']
})
export class LogsComponent implements OnInit {
  logs: Log[] = [];

  constructor(private logService: LogService) { }

  ngOnInit(): void {
    this.getLogs();
  }

  getLogs(): void {
    this.logs = this.logService.getLogs();
  }

}
