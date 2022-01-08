import { Component, OnInit } from '@angular/core';

import { RemoteAddrRequestsCount } from '../remote-addr-requests-count';
import { RemoteAddrRequestsCountService } from '../remote-addr-requests-count.service';

@Component({
  selector: 'app-remote-addrs-requests-count',
  templateUrl: './remote-addrs-requests-count.component.html',
  styleUrls: ['./remote-addrs-requests-count.component.css']
})
export class RemoteAddrsRequestsCountComponent implements OnInit {
  remoteAddrsRequestsCount: RemoteAddrRequestsCount[] = [];

  constructor(private remoteAddrRequestsCountService: RemoteAddrRequestsCountService) { }

  ngOnInit(): void {
    this.getRemoteAddrsRequestsCountService();
  }

  getRemoteAddrsRequestsCountService(): void {
      this.remoteAddrRequestsCountService.getRemoteAddrsRequestsCount()
          .subscribe(remoteAddrsRequestsCount => this.remoteAddrsRequestsCount = remoteAddrsRequestsCount);
  }

}
