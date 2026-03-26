import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DonorListComponent } from './donor-list-component';

describe('DonorListComponent', () => {
  let component: DonorListComponent;
  let fixture: ComponentFixture<DonorListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DonorListComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DonorListComponent);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
