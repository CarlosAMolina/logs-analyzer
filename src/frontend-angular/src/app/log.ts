export interface Log {
  remoteAddr: string;
  remoteUser: string;
  timeLocal: string;
  request: string;
  status: number;
  bodyBytesSent: number;
  httpReferer: string;
  httpUserAgent: string;
  checkedVt?: boolean;
}
