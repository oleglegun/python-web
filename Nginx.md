# Nginx

### Important files

| Action                           | Dir                         |
|:---------------------------------|:----------------------------|
| Config                           | `/etc/nginx/nginx.conf`     |
| Run script                       | `/etc/init.d/nginx`         |
| PID-file (int for kill, restart) | `/var/run/nginx.pid`        |
| Access-log                       | `/var/log/nginx/access.log` |
| Error-log                        | `/var/log/nginx/error.log`  |

### Processes on Web Server
1. Master (demon)
    * Read/Validate config
    * Open socket
    * Open log files
    * Create child processes (workers)
    * Graceful Restart
2. Worker (www-data, 1+ processes)
    * Process incoming connections




