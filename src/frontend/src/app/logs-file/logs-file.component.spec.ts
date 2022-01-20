import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LogsFileComponent } from './logs-file.component';

describe('LogsFileComponent', () => {
  let component: LogsFileComponent;
  let fixture: ComponentFixture<LogsFileComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LogsFileComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LogsFileComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
