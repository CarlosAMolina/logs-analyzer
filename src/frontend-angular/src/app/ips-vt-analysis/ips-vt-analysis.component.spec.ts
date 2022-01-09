import { ComponentFixture, TestBed } from '@angular/core/testing';

import { IpsVtAnalysisComponent } from './ips-vt-analysis.component';

describe('IpsVtAnalysisComponent', () => {
  let component: IpsVtAnalysisComponent;
  let fixture: ComponentFixture<IpsVtAnalysisComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ IpsVtAnalysisComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(IpsVtAnalysisComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
