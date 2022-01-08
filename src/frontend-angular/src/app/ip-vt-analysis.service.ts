import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

import { IpVtAnalysis } from './ip-vt-analysis';
import { IPS_VT_ANALYSIS } from './mock-ips-vt-analysis';
import { MessageService } from './message.service';

@Injectable({
  providedIn: 'root'
})
export class IpVtAnalysisService {
  constructor(private messageService: MessageService) { }

  getIpsVtAnalysis(): Observable<IpVtAnalysis[]> {
    const ipsVtAnalysis = of(IPS_VT_ANALYSIS);
    this.messageService.add('IpVtAnalysisService: fetched ipsVtAnalysis');
    return ipsVtAnalysis;
  }
}
