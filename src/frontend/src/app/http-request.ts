export interface HttpRequestPost<T> {
  bodyObject: object;
  operation: string;
  responseDefault: T;
  service: string;
  url: string;
}
