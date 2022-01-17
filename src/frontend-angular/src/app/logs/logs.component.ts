import { Component, OnInit } from '@angular/core';

import { Log } from '../log';
import { LogFileStorageService } from '../log-file-storage.service';
import { LogService } from '../log.service';

@Component({
  selector: 'app-logs',
  templateUrl: './logs.component.html',
  styleUrls: ['./logs.component.css']
})
export class LogsComponent implements OnInit {
  logs: Log[] = [];

  constructor(private logService: LogService, public logFileStorageService: LogFileStorageService) { }

  ngOnInit(): void {
    this.getLogs();
  }

  getLogs(): void {
    this.logService.getLogs(this.logFileStorageService.logFile.path)
        .subscribe(logs => this.logs = logs);
  }

  getStringShortenedAsHtml(value: string): string {
    const maxLength = 50;
    let result = '';
    if (value.length < maxLength) {
        result = `<td>${value}</td>`;
    } else {
        result = `<td>${value.slice(0, maxLength)} <a href="${value}" title="${value}">(hover for full log)</a> </td>`;
    }
    return result;
  }

  getVtAnalysis() {
    const ips = this.getIpsToAnalyzeInVt();
    // TODO continue here
    console.log('VT checked:'); // TODO delete
    console.log(ips); // TODO delete
  }

  private getIpsToAnalyzeInVt(): string[] {
    const result = this.logs.filter(this.isVtChecked).map(log => {
        return log.remoteAddr
    });
    return [...new Set(result)];
  }

  private isVtChecked(log: Log): boolean {
    return log.checkedVt === true;
  }

}
