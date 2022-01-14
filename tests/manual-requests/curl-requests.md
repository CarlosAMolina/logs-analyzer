```bash
curl -i -X POST localhost:5000/log-file-is-file -H "Content-Type: application/json" -d '{"logs-file": "/tmp/access.log"}'
curl -i -X POST localhost:5000/logs-all -H "Content-Type: application/json" -d '{"logs-file": "/tmp/access.log"}'
curl -i -X POST localhost:5000/remote-addrs-count -H "Content-Type: application/json" -d '{"logs-file": "/tmp/access.log"}'
curl -i -X POST localhost:5000/ips-vt -H "Content-Type: application/json" -d '{"ips": ["8.8.8.8", "8.8.4.4"]}'
```
