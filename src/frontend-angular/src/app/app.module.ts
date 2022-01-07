import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { LogsPathComponent } from './logs-path/logs-path.component';
import { IpsVtComponent } from './ips-vt/ips-vt.component';
import { RemoteAddrsRequestsCountComponent } from './remote-addrs-requests-count/remote-addrs-requests-count.component';
import { LogsAllComponent } from './logs-all/logs-all.component';

@NgModule({
  declarations: [
    AppComponent,
    LogsPathComponent,
    IpsVtComponent,
    RemoteAddrsRequestsCountComponent,
    LogsAllComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
