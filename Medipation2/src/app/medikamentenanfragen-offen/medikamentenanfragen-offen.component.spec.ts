import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MedikamentenanfragenOffenComponent } from './medikamentenanfragen-offen.component';

describe('MedikamentenanfragenOffenComponent', () => {
  let component: MedikamentenanfragenOffenComponent;
  let fixture: ComponentFixture<MedikamentenanfragenOffenComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MedikamentenanfragenOffenComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MedikamentenanfragenOffenComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
