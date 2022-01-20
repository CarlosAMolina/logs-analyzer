import { TestBed } from '@angular/core/testing';

import { LogFileStorageService } from './log-file-storage.service';

describe('LogFileStorageService', () => {
  let service: LogFileStorageService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(LogFileStorageService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
