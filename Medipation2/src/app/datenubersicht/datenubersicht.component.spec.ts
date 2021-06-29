import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DatenubersichtComponent } from './datenubersicht.component';

describe('DatenubersichtComponent', () => {
  let component: DatenubersichtComponent;
  let fixture: ComponentFixture<DatenubersichtComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DatenubersichtComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DatenubersichtComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
