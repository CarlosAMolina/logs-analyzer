import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LogsPathComponent } from './logs-path.component';

describe('LogsPathComponent', () => {
  let component: LogsPathComponent;
  let fixture: ComponentFixture<LogsPathComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LogsPathComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LogsPathComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
