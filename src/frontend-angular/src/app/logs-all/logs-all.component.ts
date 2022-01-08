import { Component, OnInit } from '@angular/core';

import { Log } from '../log';
import { LogService } from '../log.service';
import { LOGS } from '../mock-logs';

@Component({
  selector: 'app-logs-all',
  templateUrl: './logs-all.component.html',
  styleUrls: ['./logs-all.component.css']
})
export class LogsAllComponent implements OnInit {
  logs: Log[] = [];

  constructor(private logService: LogService) { }

  ngOnInit(): void {
    this.getLogs();
  }

  getLogs(): void {
    this.logs = this.logService.getLogs();
  }

}
