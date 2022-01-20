import { TestBed } from '@angular/core/testing';

import { RemoteAddrRequestsCountService } from './remote-addr-requests-count.service';

describe('RemoteAddrRequestsCountService', () => {
  let service: RemoteAddrRequestsCountService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RemoteAddrRequestsCountService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
