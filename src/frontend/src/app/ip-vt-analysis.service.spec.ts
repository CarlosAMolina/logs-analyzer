import { TestBed } from '@angular/core/testing';

import { IpVtAnalysisService } from './ip-vt-analysis.service';

describe('IpVtAnalysisService', () => {
  let service: IpVtAnalysisService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(IpVtAnalysisService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
