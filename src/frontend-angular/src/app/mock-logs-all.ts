import { Log } from './log';

export const LOGS_ALL: Log[] = [
  {
    remoteAddr: "8.8.8.8",
    remoteUser: "user 1",
    timeLocal: "2021-12-06 00:39:14+01:00",
    request: "GET / HTTP/1.1",
    status: 200,
    bodyBytesSent: 300,
    httpReferer: "-",
    httpUserAgent: "user agent 1",
  },
  {
    remoteAddr: "8.8.4.4",
    remoteUser: "user 2",
    timeLocal: "2021-12-06 00:40:14+01:00",
    request: "GET 2 / HTTP/1.1",
    status: 202,
    bodyBytesSent: 302,
    httpReferer: "referer 2",
    httpUserAgent: "user agent 2",
  },
  {
    remoteAddr: "8.8.8.8",
    remoteUser: "user 3",
    timeLocal: "2021-12-06 00:41:14+01:00",
    request: "GET 3 / HTTP/1.1",
    status: 203,
    bodyBytesSent: 303,
    httpReferer: "referer 3",
    httpUserAgent: "user agent 3",
  },
];

