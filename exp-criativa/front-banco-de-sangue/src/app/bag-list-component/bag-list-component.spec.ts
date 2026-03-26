import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BagListComponent } from './bag-list-component';

describe('BagListComponent', () => {
  let component: BagListComponent;
  let fixture: ComponentFixture<BagListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BagListComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BagListComponent);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
