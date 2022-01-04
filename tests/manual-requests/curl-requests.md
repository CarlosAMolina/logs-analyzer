```bash
curl -i -X POST localhost:5000/logs-all -H "Content-Type: application/json" -d '{"logs-path": "/tmp/access.log"}'
curl -i -X POST localhost:5000/remote-addrs-count -H "Content-Type: application/json" -d '{"logs-path": "/tmp/access.log"}'
```
