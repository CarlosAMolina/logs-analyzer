import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LogsPathComponent } from './logs-path/logs-path.component';
import { RemoteAddrsRequestsCountComponent } from './remote-addrs-requests-count/remote-addrs-requests-count.component';
import { IpsVtAnalysisComponent } from './ips-vt-analysis/ips-vt-analysis.component';
import { LogsComponent } from './logs/logs.component';

const routes: Routes = [
  { path: '', redirectTo: '/logs-path', pathMatch: 'full' },
  { path: 'ips-vt-analysis', component: IpsVtAnalysisComponent },
  { path: 'logs', component: LogsComponent },
  { path: 'logs-path', component: LogsPathComponent },
  { path: 'remote-addrs-requests-count', component: RemoteAddrsRequestsCountComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
