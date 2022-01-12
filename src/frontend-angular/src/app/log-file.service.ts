import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { LogFile } from './log-file';
import { MessageService } from './message.service';

@Injectable({
  providedIn: 'root'
})
export class LogFileService {
  private isFileUrl = 'http://127.0.0.1:5000/log-file-is-file';

  // TODO refactor extract HTTP code used by other modules too code to a common module

  httpOptions = {
    headers: new HttpHeaders(
      {
        'content-type': 'application/json',
      }
    )
  };

  logPath: any; // TODO replace anys to str

  constructor(
    private http: HttpClient,
    private messageService: MessageService
  ) { }

  private log(message: string) {
    this.messageService.add(`LogFileService: ${message}`);
  }

  isFile(logPath: string): Observable<LogFile> {
    const bodyObject = {  
      path: logPath
    };  
    const body = JSON.stringify(bodyObject);
    return this.http.post<LogFile>(this.isFileUrl, body, this.httpOptions)
      .pipe(
        tap((newData:LogFile) => this.log(`fetched isFile. Value=${JSON.stringify(newData)}`)),
        catchError(this.handleError<LogFile>('isFile', { isFile: false, path: logPath } ))
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
