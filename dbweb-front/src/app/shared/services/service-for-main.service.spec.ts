import { TestBed } from '@angular/core/testing';

import { ServiceForMainService } from './service-for-main.service';

describe('ServiceForMainService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: ServiceForMainService = TestBed.get(ServiceForMainService);
    expect(service).toBeTruthy();
  });
});
