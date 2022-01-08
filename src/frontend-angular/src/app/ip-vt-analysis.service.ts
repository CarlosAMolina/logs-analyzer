import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

import { IpVtAnalysis } from './ip-vt-analysis';
import { IPS_VT_ANALYSIS } from './mock-ips-vt-analysis';

@Injectable({
  providedIn: 'root'
})
export class IpVtAnalysisService {
  getIpsVtAnalysis(): Observable<IpVtAnalysis[]> {
    const ipsVtAnalysis = of(IPS_VT_ANALYSIS);
    return ipsVtAnalysis;
  }

  constructor() { }
}
