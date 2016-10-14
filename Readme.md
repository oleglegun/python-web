# Python 2 web scripts

### Usage

Start web server

```bash
python fork.py
```

Connect to it from the same machine (different terminal)

```
telnet 127.0.0.1 8080
```

or easy switch between screens using GNU `screen`:

```
screen -S new_screen
```

`C-a d` - exit from created screen

`screen -ls` - show all screens

`screen -r` - return to last screen

### Show forked processes in real time

```
watch "ps ax | grep fork"
```

## Theory

### Ways to work with sockets

1. **blocking IO** - wait for event
2. **fork** - create children process (copy all memory scope) that waits
   for event
3. **prefork** - hand out socket to processes
4. **AIO** - iterate on happened events (technologies: select, kqueue,
   poll, epoll...)
5. **threads** - like **fork**, but inside 1 process (all threads have
   shared memory - can lead to errors)

### Popular Web Servers

* **Apache** - prefork, worker, `C`
* **IIS, Tomcat, Jetty** - threads, `Java`
* **Starman, Hypnotoad** - prefork, `HLPL`
* **nginx, lighttpd** - async, `C`
* **haproxy** - proxy, `C`
* **Node.js, Tornado** - async, `HLPL`
* **Erlang!**
* **dev servers**

`HLPL` - High-Level Programming Language

### Frontend & Backend

#### Frontend (90% traffic w/o logic)

*  Serve static files
*  Proxies requests to backend
*  SSI, SSL, TSL
*  Load Balancing
*  Caching
*  Image resize, gzip.

#### Backend

*  Logic

### Ways to work w/ Backend

*  CGI
*  FastCGI
*  mod_perl, mod_python, mod_php..
*  PSGI, WSGI, Rack

### WSGI Communication Agreement (gunicorn - Django)

```python
def simple_wsgi_app(environ, start_responce):
    start_responce('200 OK', [('Content-Type', 'text/plain')])
    yield 'Hello, world!'
```

**gunicorn** is App Server (written on Python) for Django that processes
requests from Nginx (faster than Django's own server) and calls Django's
callback functions. **gunicorn** parses headers, body, url of the
request, imports python function for processing requests (logic layer),
calls that function for that request, sends return value from it to
Nginx.

[Start gunicorn](http://gunicorn.org/#quickstart): `gunicorn -b
0.0.0.0:8080 project.wsgi:application`


