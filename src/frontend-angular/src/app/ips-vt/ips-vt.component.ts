import { Component, OnInit } from '@angular/core';

import { IPS } from '../mock-ips';
import { IPS_VT_ANALYSIS } from '../mock-ips-vt-analysis';

@Component({
  selector: 'app-ips-vt',
  templateUrl: './ips-vt.component.html',
  styleUrls: ['./ips-vt.component.css']
})
export class IpsVtComponent implements OnInit {
  ips = IPS;
  ipsVTAnalysis = IPS_VT_ANALYSIS;

  constructor() { }

  ngOnInit(): void {
  }

}
