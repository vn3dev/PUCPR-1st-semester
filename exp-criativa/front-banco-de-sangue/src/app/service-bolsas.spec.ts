import { TestBed } from '@angular/core/testing';

import { ServiceBolsas } from './service-bolsas';

describe('ServiceBolsas', () => {
  let service: ServiceBolsas;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ServiceBolsas);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
