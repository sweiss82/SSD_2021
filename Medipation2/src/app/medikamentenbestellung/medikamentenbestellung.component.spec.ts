import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MedikamentenbestellungComponent } from './medikamentenbestellung.component';

describe('MedikamentenbestellungComponent', () => {
  let component: MedikamentenbestellungComponent;
  let fixture: ComponentFixture<MedikamentenbestellungComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MedikamentenbestellungComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MedikamentenbestellungComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
