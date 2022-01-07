import { Component, OnInit } from '@angular/core';

import { REMOTE_ADDRS_REQUESTS_COUNT } from '../mock-remote-addrs-requests-count';

@Component({
  selector: 'app-remote-addrs-requests-count',
  templateUrl: './remote-addrs-requests-count.component.html',
  styleUrls: ['./remote-addrs-requests-count.component.css']
})
export class RemoteAddrsRequestsCountComponent implements OnInit {

  remoteAddrsRequestsCount = REMOTE_ADDRS_REQUESTS_COUNT

  constructor() { }

  ngOnInit(): void {
  }

}
