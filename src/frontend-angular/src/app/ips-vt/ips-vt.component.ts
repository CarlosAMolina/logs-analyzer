import { Component, OnInit } from '@angular/core';

import { IPS } from '../mock-ips';
import { IpVtAnalysis } from '../ip-vt-analysis';
import { IpVtAnalysisService } from '../ip-vt-analysis.service';

@Component({
  selector: 'app-ips-vt',
  templateUrl: './ips-vt.component.html',
  styleUrls: ['./ips-vt.component.css']
})
export class IpsVtComponent implements OnInit {
  ips = IPS;
  ipsVtAnalysis: IpVtAnalysis[] = [];

  constructor(
    private ipVtAnalysisService: IpVtAnalysisService
  ) { }

  ngOnInit(): void {
    this.getIpsVtAnalysis();
  }

  getIpsVtAnalysis(): void {
    this.ipsVtAnalysis = this.ipVtAnalysisService.getIpsVtAnalysis();
  }

}
