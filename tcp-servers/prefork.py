#!/usr/local/bin/python

import os
import socket
import sys

# Prefork works like fork, but uses slightly less memory
# We always have 4 or n child processes, instead of creating one for each inbound connection

server_socket = socket.socket()
server_socket.bind(('', 8080))
server_socket.listen(10)

for i in range(4):
    child_pid = os.fork()  # fork 4 processes at once
    if child_pid == 0:
        try:
            while True:
                # each forked process tries to read from the same server socket (FD)
                # OS gives connection to each process in queue
                client_socket, remote_address = server_socket.accept()
                request = client_socket.recv(1024)
                client_socket.send(request.upper())
                print '(child {}) {} : {}'.format(os.getpid(), client_socket.getpeername(), request)
                client_socket.close()
        except KeyboardInterrupt:
            sys.exit()

try:
    os.waitpid(-1, 0)
except KeyboardInterrupt:
    sys.exit()
