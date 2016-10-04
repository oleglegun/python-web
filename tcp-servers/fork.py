#!/usr/local/bin/python

import os
import socket
import sys


server_socket = socket.socket()
server_socket.bind(('', 8080))
server_socket.listen(10)

while True:
    client_socket, remote_address = server_socket.accept()
    # When someone connects - OS gives us new File Descriptor for this connect.

    # Fork a child process. Return 0 in the child and the child's process id in the parent
    child_pid = os.fork()
    if child_pid == 0:  # Means that child process was initiated and we now in child
        request = client_socket.recv(1024)
        client_socket.send(request.upper())
        print '(child {}) {} : {}'.format(client_socket.getpeername(), request)
        client_socket.close()  # For OS GC
        sys.exit()  # kill child process
    else:  # Continues in parent process
        client_socket.close()  # If we close socket only in child, it won't close in parent

server_socket.close()
