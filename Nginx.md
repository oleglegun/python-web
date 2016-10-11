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

### Config File


```nginx
user www-data;  # user that creates processes 
worker_processes 4; # good for 4 cores processor
pid /var/run/nginx.pid;

events {
    worker_connections 768;
    # multi_accept on;
}

http {
    # Basic Settings
    
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;
    # server_tokens off;
    
    server_names_hash_bucket_size 64;
    # server_name_in_redirect off;
    
    include /etc/nginx/mime.types;
    default_type application/octet-stream;
    
}
```

`www-data` is the user that will be created by nginx. To allow nginx
processing our files - we need to add group `www-data` to our files or
change their owner to `www-data` or add read right to all users.


