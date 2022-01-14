import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Log } from './log';
import { MessageService } from './message.service';

@Injectable({
  providedIn: 'root'
})
export class LogService {
  private logsUrl = 'http://127.0.0.1:5000/logs';

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

  getLogs(logsFile: string): Observable<Log[]> {
    const bodyObject = {  
      "logs-file": logsFile 
    };  
    const body = JSON.stringify(bodyObject);
    return this.http.post<Log[]>(this.logsUrl, body, this.httpOptions)
      .pipe(
        tap((newData: Log[]) => this.log(`fetched logs. Total elements fetched = ${Object.keys(newData).length}`)),
        catchError(this.handleError<Log[]>('getLogs', []))
    );
  }

  // TODO refactor extract common http functions to other script
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
