#!/usr/local/bin/python

import socket
import select

# Asynchronous work w/ connections
# Works inside only 1 process

server_socket = socket.socket()
server_socket.bind(('', 8080))
server_socket.setblocking(0)  # Do not block (use non blocking IO operations) thus we need to use events
server_socket.listen(10)

# Create 3 lists
inputs = {server_socket}  # Dict for read (new clients connected)
outputs = {}  # Dict for write
excepts = []  # Arr for errors


while 1:
    # check if there are sockets ready for read/write
    input_ready, output_ready, except_ready = select.select(list(inputs), outputs.keys(), excepts, 0.5)  # 0.5 timeout
    for s in input_ready:
        if s == server_socket:
            client_socket, remote_address = server_socket.accept()
            client_socket.setblocking(0)
            inputs.add(client_socket)
        else:
            request = s.recv(1024)  # Read from socket
            print '{} : {}'.format(s.getpeername(), request)
            outputs[s] = request.upper()
            inputs.remove(s)
    for s in output_ready:
        if s in outputs:
            s.send(outputs[s])  # Write to socket
            del outputs[s]
            s.close()
