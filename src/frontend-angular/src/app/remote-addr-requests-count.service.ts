import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { RemoteAddrRequestsCount } from './remote-addr-requests-count';
import { MessageService } from './message.service';

@Injectable({
  providedIn: 'root'
})
export class RemoteAddrRequestsCountService {
  private remoteAddrRequestsCountUrl = 'http://127.0.0.1:5000/remote-addrs-count';

  httpOptions = {
    headers: new HttpHeaders(
      {
        'content-type': 'application/json',
      }
    )
  };

  constructor(
    private http: HttpClient,
    private messageService: MessageService
  ) { }

  private log(message: string) {
    this.messageService.add(`RemoteAddrRequestsCountService: ${message}`);
  }

  getRemoteAddrsRequestsCount(): Observable<RemoteAddrRequestsCount[]> {
    // TODO not use mocked value
    const bodyObject = {  
      "logs-file": "/tmp/access.log"
    };  
    const body = JSON.stringify(bodyObject);
    return this.http.post<RemoteAddrRequestsCount[]>(this.remoteAddrRequestsCountUrl, body, this.httpOptions)
      .pipe(
        tap((newData: RemoteAddrRequestsCount[]) => this.log(`fetched remoteAddrRequestsCount. Value=${newData}`)),
        catchError(this.handleError<RemoteAddrRequestsCount[]>('getRemoteAddrsRequestsCount', []))
    );
  }

  /**
   * Handle Http operation that failed.
   * Let the app continue.
   * @param operation - name of the operation that failed
   * @param result - optional value to return as the observable result
   */
  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
  
      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead
  
      // TODO: better job of transforming error for user consumption
      this.log(`[ERROR] ${operation} failed: ${error.message}`);
  
      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }

}
