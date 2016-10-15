# Nginx

### Important files

| Action                           |             Dir             |
|:---------------------------------|:---------------------------:|
| Config                           |   `/etc/nginx/nginx.conf`   |
| Run script                       |     `/etc/init.d/nginx`     |
| PID-file (int for kill, restart) |    `/var/run/nginx.pid`     |
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

### Server modules

| Name             | Description                                                       |
|:-----------------|:------------------------------------------------------------------|
| `mod_mime`       | Determine MIME type from file .extension                          |
| `mod_mime_magic` | Determine MIME type from file signature (first n bytes)           |
| `mod_autoindex`  | Generates files list if request was not to file, but to `folder/` |
| `mod_rewrite`    | Changes URL while processing request                              |
| `mod_gzip`       | Compresses files                                                  |

### Config File


```nginx
user www-data;  # user that creates processes 
worker_processes 4; # good for 4 cores processor
pid /var/run/nginx.pid;

events {
    worker_connections 768;
    # multi_accept on;
}

# Configure nginx to work w/ HTTP Protocol
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
    default_type application/octet-stream;  # Default MIME type
    
    # Logging Settings
    
    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;
    
    gzip on;
    gzip_disable "msie6";

    # Virtual Host Configs

    include /etc/nginx/conf.d/*.conf;  # Read all .conf files
    include /etc/nginx/sites-enabled/*;
}
```

`www-data` is the user that will be created by nginx. To allow nginx
processing our files - we need to add group `www-data` to our files or
change their owner to `www-data` or add read right to all users.

`error_log` contains all errors.

Folder `conf.d/` contain all virtual hosts like `yandex.conf`,
`legunpro.conf`...

### Example of .conf file

```nginx
upstream test {
    server 127.0.0.1:8003;  # Application server works on port 8003
}

# Virtual host#1 settings
server {
    server_name test.legun.pro www.test.legun.pro;  # must be the same in the HTTP domain
    listen 80;
    client_max_body_size 32m;

    location / {  # any URI
        proxy_pass http://test;  # redirect all requests to upstream and then send back reply from it
        # We change HTTP headers Host and X-Real-IP
        proxy_set_header Host test.legun.pro;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_read_timeout 60s;
    }

    location /static/ {
        alias /home/oleglegun/test/collected_static/;
    }

    location /media/ {
        proxy_set_header Host webdav.test.legun.pro;
        proxy_pass http://webdav.test.legun.pro;
    }
    
    location ~* ^.+\.(jpg|jpeg|gif)$ {  # ~* RegExp
        root       /www/images;  # Seach URLs here
        access_log off;
        expires    30d;
    }
}

# Virtual host#2 settings
server {
    server_name webdav.test.legun.pro;

    location /media/{ 
        access_log off;
        alias /home/oleglegun/test/webdav/;
    }

    location /webdav/ {
        alias /home/oleglegun/test/webdav/;
        dav_methods PUT DELETE MKCOL COPY MOVE;
        create_full_put_path on;
        dav_access group:rw all:rw;
    }

}
```

### Serving static files w/ `location`

| nginx `location` directive | Priority | Meaning                       | Match example |
|:---------------------------|:--------:|:------------------------------|:--------------|
| `location = /img/1.jpg`    |   ^^^^   | `=` Exact match               | `/img/1.jpg`  |
| `location /img/`           |    ^     | URI prefix match              | `/img/2.gif`  |
| `location ~* \.jpg$`       |    ^^    | `~*` RegExp match             | `/img/2.jpg`  |
| `location ^~ /pic/`        |   ^^^    | `!important` for prefix match | `/pic/1.jpg`  |


```nginx
location ~* ^.+\.(jpg|jpeg|gif)$ {
    root /www/images;  # Appends to URL
}
location /sitemap/ {
    alias /home/www/generated;  # Replaces URL, alias works only w/ prefix
}
```

`/2016/10/asdf34.jpg` -> `/www/images/2015/10/asdf34.jpg`  
`/sitemap/index.xml` -> `/home/www/generated/index.xml`

---

**Nginx** serves static content like images, css... **Nginx** proxies
other requests to the **Application Server** like **Django**. **Nginx**
can implement load balancing between Application Servers in `upstream`
section.

All requests that don't go to locations `/media/` or `/static/` go to
`/`.

| Command                               | Action             |
|:--------------------------------------|:-------------------|
| `sudo nginx`                          | Start server       |
| `sudo nginx -s stop`                  | Stop server        |
| `vim /usr/local/etc/nginx/nginx.conf` | Edit configuration |
