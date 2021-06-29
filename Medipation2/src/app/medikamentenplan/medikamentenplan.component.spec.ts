import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MedikamentenplanComponent } from './medikamentenplan.component';

describe('MedikamentenplanComponent', () => {
  let component: MedikamentenplanComponent;
  let fixture: ComponentFixture<MedikamentenplanComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MedikamentenplanComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MedikamentenplanComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
