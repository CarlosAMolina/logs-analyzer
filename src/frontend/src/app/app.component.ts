import { Component } from '@angular/core';

import { LogFileStorageService } from './log-file-storage.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Logs Analyzer';

  constructor(public logFileStorageService: LogFileStorageService) { }

  ngOnInit(): void {
  }
}
