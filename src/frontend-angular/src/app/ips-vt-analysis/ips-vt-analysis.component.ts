import { Component, OnInit } from '@angular/core';

import { IPS } from '../mock-ips';
import { IpVtAnalysis } from '../ip-vt-analysis';
import { IpVtAnalysisService } from '../ip-vt-analysis.service';

@Component({
  selector: 'app-ips-vt-analysis',
  templateUrl: './ips-vt-analysis.component.html',
  styleUrls: ['./ips-vt-analysis.component.css']
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
