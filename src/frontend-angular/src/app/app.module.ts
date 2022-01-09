import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { LogsPathComponent } from './logs-path/logs-path.component';
import { IpsVtAnalysisComponent } from './ips-vt-analysis/ips-vt-analysis.component';
import { RemoteAddrsRequestsCountComponent } from './remote-addrs-requests-count/remote-addrs-requests-count.component';
import { LogsComponent } from './logs/logs.component';
import { MessagesComponent } from './messages/messages.component';
import { AppRoutingModule } from './app-routing.module';

@NgModule({
  declarations: [
    AppComponent,
    LogsPathComponent,
    IpsVtAnalysisComponent,
    RemoteAddrsRequestsCountComponent,
    LogsComponent,
    MessagesComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
