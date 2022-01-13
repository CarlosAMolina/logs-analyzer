import { Component, OnInit } from '@angular/core';

import { RemoteAddrRequestsCount } from '../remote-addr-requests-count';
import { LogFile } from '../log-file';
import { LogFileService } from '../log-file.service';
import { RemoteAddrRequestsCountService } from '../remote-addr-requests-count.service';

@Component({
  selector: 'app-remote-addrs-requests-count',
  templateUrl: './remote-addrs-requests-count.component.html',
  styleUrls: ['./remote-addrs-requests-count.component.css']
})
export class RemoteAddrsRequestsCountComponent implements OnInit {
  remoteAddrsRequestsCount: RemoteAddrRequestsCount[] = [];

  constructor(private remoteAddrRequestsCountService: RemoteAddrRequestsCountService, public logFileService: LogFileService) { }

  ngOnInit(): void {
    this.getRemoteAddrsRequestsCountService();
  }

  getRemoteAddrsRequestsCountService(): void {
      // TODO use logFile.path
      this.remoteAddrRequestsCountService.getRemoteAddrsRequestsCount("a")
          .subscribe(remoteAddrsRequestsCount => this.remoteAddrsRequestsCount = remoteAddrsRequestsCount);
  }

}
