import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LogsAllComponent } from './logs-all.component';

describe('LogsAllComponent', () => {
  let component: LogsAllComponent;
  let fixture: ComponentFixture<LogsAllComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LogsAllComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LogsAllComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
