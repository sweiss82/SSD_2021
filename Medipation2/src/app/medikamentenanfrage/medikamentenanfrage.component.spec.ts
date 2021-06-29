import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MedikamentenanfrageComponent } from './medikamentenanfrage.component';

describe('MedikamentenanfrageComponent', () => {
  let component: MedikamentenanfrageComponent;
  let fixture: ComponentFixture<MedikamentenanfrageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MedikamentenanfrageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MedikamentenanfrageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
