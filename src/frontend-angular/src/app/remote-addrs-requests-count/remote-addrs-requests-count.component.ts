import { Component, OnInit } from '@angular/core';

import { RemoteAddrRequestsCount } from '../remote-addr-requests-count';
import { LogFileService } from '../log-file.service';
import { RemoteAddrRequestsCountService } from '../remote-addr-requests-count.service';

@Component({
  selector: 'app-remote-addrs-requests-count',
  templateUrl: './remote-addrs-requests-count.component.html',
  styleUrls: ['./remote-addrs-requests-count.component.css']
})
export class RemoteAddrsRequestsCountComponent implements OnInit {
  remoteAddrsRequestsCount: RemoteAddrRequestsCount[] = [];
  logPath: any; // TODO change anys in the project to string

  constructor(private remoteAddrRequestsCountService: RemoteAddrRequestsCountService, private logFileService: LogFileService) { }

  ngOnInit(): void {
    this.getRemoteAddrsRequestsCountService();
    this.logPath=this.logFileService.logPath;
  }

  getRemoteAddrsRequestsCountService(): void {
      this.remoteAddrRequestsCountService.getRemoteAddrsRequestsCount()
          .subscribe(remoteAddrsRequestsCount => this.remoteAddrsRequestsCount = remoteAddrsRequestsCount);
  }

}
