import { TestBed } from '@angular/core/testing';

import { MedikamentenbestellungService } from './medikamentenbestellung.service';

describe('MedikamentenbestellungService', () => {
  let service: MedikamentenbestellungService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MedikamentenbestellungService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
