export interface Log {
  blocked?: boolean;
  checkedVt?: boolean;
  remoteAddr: string;
  remoteUser: string;
  timeLocal: string;
  request: string;
  status: number;
  bodyBytesSent: number;
  httpReferer: string;
  httpUserAgent: string;
}
