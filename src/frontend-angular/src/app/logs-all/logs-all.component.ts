import { Component, OnInit } from '@angular/core';

import { LOGS_ALL } from '../mock-logs-all';

@Component({
  selector: 'app-logs-all',
  templateUrl: './logs-all.component.html',
  styleUrls: ['./logs-all.component.css']
})
export class LogsAllComponent implements OnInit {
  logsAll = LOGS_ALL;

  constructor() { }

  ngOnInit(): void {
  }

}
