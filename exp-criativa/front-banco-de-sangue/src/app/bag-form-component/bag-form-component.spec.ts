import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BagFormComponent } from './bag-form-component';

describe('BagFormComponent', () => {
  let component: BagFormComponent;
  let fixture: ComponentFixture<BagFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BagFormComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BagFormComponent);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
