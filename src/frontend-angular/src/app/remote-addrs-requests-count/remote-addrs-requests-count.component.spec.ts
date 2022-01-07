import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RemoteAddrsRequestsCountComponent } from './remote-addrs-requests-count.component';

describe('RemoteAddrsRequestsCountComponent', () => {
  let component: RemoteAddrsRequestsCountComponent;
  let fixture: ComponentFixture<RemoteAddrsRequestsCountComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RemoteAddrsRequestsCountComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RemoteAddrsRequestsCountComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
