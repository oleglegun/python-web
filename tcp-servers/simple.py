#!/usr/local/bin/python

# Single Threaded TCP Server

import socket

server_socket = socket.socket()
server_socket.bind(('', 80))  # '' listen from all IPs, Default server ip: 127.0.0.1 80
server_socket.listen(10)        # max connections queue: 10

while True:
    client_socket, remote_address = server_socket.accept()  # Accept a connection (wait in sleep for connection)
    try:
        request = client_socket.recv(1024)  # Receive data from the socket (buffer = 1024 bytes)
        client_socket.send(request.upper())
        print('{} : {}').format(client_socket.getpeername(), request)
        client_socket.close()
    except:
        pass

server_socket.close()
