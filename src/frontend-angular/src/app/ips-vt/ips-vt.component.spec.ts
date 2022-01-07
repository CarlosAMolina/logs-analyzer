import { ComponentFixture, TestBed } from '@angular/core/testing';

import { IpsVtComponent } from './ips-vt.component';

describe('IpsVtComponent', () => {
  let component: IpsVtComponent;
  let fixture: ComponentFixture<IpsVtComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ IpsVtComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(IpsVtComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
