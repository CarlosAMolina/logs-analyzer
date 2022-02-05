import { catchError, tap } from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { HttpRequestPost } from './http-request';
import { MessageService } from './message.service';

@Injectable({
  providedIn: 'root'
})
export class HttpRequestService {
  private httpOptions = {
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

  getPostResults<T>(httpRequestPost: HttpRequestPost<T>): Observable<T> {
    const body = JSON.stringify(httpRequestPost.bodyObject);
    return this.http.post<T>(httpRequestPost.url, body, this.httpOptions)
      .pipe(
        tap((newData:T) => this.log(`fetched ${httpRequestPost.operation}`)),
        catchError(this.handleError<T>(httpRequestPost.service, httpRequestPost.operation, httpRequestPost.responseDefault ))
    );
  }

  private log(message: string) {
    this.messageService.add(message);
  }

  /**
   * Handle Http operation that failed.
   * Let the app continue.
   * @param service - name of the service that failed
   * @param operation - name of the operation that failed
   * @param result - optional value to return as the observable result
   */
  private handleError<T>(service: string, operation: string, result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // TODO: better job of transforming error for user consumption
      this.log(`${service}: [ERROR] ${operation} failed: ${error.message}`);

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }

}
