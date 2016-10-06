#!/usr/local/bin/python

import os
import socket
import sys


server_socket = socket.socket()
server_socket.bind(('', 8080))
server_socket.listen(10)

while True:
    client_socket, remote_address = server_socket.accept()  # Sleep and wait for new connect
    # When someone connects - OS gives parent process new File Descriptor for this connect (socket)
    # In this FD we can read/write to connected client

    # We fork() w/ this new FD and continue working w/ it in child process
    child_pid = os.fork()  # Fork a child process. Return 0 in the child and the child's process id in the parent

    if child_pid == 0:  # Means that child process was initiated and we now in child
        request = client_socket.recv(1024)
        client_socket.send(request.upper())
        print '(child {}) {} : {}'.format(child_pid, client_socket.getpeername(), request)
        client_socket.close()  # Close child's FD for socket (for OS GC)
        sys.exit()  # kill child process
    else:  # Continues in parent process
        client_socket.close()  # If we close socket FD only in child, it won't close in parent => memory leaks
        # When there are no links to FD -> OS removes it from memory

server_socket.close()
