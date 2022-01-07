import { Injectable } from '@angular/core';

import { IpVtAnalysis } from './ip-vt-analysis';
import { IPS_VT_ANALYSIS } from './mock-ips-vt-analysis';

@Injectable({
  providedIn: 'root'
})
export class IpVtAnalysisService {
  getIpsVtAnalysis(): IpVtAnalysis[] {
    return IPS_VT_ANALYSIS;
  }

  constructor() { }
}
